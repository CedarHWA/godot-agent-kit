"""Build a deterministic source distribution; never includes local paths, caches or weights."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = {"VERSION", "README.md", "AGENTS.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "CHANGELOG.md", "config.example.json",
              "requirements.txt", "requirements-comfy.txt", "requirements-lock.txt", "requirements-comfy-lock.txt", "setup.ps1", "install.ps1", "doctor.ps1", ".gitignore", ".gitattributes", ".gdignore"}
ROOT_DIRS = {"skills", "toolkit", "tools", "adapters", "tests", "docs", ".github"}


def sources():
    for path in sorted(ROOT.rglob("*")):
        relative = path.relative_to(ROOT)
        if relative.parts[0] not in ROOT_DIRS and relative.as_posix() not in ROOT_FILES:
            continue
        ignore_marker = path.name == ".gdignore" and relative.as_posix().startswith("skills/godot-project-init/assets/template/")
        if (not ignore_marker and any(p in {"__pycache__", "work", ".local", ".venv", ".godot"} for p in relative.parts)) or path.name == "local.json" or path.suffix == ".pyc":
            continue
        if path.is_symlink() or (path.exists() and getattr(path.stat(follow_symlinks=False), "st_file_attributes", 0) & 0x400):
            raise ValueError(f"Unexpected link in release: {relative}")
        if path.is_file():
            yield relative.as_posix(), path.read_bytes()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--out", type=Path, default=ROOT / "dist")
    args = p.parse_args()
    version = (ROOT / "VERSION").read_text().strip()
    args.out.mkdir(parents=True, exist_ok=True)
    archive = args.out / f"godot-agent-kit-{version}.zip"
    files = dict(sources())
    manifest = {"version": version, "files": {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}}
    files["RELEASE-MANIFEST.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as output:
        for name, data in sorted(files.items()):
            entry = zipfile.ZipInfo("godot-agent-kit/" + name, date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o644 << 16
            output.writestr(entry, data)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix(".zip.sha256").write_text(digest + "  " + archive.name + "\n", encoding="utf-8")
    print(json.dumps({"archive": str(archive), "sha256": digest, "files": len(files), "bytes": archive.stat().st_size}, indent=2))


if __name__ == "__main__":
    main()
