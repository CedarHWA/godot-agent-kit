from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from toolkit import cli
import init_project


class OwnedTemporary(unittest.TestCase):
    def setUp(self):
        (ROOT / "work").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="distribution-", dir=ROOT / "work")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()


class InstallTests(OwnedTemporary):
    def payload(self, version="one"):
        return {"godot-dev/SKILL.md": version.encode(), "godot-dev/references/topic.md": b"reference"}

    def apply(self, version="one", dry=False):
        with patch.object(cli, "bundle", return_value=self.payload(version)):
            return cli.install(self.root, ["godot-dev"], dry_run=dry)

    def test_install_and_idempotence(self):
        self.assertTrue(self.apply()["applied"])
        history = cli.state_for(self.root)["history"]
        self.assertEqual(self.apply()["changed"], 0)
        self.assertEqual(cli.state_for(self.root)["history"], history)

    def test_dry_run_no_mutation(self):
        self.assertFalse(self.apply(dry=True)["applied"])
        self.assertEqual(list(self.root.iterdir()), [])

    def test_upgrade_and_rollback_restores_bytes_and_receipt(self):
        self.apply()
        previous = cli.state_for(self.root)
        update = self.apply("two")
        self.assertEqual((self.root / "godot-dev/SKILL.md").read_text(), "two")
        self.assertTrue(cli.restore(self.root, update["transaction"])["restored"])
        self.assertEqual((self.root / "godot-dev/SKILL.md").read_text(), "one")
        self.assertEqual(cli.state_for(self.root), previous)

    def test_user_edits_preserved_and_no_partial_upgrade(self):
        self.apply()
        file = self.root / "godot-dev/SKILL.md"
        file.write_text("user instructions", encoding="utf-8")
        result = self.apply("two")
        self.assertFalse(result["applied"])
        self.assertEqual(file.read_text(), "user instructions")
        self.assertEqual((self.root / ".godot-agent-kit/proposals/godot-dev/SKILL.md").read_text(), "two")

    def test_rollback_refuses_later_user_edit(self):
        first = self.apply()
        (self.root / "godot-dev/SKILL.md").write_text("user")
        self.assertFalse(cli.restore(self.root, first["transaction"])["restored"])

    def test_uninstall_preserves_modified_and_unmanaged_files(self):
        self.apply()
        (self.root / "godot-dev/SKILL.md").write_text("user")
        (self.root / "godot-dev/mine.txt").write_text("mine")
        result = cli.uninstall(self.root, ["godot-dev"])
        self.assertEqual(result["preserved"], ["godot-dev/SKILL.md"])
        self.assertFalse((self.root / "godot-dev/references/topic.md").exists())
        self.assertTrue((self.root / "godot-dev/mine.txt").exists())

    def test_identical_unmanaged_file_is_never_claimed(self):
        file = self.root / "godot-dev/SKILL.md"
        file.parent.mkdir()
        file.write_bytes(b"one")
        self.apply()
        self.assertNotIn("godot-dev/SKILL.md", cli.state_for(self.root)["files"])
        cli.uninstall(self.root, ["godot-dev"])
        self.assertEqual(file.read_bytes(), b"one")

    def test_failure_rolls_back_written_files(self):
        real_write = cli.write
        failed = False
        def interrupted(path, data):
            nonlocal failed
            if path == self.root / "godot-dev/references/topic.md" and not failed:
                failed = True
                raise OSError("simulated write failure")
            return real_write(path, data)
        with patch.object(cli, "write", side_effect=interrupted):
            with self.assertRaises(OSError):
                self.apply()
        self.assertFalse((self.root / "godot-dev/SKILL.md").exists())
        self.assertEqual(cli.state_for(self.root)["files"], {})
        self.assertFalse((self.root / ".godot-agent-kit/pending.json").exists())

    def test_corrupt_backup_is_detected_before_any_restore(self):
        self.apply()
        update = self.apply("two")
        backup = self.root / (".godot-agent-kit/history/" + update["transaction"] + "/files/godot-dev/SKILL.md")
        backup.write_bytes(b"broken")
        with self.assertRaisesRegex(ValueError, "Corrupt"):
            cli.restore(self.root, update["transaction"])
        self.assertEqual((self.root / "godot-dev/SKILL.md").read_text(), "two")

    def test_receipt_cannot_escape_skill_roots(self):
        cli.write(self.root / ".godot-agent-kit/state.json", cli.json_bytes({"schema": 1, "files": {"../../escape": "bad"}}))
        with self.assertRaises(ValueError):
            self.apply()

    def test_parent_traversal_and_drive_absolute_paths_rejected(self):
        for path in ("../out", "C:/out", "godot-dev/../../out", "godot-dev\\..\\out"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                cli.inside(self.root, path)

    @unittest.skipUnless(os.name == "nt", "Windows junction test")
    def test_junction_target_rejected(self):
        target = self.root / "elsewhere"
        target.mkdir()
        link = self.root / "linked"
        command = f"New-Item -ItemType Junction -Path '{link}' -Target '{target}' | Out-Null"
        subprocess.run(["powershell", "-NoProfile", "-Command", command], check=True, capture_output=True)
        try:
            with self.assertRaisesRegex(ValueError, "reparse"):
                cli.checked(link / "skills")
        finally:
            link.rmdir()

    def test_full_init_distribution_contains_canonical_dev(self):
        payload = cli.bundle(["godot-project-init"])
        for rel, data in cli.bundle(["godot-dev"]).items():
            embedded = rel + ".template" if rel == "godot-dev/SKILL.md" else rel
            self.assertEqual(payload["godot-project-init/assets/" + embedded], data)
        self.assertNotIn("godot-project-init/local.json", payload)
        self.assertIn("godot-project-init/scripts/doctor.py", payload)

    def test_host_scope_mapping(self):
        (self.root / ".git").mkdir()
        args = argparse.Namespace(skills_dir=None, scope="project", project=self.root, agent="deepseek-harness")
        self.assertEqual(cli.target_root(args), self.root / ".dsh/skills")
        args.agent = "both"
        self.assertEqual(cli.target_root(args), self.root / ".agents/skills")
        args.scope, args.agent = "user", "deepseek-harness"
        with patch.dict(os.environ, {"DSH_HOME": str(self.root / "home")}):
            self.assertEqual(cli.target_root(args), self.root / "home/skills")
        args.agent = "codex"
        with patch.dict(os.environ, {"CODEX_HOME": str(self.root / "codex-home")}):
            self.assertEqual(cli.target_root(args), self.root / "codex-home/skills")

    def test_harness_subproject_cannot_install_to_an_invisible_root(self):
        (self.root / ".git").mkdir()
        args = argparse.Namespace(skills_dir=None, scope="project", project=self.root / "subgame", agent="deepseek-harness")
        with self.assertRaisesRegex(ValueError, "Harness resolves"):
            cli.target_root(args)


def init_args(path, **kw):
    values = dict(path=path, mode="auto", name=None, codex_project_name=None,
                  dimension=None, engine_version=None, renderer=None, platform=None,
                  godot=None, keep_existing=[], dry_run=True, desktop_instance=None,
                  profile="core", agent="codex", config=None, docs_mode="online")
    values.update(kw)
    return argparse.Namespace(**values)


class InitializerTests(OwnedTemporary):
    def test_core_no_comfy_config_or_weights(self):
        plan = init_project.build_plan(init_args(self.root / "project"))
        desired = plan[3]
        self.assertNotIn(".local/comfyui-bootstrap.json", desired)
        self.assertFalse(any(p.startswith("tools/comfyui/") for p in desired))
        self.assertTrue(json.loads(desired[".bootstrap/assets-lock.json"])["model"] is None)

    def test_harness_project_has_resolvable_skill_and_rules(self):
        desired = init_project.build_plan(init_args(self.root / "project", agent="deepseek-harness"))[3]
        self.assertIn(".dsh/skills/godot-dev/SKILL.md", desired)
        self.assertIn(b".dsh/skills/godot-dev/SKILL.md", desired["AGENTS.md"])
        self.assertNotIn(".agents/skills/godot-dev/SKILL.md", desired)

    def test_missing_desktop_tools_is_an_error(self):
        with patch("init_project.discover", return_value={"python": sys.executable}), self.assertRaisesRegex(ValueError, "Comfy Desktop"):
            init_project.build_plan(init_args(self.root / "project", profile="desktop-wai"))

    def test_desktop_profile_preserves_wai_workflows(self):
        config = {"python": sys.executable, "comfyui_bootstrap": {k: "C:/test/" + k for k in ("desktop_exe", "desktop_data", "mcp", "comfy_bin")}}
        with patch("init_project.discover", return_value=config):
            desired = init_project.build_plan(init_args(self.root / "project", profile="desktop-wai"))[3]
        self.assertIn("tools/comfyui/workflows/wai-t2i.api.json", desired)
        self.assertIn("tools/comfyui/workflows/wai-t2i.ui.json", desired)
        self.assertIn(".local/comfyui-bootstrap.json", desired)

    def test_different_engine_version_never_silent_migration(self):
        project = self.root / "project"
        project.mkdir()
        (project / "project.godot").write_text('config_version=5\n[application]\nconfig/features=PackedStringArray("4.5")\n')
        with self.assertRaisesRegex(ValueError, "migration"):
            init_project.build_plan(init_args(project))
        desired = init_project.build_plan(init_args(project, engine_version="4.5.2"))[3]
        self.assertNotIn("project.godot", desired)
        self.assertIn(b"en/4.5/", desired["docs/godot/README.md"])

    def test_online_document_links_point_at_selected_version(self):
        desired = init_project.build_plan(init_args(self.root / "project", engine_version="4.5.2"))[3]
        self.assertIn(b"https://docs.godotengine.org/en/4.5/", desired["docs/development.md"])
        self.assertNotIn(b"](godot/", desired["docs/development.md"])
        self.assertNotIn(b"CATALOG.md", desired["AGENTS.md"])

    def test_existing_profile_requires_explicit_migration(self):
        project = self.root / "project"
        (project / ".bootstrap").mkdir(parents=True)
        (project / ".bootstrap/state.json").write_text(json.dumps({"parameters": {"profile": "desktop-wai"}}))
        with self.assertRaisesRegex(ValueError, "migrate-profile"):
            init_project.build_plan(init_args(project))

    def test_endpoint_requires_explicit_valid_url(self):
        for url in ("", "file:///etc/passwd", "http://user:secret@localhost:8188"):
            with patch("init_project.discover", return_value={"comfyui_endpoint": {"url": url}}), self.assertRaises(ValueError):
                init_project.build_plan(init_args(self.root / "project", profile="endpoint"))


class UserCliTests(OwnedTemporary):
    def test_both_user_install_and_rollback_with_isolated_homes(self):
        env = dict(os.environ, CODEX_HOME=str(self.root / "codex"), DSH_HOME=str(self.root / "dsh"), PYTHONUTF8="1")
        command = [sys.executable, "-B", str(ROOT / "toolkit/cli.py")]
        install = subprocess.run(command + ["install", "--agent", "both", "--scope", "user", "--skills", "dev"], env=env, capture_output=True, text=True, encoding="utf-8", timeout=30)
        self.assertEqual(install.returncode, 0, install.stderr)
        report = json.loads(install.stdout)
        self.assertEqual(len(report["roots"]), 2)
        for directory in ("codex", "dsh"):
            self.assertTrue((self.root / directory / "skills/godot-dev/SKILL.md").is_file())
        rollback = subprocess.run(command + ["rollback", "--agent", "both", "--scope", "user"], env=env, capture_output=True, text=True, encoding="utf-8", timeout=30)
        self.assertEqual(rollback.returncode, 0, rollback.stderr)
        for directory in ("codex", "dsh"):
            self.assertFalse((self.root / directory / "skills/godot-dev/SKILL.md").exists())

    def test_recover_incomplete_transaction(self):
        with patch.object(cli, "bundle", return_value={"godot-dev/SKILL.md": b"old"}):
            cli.install(self.root, ["godot-dev"])
        with patch.object(cli, "bundle", return_value={"godot-dev/SKILL.md": b"new"}):
            changed = cli.install(self.root, ["godot-dev"])
        # Recreate the crash window after data writes but before pending is cleared.
        cli.write(self.root / ".godot-agent-kit/pending.json", cli.json_bytes({"id": changed["transaction"]}))
        command = [sys.executable, "-B", str(ROOT / "toolkit/cli.py"), "recover", "--skills-dir", str(self.root)]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / "godot-dev/SKILL.md").read_bytes(), b"old")
        self.assertFalse((self.root / ".godot-agent-kit/pending.json").exists())


if __name__ == "__main__":
    unittest.main()
