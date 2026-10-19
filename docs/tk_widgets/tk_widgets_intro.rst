====================================================
Tkinter widgets
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html>`_

----

What is a widget?
-------------------

| A **widget** is one part of a window that the user can see or use: a button, a box to type in, a slider, a picture, and so on.
| An app is built by putting widgets into a window. **Tkinter** is the Python library used to make windows and widgets.
| Each widget has **options** (to change how it looks) and **methods** (actions it can do).

----

Making a window
-------------------

| Every Tkinter program starts and ends the same way:

.. code-block:: python

    import tkinter as tk            # Load the tkinter library and call it "tk"

    root = tk.Tk()                  # Make the main window, called "root"
    root.geometry("300x200")        # Window size: 300 pixels wide, 200 pixels high
    root.title("My app")            # Words in the title bar

    # Widgets go here

    root.mainloop()                 # Keep the window open until the user closes it

| ``mainloop()`` must be the **last** line. It keeps the window open and waits for the user to click and type.

----

Making a widget
-------------------

| Every widget is made in two steps:

#. **Create** the widget: ``name = tk.WidgetType(parent, option=value, option=value)``
#. **Place** the widget in the window: ``name.pack()``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("My app")

    greeting = tk.Label(root, text="Hello!", font=("Arial", 24), fg="blue")   # 1. Create
    greeting.pack()                                                            # 2. Place

    root.mainloop()

| ``parent`` is where the widget lives, usually ``root`` (the window) or a **Frame**.
| **Options** such as ``text``, ``font`` and ``fg`` are written as ``option=value``, separated by commas.

----

Options and methods
----------------------

| **Options** change how a widget looks or behaves. Set them when the widget is made, or change them later with ``config()``.

.. code-block:: python

    greeting = tk.Label(root, text="Hello!")    # Set an option when the widget is made
    greeting.config(text="Goodbye!")            # Change an option later

| **Methods** are actions a widget can do. They are written after a dot, with brackets.

.. code-block:: python

    typed = name_entry.get()                    # Read what was typed in an Entry
    name_entry.delete(0, tk.END)                # Clear the Entry

----

Placing widgets
-------------------

| A widget will not appear until it is placed in the window. Tkinter has three ways to place widgets.

pack
~~~~~~~~~~~~~~~~~~

| ``pack()`` stacks widgets one after another, from top to bottom. It is the easiest to use.
| ``pack(side="left")`` puts them side by side. ``pady`` and ``padx`` add space around them.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("pack")

    tk.Label(root, text="First").pack(pady=5)
    tk.Label(root, text="Second").pack(pady=5)
    tk.Label(root, text="Third").pack(pady=5)

    root.mainloop()

grid
~~~~~~~~~~~~~~~~~~

| ``grid()`` places widgets in **rows** and **columns**, like a table. Rows and columns are counted from **0**.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("grid")

    tk.Label(root, text="Name:").grid(row=0, column=0)
    tk.Entry(root).grid(row=0, column=1)
    tk.Label(root, text="Age:").grid(row=1, column=0)
    tk.Entry(root).grid(row=1, column=1)

    root.mainloop()

place
~~~~~~~~~~~~~~~~~~

| ``place()`` puts a widget at an exact spot, measured in pixels from the top-left corner of the window.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("place")

    tk.Label(root, text="Top left").place(x=10, y=10)
    tk.Label(root, text="Over here").place(x=180, y=140)

    root.mainloop()

.. note::

    Use only **one** of ``pack``, ``grid`` or ``place`` for widgets that share the same parent.
    Mixing ``pack`` and ``grid`` in the same window can make the program freeze.
    To use different layouts in different parts of the window, put each part in its own **Frame**.

----

The widgets
--------------

| Click a widget's name to go to its page.

.. list-table::
    :header-rows: 1
    :widths: 25 75

    * - Widget
      - What it is for
    * - :doc:`Button <tk_button>`
      - A button the user clicks to make something happen.
    * - :doc:`Canvas <tk_canvas>`
      - An area to draw lines, shapes, words and pictures on.
    * - :doc:`Checkbutton <tk_checkbutton>`
      - A tick box. The user can tick as many as they like.
    * - :doc:`Entry <tk_entry>`
      - A box for typing one line, e.g. a name or a number.
    * - :doc:`Frame <tk_frame>`
      - An invisible box that holds and groups other widgets.
    * - :doc:`Label <tk_label>`
      - Shows words or a picture.
    * - :doc:`LabelFrame <tk_labelframe>`
      - A frame with a border and a title.
    * - :doc:`Listbox <tk_listbox>`
      - A list of items the user can choose from.
    * - :doc:`Menu <tk_menu>`
      - A menu bar along the top of the window, or a right-click menu.
    * - :doc:`Menubutton <tk_menubutton>`
      - A button that opens a drop-down menu.
    * - :doc:`Message <tk_message>`
      - Shows longer text that wraps onto new lines by itself.
    * - :doc:`OptionMenu <tk_optionmenu>`
      - A drop-down list for choosing one item.
    * - :doc:`PanedWindow <tk_panedwindow>`
      - Splits an area into sections the user can resize by dragging.
    * - :doc:`Radiobutton <tk_radiobutton>`
      - Round buttons in a group. The user can choose only one.
    * - :doc:`Scale <tk_scale>`
      - A slider for choosing a number.
    * - :doc:`Scrollbar <tk_scrollbar>`
      - Lets the user scroll through a Listbox, Text or Canvas.
    * - :doc:`Spinbox <tk_spinbox>`
      - A box with up and down arrows for choosing a number.
    * - :doc:`Text <tk_text>`
      - A big box for typing or showing many lines of text.
    * - :doc:`Toplevel <tk_toplevel>`
      - An extra window.

----

Choosing the right widget
----------------------------

.. list-table::
    :header-rows: 1
    :widths: 50 50

    * - I want to...
      - Use a...
    * - Show some words
      - Label
    * - Show a paragraph of words
      - Message (or Label with ``wraplength``)
    * - Let the user type one line
      - Entry
    * - Let the user type lots of lines
      - Text
    * - Let the user click to do something
      - Button
    * - Let the user choose **one** option
      - Radiobutton, OptionMenu or Listbox
    * - Let the user choose **many** options
      - Checkbutton or Listbox (``selectmode="multiple"``)
    * - Let the user choose a number
      - Scale or Spinbox
    * - Draw shapes or make a game
      - Canvas
    * - Group widgets together
      - Frame or LabelFrame
    * - Add File / Edit / Help menus
      - Menu
    * - Open another window
      - Toplevel

----

.. admonition:: Tasks

    #. Write the four lines that every Tkinter program needs to make a window titled "Test" that is 400x300.
    #. Add a label that says "Welcome" and place it with ``pack()``.
    #. Use ``grid()`` to place a label "Username:" in row 0, column 0 and an Entry in row 0, column 1.
    #. Use the "Choosing the right widget" table. Which widget would you use for: (a) choosing a volume from 0 to 100, (b) choosing your year level from a list, (c) typing a story?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("400x300")
                    root.title("Test")

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("400x300")
                    root.title("Test")

                    welcome_label = tk.Label(root, text="Welcome")
                    welcome_label.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("400x300")
                    root.title("Test")

                    tk.Label(root, text="Username:").grid(row=0, column=0)
                    tk.Entry(root).grid(row=0, column=1)

                    root.mainloop()

            .. tab-item:: Q4

                | (a) Scale (or Spinbox)
                | (b) OptionMenu (or Radiobutton or Listbox)
                | (c) Text
