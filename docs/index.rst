sphinx-ymmsl documentation
==========================

**sphinx-ymmsl** is a Sphinx extension that automatically generates documentation from yMMSL files. 

For more information about yMMSL files and the yMMSL language specification, see the `yMMSL documentation <https://ymmsl-python.readthedocs.io/en/develop/index.html>`_.

Examples
========

This section shows several examples of how yMMSL files are converted into Markdown documentation.

Macro-Micro Model
-------------

Below is an example of a macro-micro model, this example was taken from the `yMMSL documentation <https://ymmsl-python.readthedocs.io/en/develop/basic_usage.html>`_.

Input File
~~~~~~~~~~

.. literalinclude:: examples/example_model.ymmsl
   :language: ymmsl
   :caption: example_model.ymmsl

Converted Output
~~~~~~~~~~~~~~~~

The yMMSL file is processed and generates the following documentation: 

.. ymmsl:: examples/example_model.ymmsl

