"""Tests for scripts/security_scan.py"""

import os
import tempfile

from security_scan import security_scan


def _make_skill_with_files(tmp_path, files):
    """Create a skill directory with specified files for testing."""
    skill_dir = os.path.join(tmp_path, "test-skill")
    os.makedirs(skill_dir, exist_ok=True)
    for name, content in files.items():
        path = os.path.join(skill_dir, name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)
    return skill_dir


class TestSecurityScan:
    def test_clean_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill_with_files(tmp, {
                "SKILL.md": "---\nname: test\n---\n# Test\n",
                "scripts/main.py": "print('hello')\n",
            })
            result = security_scan(skill_dir)
            assert result["clean"] is True
            assert len(result["issues"]) == 0

    def test_detects_openai_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill_with_files(tmp, {
                "scripts/main.py": 'api_key = "sk-abcdefghijklmnopqrstuvwxyz1234567890"\n',
            })
            result = security_scan(skill_dir)
            assert result["clean"] is False
            assert any(i["pattern"] == "OpenAI API Key" for i in result["issues"])

    def test_detects_aws_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill_with_files(tmp, {
                "config.txt": "aws_key=AKIAIOSFODNN7EXAMPLE\n",
            })
            result = security_scan(skill_dir)
            assert result["clean"] is False
            assert any(i["pattern"] == "AWS Access Key" for i in result["issues"])

    def test_detects_github_token(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill_with_files(tmp, {
                "scripts/deploy.py": 'token = "ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh1234"\n',
            })
            result = security_scan(skill_dir)
            assert result["clean"] is False
            assert any(i["pattern"] == "GitHub Personal Access Token" for i in result["issues"])

    def test_detects_env_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill_with_files(tmp, {
                ".env": "SECRET=value\n",
            })
            result = security_scan(skill_dir)
            assert result["clean"] is False
            assert any(i["pattern"] == "Sensitive file" for i in result["issues"])

    def test_detects_eval_usage(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill_with_files(tmp, {
                "scripts/danger.py": "result = eval(user_input)\n",
            })
            result = security_scan(skill_dir)
            assert result["clean"] is False
            assert any(i["pattern"] == "eval() usage" for i in result["issues"])

    def test_detects_exec_usage(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill_with_files(tmp, {
                "scripts/danger.py": "exec(code_string)\n",
            })
            result = security_scan(skill_dir)
            assert result["clean"] is False
            assert any(i["pattern"] == "exec() usage" for i in result["issues"])

    def test_nonexistent_path(self):
        result = security_scan("/nonexistent/path/xyz")
        assert result["clean"] is False
        assert any(i["pattern"] == "missing_directory" for i in result["issues"])

    def test_severity_sorting(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill_with_files(tmp, {
                ".env": "SECRET=value\n",
                "scripts/code.py": 'x = eval("1+1")\n',
            })
            result = security_scan(skill_dir)
            assert result["clean"] is False
            severities = [i["severity"] for i in result["issues"]]
            severity_order = {"high": 0, "medium": 1, "low": 2}
            numeric = [severity_order[s] for s in severities]
            assert numeric == sorted(numeric)

    def test_detects_generic_secret(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill_with_files(tmp, {
                "config.yaml": 'api_key: "mysupersecretkey123"\n',
            })
            result = security_scan(skill_dir)
            assert result["clean"] is False
            assert any(i["pattern"] == "Generic Secret" for i in result["issues"])

    def test_skips_binary_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = _make_skill_with_files(tmp, {
                "data.bin": "",
            })
            bin_path = os.path.join(skill_dir, "data.bin")
            with open(bin_path, "wb") as f:
                f.write(b"\x00\x01\x02\x03sk-abcdefghijklmnopqrstuvwxyz1234567890")
            result = security_scan(skill_dir)
            assert result["clean"] is True
