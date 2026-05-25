====================================================
tk command binding
====================================================

Overview
----------------------------------------------------

In Tkinter, **command binding** allows you to connect a widget (such as a
button or slider) to a Python function. When the user interacts with the
widget (e.g., clicks a button), the linked function is executed.

This is essential for making your GUI interactive.


Basic Syntax
----------------------------------------------------

The general syntax for command binding is:

.. code-block:: python

    widget = tk.Widget(parent, command=function_name)

Explanation:

- The `command` option is used to bind a function to the widget.
- Do NOT use parentheses `()` after the function name.
- Writing `command=my_function()` will execute the function immediately.

----

Example 1: Button Command Binding
----------------------------------------------------

.. code-block:: python

    import tkinter as tk

    def say_hello():
        print("Hello!")

    root = tk.Tk()

    button = tk.Button(root, text="Click Me", command=say_hello)
    button.pack()

    root.mainloop()

Explanation:

- When the button is clicked, `say_hello` runs.
- The function is passed as a reference, not called immediately.

----

Example 2: Using Lambda for Arguments
----------------------------------------------------

Sometimes you need to pass arguments to a function.

.. code-block:: python

    import tkinter as tk

    def greet(name):
        print("Hello", name)

    root = tk.Tk()

    button = tk.Button(root, text="Click",
                       command=lambda: greet("Alice"))
    button.pack()

    root.mainloop()

Explanation:

- `lambda` creates an anonymous function.
- This allows passing arguments safely.

----

Example 3: Using Tkinter Variables (DoubleVar)
----------------------------------------------------

Command bindings often work with Tkinter variables like `DoubleVar`.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()

    value = tk.DoubleVar()

    def show_value():
        print(value.get())

    scale = tk.Scale(root, from_=0, to=10,
                     resolution=0.1,
                     variable=value)
    scale.pack()

    button = tk.Button(root, text="Print Value",
                       command=show_value)
    button.pack()

    root.mainloop()

Explanation:

- `DoubleVar()` stores a floating-point number.
- The scale updates `value` automatically.
- The button prints the current value using `.get()`.

----

Common Widgets Supporting command
----------------------------------------------------

The following widgets support the `command` option:

- Button
- Checkbutton
- Radiobutton
- Scale
- Menu items

Example:

.. code-block:: python

    checkbox = tk.Checkbutton(root, text="Accept",
                              command=my_function)

----

command vs bind()
----------------------------------------------------

Tkinter provides two ways to handle events:

1. command (simple)
2. bind() (advanced)


----

Using command
----------------------------------------------------

- Easy to use
- No event object
- Works for common actions

.. code-block:: python

    tk.Button(root, command=my_function)

----------------------------------------------------
Using bind()
----------------------------------------------------

- More control (keyboard, mouse events)
- Provides event information

.. code-block:: python

    def on_click(event):
        print("Mouse clicked at", event.x, event.y)

    widget.bind("<Button-1>", on_click)

----

Key Differences
----------------------------------------------------

- `command` is simpler, used for basic widget actions.
- `bind()` is more powerful, used for detailed event handling.


Summary
----------------------------------------------------

- `command` links a widget to a function.
- Do not call the function directly (no parentheses).
- Use `lambda` to pass arguments.
- Combine with Tkinter variables (`DoubleVar`, `IntVar`) for dynamic GUIs.
- Use `bind()` for advanced event handling.


