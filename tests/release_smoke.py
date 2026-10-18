"""Verify release manifest and install/init from the extracted package, not the checkout."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("archive", type=Path)
    args = p.parse_args()
    (ROOT / "work").mkdir(exist_ok=True)
    count = 0
    with tempfile.TemporaryDirectory(prefix="release-", dir=ROOT / "work") as tmp:
        temp = Path(tmp).resolve()
        with zipfile.ZipFile(args.archive) as archive:
            for item in archive.infolist():
                target = (temp / item.filename).resolve()
                if not target.is_relative_to(temp):
                    raise ValueError("Archive path escapes extraction directory")
            archive.extractall(temp)
        source = temp / "godot-agent-kit"
        manifest = json.loads((source / "RELEASE-MANIFEST.json").read_text(encoding="utf-8"))
        for relative, digest in manifest["files"].items():
            target = source / relative
            if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
                raise ValueError("Release checksum mismatch: " + relative)
            count += 1
        install = [sys.executable, "-B", str(source / "toolkit/cli.py"), "install", "--skills-dir", str(temp / "skills"), "--skills", "init"]
        subprocess.run(install, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
        init = [sys.executable, "-B", str(temp / "skills/godot-project-init/scripts/init_project.py"), "--path", str(temp / "game"), "--profile", "core", "--docs-mode", "online"]
        subprocess.run(init, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
        for relative in ("work/.gdignore", ".local/.gdignore", "tools/.gdignore", ".agents/skills/godot-dev/SKILL.md", "scenes/main/main.tscn"):
            if not (temp / "game" / relative).is_file():
                raise ValueError("Installed release is incomplete: " + relative)
    report = {"passed": True, "manifest_files": count, "extracted_installer": True, "installed_initializer": True,
              "project_ignore_markers": True, "temporary_directories_removed": True}
    (ROOT / ".local").mkdir(exist_ok=True)
    (ROOT / ".local/release-smoke.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
