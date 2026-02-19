Examples
========

This section demonstrates how yMMSL files are converted to Markdown documentation using the ``ymmsl`` directive.

Example Model
-------------

Below is an example of a macro-micro model. The yMMSL input file (``examples/example_model.ymmsl``) is automatically converted to formatted documentation.

Input File
~~~~~~~~~~

.. literalinclude:: examples/example_model.ymmsl
   :language: ymmsl
   :caption: examples/example_model.ymmsl

Converted Output
~~~~~~~~~~~~~~~~

The ``.. ymmsl::`` directive processes the yMMSL file and generates the following documentation:

.. ymmsl:: examples/example_model.ymmsl
