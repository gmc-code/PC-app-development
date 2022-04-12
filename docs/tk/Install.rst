====================================================
Install
====================================================

| See: https://tkdocs.com/tutorial/install.html

| Tcl/Tk version 8.6.10 is installed with python 3.10.

.. code-block:: python

    import tkinter


    print(tkinter.Tcl().eval('info patchlevel'))
    # 8.6.10

----

pip install pygubu

pygubu takes an xml file and builds a user interface via tkinter

pip install pygubu-designer
pygubu-designer is a WYSIWYG program to create the xml for pygubu to use.
