"""Tests for scripts/export_utils.py"""

import os
import tempfile

from export_utils import (
    get_skill_version,
    should_include_file,
    validate_skill_structure,
)


class TestGetSkillVersion:
    def test_override_takes_precedence(self):
        with tempfile.TemporaryDirectory() as tmp:
            assert get_skill_version(tmp, "2.5.0") == "v2.5.0"

    def test_override_with_v_prefix(self):
        with tempfile.TemporaryDirectory() as tmp:
            assert get_skill_version(tmp, "v3.0.0") == "v3.0.0"

    def test_default_version(self):
        with tempfile.TemporaryDirectory() as tmp:
            assert get_skill_version(tmp) == "v1.0.0"

    def test_reads_from_skill_md(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_md = os.path.join(tmp, "SKILL.md")
            with open(skill_md, "w") as f:
                f.write("---\nname: test\nversion: 4.2.1\n---\n# Test\n")
            result = get_skill_version(tmp)
            assert result == "v4.2.1"

    def test_does_not_change_cwd(self):
        original_cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as tmp:
            get_skill_version(tmp)
        assert os.getcwd() == original_cwd


class TestShouldIncludeFile:
    def test_includes_normal_files(self):
        assert should_include_file("/path/main.py", "main.py") is True
        assert should_include_file("/path/SKILL.md", "SKILL.md") is True

    def test_excludes_ds_store(self):
        assert should_include_file("/path/.DS_Store", ".DS_Store") is False

    def test_excludes_env(self):
        assert should_include_file("/path/.env", ".env") is False

    def test_excludes_pyc(self):
        assert should_include_file("/path/module.pyc", "module.pyc") is False

    def test_excludes_credentials(self):
        assert should_include_file("/path/credentials.json", "credentials.json") is False
        assert should_include_file("/path/secrets.json", "secrets.json") is False
        assert should_include_file("/path/api_keys.json", "api_keys.json") is False


class TestValidateSkillStructure:
    def test_valid_structure(self):
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "SKILL.md"), "w") as f:
                f.write("---\nname: test\ndescription: A test skill\n---\n# Test\n")
            valid, issues = validate_skill_structure(tmp)
            assert valid is True
            assert len(issues) == 0

    def test_missing_skill_md(self):
        with tempfile.TemporaryDirectory() as tmp:
            valid, issues = validate_skill_structure(tmp)
            assert valid is False
            assert any("SKILL.md" in i for i in issues)

    def test_missing_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "SKILL.md"), "w") as f:
                f.write("# No frontmatter here\n")
            valid, issues = validate_skill_structure(tmp)
            assert valid is False
            assert any("frontmatter" in i.lower() for i in issues)

    def test_missing_name_field(self):
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "SKILL.md"), "w") as f:
                f.write("---\ndescription: test\n---\n# Test\n")
            valid, issues = validate_skill_structure(tmp)
            assert valid is False
            assert any("name" in i.lower() for i in issues)

    def test_nonexistent_path(self):
        valid, issues = validate_skill_structure("/nonexistent/xyz")
        assert valid is False
