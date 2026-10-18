"""Bind a normal Comfy Desktop Standalone instance; Desktop owns its lifecycle."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import socket
import subprocess
import sys
import tomllib
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / ".local/comfyui-instance.json"
REQUEST = ROOT / ".local/comfyui-request.json"
MCP_HOME = ROOT / ".local/comfyui-mcp"
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)


def within(path, root=ROOT):
    path, root = Path(path).resolve(), Path(root).resolve()
    if not path.is_relative_to(root) or len(root.parts) < 3:
        raise ValueError(f"Path escapes allowed directory: {path}")
    return path


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write(path, value, root=ROOT):
    path = within(path, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def sources():
    value = read(ROOT / ".local/comfyui-bootstrap.json")
    for key in ("desktop_exe", "desktop_data", "mcp", "comfy_bin"):
        if key not in value or not Path(value[key]).exists():
            raise ValueError(f"Missing existing {key}; inspect installation and explicitly update bootstrap paths")
    return value


def desktop_read(seed, filename):
    path = Path(seed["desktop_data"]) / filename
    actual = path.resolve()
    # MSIX can redirect Roaming reads to Codex's private LocalCache. That
    # registry is invisible to the Desktop launched from the Start menu.
    if os.path.normcase(str(actual)) != os.path.normcase(os.path.abspath(path)):
        raise ValueError(f"Desktop configuration redirected to {actual}; use the Start-menu Desktop registry")
    return read(path)


def registry(seed):
    # Read only: Desktop's UI owns registration, installation and settings.
    value = desktop_read(seed, "installations.json")
    if not isinstance(value, list):
        raise ValueError("Unsupported Desktop registry; inspect installed Desktop version")
    return value


def shared_model_roots(seed):
    values = desktop_read(seed, "settings.json").get("modelsDirs", [])
    if not isinstance(values, list) or not values:
        raise ValueError("Desktop has no shared model directories; configure an existing model library first")
    roots = []
    for value in values:
        path = Path(value).resolve()
        if not path.is_dir() or path == Path(path.anchor):
            raise ValueError(f"Invalid existing shared model directory: {path}")
        if path not in roots:
            roots.append(path)
    return roots


def shared_model(seed, base, model, verify_hash=False):
    roots = shared_model_roots(seed)
    candidates = []
    for root in roots:
        path = within(root / model["destination"], root)
        if path.is_file() and path not in candidates:
            candidates.append(path)
    if len(candidates) != 1:
        raise ValueError("WAI missing or ambiguous in Desktop shared model directories; inspect existing library")
    checkpoint = candidates[0]
    # A same-named local weight could shadow the shared file in ComfyUI's loader.
    local = Path(base) / "models" / model["destination"]
    if local.exists():
        raise ValueError("Local WAI duplicate conflicts with shared model selection; explicitly migrate it, never delete automatically")
    stat = checkpoint.stat()
    if stat.st_size != model["bytes"]:
        raise ValueError("Shared WAI size differs from the pinned model")
    if verify_hash and sha(checkpoint) != model["sha256"]:
        raise ValueError("Shared WAI SHA256 differs from the pinned model; do not overwrite shared weights")
    return {"mode": "desktop_shared", "roots": [str(p) for p in roots],
            "checkpoint": str(checkpoint), "bytes": stat.st_size, "mtime_ns": stat.st_mtime_ns}


def installation(seed, instance_id):
    matches = [x for x in registry(seed) if x.get("id") == instance_id]
    if len(matches) != 1:
        raise ValueError("Bound Desktop instance missing/ambiguous; never fall back to another instance")
    item = matches[0]
    if item.get("sourceId") != "standalone" or item.get("status") != "installed":
        raise ValueError("Use a fully installed normal Desktop Standalone instance")
    install = Path(item["installPath"]).resolve()
    if len(install.parts) < 3 or install.parent == Path(install.anchor):
        raise ValueError("Instance must not be placed directly in a drive root")
    marker = install / ".comfyui-desktop-2"
    marker_value = marker.read_text(encoding="utf-8").strip() if marker.is_file() else None
    if marker_value == "tracked":
        # Desktop's native Add Existing flow writes "tracked", not its new ID.
        # Accept it only for an already-owned, uniquely registered project path.
        owner = install / ".godot-project-binding.json"
        same_path = [x for x in registry(seed) if x.get("installPath") and Path(x["installPath"]).resolve() == install]
        if not owner.is_file() or Path(read(owner)["project"]).resolve() != ROOT or len(same_path) != 1:
            raise ValueError("Tracked Desktop instance has no unique project ownership")
    elif marker_value != instance_id:
        raise ValueError("Desktop installation marker does not match instance ID")
    base = within(install / "ComfyUI", install)
    python = within(base / ".venv/Scripts/python.exe", install)
    if not (base / "main.py").is_file() or not python.is_file():
        raise ValueError("Normal Desktop core or instance Python is missing")
    if item.get("useSharedModels", True) is not True:
        raise ValueError("Desktop > Manage: enable shared model directories")
    if any(item.get(k, True) is not False for k in ("useSharedInput", "useSharedOutput")):
        raise ValueError("Desktop > Manage: disable shared input and shared output first")
    if item.get("browserPartition") != "unique":
        raise ValueError("Desktop > Manage: use this instance's own browser session")
    if item.get("modelDirs") or item.get("modelDirsPrimary"):
        raise ValueError("Use Desktop's existing shared model directories; review extra per-instance model overrides first")
    for key in ("inputDir", "outputDir"):
        if item.get(key):
            within(item[key], base)
    args = item.get("launchArgs", "")
    if re.search(r"--(?:base-directory|models-directory|user-directory|input-directory|output-directory|extra-model-paths-config)(?:\s|=|$)", args):
        raise ValueError("Use Desktop's normal instance storage; remove directory overrides in launch arguments")
    if (base / "extra_model_paths.yaml").exists():
        raise ValueError("Extra model YAML requires explicit review; use Desktop-managed shared model paths")
    ports = re.findall(r"(?:^|\s)--port(?:=|\s+)(\d+)(?=\s|$)", args)
    if len(ports) != 1 or not 1024 <= int(ports[0]) <= 65535:
        raise ValueError("Set one explicit --port in Desktop > Manage using comfyui-request.json")
    port = int(ports[0])
    for other in registry(seed):
        if other.get("id") != instance_id and re.search(rf"(?:^|\s)--port(?:=|\s+){port}(?=\s|$)", other.get("launchArgs", "")):
            raise ValueError("Another Desktop instance uses this explicit port; choose a unique port")
    for rel in ("models", "custom_nodes", "input", "output", "user", ".venv"):
        within(base / rel, install)
    binding = install / ".godot-project-binding.json"
    if binding.exists() and Path(read(binding)["project"]).resolve() != ROOT:
        raise ValueError("This Desktop instance is already bound to another project")
    return item, install, base, python, port


def config():
    cfg = read(CONFIG)
    if cfg.get("schema") != 3 or not cfg.get("desktop_instance_id"):
        raise ValueError("Older binding: follow explicit shared-model migration; preserve existing instance/files")
    if Path(cfg["project"]).resolve() != ROOT:
        raise ValueError("Project moved; explicitly rebind paths before connecting")
    _, install, base, python, port = installation(cfg, cfg["desktop_instance_id"])
    if read(install / ".godot-project-binding.json").get("desktop_instance_id") != cfg["desktop_instance_id"]:
        raise ValueError("Project ownership marker has a different Desktop ID; explicitly rebind")
    if Path(cfg["base"]).resolve() != base or Path(cfg["install_path"]).resolve() != install or cfg["port"] != port:
        raise ValueError("Desktop instance path/port changed; explicitly rebind the same ID")
    if cfg["url"] != f"http://127.0.0.1:{port}" or Path(cfg["python"]).resolve() != python or not cfg.get("ready"):
        raise ValueError("Binding incomplete or inconsistent; rerun setup with the same instance ID")
    if shared_model(cfg, base, cfg["model"]) != cfg.get("model_storage"):
        raise ValueError("Shared WAI file or Desktop model paths changed; reverify and explicitly rebind the same ID")
    return cfg


def plan(seed):
    parameters = read(ROOT / ".bootstrap/state.json")["parameters"]
    name = parameters.get("codex_project_name") or parameters["name"]
    if not name.strip() or name != name.strip():
        raise ValueError("Use the exact non-empty Codex project name")
    # The display name is exact. Desktop alone sanitizes its directory name.
    directory_name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name).strip().rstrip(". ")
    if not directory_name or directory_name in (".", ".."):
        raise ValueError("Project name cannot form an installation directory")
    if REQUEST.exists():
        value = read(REQUEST)
        if Path(value["project"]).resolve() != ROOT:
            raise ValueError("Instance request belongs to a different project path")
        value.update(name=name, suggested_install_path=str(Path(value["install_parent"]) / directory_name),
                     useSharedModels=True, shared_model_dirs=[str(p) for p in shared_model_roots(seed)])
        write(REQUEST, value)
        return value
    parent = Path(desktop_read(seed, "settings.json")["installDir"]).resolve()
    if not parent.is_dir() or parent == Path(parent.anchor):
        raise ValueError("Choose an existing Desktop install parent below the drive root")
    used = {int(p) for x in registry(seed) for p in re.findall(r"--port(?:=|\s+)(\d+)", x.get("launchArgs", ""))}
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    if port in used:
        raise ValueError("Suggested port is reserved by another instance; rerun planning")
    value = {"project": str(ROOT), "name": name, "install_parent": str(parent),
             "suggested_install_path": str(parent / directory_name), "port": port,
             "launch_args": f"--enable-manager --port {port}",
             "useSharedModels": True, "useSharedInput": False, "useSharedOutput": False,
             "shared_model_dirs": [str(p) for p in shared_model_roots(seed)]}
    write(REQUEST, value)
    return value


def setup(instance_id=None):
    if CONFIG.exists():
        previous = read(CONFIG)
        if previous.get("schema") not in (2, 3):
            raise ValueError("Legacy backend detected: explicitly migrate first; no automatic replacement/deletion")
        if previous.get("schema") == 2 and not instance_id:
            raise ValueError("v1.3 binding needs explicit shared-model migration and setup --installation-id <same ID>")
        if instance_id and previous["desktop_instance_id"] != instance_id:
            raise ValueError("Project already bound to another ID; do not silently replace its instance")
        if not instance_id and previous.get("ready"):
            cfg = config()
            configure_mcp(cfg)
            install_ui(cfg)
            return {"state": "existing", "ready": True, "id": cfg["id"], "url": cfg["url"], "base": cfg["base"],
                    "model_storage": cfg["model_storage"], "model_bytes_copied": 0}
        instance_id = instance_id or previous["desktop_instance_id"]
    seed = sources()
    if not instance_id:
        return {"state": "desktop_instance_required", "ready": False, "request": plan(seed),
                "next": "Use the skill's desktop_instance.py to create a normal Desktop instance with this exact project name; then setup --installation-id <actual ID>"}
    item, install, base, python, port = installation(seed, instance_id)
    model = read(ROOT / "tools/comfyui/wai-model.json")
    storage = shared_model(seed, base, model, verify_hash=True)
    cfg = {"schema": 3, "id": instance_id, "desktop_instance_id": instance_id, "ready": False,
           "project": str(ROOT), "install_path": str(install), "base": str(base), "port": port,
           "url": f"http://127.0.0.1:{port}", "python": str(python), "helper_python": sys.executable,
           "mcp": seed["mcp"], "comfy_bin": seed["comfy_bin"], "desktop_data": seed["desktop_data"],
           "desktop_name_at_bind": item.get("name"), "comfy_version_at_bind": item.get("comfyVersion"),
           "model": model, "model_storage": storage}
    write(CONFIG, cfg)
    write(install / ".godot-project-binding.json", {"schema": 1, "project": str(ROOT), "desktop_instance_id": instance_id}, install)
    configure_mcp(cfg)
    install_ui(cfg)
    cfg["ready"] = True
    write(CONFIG, cfg)
    return {"state": "bound", "ready": True, "id": instance_id, "url": cfg["url"], "base": str(base),
            "model_storage": storage, "model_bytes_copied": 0, "checkpoint_sha256": model["sha256"]}


def install_ui(cfg):
    dest = within(Path(cfg["base"]) / "user/default/workflows/wai-t2i.json", Path(cfg["base"]))
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / "tools/comfyui/workflows/wai-t2i.ui.json", dest)


def configure_mcp(cfg):
    entry = {"command": cfg["helper_python"], "args": [str(ROOT / "tools/project_comfyui.py"), "mcp"],
             "startup_timeout_sec": 60, "tool_timeout_sec": 180,
             "enabled_tools": ["server_info", "system_stats", "nodes", "validate_workflow", "run_workflow", "job", "fetch_outputs", "upload_file", "free_memory", "list_workflow_slots", "list_workflow_notes", "set_workflow_slot"]}
    from host_mcp import configure
    agent = read(ROOT / ".bootstrap/state.json").get("parameters", {}).get("agent", "codex")
    configure(ROOT, entry, agent)
    ini = within(MCP_HOME / "home/AppData/Local/comfy-cli/config.ini")
    ini.parent.mkdir(parents=True, exist_ok=True)
    ini.write_text(f"[DEFAULT]\ndefault_workspace = {cfg['base']}\nenable_tracking = False\n", encoding="utf-8")
    for rel in ("home/AppData/Roaming", "cache", "temp"):
        within(MCP_HOME / rel).mkdir(parents=True, exist_ok=True)


def environment(cfg):
    env = dict(os.environ)
    for name in ("COMFYUI_URL", "COMFYUI_HOST", "COMFYUI_PORT", "COMFY_WHERE", "COMFY_MCP_REMOTE_SHARED_MODELS"):
        env.pop(name, None)
    env.update(PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1", COMFY_NO_TELEMETRY="1",
               USERPROFILE=str(MCP_HOME / "home"), LOCALAPPDATA=str(MCP_HOME / "home/AppData/Local"),
               APPDATA=str(MCP_HOME / "home/AppData/Roaming"), TEMP=str(MCP_HOME / "temp"), TMP=str(MCP_HOME / "temp"),
               COMFY_PROJECT=str(ROOT), COMFY_LOCAL_URL=cfg["url"], COMFY_CACHE_DIR=str(MCP_HOME / "cache"), COMFY_BIN=cfg["comfy_bin"])
    return env


def identity(cfg):
    # Desktop can launch relative main.py: verify the actual listening process.
    script = """import json,sys,psutil,pathlib
c=json.loads(sys.argv[1]); root=pathlib.Path(c['install_path']).resolve(); base=pathlib.Path(c['base']).resolve()
owners={x.pid for x in psutil.net_connections(kind='tcp') if x.laddr.port==c['port'] and x.status=='LISTEN'}
if not owners: print('false'); sys.exit(0)
for pid in owners:
 p=psutil.Process(pid); argv=p.cmdline(); cwd=pathlib.Path(p.cwd()).resolve()
 mains=[(cwd/pathlib.Path(a)).resolve() for a in argv if pathlib.Path(a).name=='main.py']
 if base/'main.py' not in mains or not pathlib.Path(p.exe()).resolve().is_relative_to(root):
  raise ValueError('Port belongs to a different process/instance')
print('true')
"""
    result = subprocess.run([str(Path(cfg["mcp"]).with_name("python.exe")), "-B", "-c", script, json.dumps(cfg)],
                            capture_output=True, text=True, encoding="utf-8", creationflags=NO_WINDOW)
    if result.returncode:
        raise ValueError("Instance process identity check failed: " + result.stderr.strip())
    if not json.loads(result.stdout):
        return False
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(cfg["url"] + "/system_stats", timeout=3) as response:
            return "system" in json.load(response)
    except OSError:
        return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("setup", "list", "status", "mcp", "call"))
    parser.add_argument("--installation-id", help="Actual ID from Desktop's normal New Instance wizard")
    parser.add_argument("--request", type=Path, help="JSON {name, arguments} for a real MCP tools/call")
    args = parser.parse_args()
    if args.action == "setup":
        result = setup(args.installation_id)
    elif args.action == "list":
        result = [{k: x.get(k) for k in ("id", "name", "sourceId", "status", "installPath", "launchArgs")} for x in registry(sources())]
    else:
        cfg = config()
        running = identity(cfg)
        if args.action == "status":
            result = {"ready": True, "running": running, "url": cfg["url"], "id": cfg["id"], "base": cfg["base"],
                      "model_storage": cfg["model_storage"], "lifecycle": "Comfy Desktop"}
        elif args.action == "mcp":
            if not running:
                raise ValueError("Bound instance is stopped; follow docs/asset-pipeline.md to run desktop_instance.py open/start via Explorer Shell, then reconnect project MCP")
            return subprocess.call([cfg["mcp"]], cwd=ROOT, env=environment(cfg),
                                   stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, creationflags=NO_WINDOW)
        else:
            if not args.request:
                parser.error("call requires --request")
            if not running:
                raise ValueError("Bound instance is stopped; follow docs/asset-pipeline.md to run desktop_instance.py open/start via Explorer Shell, then reconnect project MCP")
            from stdio_mcp import MCPClient
            request = read(args.request)
            with MCPClient(cfg["mcp"], env=environment(cfg), cwd=ROOT, log=within(MCP_HOME / "mcp-call.log")) as client:
                client.initialize()
                result = client.call(request["name"], request.get("arguments", {}), timeout=180)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if isinstance(result, dict) and result.get("state") == "desktop_instance_required":
        return 3
    return 1 if isinstance(result, dict) and result.get("isError") else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    try:
        sys.exit(main())
    except (ValueError, KeyError, OSError, subprocess.SubprocessError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
