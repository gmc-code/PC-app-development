====================================================
tk Menu
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Menu>`_
| See: `<https://www.geeksforgeeks.org/python-menu-widget-in-tkinter/>`_

----

Usage
-------------

| The `tkinter.Menu` widget is used to create top-level menus, pull-down menus, and pop-up (context) menus.
| To create a menu widget, the general syntax is
| (assuming import via "import tkinter as tk"):

.. py:function:: menu_widget = tk.Menu(parent, option=value)


| `parent` is the window or frame object.
| Options can be passed as parameters separated by commas.



| A `Menu` widget is typically used in conjunction with a `tk.Tk` root window as a menu bar, or as a standalone component for submenus.

---

Sample Menu
----------------------

| The code below creates a simple file menu with an "Exit" command.

.. code-block:: python


    import tkinter as tk

    root = tk.Tk()
    root.title("Menu Example")
    root.geometry("300x200")

    # 1. Create the main Menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # 2. Create a "File" submenu
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)

    # 3. Add commands to the "File" submenu
    file_menu.add_command(label="Exit", command=root.quit)

    root.mainloop()


----

Common Menu Methods
---------------------------

.. py:function:: menu_widget.add_command(label=text, command=function)


    | Adds a new command button to the menu.



.. py:function:: menu_widget.add_cascade(label=text, menu=submenu)


    | Adds a new submenu to the menu.



.. py:function:: menu_widget.add_separator()


    | Adds a horizontal line separator to the menu.



.. py:function:: menu_widget.add_checkbutton(label=text, variable=tk_var)


    | Adds a checkbutton item to the menu.



---

Parameter syntax
----------------------------

.. py:function:: menu_widget = tk.Menu(parent, option=value)


    **Parameters:**

    .. py:attribute:: activebackground

        | Syntax: ``menu_widget.config(activebackground="color")``
        | Description: Background color of the item when active or hovered.
        | Default: SystemHighlight

    .. py:attribute:: activeforeground

        | Syntax: ``menu_widget.config(activeforeground="color")``
        | Description: Text color of the item when active or hovered.
        | Default: SystemHighlightText

    .. py:attribute:: background or bg

        | Syntax: ``menu_widget.config(bg="color")``
        | Description: Background color of the menu.

    .. py:attribute:: font

        | Syntax: ``menu_widget.config(font=("FontName", size, style))``
        | Description: Font of the menu items.

    .. py:attribute:: fg or foreground

        | Syntax: ``menu_widget.config(fg="color")``
        | Description: Text color of the menu items.

    .. py:attribute:: tearoff

        | Syntax: ``menu_widget.config(tearoff=boolean)``
        | Description: Whether the menu can be "torn off" into a separate window.
        | Default: 1



----

## Default options

| Code to get the defaults for each menu option is below.

.. code-block:: python


    import tkinter as tk

    root = tk.Tk()
    menu = tk.Menu(root)

    for option in menu.keys():
        print(f"{option}: {menu.cget(option)}")

    root.mainloop()

