
====================================================
tk command binding
====================================================

Overview
----------------------------------------------------

| In Tkinter, **command binding** allows you to connect a widget (such as a
button or slider) to a Python function.
| When the user interacts with the
widget (e.g., clicks a button), the linked function is executed.
| This is essential for making your GUI interactive.
| This is best for buttons, menus, scales, spinboxes

| Many Tkinter widgets support the ``command`` option.
| A callback function is called automatically when the user interacts with the widget.
| The callback can then modify other widgets in the window.


----

Basic Syntax
----------------------------------------------------

The general syntax for command binding is:

.. code-block:: python

    widget = tk.Widget(parent, command=function_name)

Explanation:

- The `command` option is used to bind a function to the widget.
- Do NOT use parentheses `()` after the function name.

----

Example 1: Button Command Binding
----------------------------------------------------

.. code-block:: python

    import tkinter as tk


    def change_text():
        label.config(text="Button pressed!")


    # Create the main window
    root = tk.Tk()
    root.geometry("200x100")  # Set window size
    root.title("Button -> label Example")  # Set window title

    button = tk.Button(root, text="Click me", command=change_text)
    button.pack(pady=10)

    label = tk.Label(root, text="Waiting...")
    label.pack(pady=10)

    root.mainloop()

Explanation:

- The `command` option is used to bind `change_text` to the button.
- When the button is clicked, `change_text` runs.
- The label is updated with the new text.

----

Example 2: Using Lambda for Arguments
----------------------------------------------------

Sometimes you need to pass arguments to a function.

.. code-block:: python

    import tkinter as tk


    def greet(name):
        label.config(text=f"Hello {name}.")


    # Create the main window
    root = tk.Tk()
    root.geometry("200x100")  # Set window size
    root.title("Button lambda -> label Example")  # Set window title

    button = tk.Button(root, text="Click", command=lambda: greet("Alice"))
    button.pack(pady=10)

    label = tk.Label(root, text="Waiting...")
    label.pack(pady=10)

    root.mainloop()


Explanation:

- `lambda` creates an anonymous function.
- This allows passing arguments safely.

----

Example 3: Checkbutton  Command Binding
----------------------------------------------------

.. py:function:: tk.Checkbutton(..., command=function)

    | A Checkbutton calls the function whenever it is selected or deselected.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()

    selected = tk.IntVar()

    def update():
        if selected.get():
            label.config(text="Checked")
        else:
            label.config(text="Unchecked")

    check = tk.Checkbutton(
        root,
        text="Option",
        variable=selected,
        command=update
    )

    label = tk.Label(root, text="Unchecked")

    check.pack()
    label.pack()

    root.mainloop()



----


.. py:function:: tk.Radiobutton(..., command=function)

    | A Radiobutton calls the function whenever a different option is selected.

    .. code-block:: python

        import tkinter as tk

        root = tk.Tk()

        choice = tk.StringVar(value="Red")

        def update():
            label.config(text=choice.get())

        tk.Radiobutton(
            root,
            text="Red",
            variable=choice,
            value="Red",
            command=update
        ).pack()

        tk.Radiobutton(
            root,
            text="Blue",
            variable=choice,
            value="Blue",
            command=update
        ).pack()

        label = tk.Label(root, text="Red")
        label.pack()

        root.mainloop()



----

.. py:function:: tk.Scale(..., command=function)

    | A Scale passes the current slider value to the callback.

    .. code-block:: python

        import tkinter as tk

        root = tk.Tk()

        def update(value):
            label.config(text=value)

        scale = tk.Scale(
            root,
            from_=0,
            to=100,
            command=update
        )

        label = tk.Label(root, text="0")

        scale.pack()
        label.pack()

        root.mainloop()



----

.. py:function:: tk.Spinbox(..., command=function)

    | A Spinbox calls the function whenever the arrow buttons change the value.

    .. code-block:: python

        import tkinter as tk

        root = tk.Tk()

        def update():
            label.config(text=spin.get())

        spin = tk.Spinbox(
            root,
            from_=1,
            to=10,
            command=update
        )

        label = tk.Label(root, text="1")

        spin.pack()
        label.pack()

        root.mainloop()

----


.. py:function:: tk.OptionMenu(..., command=function)

    | An OptionMenu passes the selected option to the callback.

    .. code-block:: python

        import tkinter as tk

        root = tk.Tk()

        selected = tk.StringVar(value="Apple")

        def update(choice):
            label.config(text=choice)

        menu = tk.OptionMenu(
            root,
            selected,
            "Apple",
            "Orange",
            "Pear",
            command=update
        )

        label = tk.Label(root, text="Apple")

        menu.pack()
        label.pack()

        root.mainloop()



----

.. py:function:: tk.Menubutton(...)

    | A Menubutton uses the commands of its attached Menu.

    .. code-block:: python

        import tkinter as tk

        root = tk.Tk()

        def update():
            label.config(text="Green selected")

        button = tk.Menubutton(root, text="Colours")

        menu = tk.Menu(button, tearoff=0)
        menu.add_command(label="Green", command=update)

        button.config(menu=menu)

        button.pack()

        label = tk.Label(root, text="Waiting...")
        label.pack()

        root.mainloop()


----

.. py:function:: tk.Scrollbar(..., command=widget.yview)

    | A Scrollbar usually controls another widget by calling one of its scrolling methods.

    .. code-block:: python

        import tkinter as tk

        root = tk.Tk()

        text = tk.Text(root, width=20, height=5)

        scrollbar = tk.Scrollbar(
            root,
            command=text.yview
        )

        text.config(yscrollcommand=scrollbar.set)

        text.pack(side="left")
        scrollbar.pack(side="right", fill="y")

        root.mainloop()





