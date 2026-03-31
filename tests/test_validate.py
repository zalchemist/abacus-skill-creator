"""Tests for scripts/validate.py"""

import os
import tempfile

from validate import (
    _extract_local_links,
    _field_exists_in_frontmatter,
    _parse_frontmatter,
    _parse_yaml_field,
    _subfield_exists,
    validate_skill,
)


def _make_skill(tmp_path, frontmatter_body, extra_files=None):
    """Create a minimal skill directory with SKILL.md for testing."""
    skill_dir = os.path.join(tmp_path, "test-skill")
    os.makedirs(skill_dir, exist_ok=True)
    with open(os.path.join(skill_dir, "SKILL.md"), "w") as f:
        f.write(frontmatter_body)
    if extra_files:
        for name, content in extra_files.items():
            path = os.path.join(skill_dir, name)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                f.write(content)
    return skill_dir


class TestParseFrontmatter:
    def test_valid_frontmatter(self):
        content = "---\nname: test\n---\nBody here"
        fm, body = _parse_frontmatter(content)
        assert fm == "name: test"
        assert body == "Body here"

    def test_missing_opening(self):
        fm, body = _parse_frontmatter("no frontmatter here")
        assert fm is None
        assert body is None

    def test_missing_closing(self):
        fm, body = _parse_frontmatter("---\nname: test\nno closing")
        assert fm is None
        assert body is None

    def test_empty_frontmatter(self):
        content = "---\n---\nBody"
        fm, body = _parse_frontmatter(content)
        assert fm == ""
        assert body == "Body"


class TestParseYamlField:
    def test_simple_field(self):
        fm = "name: my-skill\ndescription: a test"
        assert _parse_yaml_field(fm, "name") == "my-skill"
        assert _parse_yaml_field(fm, "description") == "a test"

    def test_missing_field(self):
        fm = "name: my-skill"
        assert _parse_yaml_field(fm, "description") is None

    def test_block_scalar(self):
        fm = "description: >-\n  This is a long\n  description text"
        result = _parse_yaml_field(fm, "description")
        assert result == "This is a long description text"


class TestFieldExists:
    def test_exists(self):
        fm = "name: test\nlicense: MIT"
        assert _field_exists_in_frontmatter(fm, "name") is True
        assert _field_exists_in_frontmatter(fm, "license") is True

    def test_not_exists(self):
        fm = "name: test"
        assert _field_exists_in_frontmatter(fm, "license") is False


class TestSubfieldExists:
    def test_exists(self):
        fm = "metadata:\n  author: test\n  version: 1.0"
        assert _subfield_exists(fm, "metadata", "author") is True
        assert _subfield_exists(fm, "metadata", "version") is True

    def test_not_exists(self):
        fm = "metadata:\n  author: test"
        assert _subfield_exists(fm, "metadata", "version") is False


class TestExtractLocalLinks:
    def test_local_links(self):
        body = "See [guide](references/guide.md) and [api](scripts/api.py)"
        links = _extract_local_links(body)
        assert "references/guide.md" in links
        assert "scripts/api.py" in links

    def test_ignores_urls(self):
        body = "Visit [site](https://example.com) and [mail](mailto:a@b.com)"
        links = _extract_local_links(body)
        assert len(links) == 0

    def test_ignores_anchors(self):
        body = "See [section](#heading)"
        links = _extract_local_links(body)
        assert len(links) == 0

    def test_strips_anchors_from_paths(self):
        body = "See [guide](references/guide.md#section)"
        links = _extract_local_links(body)
        assert links == ["references/guide.md"]


class TestValidateSkill:
    def test_valid_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill(
                tmp,
                "---\nname: test-skill\ndescription: A test skill\n---\n# Test Skill\n",
            )
            result = validate_skill(skill_dir)
            assert result["valid"] is True
            assert len(result["errors"]) == 0

    def test_missing_directory(self):
        result = validate_skill("/nonexistent/path/xyz")
        assert result["valid"] is False
        assert any("does not exist" in e for e in result["errors"])

    def test_missing_skill_md(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = validate_skill(tmp)
            assert result["valid"] is False
            assert any("SKILL.md not found" in e for e in result["errors"])

    def test_missing_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill(
                tmp,
                "---\ndescription: A test\n---\n# Test\n",
            )
            result = validate_skill(skill_dir)
            assert result["valid"] is False
            assert any("'name' field is missing" in e for e in result["errors"])

    def test_missing_description(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill(
                tmp,
                "---\nname: test-skill\n---\n# Test\n",
            )
            result = validate_skill(skill_dir)
            assert result["valid"] is False
            assert any("'description' field is missing" in e for e in result["errors"])

    def test_invalid_name_uppercase(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = os.path.join(tmp, "TestSkill")
            os.makedirs(skill_dir)
            with open(os.path.join(skill_dir, "SKILL.md"), "w") as f:
                f.write("---\nname: TestSkill\ndescription: test\n---\n# Test\n")
            result = validate_skill(skill_dir)
            assert result["valid"] is False
            assert any("lowercase" in e for e in result["errors"])

    def test_name_too_long(self):
        with tempfile.TemporaryDirectory() as tmp:
            long_name = "a" * 65
            skill_dir = os.path.join(tmp, long_name)
            os.makedirs(skill_dir)
            with open(os.path.join(skill_dir, "SKILL.md"), "w") as f:
                f.write(f"---\nname: {long_name}\ndescription: test\n---\n# Test\n")
            result = validate_skill(skill_dir)
            assert result["valid"] is False
            assert any("exceeds" in e for e in result["errors"])

    def test_warnings_for_missing_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill(
                tmp,
                "---\nname: test-skill\ndescription: A test skill\n---\n# Test\n",
            )
            result = validate_skill(skill_dir)
            assert result["valid"] is True
            assert any("metadata" in w.lower() for w in result["warnings"])

    def test_broken_local_link_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill(
                tmp,
                "---\nname: test-skill\ndescription: A test\n---\nSee [doc](nonexistent.md)\n",
            )
            result = validate_skill(skill_dir)
            assert any("nonexistent.md" in w for w in result["warnings"])
