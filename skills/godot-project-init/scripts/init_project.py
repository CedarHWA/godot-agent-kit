"""Idempotent Godot project bootstrap. Standard library only; no network access."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import subprocess
from pathlib import Path
from comfy_plan import baseline
from environment import discover

SKILL_ROOT = Path(__file__).resolve().parents[1]
ASSETS = SKILL_ROOT / "assets"


def dev_source():
    if (ASSETS / "godot-dev/SKILL.md.template").is_file():
        return ASSETS / "godot-dev"
    canonical = SKILL_ROOT.parent / "godot-dev"
    return canonical if (canonical / "SKILL.md").is_file() else ASSETS / "godot-dev"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else default


def safe_path(root: Path, relative: str) -> Path:
    path = root / relative
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes project (including symlinks): {relative}")
    return path


def build_plan(args):
    target = args.path.resolve()
    if len(target.parts) < 3 or target == Path(target.anchor):
        raise ValueError("Do not create files/folders directly in a drive root; choose an existing parent folder.")
    ancestor = target
    while not ancestor.exists() and ancestor != ancestor.parent:
        ancestor = ancestor.parent
    if ancestor == Path(target.anchor):
        raise ValueError("Creating this target would create a new folder in the drive root; choose an existing parent directory below the drive root.")
    state_path = safe_path(target, ".bootstrap/state.json")
    state = read_json(state_path, {})
    mode = args.mode
    if mode == "auto":
        mode = "supplement" if (target / "project.godot").is_file() else "new"
    if args.mode == "new" and target.exists() and any(target.iterdir()) and not state:
        raise ValueError("Target is not empty. Use --mode auto to preserve existing files, or supplement for an existing Godot project.")
    if mode == "supplement" and not (target / "project.godot").is_file():
        raise ValueError("Supplement requires an existing project.godot")
    config = dict(state.get("parameters", {}))
    requested_profile = getattr(args, "profile", None)
    current_profile = config.get("profile") or ("desktop-wai" if (target / ".local/comfyui-instance.json").exists() else None)
    if requested_profile and current_profile and requested_profile != current_profile and not getattr(args, "migrate_profile", False):
        raise ValueError("Changing asset profile requires --migrate-profile; existing instances/files are preserved")
    profile_id = requested_profile or current_profile or "core"
    profile = read_json(ASSETS / "profiles" / (profile_id + ".json"), {})
    if not profile:
        raise ValueError(f"Unknown profile: {profile_id}")
    config["profile"] = profile_id
    config["agent"] = getattr(args, "agent", None) or config.get("agent", "codex")
    existing_config = ""
    if mode == "supplement":
        existing_config = (target / "project.godot").read_text(encoding="utf-8-sig")
        name_match = re.search(r'^config/name\s*=\s*("(?:[^"\\]|\\.)*")', existing_config, re.MULTILINE)
        if name_match and "name" not in config:
            config["name"] = json.loads(name_match.group(1))
    for key, value in {"name": args.name, "dimension": args.dimension, "engine_version": args.engine_version, "renderer": args.renderer, "platform": args.platform}.items():
        if value is not None:
            config[key] = value
    config.setdefault("name", target.name)
    if args.codex_project_name is not None:
        config["codex_project_name"] = args.codex_project_name
    config.setdefault("codex_project_name", config["name"])
    if not isinstance(config["codex_project_name"], str) or not config["codex_project_name"].strip() or config["codex_project_name"] != config["codex_project_name"].strip():
        raise ValueError("Provide the exact, non-empty Codex project display name")
    for key in ("dimension", "engine_version", "renderer", "platform"):
        config.setdefault(key, profile[key])
    if not re.fullmatch(r"\d+\.\d+\.\d+", config["engine_version"]):
        raise ValueError("engine-version must be a pinned major.minor.patch")
    docs_version = ".".join(config["engine_version"].split(".")[:2])
    if mode == "supplement":
        features = re.search(r'config/features\s*=\s*PackedStringArray\("(\d+\.\d+)"', existing_config)
        if features and features.group(1) != docs_version:
            raise ValueError(f"Existing project declares Godot {features.group(1)}, requested docs {docs_version}; migration must be explicit")
    docs_mode = getattr(args, "docs_mode", None) or config.get("docs_mode", "bundled")
    config["docs_mode"] = docs_mode
    docs_root = getattr(args, "docs_root", None) or ASSETS / "docs" / "godot" / docs_version
    manifest = read_json(docs_root / "manifest.json", {})
    if docs_mode == "bundled" and (not manifest.get("complete") or manifest.get("docs_version") != docs_version):
        raise ValueError(f"A complete, matching documentation snapshot is required: {docs_root}")
    config["docs_version"] = docs_version
    replacements = {
        "__PROJECT_NAME__": config["name"],
        "__PROJECT_NAME_JSON__": json.dumps(config["name"], ensure_ascii=False),
        "__ENGINE_VERSION__": config["engine_version"],
        "__DOCS_VERSION__": docs_version,
        "__WORLD_TYPE__": "Node3D" if config["dimension"] == "3d" else "Node2D",
        "__RENDERER__": config["renderer"],
        "__RENDERER_FEATURE__": {"gl_compatibility": "GL Compatibility", "mobile": "Mobile", "forward_plus": "Forward Plus"}[config["renderer"]],
        "__PLATFORM__": config["platform"],
        "__SKILL_ROOT__": ".dsh/skills" if config["agent"] == "deepseek-harness" else ".agents/skills",
    }
    desired = {}
    for path in sorted((ASSETS / "template").rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        rel = path.relative_to(ASSETS / "template").as_posix()
        if profile_id != "desktop-wai" and (rel.startswith("tools/comfyui/") or rel == "tests/test_comfyui_binding.py"):
            continue
        if mode == "supplement" and (rel == "project.godot" or rel.startswith(("main/", "scenes/", "scripts/", "resources/", "assets/", "tests/")) or rel in ("docs/requirements.md", "docs/architecture.md", "docs/editor-contract.json")):
            continue
        text = path.read_text(encoding="utf-8")
        for before, after in replacements.items():
            text = text.replace(before, after)
        if docs_mode == "online" and path.suffix == ".md":
            text = re.sub(r'\]\((?:\.\./)?godot/' + re.escape(docs_version) + r'/([^)#]+)\.md(#[^)]*)?\)',
                          lambda m: f"](https://docs.godotengine.org/en/{docs_version}/{m[1]}.html{m[2] or ''})", text)
            if rel == "AGENTS.md":
                text = re.sub(r"## 官方文档查阅\n.*?(?=## 验证与交付)",
                              f"## 官方文档查阅\n- 本项目显式采用 online 模式，未安装离线正文或索引。\n- API 和生命周期查 https://docs.godotengine.org/en/{docs_version}/ 对应版本正文；实际解析和运行结果优先。\n- 更新引擎或文档版本需要明确迁移，不静默使用新版资料。\n\n", text, flags=re.S)
            elif rel == "README.md":
                text = re.sub(r"官方文档实际正文与许可证位于.*?\n", f"本项目采用 online 模式，官方文档见 https://docs.godotengine.org/en/{docs_version}/ ，未安装离线正文或索引。\n", text)
                text = text.replace(f"`godot/{docs_version}/` 是可检索的官方 Markdown 正文", "官方文档按明确选择的 online 模式查对应版本官网")
        desired[rel] = text.encode("utf-8")
    source = dev_source()
    if not (source / "SKILL.md").is_file() and not (source / "SKILL.md.template").is_file():
        raise ValueError("Complete godot-dev bundle missing; install with the repository installer")
    skill_root = replacements["__SKILL_ROOT__"]
    for path in sorted(source.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts:
            relative = path.relative_to(source).as_posix()
            if relative == "SKILL.md.template":
                relative = "SKILL.md"
            desired[skill_root + "/godot-dev/" + relative] = path.read_bytes()
    for path in sorted(docs_root.rglob("*")) if docs_mode == "bundled" else []:
        if path.is_file():
            desired[f"docs/godot/{docs_version}/" + path.relative_to(docs_root).as_posix()] = path.read_bytes()
    # Generate only this project's baseline. No shared endpoint or workflow bundle.
    model = read_json(ASSETS / "template/tools/comfyui/wai-model.json", {})
    if profile_id == "desktop-wai":
        desired.update(baseline(model))
    desired[".bootstrap/assets-lock.json"] = (json.dumps({
        "schema": 3, "profile": profile_id, "workflow_ids": ["wai-t2i"] if profile_id == "desktop-wai" else [],
        "model_storage": "desktop_shared" if profile_id == "desktop-wai" else profile_id,
        "model": model if profile_id == "desktop-wai" else None, "instance": ".local/comfyui-instance.json" if profile_id == "desktop-wai" else None,
        "files": {rel: digest(data) for rel, data in desired.items() if rel.startswith("tools/comfyui/")},
    }, ensure_ascii=False, indent=2) + "\n").encode()
    desired[".bootstrap/docs-lock.json"] = (json.dumps({
        "docs_version": docs_version, "mode": docs_mode, "archive_sha256": manifest.get("archive_sha256"),
        "snapshot_at": manifest.get("snapshot_at"), "converter_version": manifest.get("converter_version"),
        "pages": manifest.get("completed_pages", 0), "source": manifest.get("source_base", f"https://docs.godotengine.org/en/{docs_version}/"),
    }, ensure_ascii=False, indent=2) + "\n").encode()
    config_file = getattr(args, "config", None)
    if config_file is None and (SKILL_ROOT / "local.json").is_file():
        config_file = SKILL_ROOT / "local.json"
    local = discover(config_file, target)
    local.pop("schema", None)
    sources = local.pop("comfyui_bootstrap", {})
    endpoint = local.pop("comfyui_endpoint", {})
    local.pop("asset_tools", None)
    if profile_id == "desktop-wai" and not all(sources.get(k) for k in ("desktop_exe", "desktop_data", "mcp", "comfy_bin")):
        raise ValueError("desktop-wai requires configured Comfy Desktop and MCP tool locations; use --config or environment variables")
    source_config = safe_path(target, ".local/comfyui-bootstrap.json")
    # These are one-time seed locations, never the active project endpoint.
    if profile_id == "desktop-wai":
        desired[".local/comfyui-bootstrap.json"] = source_config.read_bytes() if source_config.exists() else (json.dumps(sources, ensure_ascii=False, indent=2) + "\n").encode()
    if profile_id == "endpoint":
        from urllib.parse import urlparse
        url = endpoint.get("url", "").rstrip("/")
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https") or not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment:
            raise ValueError("endpoint profile requires comfyui_endpoint.url (HTTP(S), without credentials/query/fragment)")
        desired[".local/comfyui-endpoint.json"] = (json.dumps({"schema": 1, "url": url}, indent=2) + "\n").encode()
    if profile_id != "desktop-wai":
        desired["docs/asset-pipeline.md"] = (ASSETS / "asset-pipeline-portable.md").read_bytes()
    if docs_mode == "online":
        desired["docs/godot/README.md"] = f"# Godot {docs_version}\n\nOfficial reference: https://docs.godotengine.org/en/{docs_version}/\n\nNo offline snapshot was installed (--docs-mode online).\n".encode()
    if args.godot:
        local["godot"] = str(args.godot.resolve())
    local.setdefault("python", sys.executable)
    if local:
        desired[".local/toolchain.json"] = (json.dumps(local, ensure_ascii=False, indent=2) + "\n").encode()
    owned = state.get("files", {})
    keep = set(args.keep_existing)
    unknown = keep - desired.keys()
    if unknown:
        raise ValueError(f"--keep-existing must name a planned project file: {sorted(unknown)}")
    plan = []
    for rel, content in desired.items():
        dest = safe_path(target, rel)
        current = digest(dest.read_bytes()) if dest.is_file() else None
        new = digest(content)
        if rel in keep:
            if current is None:
                raise ValueError(f"--keep-existing requires an existing, reviewed file: {rel}")
            action = "preserve"
        elif current is None:
            action = "create"
        elif current == new:
            action = "unchanged"
        elif owned.get(rel) == current and not rel.startswith(".local/"):
            action = "update"
        else:
            action = "conflict"
        plan.append({"path": rel, "action": action, "sha256": new})
    return target, state, config, desired, plan, mode


def run(args):
    target, state, config, desired, plan, mode = build_plan(args)
    counts = {key: sum(item["action"] == key for item in plan) for key in ("create", "update", "unchanged", "preserve", "conflict")}
    summary = {"target": str(target), "mode": mode, "dry_run": args.dry_run, "parameters": config, "counts": counts,
               "preserved": [p["path"] for p in plan if p["action"] == "preserve"],
               "conflicts": [p["path"] for p in plan if p["action"] == "conflict"]}
    if not args.dry_run:
        files = dict(state.get("files", {}))
        for item in plan:
            rel, action = item["path"], item["action"]
            if action == "conflict":
                dest = safe_path(target, ".bootstrap/proposals/" + rel)
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(desired[rel])
            elif action in ("create", "update"):
                dest = safe_path(target, rel)
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(desired[rel])
                files[rel] = item["sha256"]
            elif action == "preserve":
                files.pop(rel, None)
            elif rel in files:
                files[rel] = item["sha256"]
        # Identical unmanaged files remain unmanaged; future runs cannot claim them.
        state_path = safe_path(target, ".bootstrap/state.json")
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text(json.dumps({"schema": 1, "bootstrap_version": "2.0.1", "parameters": config, "files": files}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if not counts["conflict"] and config["profile"] == "desktop-wai":
            command = [sys.executable, "-B", str(target / "tools/project_comfyui.py"), "setup"]
            if args.desktop_instance:
                command += ["--installation-id", args.desktop_instance]
            result = subprocess.run(command,
                                    capture_output=True, text=True, encoding="utf-8")
            if result.returncode not in (0, 3):
                summary["comfyui"] = {"ready": False, "error": result.stderr.strip() or result.stdout.strip()}
            else:
                summary["comfyui"] = json.loads(result.stdout)
        elif counts["conflict"]:
            summary["comfyui"] = {"ready": False, "reason": "Merge conflicts before provisioning; rerun initialization"}
        else:
            summary["comfyui"] = {"profile": config["profile"], "configured": config["profile"] == "endpoint", "live_validation": "not_run"}
        safe_path(target, ".bootstrap/last-run.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    else:
        summary["comfyui"] = {"profile": config["profile"], "operation": "plan only; no services started or contacted", "instance_name": config["codex_project_name"], "shared_checkpoint_bytes": model_bytes() if config["profile"] == "desktop-wai" else 0, "model_bytes_copied": 0}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if counts["conflict"]:
        return 2
    if summary.get("comfyui", {}).get("state") == "desktop_instance_required":
        return 3
    return 1 if summary.get("comfyui", {}).get("ready") is False else 0


def model_bytes():
    return read_json(ASSETS / "template/tools/comfyui/wai-model.json", {})["bytes"]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--path", type=Path, required=True)
    p.add_argument("--mode", choices=("auto", "new", "supplement"), default="auto", help="Auto preserves existing files and supplements an existing project.godot")
    p.add_argument("--keep-existing", action="append", default=[], metavar="RELATIVE_PATH", help="Keep a reviewed/merged planned file unmanaged; repeat per file")
    p.add_argument("--name")
    p.add_argument("--project-display-name", "--codex-project-name", dest="codex_project_name", help="Exact host project display name, otherwise Godot project name; old flag remains compatible")
    p.add_argument("--profile", choices=("core", "desktop-wai", "endpoint"), help="Existing project profile is preserved; new projects default to core")
    p.add_argument("--agent", choices=("codex", "deepseek-harness", "both"))
    p.add_argument("--config", type=Path, help="Machine JSON; no personal paths are shipped")
    p.add_argument("--migrate-profile", action="store_true", help="Explicit profile change; never deletes old instances or configuration")
    p.add_argument("--docs-mode", choices=("bundled", "online"))
    p.add_argument("--docs-root", type=Path, help="Validated matching offline snapshot; see sync_docs.py")
    p.add_argument("--dimension", choices=("2d", "3d"))
    p.add_argument("--engine-version")
    p.add_argument("--renderer", choices=("gl_compatibility", "mobile", "forward_plus"))
    p.add_argument("--platform")
    p.add_argument("--godot", type=Path)
    p.add_argument("--desktop-instance", help="Actual ID of a normal Desktop Standalone instance created for this project")
    p.add_argument("--dry-run", action="store_true")
    try:
        return run(p.parse_args())
    except (ValueError, OSError) as exc:
        p.exit(1, str(exc) + "\n")


if __name__ == "__main__":
    sys.exit(main())
