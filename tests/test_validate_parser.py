import unittest

from scripts.validate import (
    _field_exists_in_frontmatter,
    _parse_frontmatter,
    _parse_yaml_field,
)


class ValidateParserTests(unittest.TestCase):
    def test_parse_frontmatter_uses_line_delimiter_only(self) -> None:
        content = (
            "---\n"
            "name: sample-skill\n"
            'description: "Value with --- inside"\n'
            "---\n"
            "Body line\n"
        )
        frontmatter, body = _parse_frontmatter(content)

        self.assertIsNotNone(frontmatter)
        self.assertEqual(_parse_yaml_field(frontmatter or "", "name"), "sample-skill")
        self.assertEqual(body, "Body line")

    def test_parse_yaml_field_ignores_nested_keys(self) -> None:
        frontmatter = (
            "metadata:\n"
            "  license: MIT\n"
            "name: parser-skill\n"
        )
        self.assertEqual(_parse_yaml_field(frontmatter, "name"), "parser-skill")
        self.assertIsNone(_parse_yaml_field(frontmatter, "license"))
        self.assertFalse(_field_exists_in_frontmatter(frontmatter, "license"))

    def test_field_exists_does_not_match_prefix(self) -> None:
        frontmatter = (
            "license_key: value\n"
            "name: prefix-skill\n"
        )
        self.assertFalse(_field_exists_in_frontmatter(frontmatter, "license"))
        self.assertTrue(_field_exists_in_frontmatter(frontmatter, "name"))

    def test_parse_yaml_block_scalar_still_supported(self) -> None:
        frontmatter = (
            "description: >-\n"
            "  first line\n"
            "  second line\n"
            "name: scalar-skill\n"
        )
        self.assertEqual(
            _parse_yaml_field(frontmatter, "description"),
            "first line second line",
        )
        self.assertEqual(_parse_yaml_field(frontmatter, "name"), "scalar-skill")


if __name__ == "__main__":
    unittest.main()
