====================================================
ttk Sizegrip
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#sizegrip>`_

----

What is a Sizegrip?
----------------------

| A **Sizegrip** is the small pattern of dots or lines in the **bottom-right corner** of a window.
| The user drags it to make the window bigger or smaller.
| Windows can already be resized from their edges, but a Sizegrip shows the user clearly where to grab. tk has no Sizegrip; it only comes with ttk.

----

Making a Sizegrip
--------------------

| A Sizegrip should go in the **bottom-right corner** of the window.
| With ``pack``, put it at the bottom, on the right: ``pack(side="bottom", anchor="se")``. ``"se"`` means south-east, the bottom-right corner.
| Pack the Sizegrip **first**, so other widgets do not take its place.

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first Sizegrip")

    grip = ttk.Sizegrip(root)                       # 1. Create it
    grip.pack(side="bottom", anchor="se")           # 2. Bottom-right corner

    ttk.Label(root, text="Drag the bottom-right corner", font=("Arial", 12)).pack(pady=60)

    root.mainloop()                 # Keep the window open

----

Sizegrip options
-------------------

| A Sizegrip has very few options. The useful ones are ``style`` and ``cursor``.

cursor
~~~~~~~~~~~~~~~~~~

| **What it does:** changes the mouse pointer over the Sizegrip. Most computers already show a resize arrow.
| **How to write it:** ``cursor="sizing"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("cursor")

    ttk.Sizegrip(root, cursor="sizing").pack(side="bottom", anchor="se")
    ttk.Label(root, text="Point at the corner").pack(pady=60)

    root.mainloop()

----

Using a Sizegrip
-------------------

With a status bar
~~~~~~~~~~~~~~~~~~~~

| Many apps have a **status bar** along the bottom, with the Sizegrip at its right-hand end.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("350x220")
    root.title("Status bar")

    status_bar = ttk.Frame(root, relief="sunken", borderwidth=1)
    status_bar.pack(side="bottom", fill="x")

    ttk.Sizegrip(status_bar).pack(side="right")
    ttk.Label(status_bar, text="Ready").pack(side="left", padx=5)

    notes_box = tk.Text(root, wrap="word")
    notes_box.insert("1.0", "Drag the corner to make this window bigger.")
    notes_box.pack(fill="both", expand=True)

    root.mainloop()

| ``fill="both", expand=True`` makes the Text box grow when the window is made bigger.

With grid
~~~~~~~~~~~~~~~~~~

| With ``grid``, put the Sizegrip in the bottom-right cell with ``sticky="se"``.
| ``rowconfigure`` and ``columnconfigure`` with ``weight=1`` let row 0 and column 0 grow when the window is resized.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("grid")

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    big_box = tk.Text(root)
    big_box.grid(row=0, column=0, sticky="nsew")      # Fills its cell

    ttk.Sizegrip(root).grid(row=1, column=0, sticky="se")

    root.mainloop()

Stopping resizing
~~~~~~~~~~~~~~~~~~~~

| ``root.resizable(False, False)`` stops the window being resized. Leave out the Sizegrip in that case, or the user will think they can drag it.
| ``root.minsize(width, height)`` stops the window being made smaller than a size.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("minsize")
    root.minsize(250, 150)                          # Cannot be made smaller than this

    ttk.Sizegrip(root).pack(side="bottom", anchor="se")
    ttk.Label(root, text="Try to make me tiny!").pack(pady=60)

    root.mainloop()

----

Styling a Sizegrip
---------------------

| The style is ``"TSizegrip"``. ``background`` sets the colour behind the grip, so it can match a coloured status bar.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Sizegrip style")

    style = ttk.Style()
    style.configure("Status.TFrame", background="lightsteelblue")
    style.configure("Status.TLabel", background="lightsteelblue")
    style.configure("Status.TSizegrip", background="lightsteelblue")

    status_bar = ttk.Frame(root, style="Status.TFrame")
    status_bar.pack(side="bottom", fill="x")
    ttk.Sizegrip(status_bar, style="Status.TSizegrip").pack(side="right")
    ttk.Label(status_bar, text="Saved", style="Status.TLabel").pack(side="left", padx=5)

    root.mainloop()

----

Quick reference
-------------------

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Code
      - What it does
      - Example
    * - ``ttk.Sizegrip(root)``
      - Make a Sizegrip
      - ``grip = ttk.Sizegrip(root)``
    * - ``pack(side="bottom", anchor="se")``
      - Put it in the bottom-right corner
      - ``grip.pack(side="bottom", anchor="se")``
    * - ``grid(sticky="se")``
      - Bottom-right of a grid cell
      - ``grip.grid(row=1, column=0, sticky="se")``
    * - ``root.minsize()``
      - Smallest window size
      - ``root.minsize(250, 150)``
    * - ``root.resizable()``
      - Allow or stop resizing
      - ``root.resizable(False, False)``
    * - ``"TSizegrip"``
      - Style name
      - ``style.configure("TSizegrip", background="white")``

----

.. admonition:: Tasks

    #. Make a window titled "Resize me" that is 300x200 with a Sizegrip in the bottom-right corner.
    #. Add a Text box that grows when the window is made bigger.
    #. Stop the window being made smaller than 200 x 120.
    #. Make a status bar along the bottom with the label "Words: 0" on the left and the Sizegrip on the right.

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
                    root.title("Resize me")

                    ttk.Sizegrip(root).pack(side="bottom", anchor="se")

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Resize me")

                    ttk.Sizegrip(root).pack(side="bottom", anchor="se")

                    text_box = tk.Text(root)
                    text_box.pack(fill="both", expand=True)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Resize me")
                    root.minsize(200, 120)

                    ttk.Sizegrip(root).pack(side="bottom", anchor="se")

                    text_box = tk.Text(root)
                    text_box.pack(fill="both", expand=True)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Resize me")

                    status_bar = ttk.Frame(root)
                    status_bar.pack(side="bottom", fill="x")
                    ttk.Sizegrip(status_bar).pack(side="right")
                    ttk.Label(status_bar, text="Words: 0").pack(side="left", padx=5)

                    text_box = tk.Text(root)
                    text_box.pack(fill="both", expand=True)

                    root.mainloop()
