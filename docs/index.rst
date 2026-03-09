sphinx-ymmsl documentation
==========================

**sphinx-ymmsl** is a Sphinx extension that automatically generates documentation from yMMSL files. 

When you use the ``.. ymmsl::`` directive in your Sphinx documentation, the extension:

1. **Parses** the yMMSL file to extract information
2. **Generates** formatted Markdown documentation
3. **Converts** the Markdown to reStructuredText nodes that Sphinx can render as HTML

This allows you to maintain your yMMSL files and automatically generate human-readable documentation without manual duplication.

For more information about yMMSL files and the yMMSL language specification, see the `yMMSL documentation <https://ymmsl-python.readthedocs.io/en/develop/index.html>`_.

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   get_started
   examples
