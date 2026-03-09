Get Started
===============

This page gives a quick overview of how to get started with **sphinx-ymmsl**.

Installation
------------

To install sphinx-ymmsl use pip: 

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

Basic Usage
-----------

Once the extension is configured, you can use the ``.. ymmsl::`` directive in your reStructuredText files to include documentation generated from a yMMSL file.

Syntax
~~~~~~

The basic syntax is:

.. code-block:: rst

   .. ymmsl:: path/to/your/file.ymmsl

The path should be relative to your Sphinx source directory (typically the ``docs/`` folder).


When Sphinx builds your documentation, the ``.. ymmsl::`` directive will:

1. Parse the yMMSL file
2. Generate formatted Markdown documentation
3. Convert the Markdown to HTML

