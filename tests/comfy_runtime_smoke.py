"""Handshake with the newly installed comfy-mcp; never contacts a model or submits a job."""
from pathlib import Path
import argparse
import json
import os
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills/godot-project-init/assets/template/tools"))
from stdio_mcp import MCPClient


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mcp", type=Path, default=ROOT / ".local/comfy-runtime/Scripts/comfy-mcp.exe")
    p.add_argument("--comfy", type=Path, default=ROOT / ".local/comfy-runtime/Scripts/comfy.exe")
    args = p.parse_args()
    (ROOT / "work").mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="comfy-protocol-", dir=ROOT / "work") as tmp:
        temp = Path(tmp).resolve()
        env = {"COMFY_NO_TELEMETRY": "1", "COMFY_PROJECT": str(temp), "COMFY_LOCAL_URL": "http://127.0.0.1:1",
               "COMFY_BIN": str(args.comfy.resolve()), "COMFY_CACHE_DIR": str(temp / "cache"),
               "USERPROFILE": str(temp), "APPDATA": str(temp / "Roaming"), "LOCALAPPDATA": str(temp / "Local"),
               "PYTHONUTF8": "1", "PYTHONDONTWRITEBYTECODE": "1", "TEMP": str(temp), "TMP": str(temp)}
        for key in ("APPDATA", "LOCALAPPDATA", "COMFY_CACHE_DIR"):
            Path(env[key]).mkdir()
        with MCPClient(args.mcp.resolve(), env=env, cwd=temp, log=temp / "stderr.log") as client:
            hello = client.initialize()
            listed = client.request("tools/list")
            names = {t["name"] for t in listed["tools"]}
            required = {"server_info", "system_stats", "nodes", "validate_workflow", "run_workflow", "job", "fetch_outputs"}
            if not required.issubset(names):
                raise ValueError("Required workflow tools missing: " + str(required - names))
            report = {"passed": True, "protocol": hello["protocolVersion"], "server": hello["serverInfo"],
                      "tools": sorted(names), "generation_requests": 0, "backend_started": False}
    (ROOT / ".local").mkdir(exist_ok=True)
    (ROOT / ".local/comfy-protocol.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
