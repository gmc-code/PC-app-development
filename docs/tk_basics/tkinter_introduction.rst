====================================================
Introduction to tkinter
====================================================

| **Tkinter** is a standard Python GUI (Graphical User Interface) library that provides tools and widgets to create desktop applications with graphical interfaces.
| **Tkinter** allows you to create windows, buttons, labels, text boxes, and other GUI components to build interactive applications in Python.


Key references:
---------------------

| Latest python versions: `<https://www.python.org/downloads/>`_

| Tk Docs http://www.tkdocs.com/>`_
| Tk Refs `<https://tkdocs.com/pyref/index.html>`_
| Tutorial `<https://tkdocs.com/tutorial/index.html>`_
| `<https://docs.python.org/3.14/library/tk.html>`_
| `<https://docs.python.org/3.14/library/tkinter.ttk.html>`_


| Python Tutorial `<https://www.pythontutorial.net/tkinter/>`_
| Tkinter (GUI Programming) - Python Tutorial. `<https://pythonbasics.org/tkinter/>`_.
| What is Tkinter for Python? - GeeksforGeeks. `<https://www.geeksforgeeks.org/introduction-to-tkinter>`_.
| tk widgets: `<https://www.geeksforgeeks.org/python-gui-tkinter/>`_

----

Version checks
----------------

| Check python version:

.. code-block:: python

    import sys

    print(sys.version)

----

| Check the Tk version:
| Tcl/Tk version 8.6.14 with python 3.13.
| Tcl/Tk version 8.6.15 with python 3.14.

.. code-block:: python

    import tkinter as tk

    print(tk.Tcl().eval('info patchlevel'))




