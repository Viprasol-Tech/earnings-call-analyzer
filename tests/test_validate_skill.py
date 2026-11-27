"""Tests for scripts/validate_skill.py (standard library only).

Run from the repo root:  python -m unittest discover -s tests
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "validate_skill.py"
spec = importlib.util.spec_from_file_location("validate_skill", SCRIPT)
validate_skill = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate_skill)

DESCRIPTION = "Analyze an earnings call transcript and report KPIs versus guidance."


def run_main(frontmatter: str) -> int:
    """Run main() against a throwaway skill folder with the given frontmatter."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "skill.md").write_text(f"---\n{frontmatter}\n---\n# Skill\n", encoding="utf-8")
        (root / "examples").mkdir()
        (root / "examples" / "one.md").write_text("example\n", encoding="utf-8")
        with mock.patch.object(validate_skill, "_repo_root", return_value=root):
            return validate_skill.main()


class ValidateSkillTests(unittest.TestCase):
    def test_passes_with_name_and_description(self):
        self.assertEqual(run_main(f"name: demo\ndescription: {DESCRIPTION}"), 0)

    def test_fails_when_name_is_an_empty_quoted_string(self):
        for empty in ('""', "''"):
            with self.subTest(name=empty):
                self.assertEqual(run_main(f"name: {empty}\ndescription: {DESCRIPTION}"), 1)

    def test_quotes_are_not_part_of_the_value(self):
        fields = validate_skill._parse_frontmatter('---\nname: "demo"\n---\n')
        self.assertEqual(fields["name"], "demo")


if __name__ == "__main__":
    unittest.main()
