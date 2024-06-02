====================================================
Introduction to tkinter
====================================================

| **Tkinter** is a standard Python GUI (Graphical User Interface) library that provides tools and widgets to create desktop applications with graphical interfaces.
| **Tkinter** allows you to create windows, buttons, labels, text boxes, and other GUI components to build interactive applications in Python.


Key references:
---------------------


| Tk Docs http://www.tkdocs.com/
| Tk Refs https://tkdocs.com/pyref/index.html
| Tutorial https://tkdocs.com/tutorial/index.html
| https://docs.python.org/3.12/library/tk.html
| https://docs.python.org/3.12/library/tkinter.ttk.html


| Python Tutorial https://www.pythontutorial.net/tkinter/
| Tkinter (GUI Programming) - Python Tutorial. https://pythonbasics.org/tkinter/.
| What is Tkinter for Python? - GeeksforGeeks. https://www.geeksforgeeks.org/introduction-to-tkinter/.
| tk widgets: https://www.geeksforgeeks.org/python-gui-tkinter/

----

Version checks
----------------

| Check python version:

.. code-block:: python

    import sys

    print(sys.version)

----

| Check the Tk version:
| Tcl/Tk version 8.6.13 is installed with python 3.12.

.. code-block:: python

    import tkinter

    print(tkinter.Tcl().eval('info patchlevel'))




