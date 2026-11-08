"""Lightweight package tests. These do not replace real agent evaluation."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SkillPackageTests(unittest.TestCase):
    def test_validator_passes(self):
        p = subprocess.run(
            [sys.executable, str(ROOT / "scripts/validate_skill.py")],
            cwd=str(ROOT), capture_output=True, text=True, check=False,
        )
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)

    def test_read_only_health_report(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "README.md").write_text("hello\n", encoding="utf-8")
            output = root / "reports" / "health.md"
            data = root / "reports" / "health.json"
            p = subprocess.run(
                [sys.executable, str(ROOT / "scripts/repo_health.py"),
                 "--root", str(root), "--output", str(output), "--json", str(data)],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertTrue(output.exists())
            report = json.loads(data.read_text(encoding="utf-8"))
            self.assertEqual(report["kind"], "repository_metadata_inventory_only")
            self.assertFalse(report["git"]["is_git_repository"])
            self.assertTrue(next(x for x in report["observations"] if x["domain"] == "readme")["present"])
            self.assertIn("not_checked", report)
            self.assertIn("vulnerability advisories", output.read_text(encoding="utf-8"))

    def test_evaluation_suite_has_separate_maintainer_scenario(self):
        scenarios = json.loads((ROOT / "evals/scenarios.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(scenarios), 15)
        own = next(x for x in scenarios if x["id"] == "skill-source-change")
        self.assertIn("handoff_to_separate_lifecycle_maintainer", own["decision"])

    def test_source_not_claimed_as_active_automation(self):
        content = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("**not** an autonomous runtime", content)
        self.assertIn("separately installed maintainer skill", content)
        self.assertIn("Phase 0", content)
        self.assertIn("budget", content)


if __name__ == "__main__":
    unittest.main()
