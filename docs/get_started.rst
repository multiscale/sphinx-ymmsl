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

