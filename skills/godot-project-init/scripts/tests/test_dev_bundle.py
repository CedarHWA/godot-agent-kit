"""Offline tests of actual initializer plans; never provisions ComfyUI or runs upstream code."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import init_project

TEST_ROOT = Path.cwd() / "work/dev-skill-validation"


def args_for(path: Path, **changes):
    values = dict(path=path, mode="auto", name=None, codex_project_name=None,
                  dimension=None, engine_version=None, renderer=None, platform=None,
                  godot=None, keep_existing=[], dry_run=True, desktop_instance=None)
    values.update(changes)
    return argparse.Namespace(**values)


def check_local_links(desired: dict[str, bytes]):
    """Resolve installed skill links against the generated bundle, not source layout."""
    prefix = ".agents/skills/godot-dev/"
    for rel, data in desired.items():
        if not rel.startswith(prefix) or not rel.endswith(".md"):
            continue
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", data.decode("utf-8")):
            if "://" in link or link.startswith("#"):
                continue
            target = (Path(rel).parent / link.split("#", 1)[0]).as_posix()
            if target not in desired:
                raise ValueError(f"Broken installed skill link: {rel} -> {target}")


class DevBundleTests(unittest.TestCase):
    def setUp(self):
        TEST_ROOT.mkdir(parents=True, exist_ok=True)
        temporary = Path(tempfile.mkdtemp(prefix="bundle-", dir=TEST_ROOT)).resolve()
        def cleanup():
            if temporary.parent != TEST_ROOT.resolve() or temporary.is_symlink() or getattr(temporary.stat(follow_symlinks=False), "st_file_attributes", 0) & 0x400:
                raise ValueError("Test cleanup target escaped its workspace")
            shutil.rmtree(temporary)
        self.addCleanup(cleanup)
        self.path = temporary / "project"
        self.result = init_project.build_plan(args_for(self.path))

    def materialize(self):
        _, _, config, desired, _, _ = self.result
        for relative, data in desired.items():
            target = self.path / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        (self.path / ".bootstrap/state.json").write_text(json.dumps({
            "schema": 1, "bootstrap_version": "1.8.0", "parameters": config,
            "files": {rel: init_project.digest(data) for rel, data in desired.items()},
        }), encoding="utf-8")
        return desired

    def test_new_project_contains_full_recursive_skill(self):
        desired = self.result[3]
        source = init_project.dev_source()
        for path in source.rglob("*"):
            if not path.is_file() or "__pycache__" in path.parts:
                continue
            relative = path.relative_to(source).as_posix()
            if relative == "SKILL.md.template":
                relative = "SKILL.md"
            self.assertEqual(path.read_bytes(), desired[".agents/skills/godot-dev/" + relative])
        self.assertNotIn(".agents/skills/godot-dev/SKILL.md.template", desired)
        check_local_links(desired)

    def test_missing_nested_reference_is_detected(self):
        desired = dict(self.result[3])
        del desired[".agents/skills/godot-dev/references/scene-and-resource-design.md"]
        with self.assertRaises(ValueError):
            check_local_links(desired)

    def test_materialized_new_project_is_idempotent(self):
        self.materialize()
        result = init_project.build_plan(args_for(self.path, mode="new"))
        self.assertTrue(all(item["action"] == "unchanged" for item in result[4]))

    def test_new_entry_resolves_scene_and_separate_script(self):
        desired = self.result[3]
        config = desired["project.godot"].decode("utf-8")
        main_path = re.search(r'run/main_scene="res://([^"\n]+)"', config).group(1)
        self.assertEqual(main_path, "scenes/main/main.tscn")
        scene = desired[main_path].decode("utf-8")
        script_path = re.search(r'type="Script" path="res://([^"\n]+)"', scene).group(1)
        self.assertEqual(script_path, "scripts/main/main.gd")
        self.assertIn(script_path, desired)
        self.assertFalse(any(rel.startswith("main/") for rel in desired))
        contract = json.loads(desired["docs/editor-contract.json"])
        self.assertEqual(contract["scenes"][0]["path"], "res://" + main_path)

    def test_supplement_keeps_existing_entry_in_another_layout(self):
        self.path.mkdir(parents=True)
        original = b'config_version=5\n[application]\nrun/main_scene="res://custom/start.tscn"\n'
        (self.path / "project.godot").write_bytes(original)
        desired = init_project.build_plan(args_for(self.path))[3]
        self.assertNotIn("project.godot", desired)
        self.assertFalse(any(rel.startswith(("main/", "scenes/", "scripts/", "resources/", "assets/", "tests/")) for rel in desired))
        self.assertEqual((self.path / "project.godot").read_bytes(), original)

    def test_supplement_preserves_game_and_contract(self):
        self.materialize()
        desired = init_project.build_plan(args_for(self.path))[3]
        self.assertNotIn("project.godot", desired)
        for rel in ("docs/requirements.md", "docs/architecture.md", "docs/editor-contract.json"):
            self.assertNotIn(rel, desired)
        self.assertFalse(any(rel.startswith(("main/", "scenes/", "scripts/", "resources/", "assets/", "tests/")) for rel in desired))
        check_local_links(desired)

    def test_user_edited_topic_is_a_conflict(self):
        self.materialize()
        rel = ".agents/skills/godot-dev/references/ui-and-input.md"
        (self.path / rel).write_text("User's own layout contract\n", encoding="utf-8")
        plan = init_project.build_plan(args_for(self.path))[4]
        self.assertEqual(next(item["action"] for item in plan if item["path"] == rel), "conflict")
        self.assertEqual((self.path / rel).read_text(encoding="utf-8"), "User's own layout contract\n")

    def test_reviewed_keep_existing_is_preserved(self):
        self.materialize()
        rel = ".agents/skills/godot-dev/references/ui-and-input.md"
        (self.path / rel).write_text("Reviewed custom topic\n", encoding="utf-8")
        plan = init_project.build_plan(args_for(self.path, keep_existing=[rel]))[4]
        self.assertEqual(next(item["action"] for item in plan if item["path"] == rel), "preserve")

    def test_owned_old_topic_is_updatable(self):
        self.materialize()
        rel = ".agents/skills/godot-dev/SKILL.md"
        old = b"old managed skill\n"
        (self.path / rel).write_bytes(old)
        state_path = self.path / ".bootstrap/state.json"
        state = json.loads(state_path.read_text(encoding="utf-8"))
        state["files"][rel] = init_project.digest(old)
        state_path.write_text(json.dumps(state), encoding="utf-8")
        plan = init_project.build_plan(args_for(self.path))[4]
        self.assertEqual(next(item["action"] for item in plan if item["path"] == rel), "update")

    def test_sources_are_pinned_and_no_upstream_scripts_installed(self):
        desired = self.result[3]
        sources = json.loads(desired[".agents/skills/godot-dev/references/sources.json"])
        self.assertGreater(len(sources["repositories"]), 0)
        for source in sources["repositories"]:
            self.assertRegex(source["commit"], r"^[0-9a-f]{40}$")
            self.assertFalse(source["vendored_code_or_text"])
            for item in source["retrieved_files"]:
                self.assertIn(source["commit"], item["url"])
                self.assertRegex(item["sha256"], r"^[0-9a-f]{64}$")
        skill_files = [p for p in desired if p.startswith(".agents/skills/godot-dev/")]
        self.assertFalse(any(p.endswith((".gd", ".py", ".ps1", ".sh")) for p in skill_files))

    def run_wrapper(self, extra):
        powershell = shutil.which("powershell") or shutil.which("pwsh")
        if not powershell:
            self.skipTest("PowerShell unavailable; wrapper forwarding not tested")
        tools = self.path / "tools"
        tools.mkdir(parents=True)
        (tools / "check.ps1").write_bytes(self.result[3]["tools/check.ps1"])
        # A child process records arguments only. Real Godot checks are separate integration tests.
        (tools / "check_project.py").write_text(
            "import json, sys\nfrom pathlib import Path\n"
            "Path(__file__).with_name('received.json').write_text(json.dumps(sys.argv[1:]), encoding='utf-8')\n",
            encoding="utf-8",
        )
        result = subprocess.run([powershell, "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
                                 str(tools / "check.ps1"), "-Python", sys.executable] + extra,
                                capture_output=True, timeout=20)
        return result, tools / "received.json"

    def test_wrapper_forwards_selected_behavior_test(self):
        result, received = self.run_wrapper(["-TestScript", "res://tests/selected.gd"])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(received.read_text(encoding="utf-8")),
                         ["--test-script", "res://tests/selected.gd"])

    def test_wrapper_rejects_unknown_flag_before_running_checks(self):
        result, received = self.run_wrapper(["-MisspelledTestScript", "res://tests/selected.gd"])
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(received.exists())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--work-root", type=Path, default=TEST_ROOT)
    options, unittest_args = parser.parse_known_args()
    TEST_ROOT = options.work_root.resolve()
    if TEST_ROOT == Path(TEST_ROOT.anchor) or len(TEST_ROOT.parts) < 3:
        parser.error("Use a dedicated task directory below the workspace, not a drive root")
    unittest.main(argv=[sys.argv[0]] + unittest_args, verbosity=2)
