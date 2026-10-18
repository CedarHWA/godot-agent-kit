"""Prepare a project WAI task copy and provenance; does not submit a generation."""
import copy
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--list", action="store_true")
    p.add_argument("--asset-id")
    p.add_argument("--params", type=Path)
    args = p.parse_args()
    if args.list:
        print(json.dumps({"workflow": "wai-t2i", "params": {"prompt": "required text", "negative": "optional text", "seed": "0..2^64-1", "width": "512..1344, multiple of 64", "height": "512..1344, multiple of 64", "steps": "1..40", "cfg": "1..10"}}))
        return
    if not args.params or not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,63}", args.asset_id or ""):
        p.error("Provide --params and a unique lowercase --asset-id")
    params = json.loads(args.params.read_text(encoding="utf-8"))
    if not isinstance(params, dict) or set(params) - {"prompt", "negative", "seed", "width", "height", "steps", "cfg"}:
        p.error("Unknown parameter(s)")
    if not isinstance(params.get("prompt"), str) or not params["prompt"].strip():
        p.error("Non-empty prompt is required")
    for key, low, high in (("seed", 0, 2**64-1), ("width", 512, 1344), ("height", 512, 1344), ("steps", 1, 40), ("cfg", 1, 10)):
        if key in params and (type(params[key]) not in ((int, float) if key == "cfg" else (int,)) or not low <= params[key] <= high):
            p.error(f"Invalid {key}")
    for key in ("width", "height"):
        if key in params and params[key] % 64:
            p.error(f"{key} must be a multiple of 64")
    if "negative" in params and not isinstance(params["negative"], str):
        p.error("negative must be text")
    from project_comfyui import config
    cfg = config()
    if Path(cfg["project"]).resolve() != ROOT or not cfg.get("ready"):
        p.error("Project instance is not ready or belongs to another path")
    model = cfg["model"]
    checkpoint = Path(cfg["model_storage"]["checkpoint"])
    if not checkpoint.is_file() or checkpoint.stat().st_size != model["bytes"]:
        p.error("Shared checkpoint missing or incorrect size")
    path = ROOT / "tools/comfyui/workflows/wai-t2i.api.json"
    workflow = copy.deepcopy(json.loads(path.read_text(encoding="utf-8")))
    workflow["3"]["inputs"]["text"] = params["prompt"]
    if "negative" in params:
        workflow["4"]["inputs"]["text"] = params["negative"]
    for key in ("width", "height"):
        if key in params:
            workflow["5"]["inputs"][key] = params[key]
    for key in ("seed", "steps", "cfg"):
        if key in params:
            workflow["6"]["inputs"][key] = params[key]
    workflow["8"]["inputs"]["filename_prefix"] = "wai/" + args.asset_id
    target = ROOT / "work/assets-staging" / args.asset_id
    if not target.resolve().is_relative_to(ROOT):
        p.error("Task directory escapes project")
    target.mkdir(parents=True, exist_ok=False)
    content = (json.dumps(workflow, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    workflow_path = target / "workflow.api.json"
    workflow_path.write_bytes(content)
    record = {"schema": 1, "asset_id": args.asset_id, "state": "prepared_not_submitted", "instance_id": cfg["id"],
              "server": cfg["url"], "model": model, "model_storage": cfg["model_storage"], "params": params,
              "workflow_sha256": hashlib.sha256(content).hexdigest(),
              "visual_review": "not_reviewed", "license_review": "see docs/asset-policy.json and tools/comfyui/WAI-LICENSE.md"}
    (target / "asset.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"workflow_path": str(workflow_path), "record": str(target / "asset.json")}, ensure_ascii=False))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    main()
