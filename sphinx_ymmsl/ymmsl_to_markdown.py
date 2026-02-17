"""Generation of a markdown file based on a yMMSL file."""

import argparse
from pathlib import Path

import ymmsl

from .markdown_utilities import (
    demote_markdown_headers,
    format_title,
    markdown_table,
)


def model_markdown_generation(cfg: ymmsl.v0_2.Configuration) -> str:
    """
    Generate Markdown documentation for models in a yMMSL configuration.

    The generated documentation includes:
    - Model titles along with their descriptions.
    - Conduits listed as bullet points.
    - Components with their descriptions, ports presented in tables, and implementation.
    - A table of supported settings for each model.
    """
    if not cfg.models:
        return ""

    markdown_lines = ["## Models", ""]

    for model_name, model_data in cfg.models.items():
        markdown_lines.append(f"### {format_title(model_name)}")

        if model_data.description:
            desc = demote_markdown_headers(model_data.description.strip(), level=3)
            markdown_lines.extend([desc, ""])

        if model_data.conduits:
            markdown_lines.append("#### Conduits")
            for conduit in model_data.conduits:
                markdown_lines.append(f"* {conduit.sender}: {conduit.receiver}")
            markdown_lines.append("")

        if model_data.components:
            for comp_name, component in model_data.components.items():
                markdown_lines.append(f"#### {format_title(comp_name)}")

                if component.description:
                    comp_desc = demote_markdown_headers(
                        component.description.strip(), level=4
                    )
                    markdown_lines.extend([comp_desc, ""])

                if component.ports:
                    headers = ["Operator", "Port Name"]
                    rows = [
                        (component.ports[port_name].operator.name, port_name)
                        for port_name in component.ports
                    ]
                    markdown_lines.extend([markdown_table(headers, rows), ""])

                if component.implementation:
                    markdown_lines.extend(
                        [f"**Implementation**: `{component.implementation}`", ""]
                    )

                if component.multiplicity:
                    markdown_lines.extend(
                        [f"**Multiplicity**: `{component.multiplicity}`", ""]
                    )

        if model_data.supported_settings:
            markdown_lines.append("#### Supported Settings")
            headers = ["Parameter", "Type", "Description"]
            rows = [
                (param_name, str(setting.typ), setting.description or "")
                for param_name, setting in model_data.supported_settings
            ]
            markdown_lines.extend([markdown_table(headers, rows), ""])

            markdown_lines.append(
                "For more information about the types: [yMMSL documentation](https://ymmsl-python.readthedocs.io/en/develop/index.html)."
            )
            markdown_lines.append("")

    return "\n".join(markdown_lines)


def ymmsl_to_markdown(ymmsl_path: Path) -> str:
    """
    Generate complete Markdown documentation for a yMMSL file.

    The documentation includes:
        - A title based on the yMMSL file name.
        - The configuration description, if available.
        - The yMMSL file name and version.
        - Detailed model documentation defined by model_markdown_generation.
    """
    cfg = ymmsl.load_as(ymmsl.v0_2.Configuration, ymmsl_path)

    markdown_lines = []
    markdown_lines.append(f"# yMMSL {format_title(ymmsl_path.stem)} Documentation")

    if cfg.description:
        desc = demote_markdown_headers(cfg.description.strip())
        markdown_lines.extend([desc, ""])

    markdown_lines.append(f"**Model file**: `{ymmsl_path.name}`")

    # Extract version from file
    for line in ymmsl_path.read_text().splitlines():
        if line.startswith("ymmsl_version:"):
            version_value = line.split(":", 1)[1].strip()
            markdown_lines.append(f"**yMMSL version**: `{version_value}`")

    markdown_lines.append("")

    markdown_lines.append(model_markdown_generation(cfg))

    return "\n".join(markdown_lines)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate Markdown documentation from a yMMSL file."
    )
    parser.add_argument("input", type=Path, help="Path to input .ymmsl file")
    parser.add_argument("output", type=Path, help="Path to output .md file")

    args = parser.parse_args()

    markdown_text = ymmsl_to_markdown(args.input)

    args.output.write_text(markdown_text, encoding="utf-8")
    print(f"Markdown file saved as: {args.output}")


if __name__ == "__main__":
    main()
