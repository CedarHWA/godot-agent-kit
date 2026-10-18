"""Run portable regressions and retained Desktop regressions in separate processes."""
from pathlib import Path
import argparse
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--report", type=Path, default=ROOT / ".local/tests.json")
    args = p.parse_args()
    reports = []
    commands = [
        [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v"],
        [sys.executable, "-B", "skills/godot-project-init/scripts/tests/test_dev_bundle.py"],
        [sys.executable, "-B", "-m", "unittest", "discover", "-s", "skills/godot-project-init/scripts/tests", "-p", "test_desktop_instance.py", "-v"],
        [sys.executable, "-B", "skills/godot-project-init/assets/template/tests/test_comfyui_binding.py", "-v"],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240,
                                env=dict(os.environ, PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1", GODOT_INIT_TEST_TEMP=str(ROOT / "work")))
        print(result.stdout + result.stderr, flush=True)
        reports.append({"command": command[3:] if command[2] == "-m" else command[2:], "passed": result.returncode == 0,
                        "exit_code": result.returncode, "output": result.stdout + result.stderr})
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps({"passed": all(r["passed"] for r in reports), "suites": reports}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if all(r["passed"] for r in reports) else 1


if __name__ == "__main__":
    sys.exit(main())
