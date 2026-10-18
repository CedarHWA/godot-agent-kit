"""Host-specific MCP configuration; only project-local, conflict-safe additions."""
from __future__ import annotations

import json
from pathlib import Path
import tomllib


def safe(root, relative):
    path = root / relative
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Configuration path escapes project: {relative}")
    for ancestor in (path, *path.parents):
        if ancestor.is_symlink() or (ancestor.exists() and getattr(ancestor.stat(follow_symlinks=False), "st_file_attributes", 0) & 0x400):
            raise ValueError(f"Configuration path contains a reparse point: {ancestor}")
    return path


def configure(root: Path, entry: dict, agent: str):
    if agent not in ("codex", "deepseek-harness", "both"):
        raise ValueError(f"Unsupported agent: {agent}")
    planned = {}
    if agent in ("codex", "both"):
        path = safe(root, ".codex/config.toml")
        old = path.read_text(encoding="utf-8-sig") if path.exists() else ""
        existing = tomllib.loads(old).get("mcp_servers", {}).get("comfyui_project")
        if existing is not None and existing != entry:
            raise ValueError("Existing Codex comfyui_project differs; merge explicitly")
        if existing is None:
            block = "\n# Godot Agent Kit project binding\n[mcp_servers.comfyui_project]\n"
            block += "\n".join(f"{key} = {json.dumps(value, ensure_ascii=False)}" for key, value in entry.items()) + "\n"
            tomllib.loads(old + block)
            planned[path] = old + block
    if agent in ("deepseek-harness", "both"):
        path = safe(root, ".dsh/comfyui.cordis.yml")
        payload = [{"insert": [{"id": "godot-kit-comfyui", "name": "@deepseek-ai/dsh-mcp-client", "config": {
            "serverName": "comfyui_project", "transport": "stdio", "command": entry["command"],
            "args": entry["args"], "cwd": str(root), "toolCallTimeoutMs": 180000,
            "failOnStartupError": True}}]}]
        content = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"  # JSON is valid YAML; no YAML dependency.
        if path.exists() and path.read_text(encoding="utf-8-sig") != content:
            raise ValueError("Existing Harness overlay differs; preserve it and merge explicitly")
        if not path.exists():
            planned[path] = content
    # Validate every target first so an existing conflict causes no partial config change.
    for path, content in planned.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return [str(p) for p in planned]
