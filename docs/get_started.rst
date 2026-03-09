Get Started
===============

This guide will help you get started with **sphinx-ymmsl**, a Sphinx extension that automatically generates documentation from yMMSL files.

Installation
------------

You can install sphinx-ymmsl using pip:

.. code-block:: bash

   pip install sphinx-ymmsl

Configuration
-------------

To use sphinx-ymmsl in your Sphinx documentation project, you need to add it to the list of extensions in your ``conf.py`` file:

.. code-block:: python

   extensions = [
       'sphinx_ymmsl',
       # ... other extensions
   ]

.. note::
   The sphinx-ymmsl extension automatically loads the ``myst_parser`` extension, which is required to process the generated Markdown content.

Basic Usage
-----------

Once the extension is configured, you can use the ``.. ymmsl::`` directive in your reStructuredText files to include documentation generated from a yMMSL file.

Syntax
~~~~~~

The basic syntax is:

.. code-block:: rst

   .. ymmsl:: path/to/your/file.ymmsl

The path should be relative to your Sphinx source directory (typically the ``docs/`` folder).

Example
~~~~~~~

Suppose you have a yMMSL file at ``docs/models/my_model.ymmsl``. You can include its documentation in your RST file like this:

.. code-block:: rst

   My Model Documentation
   ======================

   This page documents my multiscale model.

   .. ymmsl:: models/my_model.ymmsl

When Sphinx builds your documentation, the ``.. ymmsl::`` directive will:

1. Parse the yMMSL file
2. Generate formatted Markdown documentation
3. Convert the Markdown to HTML

What Gets Documented
--------------------

The sphinx-ymmsl extension automatically extracts and documents the following information from your yMMSL files:

- **Model descriptions**: High-level overview of your multiscale model
- **Supported settings**: Configuration parameters with their types and descriptions
- **Components**: Individual computational components with their descriptions
- **Ports**: Input and output ports for each component or model, including data types
- **Multiplicity**: Information about replicated components
- **Conduits**: Connections between components

Next Steps
----------

- See the :doc:`examples` page for detailed examples of yMMSL files and their generated documentation
- Learn more about the yMMSL language in the `yMMSL documentation <https://ymmsl-python.readthedocs.io/en/develop/index.html>`_
- Explore the `MUSCLE3 documentation <https://muscle3.readthedocs.io/>`_ to understand how yMMSL fits into the multiscale modeling workflow
