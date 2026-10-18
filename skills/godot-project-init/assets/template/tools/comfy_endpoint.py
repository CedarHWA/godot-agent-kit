"""Explicit existing ComfyUI API adapter. Never starts/stops servers or installs models."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import urllib.parse
import urllib.request


class Endpoint:
    def __init__(self, url):
        self.url = url.rstrip("/")
        parsed = urllib.parse.urlparse(self.url)
        if parsed.scheme not in ("http", "https") or not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment:
            raise ValueError("Explicit HTTP(S) endpoint without credentials/query/fragment required")
        self.opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

    def request(self, path, payload=None):
        data = json.dumps(payload).encode() if payload is not None else None
        req = urllib.request.Request(self.url + path, data=data, headers={"Content-Type": "application/json"} if data else {})
        with self.opener.open(req, timeout=30) as response:
            return json.load(response)

    def validate(self, workflow):
        """Node presence, required inputs, links and enum values; server validates remaining semantics on submission."""
        nodes = self.request("/object_info")
        errors = []
        if not isinstance(workflow, dict) or not workflow:
            return {"valid": False, "errors": ["Expected non-empty API prompt object, not UI workflow"]}
        for node_id, node in workflow.items():
            if not isinstance(node, dict) or node.get("class_type") not in nodes:
                errors.append(f"{node_id}: missing/unknown class_type")
                continue
            inputs = node.get("inputs", {})
            if not isinstance(inputs, dict):
                errors.append(f"{node_id}: inputs must be an object")
                continue
            schema = nodes[node["class_type"]].get("input", {})
            for name, spec in schema.get("required", {}).items():
                if name not in inputs:
                    errors.append(f"{node_id}: missing {name}")
                elif isinstance(inputs[name], list):
                    link = inputs[name]
                    if len(link) != 2 or str(link[0]) not in workflow or not isinstance(link[1], int) or link[1] < 0:
                        errors.append(f"{node_id}: invalid link {name}")
                elif isinstance(spec[0], list) and inputs[name] not in spec[0]:
                    errors.append(f"{node_id}: unavailable enum/model {name}")
        return {"valid": not errors, "errors": errors, "validation": "client preflight; server performs authoritative validation"}

    def submit(self, workflow, receipt: Path):
        # A receipt is durable recovery evidence, not a disposable temporary request.
        if receipt.exists():
            raise ValueError("Receipt already exists; query its prompt_id instead of submitting again")
        result = self.validate(workflow)
        if not result["valid"]:
            raise ValueError(json.dumps(result))
        receipt.parent.mkdir(parents=True, exist_ok=True)
        with receipt.open("x", encoding="utf-8") as stream:
            json.dump({"state": "submitting", "url": self.url, "recovery": "If outcome is unknown, inspect server queue/history before any resubmission"}, stream)
        # A transport timeout is an unknown outcome. Keep the receipt and do not auto-retry.
        result = self.request("/prompt", {"prompt": workflow})
        receipt.write_text(json.dumps({"url": self.url, **result}, indent=2) + "\n", encoding="utf-8")
        if not result.get("prompt_id") or result.get("node_errors"):
            raise ValueError(json.dumps(result))
        return result

    def fetch(self, prompt_id, output: Path):
        history = self.request("/history/" + urllib.parse.quote(prompt_id, safe=""))
        if prompt_id not in history:
            return {"complete": False, "files": []}
        job = history[prompt_id]
        if job.get("status", {}).get("status_str") == "error":
            raise ValueError("ComfyUI execution failed: " + json.dumps(job.get("status")))
        output = output.resolve()
        files = []
        for node_id, node in job.get("outputs", {}).items():
            for values in node.values():
                if not isinstance(values, list):
                    continue
                for item in values:
                    if not isinstance(item, dict) or not item.get("filename"):
                        continue
                    filename = item["filename"]
                    if Path(filename).name != filename or any(x in filename for x in ("/", "\\", ":")):
                        raise ValueError("Invalid server output filename")
                    # Flatten output into a new job directory; no overwrites or server-controlled local paths.
                    target = output / (str(len(files)) + "-" + filename)
                    if not target.resolve().is_relative_to(output):
                        raise ValueError("Output escapes destination")
                    query = urllib.parse.urlencode({k: item.get(k, "") for k in ("filename", "subfolder", "type")})
                    output.mkdir(parents=True, exist_ok=True)
                    with self.opener.open(self.url + "/view?" + query, timeout=30) as response:
                        data = response.read()
                    if not data:
                        raise ValueError("Empty server output")
                    with target.open("xb") as stream:
                        stream.write(data)
                    files.append(str(target))
        return {"complete": bool(job.get("status", {}).get("completed")), "files": files}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=("status", "nodes", "validate", "submit", "history", "fetch"))
    p.add_argument("--workflow", type=Path)
    p.add_argument("--receipt", type=Path)
    p.add_argument("--prompt-id")
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    root = Path(__file__).resolve().parents[1]
    config = json.loads((root / ".local/comfyui-endpoint.json").read_text(encoding="utf-8"))
    client = Endpoint(config["url"])
    workflow = json.loads(args.workflow.read_text(encoding="utf-8")) if args.workflow else None
    if args.action == "status":
        result = {"url": client.url, "lifecycle": "external", "stats": client.request("/system_stats")}
    elif args.action == "nodes":
        result = client.request("/object_info")
    elif args.action == "validate":
        result = client.validate(workflow)
    elif args.action == "submit":
        if not args.receipt:
            p.error("submit requires --receipt")
        result = client.submit(workflow, args.receipt)
    else:
        if not args.prompt_id:
            p.error("history/fetch requires --prompt-id")
        if args.action == "fetch" and not args.output:
            p.error("fetch requires --output")
        result = client.fetch(args.prompt_id, args.output) if args.action == "fetch" else client.request("/history/" + urllib.parse.quote(args.prompt_id, safe=""))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result.get("valid") is False else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        sys.exit(main())
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
