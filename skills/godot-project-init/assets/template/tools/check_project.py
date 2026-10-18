"""Run real Godot validation and retain honest, machine-readable results."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--godot")
    parser.add_argument("--skip-lint", action="store_true")
    parser.add_argument("--isolate-editor", action="store_true", help="Copy the standard Windows editor into temporary project storage; avoid portable editor settings")
    parser.add_argument("--test-script", action="append", default=[])
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--report-dir", type=Path, help="Project-local directory for this run's logs, report and temporary engine data")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    local_path = root / ".local/toolchain.json"
    local = json.loads(local_path.read_text(encoding="utf-8")) if local_path.exists() else {}
    godot = args.godot or os.environ.get("GODOT_PATH") or local.get("godot") or shutil.which("godot") or shutil.which("godot4")
    if not godot:
        parser.error("Set --godot / GODOT_PATH / .local/toolchain.json to the matching executable")
    logs = (root / (args.report_dir or ".local/checks")).resolve()
    if logs == root or not logs.is_relative_to(root):
        parser.error("--report-dir must stay inside the project, including symlink targets")
    logs.mkdir(parents=True, exist_ok=True)
    isolated_editor = None
    if args.isolate_editor:
        original = Path(godot).resolve()
        if os.name != "nt" or original.suffix.lower() != ".exe":
            parser.error("--isolate-editor currently supports the standard Windows Godot build")
        isolated_editor = tempfile.TemporaryDirectory(prefix="godot-engine-", dir=logs)
        isolated_path = Path(isolated_editor.name)
        shutil.copy2(original, isolated_path / original.name)
        if original.name.endswith("_console.exe"):
            executable = original.with_name(original.name.replace("_console.exe", ".exe"))
            shutil.copy2(executable, isolated_path / executable.name)
        godot = str(isolated_path / original.name)
    env = dict(os.environ)
    # Confine test game user data/cache to the project, not the user's game saves.
    for key in ("APPDATA", "LOCALAPPDATA", "XDG_DATA_HOME", "XDG_CONFIG_HOME", "XDG_CACHE_HOME"):
        folder = logs / "engine-home" / key.lower()
        folder.mkdir(parents=True, exist_ok=True)
        env[key] = str(folder)
    results = []

    def run(name: str, command: list[str], marker: str | None = None):
        try:
            process = subprocess.run(command, cwd=root, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=args.timeout)
            output = process.stdout + process.stderr
            engine_error = bool(re.search(r"(?m)^\s*(SCRIPT ERROR:|ERROR:|Parse Error:)", output))
            passed = process.returncode == 0 and not engine_error and (not marker or marker in output)
            result = {"name": name, "passed": bool(passed), "exit_code": process.returncode, "error_in_log": engine_error, "command": command}
        except subprocess.TimeoutExpired as error:
            output = "Timed out\n" + str(error.stdout or "") + str(error.stderr or "")
            result = {"name": name, "passed": False, "reason": "timeout", "command": command}
        except OSError as error:
            output = str(error)
            result = {"name": name, "passed": False, "reason": str(error), "command": command}
        (logs / (name + ".log")).write_text(output, encoding="utf-8")
        results.append(result)
        print(f"{name}: {'PASS' if result['passed'] else 'FAIL'}", flush=True)
        if not result["passed"]:
            print(output[-5000:], flush=True)
        return result["passed"], output

    passed, version = run("engine-version", [godot, "--version"])
    expected = "__ENGINE_VERSION__"
    state_file = root / ".bootstrap/state.json"
    if state_file.exists():
        expected = json.loads(state_file.read_text(encoding="utf-8"))["parameters"]["engine_version"]
    if passed and not version.strip().startswith(expected + "."):
        results[-1].update({"passed": False, "reason": f"Expected {expected}, got {version.strip()}"})
        passed = False
        print(results[-1]["reason"])
    ignored = {".godot", ".local", ".bootstrap", ".agents", "docs", "tools", "work", "addons", ".venv", "builds"}
    scripts = [str(p.relative_to(root)) for p in root.rglob("*.gd") if not any(x in ignored for x in p.relative_to(root).parts)]
    if not args.skip_lint and scripts:
        for tool in ("gdformat", "gdlint"):
            candidate = Path(sys.executable).parent / (tool + (".exe" if os.name == "nt" else ""))
            executable = str(candidate) if candidate.is_file() else shutil.which(tool)
            if executable is None:
                results.append({"name": tool, "passed": False, "reason": "Install pinned gdtoolkit in this Python environment, or explicitly use --skip-lint"})
                continue
            for start in range(0, len(scripts), 80):
                command = [executable] + (["--check"] if tool == "gdformat" else []) + scripts[start:start + 80]
                run(f"{tool}-{start // 80}", command)
    if args.skip_lint:
        results.append({"name": "lint", "skipped": True, "reason": "Explicit --skip-lint"})
    if passed:
        imported, _ = run("import", [godot, "--headless", "--path", str(root), "--editor", "--import"])
        if imported:
            if (root / "docs/editor-contract.json").exists() and (root / "tools/check_editor_structure.gd").exists():
                run("editor-structure", [godot, "--headless", "--path", str(root), "--script", "res://tools/check_editor_structure.gd"], "EDITOR_STRUCTURE_OK")
            else:
                results.append({"name": "editor-structure", "skipped": True, "reason": "No editor contract/checker; editor maintainability has not been checked"})
            tests = list(args.test_script)
            if (root / "tests/smoke_test.gd").exists():
                tests.insert(0, "res://tests/smoke_test.gd")
            for i, script in enumerate(tests):
                run(f"test-{i}", [godot, "--headless", "--path", str(root), "--script", script], "SMOKE_OK" if script == "res://tests/smoke_test.gd" else None)
            if (root / "tests/test_runtime.gd").exists():
                run("runtime", [godot, "--headless", "--path", str(root), "--script", "res://tests/test_runtime.gd"], "GAME_SHUTDOWN_OK")
            else:
                run("runtime", [godot, "--headless", "--path", str(root), "--quit-after", "90"])
    report = {"passed": all(r.get("passed", True) for r in results), "checks": results,
              "limitations": ["Headless does not verify visuals, interactive input or perceived audio quality.", "Only selected test scripts are executed."]}
    (logs / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Report: {logs / 'report.json'}")
    if isolated_editor is not None:
        isolated_editor.cleanup()
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
