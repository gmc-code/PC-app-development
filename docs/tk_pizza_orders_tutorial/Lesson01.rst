================================================
Create a window
================================================


.. image:: images/pizza_1.png
    :scale: 50%

- **Objective**: Set up the basic Tkinter root.
- **Content**:

  - Introduction to Tkinter.
  - Creating a basic root.
  - Adding a title and configuring the window size.

Introduction to Tkinter
--------------------------------

- Tkinter is a standard GUI (Graphical User Interface) library for Python.
- It provides tools to create desktop applications with windows, buttons, text fields, and more.

----

Creating a Basic Window
--------------------------------

.. code-block:: python

    import tkinter as tk

    # Create the main window
    root = tk.Tk()
    root.title("Pizza Ordering System")
    root.geometry("900x600")

    # Run the application
    root.mainloop()

- ``import tkinter as tk``: Imports the Tkinter library and assigns it the alias ``tk``.
- ``root = tk.Tk()``: Creates the main application root.
- ``root.title("Pizza Ordering System")``: Sets the title of the root.
- ``root.geometry("900x600")``: Sets the size of the window to 900 pixels wide and 600 pixels tall.
- ``root.mainloop()``: Starts the Tkinter event loop, which waits for user interactions.
