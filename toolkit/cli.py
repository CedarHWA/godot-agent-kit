"""Windows skill distribution: copy complete bundles, preserve edits, rollback atomically."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills/godot-project-init/scripts"))
from environment import discover

SKILLS = {"init": "godot-project-init", "dev": "godot-dev"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def checked(path: Path) -> Path:
    """Reject every link/junction ancestor before any mutation or recursive walk."""
    path = Path(os.path.abspath(path.expanduser()))
    for item in (path, *path.parents):
        if item.is_symlink() or (item.exists() and getattr(item.stat(follow_symlinks=False), "st_file_attributes", 0) & 0x400):
            raise ValueError(f"Refusing reparse point: {item}")
    if len(path.parts) < 3 or path.parent == Path(path.anchor):
        raise ValueError("Choose a directory below an existing parent, not a drive root")
    return path


def inside(root: Path, relative: str) -> Path:
    rel = PurePosixPath(relative)
    if rel.is_absolute() or any(p in ("..", ".") or ":" in p or "\\" in p for p in rel.parts):
        raise ValueError(f"Invalid relative path: {relative}")
    path = checked(root / Path(*rel.parts))
    if not path.is_relative_to(root):
        raise ValueError(f"Path escapes root: {relative}")
    return path


def write(path: Path, data: bytes):
    checked(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".kit-" + uuid.uuid4().hex)
    try:
        temp.write_bytes(data)
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def load(path: Path, fallback=None):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else (fallback if fallback is not None else {})


def target_root(args):
    if args.skills_dir:
        return checked(args.skills_dir)
    if args.scope == "project":
        if not args.project:
            raise ValueError("--scope project requires --project")
        base = checked(args.project)
        if args.agent in ("deepseek-harness", "both"):
            git_root = next((p for p in (base, *base.parents) if (p / ".git").exists()), None)
            if git_root and git_root != base:
                raise ValueError(f"Harness resolves this workspace at {git_root}; use that --project, or explicitly configure customSkillDirs and --skills-dir")
        return checked(base / (".dsh/skills" if args.agent == "deepseek-harness" else ".agents/skills"))
    if args.agent == "deepseek-harness":
        return checked(Path(os.environ.get("DSH_HOME", Path.home() / ".dsh")) / "skills")
    return checked(Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "skills")


def bundle(selected, config=None):
    desired = {}
    for name in selected:
        source = ROOT / "skills" / name
        for file in sorted(source.rglob("*")):
            if "__pycache__" in file.parts or file.name == "local.json" or file.suffix == ".pyc":
                continue
            checked(file)
            if file.is_file():
                desired[name + "/" + file.relative_to(source).as_posix()] = file.read_bytes()
        if name == "godot-project-init":
            # Installed init remains complete even when the user installs only it.
            for file in sorted((ROOT / "skills/godot-dev").rglob("*")):
                checked(file)
                if file.is_file() and "__pycache__" not in file.parts:
                    relative = file.relative_to(ROOT / "skills/godot-dev").as_posix()
                    if relative == "SKILL.md":
                        relative = "SKILL.md.template"  # Codex recursively discovers SKILL.md inside assets.
                    desired[name + "/assets/godot-dev/" + relative] = file.read_bytes()
            if config is not None:
                desired[name + "/local.json"] = json_bytes(config)
    return desired


def state_for(root):
    state = load(inside(root, ".godot-agent-kit/state.json"), {"schema": 1, "files": {}, "history": []})
    if state.get("schema") != 1 or not isinstance(state.get("files"), dict):
        raise ValueError("Unsupported installation receipt; preserve it and migrate explicitly")
    for relative in state["files"]:
        if relative.split("/", 1)[0] not in SKILLS.values():
            raise ValueError("Receipt contains a path outside this kit's skill bundles")
        inside(root, relative)
    return state


def install(root, selected, config=None, dry_run=False):
    root = checked(root)
    state = state_for(root)
    desired = bundle(selected, config)
    owned = dict(state["files"])
    changes, conflicts, identical = {}, [], 0
    for rel, data in desired.items():
        path = inside(root, rel)
        if path.exists() and not path.is_file():
            raise ValueError(f"Expected a file: {path}")
        current = sha(path.read_bytes()) if path.exists() else None
        if current == sha(data):
            identical += 1  # Do not claim identical unmanaged files.
        elif current is not None and current != owned.get(rel):
            conflicts.append(rel)
        else:
            changes[rel] = data
            owned[rel] = sha(data)
    for rel in state["files"]:
        if rel.split("/", 1)[0] not in selected or rel in desired or rel.endswith("/local.json"):
            continue
        path = inside(root, rel)
        if path.exists() and sha(path.read_bytes()) != state["files"][rel]:
            conflicts.append(rel)
        else:
            changes[rel] = None
            owned.pop(rel, None)
    result = {"root": str(root), "version": (ROOT / "VERSION").read_text().strip(), "dry_run": dry_run,
              "changed": len(changes), "unchanged": identical, "conflicts": conflicts}
    if conflicts:
        if not dry_run:
            for rel in conflicts:
                if rel in desired:
                    write(inside(root, ".godot-agent-kit/proposals/" + rel), desired[rel])
        result["applied"] = False
        return result
    if not dry_run and changes:
        receipt = dict(state, files=owned, version=result["version"])
        result["transaction"] = transaction(root, changes, receipt, state)
    result["applied"] = not dry_run
    return result


def transaction(root, changes, receipt, before_state):
    """Persist a recovery journal before writes; unfinished transactions block new work."""
    pending = inside(root, ".godot-agent-kit/pending.json")
    if pending.exists():
        raise ValueError("Interrupted operation: run recover before another install/uninstall/rollback")
    tx = uuid.uuid4().hex
    journal_dir = ".godot-agent-kit/history/" + tx
    before, after = {}, {}
    for rel, data in changes.items():
        path = inside(root, rel)
        before[rel] = sha(path.read_bytes()) if path.exists() else None
        after[rel] = sha(data) if data is not None else None
        if path.exists():
            write(inside(root, journal_dir + "/files/" + rel), path.read_bytes())
    journal = {"schema": 1, "id": tx, "before": before, "after": after, "state": before_state}
    write(inside(root, journal_dir + "/journal.json"), json_bytes(journal))
    write(pending, json_bytes({"id": tx}))
    try:
        for rel, data in changes.items():
            path = inside(root, rel)
            if data is None:
                if path.exists():
                    path.unlink()
            else:
                write(path, data)
        receipt["history"] = before_state.get("history", []) + [tx]
        write(inside(root, ".godot-agent-kit/state.json"), json_bytes(receipt))
        pending.unlink()
        return tx
    except BaseException:
        # Leave the journal if recovery itself is interrupted or an external edit is detected.
        restore(root, tx, interrupted=True)
        raise


def restore(root, tx, interrupted=False, dry_run=False):
    if len(tx) != 32 or any(c not in "0123456789abcdef" for c in tx):
        raise ValueError("Invalid transaction id")
    journal_dir = ".godot-agent-kit/history/" + tx
    journal = load(inside(root, journal_dir + "/journal.json"))
    if journal.get("id") != tx or journal.get("schema") != 1:
        raise ValueError("Invalid transaction journal")
    conflicts = []
    for rel, expected in journal["after"].items():
        if rel.split("/", 1)[0] not in SKILLS.values():
            raise ValueError("Journal contains a path outside the kit")
        path = inside(root, rel)
        current = sha(path.read_bytes()) if path.exists() else None
        allowed = (expected, journal["before"][rel]) if interrupted else (expected,)
        if current not in allowed:
            conflicts.append(rel)
        previous = journal["before"][rel]
        if previous is not None and sha(inside(root, journal_dir + "/files/" + rel).read_bytes()) != previous:
            raise ValueError("Corrupt rollback backup; refusing partial restore")
    if conflicts or dry_run:
        return {"restored": False, "conflicts": conflicts, "dry_run": dry_run}
    pending = inside(root, ".godot-agent-kit/pending.json")
    write(pending, json_bytes({"id": tx}))
    for rel, previous in journal["before"].items():
        path = inside(root, rel)
        if previous is None:
            if path.exists():
                path.unlink()
        else:
            write(path, inside(root, journal_dir + "/files/" + rel).read_bytes())
    write(inside(root, ".godot-agent-kit/state.json"), json_bytes(journal["state"]))
    pending.unlink()
    return {"restored": True, "transaction": tx, "conflicts": []}


def uninstall(root, selected, dry_run=False):
    state = state_for(root)
    changes, preserved = {}, []
    owned = dict(state["files"])
    for rel, digest in state["files"].items():
        if rel.split("/", 1)[0] not in selected:
            continue
        path = inside(root, rel)
        if path.exists() and sha(path.read_bytes()) != digest:
            preserved.append(rel)
        else:
            changes[rel] = None
            owned.pop(rel)
    result = {"removed": len(changes), "preserved": preserved, "dry_run": dry_run}
    if changes and not dry_run:
        result["transaction"] = transaction(root, changes, dict(state, files=owned), state)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    for action in ("install", "uninstall", "rollback", "recover"):
        p = sub.add_parser(action)
        p.add_argument("--agent", choices=("codex", "deepseek-harness", "both"), default="codex")
        p.add_argument("--scope", choices=("project", "user"), default="project")
        p.add_argument("--project", type=Path)
        p.add_argument("--skills-dir", type=Path, help="Explicit skills root, for portable/legacy/custom agent installations")
        p.add_argument("--skills", choices=("both", "init", "dev"), default="both")
        p.add_argument("--config", type=Path)
        p.add_argument("--dry-run", action="store_true")
    for action, script in (("doctor", "doctor.py"), ("init", "init_project.py")):
        sub.add_parser(action, add_help=False)
    args, rest = parser.parse_known_args()
    if args.action in ("doctor", "init"):
        import subprocess
        script = "doctor.py" if args.action == "doctor" else "init_project.py"
        return subprocess.call([sys.executable, "-B", str(ROOT / "skills/godot-project-init/scripts" / script), *rest])
    if rest:
        parser.error("Unknown arguments: " + " ".join(rest))
    try:
        roots = [target_root(args)]
        if args.agent == "both" and args.scope == "user" and not args.skills_dir:
            roots.append(checked(Path(os.environ.get("DSH_HOME", Path.home() / ".dsh")) / "skills"))
        selected = list(SKILLS.values()) if args.skills == "both" else [SKILLS[args.skills]]
        for root in roots:
            if inside(root, ".godot-agent-kit/pending.json").exists() and args.action != "recover":
                raise ValueError(f"An operation was interrupted at {root}; run recover first")
        config = discover(args.config) if args.config else None
        # Both user roots are preflighted before changing either. Receipts remain per-root.
        if args.action == "install" and len(roots) > 1:
            preview = [install(root, selected, config, True) for root in roots]
            if any(result["conflicts"] for result in preview):
                if not args.dry_run:
                    preview = [install(root, selected, config, False) if result["conflicts"] else result for root, result in zip(roots, preview)]
                print(json.dumps({"roots": preview, "applied": False}, ensure_ascii=False, indent=2))
                return 2
        results = []
        for root in roots:
            pending = inside(root, ".godot-agent-kit/pending.json")
            if args.action == "install":
                result = install(root, selected, config, args.dry_run)
            elif args.action == "uninstall":
                result = uninstall(root, selected, args.dry_run)
            elif args.action == "recover":
                result = restore(root, load(pending)["id"], interrupted=True, dry_run=args.dry_run) if pending.exists() else {"restored": False, "reason": "nothing pending"}
            else:
                history = state_for(root).get("history", [])
                result = restore(root, history[-1], dry_run=args.dry_run) if history else {"restored": False, "reason": "no history"}
            results.append({"root": str(root), **result})
        print(json.dumps(results[0] if len(results) == 1 else {"roots": results}, ensure_ascii=False, indent=2))
        return 2 if any(result.get("conflicts") or result.get("preserved") for result in results) else 0
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, str(exc) + "\n")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
