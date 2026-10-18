"""Validate package structure, skill metadata, local references and release hygiene."""
from pathlib import Path
import ast
import json
import re
import sys
from urllib.parse import urlsplit, unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills/godot-project-init/scripts"))
from verify_docs import verify
from build import sources


def main():
    errors = []
    for skill in (ROOT / "skills").iterdir():
        source = skill / "SKILL.md"
        text = source.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
        if not match:
            errors.append(f"Missing frontmatter: {source.relative_to(ROOT)}")
            continue
        metadata = yaml.safe_load(match[1])
        if metadata.get("name") != skill.name or not metadata.get("description"):
            errors.append(f"Invalid metadata: {skill.name}")
        for file in [source, *sorted((skill / "references").glob("*.md"))]:
            body = file.read_text(encoding="utf-8")
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
                url = urlsplit(link)
                if url.scheme or not url.path:
                    continue
                target = (file.parent / unquote(url.path)).resolve()
                if not target.is_relative_to(skill.resolve()) or not target.is_file():
                    errors.append(f"Broken link: {file.relative_to(ROOT)} -> {link}")
    count = 0
    package_paths = set()
    for name, data in sources():
        count += 1
        package_paths.add(name)
        if name.endswith(".py"):
            try:
                ast.parse(data.decode("utf-8"), filename=name)
            except SyntaxError as exc:
                errors.append(str(exc))
        if str(Path.home()).encode() in data or Path.home().as_posix().encode() in data:
            errors.append("Personal path leaked: " + name)
        if name.endswith(".json"):
            try:
                json.loads(data)
            except (ValueError, UnicodeDecodeError):
                errors.append("Invalid JSON: " + name)
    for required in ("work/.gdignore", ".local/.gdignore", ".agents/.gdignore", "docs/.gdignore", "tools/.gdignore"):
        if "skills/godot-project-init/assets/template/" + required not in package_paths:
            errors.append("Release loses generated-project ignore marker: " + required)
    docs = verify(ROOT / "skills/godot-project-init/assets/docs/godot/4.7")
    if not docs["passed"]:
        errors.extend(str(item) for item in docs["errors"])
    report = {"passed": not errors, "files": count, "offline_documentation": docs, "errors": errors}
    output = ROOT / ".local/validation.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": not errors, "files": count, "documentation_pages": docs["pages"], "errors": errors}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
