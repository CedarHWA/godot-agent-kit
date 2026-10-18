"""Exercise user init -> project dev through installed CLIs, without real user writes."""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RecommendedLayoutTests(unittest.TestCase):
    def setUp(self):
        (ROOT / "work").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="recommended-", dir=ROOT / "work")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.codex = self.root / "user/codex"
        self.harness = self.root / "user/dsh"
        self.env = dict(os.environ, CODEX_HOME=str(self.codex), DSH_HOME=str(self.harness),
                        PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")

    def run_cli(self, script, *args, expected=0):
        result = subprocess.run([sys.executable, "-B", str(script), *map(str, args)],
                                cwd=ROOT, env=self.env, capture_output=True, text=True,
                                encoding="utf-8", timeout=120)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def install(self, agent="both", skills="init", action="install", *extra):
        return self.run_cli(ROOT / "toolkit/cli.py", action, "--agent", agent,
                            "--scope", "user", "--skills", skills, *extra)

    def initialize(self, home, project, agent):
        return self.run_cli(home / "skills/godot-project-init/scripts/init_project.py",
                            "--path", project, "--agent", agent, "--profile", "core",
                            "--docs-mode", "online")

    def tree(self, directory):
        return {p.relative_to(directory).as_posix(): p.read_bytes()
                for p in directory.rglob("*") if p.is_file()}

    def test_recommended_flow_for_each_host_and_shared_project(self):
        # All variants are exercised using independent homes and the installed initializer.
        for agent in ("codex", "deepseek-harness", "both"):
            with self.subTest(agent=agent):
                self.codex = self.root / agent / "user/codex"
                self.harness = self.root / agent / "user/dsh"
                self.env.update(CODEX_HOME=str(self.codex), DSH_HOME=str(self.harness))
                self.install(agent)
                homes = [self.harness] if agent == "deepseek-harness" else [self.codex]
                if agent == "both":
                    homes.append(self.harness)
                for home in homes:
                    skills = home / "skills"
                    self.assertEqual([p.relative_to(skills).as_posix() for p in skills.rglob("SKILL.md")],
                                     ["godot-project-init/SKILL.md"])
                    self.assertTrue((skills / "godot-project-init/assets/godot-dev/SKILL.md.template").is_file())
                    self.assertFalse((skills / "godot-dev").exists())
                project = self.root / agent / "游戏 project"
                self.initialize(homes[0], project, agent)
                relative = ".dsh/skills/godot-dev" if agent == "deepseek-harness" else ".agents/skills/godot-dev"
                self.assertEqual(self.tree(project / relative), self.tree(ROOT / "skills/godot-dev"))
                self.assertEqual([p.relative_to(project).as_posix() for p in project.rglob("SKILL.md")],
                                 [relative + "/SKILL.md"])
                state = json.loads((project / ".bootstrap/state.json").read_text(encoding="utf-8"))
                self.assertEqual(state["bootstrap_version"], (ROOT / "VERSION").read_text().strip())
                repeated = self.initialize(homes[-1], project, agent)
                self.assertFalse(any(repeated["counts"][key] for key in ("create", "update", "conflict")))

    def test_projects_survive_user_init_update_and_uninstall_independently(self):
        config = self.root / "machine.json"
        config.write_text(json.dumps({"schema": 1, "python": sys.executable}), encoding="utf-8")
        self.install("codex")
        projects = [self.root / "game-a", self.root / "game-b"]
        for project in projects:
            self.initialize(self.codex, project, "codex")
        dev_a = projects[0] / ".agents/skills/godot-dev/SKILL.md"
        dev_a.write_bytes(dev_a.read_bytes() + b"\nProject-specific instructions.\n")
        snapshots = [self.tree(project) for project in projects]
        # A real configuration update creates a new user-install transaction.
        changed = self.install("codex", "init", "install", "--config", config)
        self.assertGreater(changed["changed"], 0)
        self.install("codex", action="uninstall")
        self.assertFalse((self.codex / "skills/godot-project-init/SKILL.md").exists())
        for project, snapshot in zip(projects, snapshots):
            self.assertEqual(self.tree(project), snapshot)
        self.assertNotEqual(dev_a.read_bytes(), (projects[1] / ".agents/skills/godot-dev/SKILL.md").read_bytes())

    def test_reinstall_init_preserves_existing_user_dev(self):
        self.install(skills="both")
        for home in (self.codex, self.harness):
            file = home / "skills/godot-dev/SKILL.md"
            file.write_bytes(file.read_bytes() + b"\nPersonal instructions.\n")
        snapshots = [self.tree(home / "skills/godot-dev") for home in (self.codex, self.harness)]
        self.install()
        for home, snapshot in zip((self.codex, self.harness), snapshots):
            self.assertEqual(self.tree(home / "skills/godot-dev"), snapshot)

    def test_legacy_defaults_still_install_both_in_project(self):
        project = self.root / "legacy-project"
        self.run_cli(ROOT / "toolkit/cli.py", "install", "--project", project)
        skills = project / ".agents/skills"
        self.assertTrue((skills / "godot-project-init/SKILL.md").is_file())
        self.assertTrue((skills / "godot-dev/SKILL.md").is_file())
        self.assertFalse(self.codex.exists())
        self.assertFalse(self.harness.exists())


if __name__ == "__main__":
    unittest.main()
