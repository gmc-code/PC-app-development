====================================================
Creating a window with tkinter
====================================================

tkinter basic window
----------------------------------------

- The code creates a basic window using tkinter.
- The window is created by instantiating the `Tk` class from the `tkinter` module.
- The `title` method sets the title of the window to "pack side".
- The `geometry` method sets the size of the window to 250 pixels wide and 150 pixels tall.
- The `mainloop` method starts the event loop, which keeps the window open and responsive to user interactions until it is closed.
- This is a fundamental structure for creating a GUI application with tkinter.
- The code is straightforward and serves as a starting point for building more complex GUI applications using tkinter.
- The window will appear with the specified title and size, and it will remain open until the user closes it.
- This code is a basic template for creating a tkinter window, and it can be expanded upon by adding widgets, event handlers, and other functionalities to create a more interactive application.


.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.title("basic window")
    root.geometry("250x150")


    root.mainloop()

