"""Machine configuration without user-specific defaults or global writes."""
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import sys


def read_json(path: Path, default=None):
    return json.loads(path.read_text(encoding="utf-8-sig")) if path.is_file() else (default if default is not None else {})


def discover(config_path: Path | None = None, project: Path | None = None) -> dict:
    """Explicit file > environment > existing project > PATH. Never read credentials."""
    existing = read_json(project / ".local/toolchain.json") if project else {}
    if project:
        existing["comfyui_bootstrap"] = read_json(project / ".local/comfyui-bootstrap.json")
        existing["comfyui_endpoint"] = read_json(project / ".local/comfyui-endpoint.json")
    explicit = read_json(config_path) if config_path else {}
    if config_path and not config_path.is_file():
        raise ValueError(f"Configuration file does not exist: {config_path}")
    if not isinstance(explicit, dict) or explicit.get("schema", 1) != 1:
        raise ValueError("Machine config must be a JSON object with schema 1")
    for section in ("comfyui_bootstrap", "comfyui_endpoint"):
        if section in explicit and not isinstance(explicit[section], dict):
            raise ValueError(f"{section} must be a JSON object")
    allowed = {"schema", "godot", "python", "comfyui_bootstrap", "comfyui_endpoint"}
    if set(explicit) - allowed:
        raise ValueError(f"Unknown configuration fields: {sorted(set(explicit) - allowed)}")
    result = {"schema": 1}
    for key, env_key, programs in (("godot", "GODOT_PATH", ("godot", "godot4")),
                                   ("python", "GODOT_KIT_PYTHON", ())):
        value = explicit.get(key) or os.environ.get(env_key) or existing.get(key)
        value = value or next((p for name in programs if (p := shutil.which(name))), None)
        if key == "python":
            value = value or sys.executable
        if value:
            resolved = shutil.which(str(value)) or str(value)
            result[key] = str(Path(resolved).expanduser().absolute())
    bootstrap = dict(existing.get("comfyui_bootstrap", {}))
    mapping = {"desktop_exe": "COMFY_DESKTOP_EXE", "desktop_data": "COMFY_DESKTOP_DATA",
               "mcp": "COMFY_MCP_EXE", "comfy_bin": "COMFY_BIN"}
    for key, env_key in mapping.items():
        value = explicit.get("comfyui_bootstrap", {}).get(key) or os.environ.get(env_key) or bootstrap.get(key)
        if not value and key in ("mcp", "comfy_bin"):
            value = shutil.which("comfy-mcp" if key == "mcp" else "comfy")
        if not value and key == "desktop_data" and os.environ.get("APPDATA"):
            candidate = Path(os.environ["APPDATA"]) / "Comfy Desktop"
            if candidate.is_dir():
                value = str(candidate)
        if value:
            bootstrap[key] = str(Path(value).expanduser().absolute())
    if bootstrap:
        result["comfyui_bootstrap"] = bootstrap
    endpoint = explicit.get("comfyui_endpoint") or existing.get("comfyui_endpoint")
    if endpoint:
        result["comfyui_endpoint"] = endpoint
    return result
