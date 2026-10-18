"""Verify all Markdown hashes, code fences and local links in a snapshot."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def verify(root: Path):
    root = root.resolve()
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    errors = []
    checked_links = 0
    code_blocks = 0
    pages = manifest["pages"]
    anchor_map = {str((root / v["path"]).resolve()): set(v["anchors"]) for v in pages.values()}
    for item in pages.values():
        path = root / item["path"]
        if not path.is_file():
            errors.append({"file": item["path"], "error": "missing"})
            continue
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != item["markdown_sha256"]:
            errors.append({"file": item["path"], "error": "hash mismatch"})
        content = data.decode("utf-8")
        outside = []
        fence = None
        for line in content.splitlines():
            match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
            if match:
                if fence is None:
                    fence = match.group(1)
                    code_blocks += 1
                elif match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence) and not match.group(2).strip():
                    fence = None
                continue
            if fence is None:
                outside.append(line)
        if fence:
            errors.append({"file": item["path"], "error": "unclosed code fence"})
        for href in re.findall(r"\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", "\n".join(outside)):
            parts = urlsplit(href)
            if parts.scheme or parts.netloc or not parts.path.endswith(".md"):
                continue
            checked_links += 1
            dest = (path.parent / unquote(parts.path)).resolve()
            if not dest.is_relative_to(root) or not dest.is_file():
                errors.append({"file": item["path"], "error": "broken local path", "href": href})
            elif parts.fragment and unquote(parts.fragment) not in anchor_map.get(str(dest), set()):
                errors.append({"file": item["path"], "error": "broken anchor", "href": href})
    if not manifest["complete"] or len(pages) != manifest["expected_pages"]:
        errors.append({"error": "snapshot incomplete"})
    if not (root / "LICENSE-docs.txt").is_file() or not (root / "ATTRIBUTION.md").is_file():
        errors.append({"error": "license/attribution missing"})
    report = {"passed": not errors, "pages": len(pages), "checked_links": checked_links, "code_blocks": code_blocks,
              "upstream_missing_anchors": len(manifest.get("upstream_missing_anchors", [])), "errors": errors}
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    result = verify(args.path)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({**result, "errors": result["errors"][:15]}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
