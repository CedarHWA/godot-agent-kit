"""Read-only, bounded environment checks; no installers, model calls or service starts."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import urllib.request

from environment import discover, read_json


def command(argv: list[str]) -> str:
    completed = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8", errors="replace",
                               timeout=20, creationflags=0x08000000 if os.name == "nt" else 0)
    if completed.returncode:
        raise ValueError(f"Command failed ({completed.returncode}): {completed.stderr[-600:]}")
    return completed.stdout.strip()


def diagnose(config: dict, profile="core", agent="codex", project: Path | None = None, verify_model=False):
    checks = []

    def check(name, required, action, remedy):
        try:
            detail = action()
            checks.append({"name": name, "status": "pass", "required": required, "detail": detail})
            return detail
        except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
            checks.append({"name": name, "status": "fail" if required else "warning", "required": required,
                           "detail": str(exc), "remedy": remedy})
            return None

    def require(condition, detail):
        if not condition:
            raise ValueError(detail)
        return detail

    check("windows", True, lambda: require(os.name == "nt", "Windows is the supported platform"), "Use Windows 10/11.")
    python = config.get("python", sys.executable)
    version = check("python", True, lambda: command([python, "-c", "import sys,json; print(json.dumps(list(sys.version_info[:3])))"]),
                    "Install Python 3.11+ and pass --python / set GODOT_KIT_PYTHON.")
    if version:
        check("python-version", True, lambda: require(tuple(json.loads(version)) >= (3, 11), version), "Use Python 3.11 or later.")
    engine = check("godot", True, lambda: command([config["godot"], "--version"]), "Set godot in the config JSON or GODOT_PATH.")
    if engine and project and (project / ".bootstrap/state.json").is_file():
        expected = read_json(project / ".bootstrap/state.json")["parameters"]["engine_version"]
        check("engine-baseline", True, lambda: require(engine.startswith(expected + "."), f"Expected {expected}, detected {engine}"),
              "Select the project's pinned Godot; do not silently migrate.")
    check("gdtoolkit", True, lambda: command([python, "-c", "import importlib.metadata as m; print(m.version('gdtoolkit'))"]),
          "Install requirements.txt into the selected Python environment.")
    for host in ("codex", "deepseek-harness") if agent == "both" else (agent,):
        executable = shutil.which("dsh" if host == "deepseek-harness" else "codex")
        check(host, False, lambda exe=executable: command([exe, "--version"]) if exe else require(False, "CLI not on PATH; desktop-only installation may still load skills"),
              "Install the selected agent and enable its CLI; verify the skill catalog in a new session.")
    if profile == "desktop-wai":
        seed = config.get("comfyui_bootstrap", {})
        for key in ("desktop_exe", "desktop_data", "mcp", "comfy_bin"):
            check(key, True, lambda k=key: require(bool(seed.get(k)) and Path(seed[k]).exists(), f"Configured {k}: {seed.get(k, '(missing)')}"),
                  f"Set comfyui_bootstrap.{key} in the machine config; see docs/windows.md.")
        if seed.get("desktop_exe") and Path(seed["desktop_exe"]).exists():
            # Read metadata only; never run the Desktop application as a probe.
            quoted = seed["desktop_exe"].replace("'", "''")
            desktop_version = check("desktop-version", True, lambda: command(["powershell", "-NoProfile", "-Command", f"(Get-Item -LiteralPath '{quoted}').VersionInfo.ProductVersion"]), "Install a version listed in the desktop-wai profile.")
            if desktop_version:
                check("desktop-adapter", True, lambda: require(bool(re.match(r"^1\.1\.7(?:\D|$)", desktop_version)), desktop_version),
                      "The native adapter is validated for Desktop 1.1.7 only. Revalidate before expanding its version allowlist.")
        check("nvidia", True, lambda: command(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"]),
              "desktop-wai requires the supported NVIDIA environment; use core/endpoint for other setups.")
        helper = str(Path(seed.get("mcp", "missing")).with_name("python.exe"))
        check("desktop-helper", True, lambda: command([helper, "-c", "import psutil,websocket; print('psutil + websocket-client OK')"]),
              "Install requirements-comfy.txt in an isolated environment and point mcp/comfy_bin to its Scripts directory.")
        def model_check():
            from importlib.util import spec_from_file_location, module_from_spec
            source = Path(__file__).resolve().parents[1] / "assets/template/tools/project_comfyui.py"
            spec = spec_from_file_location("doctor_comfy", source)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            model = read_json(source.parent / "comfyui/wai-model.json")
            roots = module.shared_model_roots(seed)
            candidates = [Path(root) / model["destination"] for root in roots]
            found = next((p for p in candidates if p.is_file()), None)
            if not found:
                raise ValueError("WAI checkpoint missing from configured Desktop shared model roots")
            if found.stat().st_size != model["bytes"]:
                raise ValueError("WAI size mismatch")
            if verify_model:
                import hashlib
                with found.open("rb") as stream:
                    if hashlib.file_digest(stream, "sha256").hexdigest() != model["sha256"]:
                        raise ValueError("WAI SHA-256 mismatch")
            return {"path": str(found), "hash_verified": verify_model}
        check("wai-model", True, model_check, "Configure the existing WAI checkpoint and Desktop model roots; doctor never downloads weights.")
    elif profile == "endpoint":
        def endpoint_check():
            from urllib.parse import urlparse
            url = config.get("comfyui_endpoint", {}).get("url", "").rstrip("/")
            parsed = urlparse(url)
            if parsed.scheme not in ("http", "https") or not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment:
                raise ValueError("Provide an explicit HTTP(S) ComfyUI URL without credentials/query/fragment")
            opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
            data = {}
            for path in ("system_stats", "object_info"):
                with opener.open(url + "/" + path, timeout=5) as response:
                    data[path] = json.load(response)
            if "system" not in data["system_stats"] or not data["object_info"]:
                raise ValueError("Endpoint does not expose ComfyUI system_stats and object_info")
            return {"url": url, "nodes": len(data["object_info"]), "lifecycle": "external"}
        check("comfy-endpoint", True, endpoint_check, "Start your existing server, check its URL and network access; this adapter does not start or modify it.")
    checks.append({"name": "sensory-acceptance", "status": "unverified", "required": False,
                   "detail": "Visual layout, interactive input and perceived audio require a real game/editor session and human or capable agent observation."})
    return {"schema": 1, "profile": profile, "agent": agent, "passed": all(c["status"] != "fail" for c in checks), "checks": checks}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config", type=Path)
    p.add_argument("--project", type=Path)
    p.add_argument("--profile", choices=("core", "desktop-wai", "endpoint"), default="core")
    p.add_argument("--agent", choices=("codex", "deepseek-harness", "both"), default="both")
    p.add_argument("--verify-model", action="store_true")
    p.add_argument("--report", type=Path)
    args = p.parse_args()
    try:
        result = diagnose(discover(args.config, args.project), args.profile, args.agent, args.project, args.verify_model)
    except (OSError, ValueError) as exc:
        result = {"schema": 1, "profile": args.profile, "agent": args.agent, "passed": False,
                  "checks": [{"name": "configuration", "required": True, "status": "fail", "detail": str(exc),
                              "remedy": "Correct the machine JSON file; see config.example.json and docs/windows.md."}]}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
