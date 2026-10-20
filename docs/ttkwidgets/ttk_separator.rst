====================================================
ttk Separator
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#separator>`_

----

What is a Separator?
-----------------------

| A **Separator** is a thin line that splits a window into sections, like a ruled line on a page.
| It does nothing except make a layout easier to read. tk has no Separator; it only comes with ttk.

----

Making a Separator
---------------------

| A Separator has almost no size of its own, so it must be **stretched** when it is placed.
| A side-to-side line uses ``pack(fill="x")``.

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first Separator")

    ttk.Label(root, text="Part 1: Questions", font=("Arial", 14)).pack(pady=10)

    line = ttk.Separator(root, orient="horizontal")    # 1. Create it
    line.pack(fill="x", padx=20, pady=10)              # 2. Stretch it across the window

    ttk.Label(root, text="Part 2: Answers", font=("Arial", 14)).pack(pady=10)

    root.mainloop()                 # Keep the window open

| ``padx=20`` stops the line touching the edges of the window. ``pady=10`` adds space above and below it.

----

Separator options
--------------------

orient
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses a side-to-side line (``"horizontal"``, the default) or an up-and-down line (``"vertical"``).
| **How to write it:** ``orient="vertical"``
| A vertical line is stretched with ``fill="y"``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Vertical separator")

    ttk.Label(root, text="Left side").pack(side="left", padx=30)

    ttk.Separator(root, orient="vertical").pack(side="left", fill="y", pady=20)

    ttk.Label(root, text="Right side").pack(side="left", padx=30)

    root.mainloop()

----

Using Separators
-------------------

Separating parts of a form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x280")
    root.title("Order form")

    ttk.Label(root, text="Pizza order", font=("Arial", 16, "bold")).pack(pady=5)
    ttk.Separator(root).pack(fill="x", padx=10, pady=5)

    ttk.Label(root, text="Name:").pack()
    ttk.Entry(root).pack()
    ttk.Separator(root).pack(fill="x", padx=10, pady=10)

    size = tk.StringVar(value="Medium")
    for choice in ["Small", "Medium", "Large"]:
        ttk.Radiobutton(root, text=choice, variable=size, value=choice).pack()
    ttk.Separator(root).pack(fill="x", padx=10, pady=10)

    ttk.Button(root, text="Order").pack()

    root.mainloop()

With grid
~~~~~~~~~~~~~~~~~~

| With ``grid``, use ``columnspan`` so the line goes across several columns, and ``sticky="ew"`` to stretch it from west to east.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("grid")

    ttk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
    ttk.Label(root, text="Score").grid(row=0, column=1, padx=10, pady=5)

    ttk.Separator(root).grid(row=1, column=0, columnspan=2, sticky="ew")

    ttk.Label(root, text="Ava").grid(row=2, column=0, pady=2)
    ttk.Label(root, text="95").grid(row=2, column=1, pady=2)
    ttk.Label(root, text="Ben").grid(row=3, column=0, pady=2)
    ttk.Label(root, text="88").grid(row=3, column=1, pady=2)

    root.mainloop()

Side-by-side sections
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("320x200")
    root.title("Two sections")

    left = ttk.Frame(root, padding=10)
    left.pack(side="left", fill="both", expand=True)
    ttk.Label(left, text="Player 1", font=("Arial", 14)).pack()
    ttk.Label(left, text="Score: 0").pack()

    ttk.Separator(root, orient="vertical").pack(side="left", fill="y", pady=10)

    right = ttk.Frame(root, padding=10)
    right.pack(side="left", fill="both", expand=True)
    ttk.Label(right, text="Player 2", font=("Arial", 14)).pack()
    ttk.Label(right, text="Score: 0").pack()

    root.mainloop()

----

Separator methods
--------------------

| A Separator has no methods of its own. ``pack_forget()`` hides it and ``destroy()`` removes it, like any widget.

----

Styling a Separator
----------------------

| The style is ``"TSeparator"``. ``background`` sets the colour of the line.
| A Separator is always thin. To make a **thick** line, use a coloured ``ttk.Frame`` with a ``height`` instead.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Separator style")

    style = ttk.Style()
    style.configure("Red.TSeparator", background="red")
    style.configure("Thick.TFrame", background="navy")

    ttk.Label(root, text="A red separator").pack(pady=5)
    ttk.Separator(root, style="Red.TSeparator").pack(fill="x", padx=20, pady=5)

    ttk.Label(root, text="A thick line (a Frame)").pack(pady=5)
    ttk.Frame(root, height=6, style="Thick.TFrame").pack(fill="x", padx=20, pady=5)

    root.mainloop()

----

Quick reference
-------------------

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option or method
      - What it does
      - Example
    * - ``orient``
      - Side-to-side or up-and-down line
      - ``orient="vertical"``
    * - ``pack(fill="x")``
      - Stretch a side-to-side line
      - ``line.pack(fill="x", padx=20)``
    * - ``pack(fill="y")``
      - Stretch an up-and-down line
      - ``line.pack(side="left", fill="y")``
    * - ``grid(sticky="ew")``
      - Stretch a line in a grid
      - ``grid(row=1, columnspan=2, sticky="ew")``
    * - ``"TSeparator"``
      - Style name; ``background`` is the line colour
      - ``style.configure("TSeparator", background="red")``

----

.. admonition:: Tasks

    #. Make a window titled "Sections" that is 300x200 with a title label, a Separator across the window, and a label underneath.
    #. Add 20 pixels of space at each end of the line and 10 pixels above and below it.
    #. Make two labels side by side with a vertical Separator between them.
    #. Make a blue Separator style and use it.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Sections")

                    ttk.Label(root, text="My Notes", font=("Arial", 16)).pack(pady=10)
                    ttk.Separator(root).pack(fill="x")
                    ttk.Label(root, text="Bring a hat").pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Sections")

                    ttk.Label(root, text="My Notes", font=("Arial", 16)).pack(pady=10)
                    ttk.Separator(root).pack(fill="x", padx=20, pady=10)
                    ttk.Label(root, text="Bring a hat").pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Side by side")

                    ttk.Label(root, text="Cats").pack(side="left", padx=40)
                    ttk.Separator(root, orient="vertical").pack(side="left", fill="y", pady=20)
                    ttk.Label(root, text="Dogs").pack(side="left", padx=40)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Blue line")

                    style = ttk.Style()
                    style.configure("Blue.TSeparator", background="blue")

                    ttk.Label(root, text="My Notes", font=("Arial", 16)).pack(pady=10)
                    ttk.Separator(root, style="Blue.TSeparator").pack(fill="x", padx=20, pady=10)
                    ttk.Label(root, text="Bring a hat").pack(pady=10)

                    root.mainloop()
