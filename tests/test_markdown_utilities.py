"""Tests for markdown_utilities module."""

from sphinx_ymmsl.markdown_utilities import (
    demote_markdown_headers,
    format_title,
    markdown_table,
)


class TestFormatTitle:
    """Tests for format_title function."""

    def test_single_underscore(self):
        """Test replacing single underscore with space."""
        assert format_title("hello_world") == "Hello World"

    def test_empty_string(self):
        """Test empty string."""
        assert format_title("") == ""


class TestDemoteMarkdownHeaders:
    """Tests for demote_markdown_headers function."""

    def test_single_header_level(self):
        """Test demoting a single level 1 header."""
        text = "# Header"
        result = demote_markdown_headers(text, level=1)
        assert result == "## Header"

    def test_no_headers(self):
        """Test text without headers."""
        text = "Just some text\nNo headers here"
        result = demote_markdown_headers(text, level=1)
        assert result == text

    def test_empty_string(self):
        """Test empty string."""
        text = ""
        result = demote_markdown_headers(text, level=1)
        assert result == ""

    def test_header_with_hash_in_text(self):
        """Test that only leading hashes are affected."""
        text = "# Header with # in text"
        result = demote_markdown_headers(text, level=1)
        assert result == "## Header with # in text"


class TestMarkdownTable:
    """Tests for markdown_table function."""

    def test_simple_table(self):
        """Test creating a simple table with different data types."""
        headers = ["Name", "Age", "Empty", "Bool", "None"]
        rows = [["Alice", 30, "", False, None], ["Bob", 25, "", True, None]]
        result = markdown_table(headers, rows)
        expected = (
            "| Name | Age | Empty | Bool | None |\n"
            "| ---- | --- | ----- | ---- | ---- |\n"
            "| Alice | 30 |  | False |  |\n"
            "| Bob | 25 |  | True |  |"
        )
        assert result == expected

    def test_pipe_in_header(self):
        """Test table with pipe character in header."""
        headers = ["Name|ID", "Age"]
        rows = [["Alice", 30]]
        result = markdown_table(headers, rows)
        expected = (
            r"| Name\|ID | Age |" + "\n"
            r"| -------- | --- |" + "\n"
            "| Alice | 30 |"
        )
        assert result == expected
