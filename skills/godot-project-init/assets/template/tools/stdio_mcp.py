"""Small JSON-RPC stdio probe used for integration acceptance tests (stdlib only)."""
import json
import os
import queue
import subprocess
import threading
import time


class MCPClient:
    def __init__(self, command, args=(), env=None, cwd=None, log=None):
        self.err = open(log, "w", encoding="utf-8") if log else subprocess.DEVNULL
        self.proc = subprocess.Popen(
            [str(command), *map(str, args)], stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=self.err, text=True, encoding="utf-8",
            env={**os.environ, **(env or {})}, cwd=cwd,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        self.messages = queue.Queue()
        self.counter = 0
        def reader():
            for line in self.proc.stdout:
                try:
                    self.messages.put(json.loads(line))
                except json.JSONDecodeError:
                    self.messages.put({"invalid_stdout": line.strip()})
            self.messages.put({"eof": True})
        threading.Thread(target=reader, daemon=True).start()

    def send(self, data):
        self.proc.stdin.write(json.dumps(data, ensure_ascii=False) + "\n")
        self.proc.stdin.flush()

    def request(self, method, params=None, timeout=60):
        self.counter += 1
        ident = self.counter
        self.send({"jsonrpc": "2.0", "id": ident, "method": method, "params": params or {}})
        deadline = time.monotonic() + timeout
        while True:
            item = self.messages.get(timeout=max(0.01, deadline - time.monotonic()))
            if "eof" in item or "invalid_stdout" in item:
                raise RuntimeError(item)
            if item.get("id") == ident and ("result" in item or "error" in item):
                if "error" in item:
                    raise RuntimeError(item["error"])
                return item["result"]
            if "method" in item and "id" in item:
                self.send({"jsonrpc": "2.0", "id": item["id"], "error": {
                    "code": -32601, "message": "Probe does not implement client requests"}})

    def initialize(self):
        result = self.request("initialize", {"protocolVersion": "2025-06-18",
            "capabilities": {}, "clientInfo": {"name": "godot-toolkit-acceptance", "version": "1.0"}})
        self.send({"jsonrpc": "2.0", "method": "notifications/initialized"})
        return result

    def call(self, name, arguments=None, timeout=90):
        return self.request("tools/call", {"name": name, "arguments": arguments or {}}, timeout)

    def close(self):
        self.proc.stdin.close()
        try:
            self.proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.proc.terminate()
            self.proc.wait(timeout=5)
        if self.err is not subprocess.DEVNULL:
            self.err.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
