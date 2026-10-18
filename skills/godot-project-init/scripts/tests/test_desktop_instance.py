"""Failure regressions; real Shell/shortcut verification is separately required."""
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import desktop_instance as adapter
import desktop_launch as launcher


class DesktopVisibilityTests(unittest.TestCase):
    def setUp(self):
        scratch = Path(os.environ.get("GODOT_INIT_TEST_TEMP", Path.cwd() / "work"))
        scratch.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="desktop-regression-", dir=scratch)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.seed = {"desktop_data": str(self.root)}
        self.item = {"id": "project-id", "name": "项目 Test", "sourceId": "standalone",
                     "status": "installed", "installPath": str(self.root / "instance")}
        self.registry = self.root / "installations.json"
        self.registry.write_text(json.dumps([self.item]), encoding="utf-8")
        self.desktop = Mock(pid=123, version="1.1.7")
        self.desktop.call.return_value = [self.item]
        self.desktop.evaluate.return_value = True

    def verify(self):
        with patch.object(adapter, "native_process", return_value={"pid": 123, "package_identity": None}):
            return adapter.visibility(self.desktop, self.seed, "project-id")

    def test_same_persisted_native_and_rendered_instance(self):
        self.assertTrue(self.verify()["dashboard_name_rendered"])

    def test_only_persisted_record_is_not_visibility(self):
        self.desktop.call.return_value = []
        with self.assertRaisesRegex(ValueError, "missing/ambiguous"):
            self.verify()

    def test_same_id_different_path_is_rejected(self):
        self.desktop.call.return_value = [dict(self.item, installPath="D:/another")]
        with self.assertRaisesRegex(ValueError, "disagree"):
            self.verify()

    def test_other_workspace_is_rejected(self):
        self.item["workspaceId"] = "another-workspace"
        self.registry.write_text(json.dumps([self.item]), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "personal list"):
            self.verify()

    def test_hidden_dashboard_entry_is_rejected(self):
        self.desktop.evaluate.return_value = False
        with self.assertRaisesRegex(ValueError, "not rendered"):
            self.verify()

    def test_redirected_registry_rejected_before_read(self):
        with patch.object(Path, "resolve", return_value=self.root / "LocalCache/installations.json"), patch.object(adapter, "read") as reader:
            with self.assertRaisesRegex(ValueError, "redirected"):
                adapter.desktop_read(self.seed, "installations.json")
            reader.assert_not_called()

    def test_packaged_desktop_not_reused(self):
        with patch.object(adapter, "package_identity", return_value="MSIX-package"):
            with self.assertRaisesRegex(ValueError, "inherited package"):
                adapter.native_process(123)

    def test_alternate_profile_not_reused(self):
        proc = Mock()
        proc.cmdline.return_value = ["Desktop.exe", "--user-data-dir=D:/different"]
        with patch.object(adapter, "package_identity", return_value=None), patch.object(adapter.psutil, "Process", return_value=proc):
            with self.assertRaisesRegex(ValueError, "alternate profile"):
                adapter.native_process(123)

    def test_worker_rejects_redirection_even_without_package_identity(self):
        with patch.object(launcher, "package_identity", return_value=None), patch.object(Path, "resolve", return_value=self.root / "LocalCache/installations.json"), patch.object(launcher.subprocess, "Popen") as spawn:
            with self.assertRaisesRegex(ValueError, "redirected"):
                launcher._worker({"config_paths": [str(self.registry)]})
            spawn.assert_not_called()

    def test_missing_config_does_not_start_desktop(self):
        with patch.object(launcher, "package_identity", return_value=None), patch.object(launcher.subprocess, "Popen") as spawn:
            with self.assertRaises(FileNotFoundError):
                launcher._worker({"config_paths": [str(self.root / "missing.json")]})
            spawn.assert_not_called()


if __name__ == "__main__":
    unittest.main()
