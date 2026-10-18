"""Installed-package Godot smoke test and Harness overlay parse, using owned temporary projects."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from toolkit import cli


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--godot", required=True, type=Path)
    parser.add_argument("--dsh", default=shutil.which("dsh"))
    parser.add_argument("--report", type=Path, default=ROOT / ".local/integration.json")
    args = parser.parse_args()
    checks = []
    (ROOT / "work").mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="integration-", dir=ROOT / "work") as temp_name:
        temp = Path(temp_name).resolve()
        config = temp / "machine.json"
        config.write_bytes(cli.json_bytes({"schema": 1, "godot": str(args.godot.resolve()), "python": sys.executable}))
        def run(name, command, cwd=ROOT, expected=0, env=None):
            completed = subprocess.run(command, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180, env=env)
            # Evidence excludes machine-specific commands and paths.
            checks.append({"name": name, "passed": completed.returncode == expected, "exit_code": completed.returncode})
            if completed.returncode != expected:
                raise ValueError(name + "\n" + completed.stdout + completed.stderr)
            return completed.stdout

        skills = temp / "installed-skills"
        run("powershell-installer", ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(ROOT / "install.ps1"),
                                      "-Python", sys.executable, "-SkillsDir", str(skills), "-Skills", "init", "-Config", str(config)])
        installed = skills / "godot-project-init"
        project = temp / "Godot 空格项目"
        command = [sys.executable, "-B", str(installed / "scripts/init_project.py"), "--path", str(project), "--agent", "deepseek-harness"]
        first = json.loads(run("installed-init-new", command))
        if first["parameters"]["profile"] != "core":
            raise ValueError("New project profile mismatch")
        second = json.loads(run("installed-init-idempotence", command))
        if any(second["counts"][key] for key in ("create", "update", "conflict")):
            raise ValueError("Idempotence failure: " + json.dumps(second))
        run("godot-checks", ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(project / "tools/check.ps1"),
                              "-Python", sys.executable, "-IsolateEditor", "-ReportDir", "work/checks"])
        engine_report = json.loads((project / "work/checks/report.json").read_text(encoding="utf-8"))
        checks.append({"name": "godot-runtime-evidence", "passed": engine_report["passed"],
                       "checks": [{k: v for k, v in c.items() if k in ("name", "passed", "skipped", "reason")} for c in engine_report["checks"]]})
        run("offline-docs", [sys.executable, "-B", str(installed / "scripts/verify_docs.py"), "--path", str(project / "docs/godot/4.7"), "--report", str(temp / "docs-check.json")])
        run("doctor-installed", [sys.executable, "-B", str(installed / "scripts/doctor.py"), "--project", str(project), "--profile", "core"])
        original = project / "docs/requirements.md"
        original.write_text("用户需求保留。", encoding="utf-8")
        run("supplement-preserves-requirements", command)
        if original.read_text(encoding="utf-8") != "用户需求保留。":
            raise ValueError("User requirements overwritten")
        rules = project / "AGENTS.md"
        rules.write_text("User-owned rules\n", encoding="utf-8")
        result = json.loads(run("supplement-reports-conflicts", command, expected=2))
        if "AGENTS.md" not in result["conflicts"] or rules.read_text() != "User-owned rules\n":
            raise ValueError("Conflict protection failed")
        run("supplement-reviewed-keep", command + ["--keep-existing", "AGENTS.md"])
        sys.path.insert(0, str(project / "tools"))
        from host_mcp import configure
        configure(project, {"command": sys.executable, "args": [str(project / "tools/project_comfyui.py"), "mcp"]}, "deepseek-harness")
        if not args.dsh:
            checks.append({"name": "harness-overlay", "passed": False, "reason": "dsh unavailable"})
        else:
            output = run("harness-overlay", [args.dsh, "headless", "--patch", str(project / ".dsh/comfyui.cordis.yml"), "--dump-config"],
                         env=dict(os.environ, DSH_HOME=str(temp / "dsh-home")))
            if "godot-kit-comfyui" not in output or "comfyui_project" not in output:
                raise ValueError("Harness did not compose the MCP overlay")
    report = {"passed": all(c["passed"] for c in checks), "checks": checks, "temporary_directories_removed": True,
              "limitations": ["No model generation, GUI interaction or subjective audio review is claimed by this tooling smoke test."]}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_bytes(cli.json_bytes(report))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
