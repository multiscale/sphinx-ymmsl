"""Utilities for generating a markdown file based on a ymmsl file."""

from typing import Any, Iterable, List


def format_title(name: str) -> str:
    """Replace underscores with spaces and capitalize each word."""
    return str(name).replace("_", " ").title()


def demote_markdown_headers(text: str, level: int = 1) -> str:
    """
    Demote markdown headers by adding extra '#' characters.
    """
    lines = text.splitlines()
    new_lines = []

    for line in lines:
        if line.startswith("#"):
            new_lines.append("#" * level + line)
        else:
            new_lines.append(line)

    return "\n".join(new_lines)


def markdown_table(headers: List[str], rows: Iterable[Any]) -> str:
    """
    Create a Markdown table.

    Args:
        headers: List of column headers.
        rows: Iterable of row iterables.
    """
    bad_headers = [h for h in headers if "|" in h]
    if bad_headers:
        # Replacing | with \| so the pipes are treated as text andd NOT as Markdown
        # table column separator.
        headers = [h.replace("|", r"\|") for h in headers]

    table_lines = []
    table_lines.append("| " + " | ".join(headers) + " |")
    table_lines.append("| " + " | ".join(["-" * len(h) for h in headers]) + " |")

    for row in rows:
        row_str = " | ".join(str(cell) if cell is not None else "" for cell in row)
        table_lines.append(f"| {row_str} |")

    return "\n".join(table_lines)
