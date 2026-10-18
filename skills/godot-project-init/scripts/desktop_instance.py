"""Create normal Desktop instances through its installed renderer bridge, without clicks.

Run with the existing MCP tool Python (psutil + websocket-client). Desktop 1.1.7.
This is an internal, version-checked adapter, not a public Comfy Desktop CLI.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import psutil
import websocket
from desktop_launch import launch_native, package_identity, shell_open, check_shortcut

SUPPORTED = {"1.1.7"}
OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def get_json(url):
    with OPENER.open(url, timeout=3) as response:
        return json.load(response)


def desktop_read(seed, filename):
    path = Path(seed["desktop_data"]) / filename
    actual = path.resolve(strict=True)
    if os.path.normcase(str(actual)) != os.path.normcase(os.path.abspath(path)):
        raise ValueError(f"Desktop configuration redirected to {actual}; stop and recover the Start-menu registry before creating instances")
    return read(path)


def native_process(pid):
    identity = package_identity(pid)
    if identity is not None:
        raise ValueError(f"Desktop inherited package {identity}; close it normally and use the native launcher")
    args = psutil.Process(pid).cmdline()
    if any(a.startswith(("--user-data-dir", "--profile-directory")) for a in args):
        raise ValueError("Desktop uses an alternate profile; use the normal Start-menu configuration")
    return {"pid": pid, "package_identity": None}


def visibility(desktop, seed, instance_id):
    if not instance_id:
        raise ValueError("Bind an installed project instance before verifying visibility")
    registry = desktop_read(seed, "installations.json")
    listed = desktop.call("getInstallations")
    matches = [x for x in listed if x.get("id") == instance_id]
    persisted = [x for x in registry if x.get("id") == instance_id]
    if len(matches) != 1 or len(persisted) != 1:
        raise ValueError("Project instance is missing/ambiguous in Desktop or its normal registry")
    item = matches[0]
    for key in ("id", "name", "sourceId", "status", "installPath", "workspaceId"):
        if item.get(key) != persisted[0].get(key):
            raise ValueError(f"Desktop and normal registry disagree on {key}")
    if item.get("status") != "installed" or item.get("sourceId") != "standalone" or item.get("workspaceId", "personal") != "personal":
        raise ValueError("Project is not an installed Standalone instance in the personal list")
    rendered = desktop.evaluate("document.body.innerText.split('\\n').some(line => line.trim() === " + json.dumps(item["name"]) + ")")
    if rendered is not True:
        raise ValueError("Project is registered but its name is not rendered on this dashboard; inspect workspace/search/window selection")
    return {"state": "visible", "desktop_version": desktop.version,
            **native_process(desktop.pid), "registry": str((Path(seed["desktop_data"]) / "installations.json").resolve()),
            "entry": {k: item.get(k) for k in ("id", "name", "installPath", "status")},
            "dashboard_name_rendered": rendered, "instance_count": len(listed)}


class Desktop:
    def __init__(self, exe, port):
        self.exe = Path(exe).resolve()
        self.port = int(port)
        listeners = [c for c in psutil.net_connections(kind="tcp")
                     if c.status == "LISTEN" and c.laddr.port == self.port]
        if not listeners or any(c.laddr.ip not in ("127.0.0.1", "::1") or not c.pid or
                                Path(psutil.Process(c.pid).exe()).resolve() != self.exe for c in listeners):
            raise ValueError("Debug port must be loopback-only and owned by the configured Comfy Desktop executable")
        self.pid = listeners[0].pid
        native_process(self.pid)
        prefix = (self.exe.parent / "resources/app.asar/out/renderer").as_posix().casefold() + "/"
        self.target = None
        for target in get_json(f"http://127.0.0.1:{self.port}/json/list"):
            url = urllib.parse.urlsplit(target.get("url", ""))
            local = urllib.parse.unquote(url.path).lstrip("/").casefold()
            if target.get("type") != "page" or url.scheme != "file" or not local.startswith(prefix):
                continue
            self.target = target
            if self.evaluate("typeof window.api?.buildInstallation === 'function'"):
                break
            self.target = None
        if not self.target:
            raise ValueError("Desktop renderer bridge is not ready; retry after startup")
        version = self.call("getAppVersion")
        if version not in SUPPORTED:
            raise ValueError(f"Desktop {version} is not verified; inspect its bridge before adapting this script")
        self.version = version

    def evaluate(self, expression, timeout=55):
        url = self.target["webSocketDebuggerUrl"]
        parsed = urllib.parse.urlsplit(url)
        if parsed.hostname != "127.0.0.1" or parsed.port != self.port:
            raise ValueError("Unexpected debugger endpoint")
        ws = websocket.create_connection(url, timeout=timeout, suppress_origin=True, http_no_proxy=["127.0.0.1"])
        try:
            ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {
                "expression": expression, "awaitPromise": True, "returnByValue": True}}))
            while True:
                response = json.loads(ws.recv())
                if response.get("id") != 1:
                    continue
                if response.get("error") or response.get("result", {}).get("exceptionDetails"):
                    raise ValueError("Desktop bridge failed: " + json.dumps(response, ensure_ascii=False))
                return response["result"]["result"].get("value")
        finally:
            ws.close()

    def call(self, method, *arguments):
        return self.evaluate(f"window.api[{json.dumps(method)}](...{json.dumps(arguments, ensure_ascii=False)})")


def open_desktop(seed, *, debug=True, shortcut=None):
    exe = Path(seed["desktop_exe"]).resolve()
    if shortcut:
        shortcut = check_shortcut(shortcut, exe)
    # Resolve files, not just APPDATA: MSIX may use LocalCache behind the same string.
    for filename in ("installations.json", "settings.json"):
        desktop_read(seed, filename)
    for proc in psutil.process_iter(["pid", "name", "exe", "cmdline"]):
        try:
            if not proc.info["exe"] or Path(proc.info["exe"]).resolve() != exe:
                continue
            args = proc.info["cmdline"] or []
            if any(a.startswith("--type=") for a in args):
                continue
            native_process(proc.pid)
            ports = [int(a.split("=", 1)[1]) for a in args if a.startswith("--remote-debugging-port=")]
            if not debug:
                if ports:
                    raise ValueError("Close the temporary debug session before reopening normally")
                return {"state": "normal_existing", **native_process(proc.pid)}
            if len(ports) == 1 and ports[0] > 0:
                return {"state": "existing", "pid": proc.pid, "port": ports[0]}
            return {"state": "restart_required", "pid": proc.pid,
                    "reason": "Desktop is already open without a script connection. Save work and close it normally, then rerun open; do not forcibly restart user work."}
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    argv = [str(exe)]
    if debug:
        argv += [f"--remote-debugging-port={port}", "--remote-debugging-address=127.0.0.1"]
    method = "explorer_shell"
    if shortcut:
        method = "explorer_start_menu_shortcut"
        shell_open(shortcut, argv[1:], cwd=exe.parent, visible=not debug)
        limit = time.monotonic() + 15
        pid = None
        while not pid and time.monotonic() < limit:
            candidates = []
            for candidate in psutil.process_iter(["exe", "cmdline"]):
                try:
                    cmd = candidate.info["cmdline"] or []
                    if candidate.info["exe"] and Path(candidate.info["exe"]).resolve() == exe and not any(a.startswith("--type=") for a in cmd):
                        candidates.append(candidate.pid)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            if len(candidates) > 1:
                raise ValueError("Multiple Desktop main processes appeared; inspect before retrying")
            pid = candidates[0] if candidates else None
            if not pid:
                time.sleep(0.2)
        if not pid:
            raise ValueError("Shortcut did not start Desktop; inspect before retrying")
    else:
        pid = launch_native(argv, cwd=exe.parent, visible=not debug,
                            config_paths=[Path(seed["desktop_data"]) / f for f in ("installations.json", "settings.json")])
    proc = psutil.Process(pid)
    deadline = time.monotonic() + 35
    while time.monotonic() < deadline:
        if not proc.is_running():
            raise ValueError("Desktop exited; check an already-running single instance before retrying")
        if not debug:
            time.sleep(2)
            if any(a.startswith("--remote-debugging") for a in proc.cmdline()):
                raise ValueError("Normal Desktop unexpectedly has debug flags")
            return {"state": "normal_started", "launch_method": method, **native_process(pid)}
        try:
            if get_json(f"http://127.0.0.1:{port}/json/list"):
                return {"state": "started", "launch_method": method, **native_process(pid), "port": port}
        except OSError:
            pass
        time.sleep(0.5)
    raise ValueError("Desktop startup timed out; inspect it before starting another process")


def select_installation(desktop, request):
    name = request["name"]
    if desktop.call("getUniqueName", name) != name or any(x["name"].casefold() == name.casefold() for x in desktop.call("getInstallations")):
        raise ValueError("An instance already has this project name. Resolve ownership explicitly; no suffix or silent reuse")
    parent = Path(request["install_parent"]).resolve()
    if not parent.is_dir() or parent == Path(parent.anchor):
        raise ValueError("Use an existing install parent below the drive root")
    directory = re.sub(r'[<>:"/\\|?*]+', "_", name).strip()
    candidate = (parent / directory).resolve()
    if candidate.parent != parent or candidate.exists() or directory.endswith((".", " ")) or re.match(r"^(?:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\.|$)", directory, re.I):
        raise ValueError("Installation directory is invalid or already exists; resolve it without adding a suffix")
    validation = desktop.call("validateInstallPath", str(parent))
    if not isinstance(validation, list) or validation:
        raise ValueError("Desktop rejected installation parent: " + json.dumps(validation))
    releases = desktop.call("getFieldOptions", "standalone", "release", {}, {"includeLatestStable": True})
    release = next((x for x in releases if x["value"] == "stable"), None)
    if not release:
        raise ValueError("Stable Desktop release unavailable; retry after inspecting network/catalog")
    selections = {"release": release}
    variants = desktop.call("getFieldOptions", "standalone", "variant", selections, {})
    variant = next((x for x in variants if x["value"] == "win-nvidia"), None)
    if not variant:
        raise ValueError("The installed catalog has no Windows NVIDIA environment")
    selections["variant"] = variant
    versions = desktop.call("getFieldOptions", "standalone", "comfyVersion", selections, {})
    if versions:
        selections["comfyVersion"] = versions[0]
    data = desktop.call("buildInstallation", "standalone", selections)
    if not data or data.get("sourceId") != "standalone" or data.get("bundledTemplateId"):
        raise ValueError("Unexpected installation plan; template model downloads must remain disabled")
    required = int(sum(x["size"] for x in data["downloadFiles"]) * 2.25)
    if shutil.disk_usage(parent).free < required:
        raise ValueError("Insufficient space for the independent Desktop environment")
    data.update(name=name, installPath=str(parent), useSharedModels=True, useSharedInput=False,
                useSharedOutput=False, browserPartition="unique", workspaceId="personal",
                launchArgs=data.get("launchArgs", "--enable-manager") + f" --port {request['port']}")
    return data, candidate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("open", "probe", "create", "status", "verify", "start", "stop", "close", "reopen"))
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--port", type=int, help="Temporary Desktop debugging port, not the ComfyUI API port")
    parser.add_argument("--shortcut", type=Path, help="Existing normal Start-menu .lnk, for open/reopen verification; never edited")
    args = parser.parse_args()
    project = args.project.resolve()
    seed = read(project / ".local/comfyui-bootstrap.json")
    session_file = project / ".local/comfyui-desktop-session.json"
    pending_file = project / ".local/comfyui-desktop-creation.json"
    if args.action in ("open", "reopen"):
        result = open_desktop(seed, debug=args.action == "open", shortcut=args.shortcut)
        if "port" in result:
            write(session_file, result)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 3 if result["state"] == "restart_required" else 0
    port = args.port or read(session_file)["port"]
    desktop = Desktop(seed["desktop_exe"], port)
    for filename in ("installations.json", "settings.json"):
        desktop_read(seed, filename)
    pending = read(pending_file) if pending_file.exists() else None
    if pending and Path(pending["project"]).resolve() != project:
        raise ValueError("Creation record belongs to another project")
    bound_path = project / ".local/comfyui-instance.json"
    bound = read(bound_path) if bound_path.exists() else None
    instance_id = bound["desktop_instance_id"] if bound else pending["id"] if pending else None
    entries = desktop.call("getInstallations")
    entry = next((x for x in entries if x["id"] == instance_id), None)
    # Desktop's list API hides installing records; its persisted registry is
    # read-only evidence for a pending installation created by this project.
    if instance_id and not entry:
        entry = next((x for x in desktop_read(seed, "installations.json") if x["id"] == instance_id), None)
    if instance_id and not entry and args.action not in ("probe", "close"):
        raise ValueError("Recorded instance disappeared; do not create a replacement silently")
    if pending and entry and (Path(entry["installPath"]).resolve() != Path(pending["install_path"]).resolve()):
        raise ValueError("Pending instance path changed; inspect before continuing")
    if args.action == "probe":
        result = {"desktop_version": desktop.version, **native_process(desktop.pid),
                  "registry": str((Path(seed["desktop_data"]) / "installations.json").resolve()),
                  "instances": [{k: x.get(k) for k in ("id", "name", "status", "installPath")} for x in entries]}
    elif args.action == "verify":
        result = visibility(desktop, seed, instance_id)
    elif args.action == "create":
        if entry:
            result = {"state": "existing", "entry": entry}
        else:
            request = read(project / ".local/comfyui-request.json")
            if Path(request["project"]).resolve() != project:
                raise ValueError("Instance request belongs to a different project")
            spec = importlib.util.spec_from_file_location("project_comfyui", project / "tools/project_comfyui.py")
            helper = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(helper)
            model = read(project / "tools/comfyui/wai-model.json")
            helper.shared_model(seed, Path(request["suggested_install_path"]) / "ComfyUI", model, verify_hash=True)
            data, expected_path = select_installation(desktop, request)
            added = desktop.call("addInstallation", data)
            if not added.get("ok"):
                raise ValueError("Desktop could not register the requested instance: " + json.dumps(added))
            entry = added["entry"]
            pending = {"project": str(project), "id": entry["id"], "name": entry["name"], "install_path": entry["installPath"], "desktop_version": desktop.version}
            write(pending_file, pending)
            if entry["name"] != request["name"] or Path(entry["installPath"]).resolve() != expected_path:
                raise ValueError("Desktop changed the requested name/path due to a concurrent collision; preserved the uninstalled record for explicit resolution")
            quoted = json.dumps(entry["id"])
            desktop.evaluate(f"""(()=>{{
              window.__godotInstallProgress={{}};
              window.api.onInstallProgress(p=>{{if(p.installationId==={quoted})window.__godotInstallProgress=p;}});
              window.__godotInstallResult=null;
              window.api.installInstance({quoted}).then(r=>window.__godotInstallResult=r).catch(e=>window.__godotInstallResult={{ok:false,message:String(e)}});
              return {{started:true}};
            }})()""")
            result = {"state": "installing", **pending}
    elif args.action == "status":
        result = {"entry": entry, "active": desktop.call("getActiveOperations"), "running": desktop.call("getRunningInstances"),
                  "launching": desktop.call("getLaunchingInstances"),
                  "progress": desktop.evaluate("window.__godotInstallProgress ?? null"), "result": desktop.evaluate("window.__godotInstallResult ?? null")}
    elif args.action in ("start", "stop"):
        if not bound or not entry or entry.get("status") != "installed":
            raise ValueError("Bind a fully installed instance before launch/stop")
        spec = importlib.util.spec_from_file_location("project_comfyui", project / "tools/project_comfyui.py")
        helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(helper)
        bound = helper.config()
        running = desktop.call("getRunningInstances")
        own_running = any(x["installationId"] == instance_id for x in running)
        quoted = json.dumps(instance_id)
        if args.action == "start":
            if own_running:
                result = {"state": "running", "id": instance_id}
            else:
                # Launch can replace the initiating renderer. Acknowledge the
                # dispatch before that transition, then poll authoritative state.
                result = desktop.evaluate(f"(()=>{{setTimeout(()=>window.api.runAction({quoted},'launch'),100);return {{state:'starting',id:{quoted}}}}})()")
        else:
            if not own_running:
                result = {"state": "stopped", "id": instance_id}
            else:
                queue = get_json(bound["url"] + "/queue")
                if queue.get("queue_running") or queue.get("queue_pending"):
                    raise ValueError("Project has pending generation work; do not stop it")
                result = desktop.evaluate(f"(()=>{{setTimeout(()=>window.api.stopComfyUI({quoted}),100);return {{state:'stopping',id:{quoted}}}}})()")
    else:
        installs = desktop_read(seed, "installations.json")
        downloads = desktop.call("listModelDownloads")
        if (desktop.call("getRunningInstances") or desktop.call("getActiveOperations") or desktop.call("getLaunchingInstances")
                or any(x.get("status") == "installing" for x in installs)
                or any(x.get("status") in ("pending", "downloading") for x in downloads)):
            raise ValueError("Desktop still has running instances/operations; finish them before closing the temporary interface")
        desktop.evaluate("(()=>{setTimeout(()=>window.api.quitApp(),100);return {closing:true}})()")
        result = {"state": "closing", "next": "Wait for process exit and debug port closure; run open + verify for persistence, then close + reopen without debug flags if restoring Desktop"}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if isinstance(result, dict) and result.get("ok") is False else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError, psutil.Error, websocket.WebSocketException) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
