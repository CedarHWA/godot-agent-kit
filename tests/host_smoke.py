"""Real host discovery without a model request, user credentials or global config writes."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import queue
import shutil
import subprocess
import sys
import tempfile
import threading

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from toolkit import cli


def codex_probe(executable, project, home, expected_root=None, user_home=None):
    home.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, CODEX_HOME=str(home), PYTHONDONTWRITEBYTECODE="1")
    if user_home:
        env.update(USERPROFILE=str(user_home), HOME=str(user_home))
    output = queue.Queue()
    with (home / "stderr.log").open("w", encoding="utf-8") as log:
        process = subprocess.Popen([executable, "app-server", "--stdio"], cwd=project, env=env,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=log,
                                   text=True, encoding="utf-8", creationflags=0x08000000 if os.name == "nt" else 0)
        def read():
            for line in process.stdout:
                output.put(line)
        reader = threading.Thread(target=read, daemon=True)
        reader.start()
        def request(ident, method, params):
            process.stdin.write(json.dumps({"id": ident, "method": method, "params": params}) + "\n")
            process.stdin.flush()
            for _ in range(100):
                message = json.loads(output.get(timeout=30))
                if message.get("id") == ident:
                    if "error" in message:
                        raise ValueError(message["error"])
                    return message["result"]
            raise ValueError("No matching response from Codex")
        try:
            request(1, "initialize", {"clientInfo": {"name": "godot-agent-kit-test", "version": "2.0.0"},
                                      "capabilities": {"experimentalApi": True}})
            process.stdin.write(json.dumps({"method": "initialized"}) + "\n")
            process.stdin.flush()
            result = request(2, "skills/list", {"cwds": [str(project)], "forceReload": True})
            entries = [skill for item in result["data"] for skill in item["skills"]]
            expected = {"godot-project-init", "godot-dev"}
            selected = [s for s in entries if s["name"] in expected and Path(s["path"]).is_relative_to(expected_root or project)]
            if {s["name"] for s in selected} != expected or len(selected) != 2:
                raise ValueError("Codex did not discover both project skills: " + json.dumps(result, ensure_ascii=False))
            return {"passed": True, "skills": [{"name": s["name"], "scope": s.get("scope"), "enabled": s.get("enabled")} for s in selected],
                    "errors": [e for item in result["data"] for e in item.get("errors", [])]}
        finally:
            process.stdin.close()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.terminate()
                process.wait(timeout=10)
            reader.join(timeout=5)
            process.stdout.close()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--codex", default=shutil.which("codex"))
    p.add_argument("--harness-runtime", type=Path, required=True, help="Installed DeepSeek Harness.exe or Node runtime")
    p.add_argument("--harness-module", type=Path, required=True, help="Installed dsh-skill-filesystem/lib/index.js")
    p.add_argument("--report", type=Path, default=ROOT / ".local/host-smoke.json")
    args = p.parse_args()
    (ROOT / "work").mkdir(exist_ok=True)
    reports = {}
    with tempfile.TemporaryDirectory(prefix="hosts-", dir=ROOT / "work") as tmp:
        temp = Path(tmp).resolve()
        for agent in ("codex", "deepseek-harness", "both"):
            project = temp / agent
            project.mkdir()
            (project / ".git").mkdir()  # Explicit nearest-project marker for Harness.
            skills = project / (".dsh/skills" if agent == "deepseek-harness" else ".agents/skills")
            result = cli.install(skills, list(cli.SKILLS.values()))
            if result["conflicts"]:
                raise ValueError(result)
            if agent in ("codex", "both"):
                reports[agent + ":codex"] = codex_probe(args.codex, project, temp / (agent + "-codex-home"))
            if agent in ("deepseek-harness", "both"):
                env = dict(os.environ, ELECTRON_RUN_AS_NODE="1")
                result = subprocess.run([str(args.harness_runtime), str(ROOT / "tests/harness_probe.cjs"), str(args.harness_module), str(project), str(temp / "harness-home")],
                                        cwd=project, env=env, capture_output=True, text=True, encoding="utf-8", timeout=60)
                if result.returncode:
                    raise ValueError(result.stdout + result.stderr)
                reports[agent + ":harness"] = json.loads(result.stdout)
        workspace = temp / "user-workspace"
        workspace.mkdir()
        (workspace / ".git").mkdir()
        user_home = temp / "user-home"
        cli.install(user_home / ".codex/skills", list(cli.SKILLS.values()))
        reports["user:codex"] = codex_probe(args.codex, workspace, user_home / ".codex", user_home / ".codex/skills", user_home)
        cli.install(user_home / ".dsh/skills", list(cli.SKILLS.values()))
        result = subprocess.run([str(args.harness_runtime), str(ROOT / "tests/harness_probe.cjs"), str(args.harness_module), str(workspace),
                                 str(user_home / ".dsh"), str(user_home / ".dsh/skills")], env=dict(os.environ, ELECTRON_RUN_AS_NODE="1"),
                                capture_output=True, text=True, encoding="utf-8", timeout=60)
        if result.returncode:
            raise ValueError(result.stdout + result.stderr)
        reports["user:harness"] = json.loads(result.stdout)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps({"passed": all(r["passed"] for r in reports.values()), "checks": reports,
                                      "model_requests": 0, "temporary_directories_removed": True}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(reports, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
