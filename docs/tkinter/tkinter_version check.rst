====================================================
Version checks
====================================================


| Check python verion:

.. code-block:: python

    import sys

    print(sys.version)

----

| Chekc the Tk version:
| Tcl/Tk version 8.6.13 is installed with python 3.12.

.. code-block:: python

    import tkinter

    print(tkinter.Tcl().eval('info patchlevel'))


