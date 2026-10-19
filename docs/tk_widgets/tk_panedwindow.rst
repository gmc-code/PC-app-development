====================================================
tk PanedWindow
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.PanedWindow>`_

----

What is a PanedWindow?
-------------------------

| A **PanedWindow** splits part of a window into two or more sections called **panes**.
| Between the panes is a line called a **sash**. The user drags the sash to make one pane bigger and the other smaller.
| You have seen this in apps like File Explorer, where you can drag the line between the folder list and the files.

----

Making a PanedWindow
-------------------------

| A PanedWindow is made differently from most widgets. Widgets go **into** it with ``.add()``, not ``.pack()``.

#. **Create** the PanedWindow and **place** it with ``.pack()``.
#. **Create** a widget for each pane, using the PanedWindow as the parent.
#. **Add** each widget to the PanedWindow with ``.add(widget)``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first PanedWindow")

    panes = tk.PanedWindow(root)                    # 1. Create the PanedWindow
    panes.pack(fill="both", expand=True)            #    and fill the window

    left_label = tk.Label(panes, text="Left", bg="lightblue")      # 2. Create the widgets
    right_label = tk.Label(panes, text="Right", bg="lightgreen")

    panes.add(left_label)                           # 3. Add them as panes
    panes.add(right_label)

    root.mainloop()                 # Keep the window open

| Move the mouse over the line between the two colours, then drag it left and right.

----

PanedWindow options
----------------------

| Options are written as ``option=value`` inside ``tk.PanedWindow( )``, separated by commas.

orient
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses whether the panes sit side by side or one above the other.
| **How to write it:** ``orient="vertical"``
| **Values:** ``"horizontal"`` (side by side, the default) and ``"vertical"`` (top and bottom).

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("orient")

    panes = tk.PanedWindow(root, orient="vertical")
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Top", bg="pink"))
    panes.add(tk.Label(panes, text="Bottom", bg="lightyellow"))

    root.mainloop()

| ``panes.add(tk.Label(panes, ...))`` creates a label and adds it in one line.

sashwidth and sashrelief
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``sashwidth`` sets how thick the dragging line is, in pixels. ``sashrelief`` sets its border style.
| **How to write them:** ``sashwidth=8, sashrelief="raised"``
| A thicker sash is easier to find and drag.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("sashwidth")

    panes = tk.PanedWindow(root, sashwidth=10, sashrelief="raised")
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Drag the", bg="lightblue"))
    panes.add(tk.Label(panes, text="thick sash", bg="lightgreen"))

    root.mainloop()

bg
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the colour of the PanedWindow. This is the colour of the **sash**, because the panes cover the rest.
| **How to write it:** ``bg="colour"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("bg")

    panes = tk.PanedWindow(root, bg="red", sashwidth=6)
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Left", bg="white"))
    panes.add(tk.Label(panes, text="Right", bg="white"))

    root.mainloop()

showhandle
~~~~~~~~~~~~~~~~~~

| **What it does:** ``showhandle=True`` draws a small square handle on the sash, showing the user where to grab it.
| **How to write it:** ``showhandle=True``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("showhandle")

    panes = tk.PanedWindow(root, showhandle=True, sashwidth=6)
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Left", bg="lightblue"))
    panes.add(tk.Label(panes, text="Right", bg="lightgreen"))

    root.mainloop()

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** draw a border around the whole PanedWindow.
| **How to write them:** ``relief="solid", borderwidth=2``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("relief")

    panes = tk.PanedWindow(root, relief="solid", borderwidth=2)
    panes.pack(fill="both", expand=True, padx=10, pady=10)

    panes.add(tk.Label(panes, text="Left", bg="lightblue"))
    panes.add(tk.Label(panes, text="Right", bg="lightgreen"))

    root.mainloop()

----

PanedWindow methods
----------------------

| A **method** is an action that a widget can do. Methods are written after a dot, e.g. ``panes.add(...)``.

add
~~~~~~~~~~~~~~~~~~

| **What it does:** puts a widget into the PanedWindow as a new pane.
| **How to write it:** ``panes.add(widget)``
| Panes appear in the order they are added. Any widget can be a pane, including a **Frame** full of other widgets.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("400x200")
    root.title("add")

    panes = tk.PanedWindow(root, sashwidth=5)
    panes.pack(fill="both", expand=True)

    # Pane 1: a list of topics
    topic_list = tk.Listbox(panes)
    for topic in ["Planets", "Stars", "Moons"]:
        topic_list.insert(tk.END, topic)
    panes.add(topic_list)

    # Pane 2: a box for notes
    notes_box = tk.Text(panes, wrap="word")
    notes_box.insert("1.0", "Type your notes here")
    panes.add(notes_box)

    root.mainloop()

add with minsize and width
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``add()`` can also have options for that pane:

- ``width=150`` sets the starting width of the pane in pixels (use ``height`` for vertical panes).
- ``minsize=80`` stops the user dragging the pane smaller than 80 pixels.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("400x200")
    root.title("minsize")

    panes = tk.PanedWindow(root, sashwidth=5)
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Menu", bg="lightblue"), width=100, minsize=80)
    panes.add(tk.Label(panes, text="Main area", bg="white"), minsize=150)

    root.mainloop()

forget
~~~~~~~~~~~~~~~~~~

| **What it does:** removes a pane from the PanedWindow.
| **How to write it:** ``panes.forget(widget)``
| Use ``panes.add(widget)`` to put it back.

.. code-block:: python

    import tkinter as tk


    def hide_help():
        panes.forget(help_label)


    def show_help():
        panes.add(help_label)


    root = tk.Tk()
    root.geometry("400x250")
    root.title("forget")

    panes = tk.PanedWindow(root, sashwidth=5)
    panes.pack(fill="both", expand=True)

    game_label = tk.Label(panes, text="Game area", bg="white")
    help_label = tk.Label(panes, text="Help:\nUse the arrow keys", bg="lightyellow")
    panes.add(game_label)
    panes.add(help_label)

    tk.Button(root, text="Hide help", command=hide_help).pack(side="left", padx=10, pady=5)
    tk.Button(root, text="Show help", command=show_help).pack(side="left", padx=10, pady=5)

    root.mainloop()

panes
~~~~~~~~~~~~~~~~~~

| **What it does:** gives back a list of the panes, so you can count them.
| **How to write it:** ``count = len(panes.panes())``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("panes")

    panes = tk.PanedWindow(root)
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="A", bg="pink"))
    panes.add(tk.Label(panes, text="B", bg="lightblue"))
    panes.add(tk.Label(panes, text="C", bg="lightgreen"))

    count_label = tk.Label(root, text=f"Number of panes: {len(panes.panes())}")
    count_label.pack()

    root.mainloop()

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options **after** the PanedWindow has been made.
| **How to write it:** ``panes.config(option=value)``

.. code-block:: python

    import tkinter as tk


    def flip():
        if panes.cget("orient") == "horizontal":
            panes.config(orient="vertical")
        else:
            panes.config(orient="horizontal")


    root = tk.Tk()
    root.geometry("300x250")
    root.title("config")

    panes = tk.PanedWindow(root, sashwidth=5)
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="One", bg="lightblue"))
    panes.add(tk.Label(panes, text="Two", bg="lightgreen"))

    tk.Button(root, text="Flip", command=flip).pack(pady=5)

    root.mainloop()

----

Panes inside panes
---------------------

| A PanedWindow can be added to another PanedWindow. This makes layouts like a code editor: a list on the left, and on the right a top pane and a bottom pane.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("400x250")
    root.title("Panes inside panes")

    outer = tk.PanedWindow(root, orient="horizontal", sashwidth=5)
    outer.pack(fill="both", expand=True)

    outer.add(tk.Label(outer, text="Files", bg="lightblue"), width=100)

    inner = tk.PanedWindow(outer, orient="vertical", sashwidth=5)     # Inside "outer"
    outer.add(inner)

    inner.add(tk.Label(inner, text="Code", bg="white"), height=150)
    inner.add(tk.Label(inner, text="Output", bg="black", fg="white"))

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
      - Side by side or top and bottom
      - ``orient="vertical"``
    * - ``sashwidth``
      - Thickness of the dragging line
      - ``sashwidth=8``
    * - ``sashrelief``
      - Border style of the dragging line
      - ``sashrelief="raised"``
    * - ``bg``
      - Colour of the sash
      - ``bg="gray"``
    * - ``showhandle``
      - Show a handle on the sash
      - ``showhandle=True``
    * - ``relief``, ``borderwidth``
      - Border around the whole widget
      - ``relief="solid", borderwidth=2``
    * - ``add()``
      - Put a widget in as a pane
      - ``panes.add(label)``
    * - ``add(..., width=)``
      - Starting size of the pane
      - ``panes.add(label, width=100)``
    * - ``add(..., minsize=)``
      - Smallest size of the pane
      - ``panes.add(label, minsize=80)``
    * - ``forget()``
      - Remove a pane
      - ``panes.forget(label)``
    * - ``panes()``
      - List of the panes
      - ``len(panes.panes())``
    * - ``config()``
      - Change options later
      - ``panes.config(sashwidth=10)``

----

.. admonition:: Tasks

    #. Make a window titled "Panes" that is 300x200. Add a PanedWindow that fills the window, with two labels side by side: "Left" on a yellow background and "Right" on an orange background.
    #. Change your PanedWindow so the panes are top and bottom, and the sash is 10 pixels thick.
    #. Make a PanedWindow with a Listbox of three animals in the left pane and a Text box in the right pane. The left pane should start 120 pixels wide.
    #. Make a PanedWindow with three panes, "Red", "Green" and "Blue", each with that colour as the background. Use ``minsize`` so no pane can be dragged smaller than 50 pixels.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Panes")

                    panes = tk.PanedWindow(root)
                    panes.pack(fill="both", expand=True)

                    left_label = tk.Label(panes, text="Left", bg="yellow")
                    right_label = tk.Label(panes, text="Right", bg="orange")
                    panes.add(left_label)
                    panes.add(right_label)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Panes")

                    panes = tk.PanedWindow(root, orient="vertical", sashwidth=10)
                    panes.pack(fill="both", expand=True)

                    top_label = tk.Label(panes, text="Top", bg="yellow")
                    bottom_label = tk.Label(panes, text="Bottom", bg="orange")
                    panes.add(top_label)
                    panes.add(bottom_label)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("400x200")
                    root.title("Animals")

                    panes = tk.PanedWindow(root, sashwidth=5)
                    panes.pack(fill="both", expand=True)

                    animal_list = tk.Listbox(panes)
                    for animal in ["Koala", "Wombat", "Platypus"]:
                        animal_list.insert(tk.END, animal)
                    panes.add(animal_list, width=120)

                    notes_box = tk.Text(panes)
                    panes.add(notes_box)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("RGB")

                    panes = tk.PanedWindow(root, sashwidth=5)
                    panes.pack(fill="both", expand=True)

                    for colour in ["Red", "Green", "Blue"]:
                        panes.add(tk.Label(panes, text=colour, bg=colour.lower(), fg="white"),
                                  minsize=50)

                    root.mainloop()
