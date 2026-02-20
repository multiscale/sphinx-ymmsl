"""Sphinx extension to generate documentation from yMMSL files."""

# See https://www.sphinx-doc.org/en/master/development/tutorials/extending_syntax.html

import importlib.metadata
from pathlib import Path

from docutils import nodes
from myst_parser.parsers.sphinx_ import MystParser
from sphinx.application import Sphinx
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective, new_document
from sphinx.util.typing import ExtensionMetadata

from .ymmsl_to_markdown import ymmsl_to_markdown

logger = logging.getLogger(__name__)


class YmmslDirective(SphinxDirective):
    """Sphinx directive to generate documentation for all models and components in a
    yMMSL file.
    """

    required_arguments = 1  # ymmsl file name

    def run(self) -> list[nodes.Node]:
        """Process yMMSL file and generate corresponding node list"""
        filename = self.arguments[0]
        logger.info("Generating documentation from ymmsl file: %s", filename)

        ymmsl_path = Path(self.env.srcdir) / filename
        markdown = ymmsl_to_markdown(ymmsl_path)

        # Use myst_parser for generated markdown. Adapted from sphinx-autodoc2
        # https://github.com/sphinx-extensions2/sphinx-autodoc2/blob/main/src/autodoc2/sphinx/docstring.py
        document = new_document(filename, self.state.document.settings)
        parser = MystParser()
        parser.parse(markdown, document)

        self.env.note_dependency(filename)
        return document.children


def setup(app: Sphinx) -> ExtensionMetadata:
    """Setup sphinx extension."""
    app.add_directive("ymmsl", YmmslDirective)

    # We need myst_parser to process the markdown we generate
    app.setup_extension("myst_parser")

    return {
        "version": importlib.metadata.version("sphinx_ymmsl"),
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
