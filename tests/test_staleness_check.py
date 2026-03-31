"""Tests for scripts/staleness_check.py"""

import os
import tempfile

from staleness_check import staleness_check


def _make_skill(tmp_path, frontmatter_content):
    """Create a minimal skill directory with SKILL.md."""
    skill_dir = os.path.join(tmp_path, "test-skill")
    os.makedirs(skill_dir, exist_ok=True)
    with open(os.path.join(skill_dir, "SKILL.md"), "w") as f:
        f.write(frontmatter_content)
    return skill_dir


class TestStalenessCheck:
    def test_nonexistent_path(self):
        result = staleness_check("/nonexistent/path/xyz")
        assert result["fresh"] is False
        assert result["review_status"] == "unknown"

    def test_missing_skill_md(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = staleness_check(tmp)
            assert result["fresh"] is False

    def test_no_temporal_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill(tmp, "---\nname: test-skill\ndescription: test\n---\n# Test\n")
            result = staleness_check(skill_dir)
            assert result["review_status"] in ("unknown", "fresh")
            assert any(
                "temporal" in i["message"].lower() or "review date" in i["message"].lower()
                for i in result["issues"]
            )

    def test_fresh_skill(self):
        from datetime import date

        today = date.today().isoformat()
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill(
                tmp,
                f"---\nname: test-skill\ndescription: test\nmetadata:\n  last_reviewed: {today}\n  review_interval_days: 90\n---\n# Test\n",
            )
            result = staleness_check(skill_dir)
            assert result["fresh"] is True
            assert result["review_status"] == "fresh"
            assert result["days_since_review"] == 0

    def test_overdue_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill(
                tmp,
                "---\nname: test-skill\ndescription: test\nmetadata:\n  last_reviewed: 2020-01-01\n  review_interval_days: 30\n---\n# Test\n",
            )
            result = staleness_check(skill_dir)
            assert result["fresh"] is False
            assert result["review_status"] == "overdue"
            assert result["days_since_review"] is not None
            assert result["days_since_review"] > 30

    def test_invalid_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill(tmp, "no frontmatter here")
            result = staleness_check(skill_dir)
            assert result["fresh"] is False
            assert result["review_status"] == "unknown"

    def test_check_deps_no_deps(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill(tmp, "---\nname: test-skill\ndescription: test\n---\n# Test\n")
            result = staleness_check(skill_dir, check_deps=True)
            assert any("No dependencies declared" in i["message"] for i in result["issues"])

    def test_check_drift_no_expectations(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill(tmp, "---\nname: test-skill\ndescription: test\n---\n# Test\n")
            result = staleness_check(skill_dir, check_drift=True)
            assert any("No schema expectations" in i["message"] for i in result["issues"])
