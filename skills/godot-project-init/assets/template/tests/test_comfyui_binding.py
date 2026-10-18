"""Regression checks for Desktop imports and Windows configuration redirection."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("project_comfyui", ROOT / "tools/project_comfyui.py")
helper = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(helper)


class DesktopBindingTests(unittest.TestCase):
    def setUp(self):
        (ROOT / "work").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="binding-test-", dir=ROOT / "work")
        self.addCleanup(self.temp.cleanup)
        self.install = Path(self.temp.name).resolve()
        self.base = self.install / "ComfyUI"
        (self.base / ".venv/Scripts").mkdir(parents=True)
        (self.base / ".venv/Scripts/python.exe").touch()
        (self.base / "main.py").touch()
        (self.install / ".comfyui-desktop-2").write_text("tracked", encoding="utf-8")
        self.owner = self.install / ".godot-project-binding.json"
        self.owner.write_text(json.dumps({"project": str(ROOT), "desktop_instance_id": "old-id"}), encoding="utf-8")
        self.record = {"id": "new-id", "sourceId": "standalone", "status": "installed",
                       "installPath": str(self.install), "useSharedInput": False,
                       "useSharedOutput": False, "browserPartition": "unique",
                       "launchArgs": "--enable-manager --port 49726"}

    def inspect(self, records=None):
        with patch.object(helper, "registry", return_value=records or [self.record]):
            return helper.installation({}, "new-id")

    def test_native_import_of_owned_environment_is_supported(self):
        self.assertEqual(self.inspect()[-1], 49726)

    def test_import_without_project_owner_is_rejected(self):
        self.owner.unlink()
        with self.assertRaisesRegex(ValueError, "unique project ownership"):
            self.inspect()

    def test_import_owned_by_another_project_is_rejected(self):
        self.owner.write_text(json.dumps({"project": str(ROOT.parent / "other-project")}), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "unique project ownership"):
            self.inspect()

    def test_duplicate_path_is_rejected(self):
        duplicate = dict(self.record, id="other-id")
        with self.assertRaisesRegex(ValueError, "unique project ownership"):
            self.inspect([self.record, duplicate])

    def test_unrelated_marker_is_rejected(self):
        (self.install / ".comfyui-desktop-2").write_text("unrelated-id", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "marker does not match"):
            self.inspect()

    def test_redirected_registry_is_rejected_before_read(self):
        with patch.object(Path, "resolve", return_value=self.install / "LocalCache/installations.json"), patch.object(helper, "read") as reader:
            with self.assertRaisesRegex(ValueError, "redirected"):
                helper.desktop_read({"desktop_data": str(self.install)}, "installations.json")
            reader.assert_not_called()

    def test_unredirected_registry_is_read(self):
        (self.install / "installations.json").write_text("[]", encoding="utf-8")
        self.assertEqual(helper.desktop_read({"desktop_data": str(self.install)}, "installations.json"), [])


if __name__ == "__main__":
    unittest.main()
