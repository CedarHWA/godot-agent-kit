from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills/godot-project-init/assets/template/tools"))
sys.path.insert(0, str(ROOT / "skills/godot-project-init/scripts"))
from host_mcp import configure
from comfy_endpoint import Endpoint
from environment import discover
from doctor import diagnose


class AdapterTests(unittest.TestCase):
    def setUp(self):
        (ROOT / "work").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="adapter-", dir=ROOT / "work")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def test_mcp_two_hosts_and_idempotence(self):
        entry = {"command": "C:/工具/python.exe", "args": ["C:/项目/tools/project_comfyui.py", "mcp"]}
        self.assertEqual(len(configure(self.root, entry, "both")), 2)
        self.assertEqual(configure(self.root, entry, "both"), [])
        patch_data = json.loads((self.root / ".dsh/comfyui.cordis.yml").read_text(encoding="utf-8"))
        self.assertEqual(patch_data[0]["insert"][0]["config"]["command"], entry["command"])

    def test_mcp_conflict_preserves_all_configs(self):
        configure(self.root, {"command": "existing"}, "codex")
        before = (self.root / ".codex/config.toml").read_bytes()
        with self.assertRaises(ValueError):
            configure(self.root, {"command": "different", "args": []}, "both")
        self.assertEqual((self.root / ".codex/config.toml").read_bytes(), before)
        self.assertFalse((self.root / ".dsh/comfyui.cordis.yml").exists())

    def test_unrelated_codex_settings_survive(self):
        path = self.root / ".codex/config.toml"
        path.parent.mkdir()
        path.write_text('model = "example"\n[mcp_servers.other]\ncommand="keep"\n')
        configure(self.root, {"command": "project"}, "codex")
        self.assertIn('command="keep"', path.read_text())

    def test_explicit_config_precedence_and_missing_config_error(self):
        config = self.root / "machine.json"
        config.write_text(json.dumps({"godot": str(self.root / "chosen.exe")}))
        with patch.dict("os.environ", {"GODOT_PATH": str(self.root / "other.exe")}):
            self.assertEqual(discover(config)["godot"], str(self.root / "chosen.exe"))
        with self.assertRaises(ValueError):
            discover(self.root / "missing.json")
        for invalid in ([], {"schema": 99}, {"comfyui_endpoint": "not an object"}):
            config.write_text(json.dumps(invalid))
            with self.assertRaises(ValueError):
                discover(config)

    def test_doctor_reports_missing_required_tools_without_starting_them(self):
        with patch("doctor.command", side_effect=OSError("missing")):
            report = diagnose({}, "core")
        self.assertFalse(report["passed"])
        self.assertTrue(any(c["name"] == "godot" and c["status"] == "fail" for c in report["checks"]))
        self.assertTrue(any(c["status"] == "unverified" for c in report["checks"]))

    def test_workflow_preflight_and_no_duplicate_submission(self):
        client = Endpoint("http://127.0.0.1:8188")
        nodes = {"Loader": {"input": {"required": {"model": [["present.safetensors"]]}}}}
        good = {"1": {"class_type": "Loader", "inputs": {"model": "present.safetensors"}}}
        bad = {"1": {"class_type": "Loader", "inputs": {"model": "missing.safetensors"}}}
        receipt = self.root / "job.json"
        with patch.object(client, "request", side_effect=[nodes, {"prompt_id": "abc", "node_errors": {}}]) as req:
            self.assertEqual(client.submit(good, receipt)["prompt_id"], "abc")
            with self.assertRaisesRegex(ValueError, "already exists"):
                client.submit(good, receipt)
            self.assertEqual(req.call_count, 2)
        with patch.object(client, "request", return_value=nodes):
            self.assertFalse(client.validate(bad)["valid"])

    def test_unknown_submission_outcome_keeps_recovery_receipt(self):
        client = Endpoint("http://127.0.0.1:8188")
        receipt = self.root / "pending.json"
        with patch.object(client, "validate", return_value={"valid": True}), patch.object(client, "request", side_effect=TimeoutError("unknown")):
            with self.assertRaises(TimeoutError):
                client.submit({"1": {}}, receipt)
        self.assertEqual(json.loads(receipt.read_text())["state"], "submitting")

    def test_server_execution_error_is_not_success(self):
        client = Endpoint("http://127.0.0.1:8188")
        with patch.object(client, "request", return_value={"id": {"status": {"status_str": "error"}}}):
            with self.assertRaisesRegex(ValueError, "execution failed"):
                client.fetch("id", self.root / "output")

    def test_endpoint_wire_protocol_and_non_overwriting_fetch(self):
        # Protocol fixture only; no model generation or game asset is claimed.
        requests = []
        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def send_payload(self, value):
                data = value if isinstance(value, bytes) else json.dumps(value).encode()
                self.send_response(200)
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def do_GET(self):
                if self.path == "/object_info":
                    self.send_payload({"Example": {"input": {"required": {}}}})
                elif self.path == "/history/job-1":
                    self.send_payload({"job-1": {"status": {"completed": True}, "outputs": {"1": {"images": [
                        {"filename": "protocol-fixture.bin", "subfolder": "", "type": "output"}]}}}})
                elif self.path.startswith("/view?"):
                    self.send_payload(b"protocol-fixture-only")
                else:
                    self.send_error(404)

            def do_POST(self):
                requests.append(json.loads(self.rfile.read(int(self.headers["Content-Length"]))))
                self.send_payload({"prompt_id": "job-1", "node_errors": {}})

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            client = Endpoint(f"http://127.0.0.1:{server.server_port}")
            workflow = {"1": {"class_type": "Example", "inputs": {}}}
            client.submit(workflow, self.root / "wire-receipt.json")
            self.assertEqual(requests, [{"prompt": workflow}])
            result = client.fetch("job-1", self.root / "wire-output")
            self.assertTrue(result["complete"])
            self.assertEqual(Path(result["files"][0]).read_bytes(), b"protocol-fixture-only")
            with self.assertRaises(FileExistsError):
                client.fetch("job-1", self.root / "wire-output")
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)


if __name__ == "__main__":
    unittest.main()
