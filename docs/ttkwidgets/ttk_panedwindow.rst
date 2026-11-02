====================================================
ttk PanedWindow
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk PanedWindow?
-----------------------------

| A **ttk PanedWindow** splits an area into **panes** with a line (a **sash**) between them. The user drags the sash to resize the panes.
| It works like a tk PanedWindow, with two differences:

- It has **fewer options**: no ``sashwidth``, ``sashrelief``, ``showhandle`` or ``bg``. Its look comes from the theme.
- ``add()`` has a ``weight`` option that controls how the panes grow when the window is resized.

----

Making a ttk PanedWindow
---------------------------

| Widgets go **into** a PanedWindow with ``.add()``, not ``.pack()``.

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk PanedWindow")

    panes = ttk.PanedWindow(root, orient="horizontal")     # 1. Create the PanedWindow
    panes.pack(fill="both", expand=True)                   #    and fill the window

    left_box = tk.Listbox(panes)                           # 2. Widgets for each pane
    left_box.insert(tk.END, "Drag the line")
    right_box = tk.Text(panes)
    right_box.insert("1.0", "between the panes")

    panes.add(left_box)                                    # 3. Add them as panes
    panes.add(right_box)

    root.mainloop()                 # Keep the window open

----

ttk PanedWindow options
--------------------------

orient
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses side by side (``"horizontal"``) or top and bottom (``"vertical"``, the default).
| **How to write it:** ``orient="horizontal"``

.. note::

    A ttk PanedWindow is ``"vertical"`` (top and bottom) by default. A tk PanedWindow is ``"horizontal"`` by default.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("orient")

    panes = ttk.PanedWindow(root, orient="vertical")
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Top", bg="pink"))
    panes.add(tk.Label(panes, text="Bottom", bg="lightyellow"))

    root.mainloop()

width and height
~~~~~~~~~~~~~~~~~~

| **What they do:** set the size of the PanedWindow in pixels, when it is not stretched with ``fill``.
| **How to write them:** ``width=250, height=120``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and height")

    panes = ttk.PanedWindow(root, orient="horizontal", width=250, height=120)
    panes.pack(pady=30)

    panes.add(tk.Label(panes, text="Left", bg="lightblue"))
    panes.add(tk.Label(panes, text="Right", bg="lightgreen"))

    root.mainloop()

----

ttk PanedWindow methods
--------------------------

add
~~~~~~~~~~~~~~~~~~

| **What it does:** puts a widget in as a new pane. Any widget can be a pane, including a **Frame** full of widgets.
| **How to write it:** ``panes.add(widget)``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("400x200")
    root.title("add")

    panes = ttk.PanedWindow(root, orient="horizontal")
    panes.pack(fill="both", expand=True)

    menu_frame = ttk.Frame(panes, padding=10)
    ttk.Button(menu_frame, text="Planets").pack(pady=3)
    ttk.Button(menu_frame, text="Stars").pack(pady=3)
    panes.add(menu_frame)

    notes_box = tk.Text(panes, wrap="word")
    notes_box.insert("1.0", "Type your notes here")
    panes.add(notes_box)

    root.mainloop()

add with weight
~~~~~~~~~~~~~~~~~~

| **What it does:** ``weight`` decides how much each pane grows when the window gets bigger.
| ``weight=0`` means the pane keeps its size. ``weight=1`` and ``weight=3`` means the second pane gets 3 times as much of the extra space.
| **How to write it:** ``panes.add(widget, weight=1)``
| Resize the window to see the difference.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("400x200")
    root.title("weight")

    panes = ttk.PanedWindow(root, orient="horizontal")
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Menu\n(weight 0)", bg="lightblue", width=12), weight=0)
    panes.add(tk.Label(panes, text="Main area\n(weight 1)", bg="white"), weight=1)

    root.mainloop()

insert and forget
~~~~~~~~~~~~~~~~~~~~

| ``panes.insert(position, widget)`` adds a pane at a position (0 is first).
| ``panes.forget(widget)`` removes a pane. Add it again to bring it back.
| Removing a pane that is not there causes a ``TclError``, so ``try`` and ``except`` stop a crash if the button is clicked twice.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def hide_help():
        try:
            panes.forget(help_label)
        except tk.TclError:
            pass                            # Already hidden, so do nothing


    def show_help():
        panes.insert(0, help_label)       # Put it back as the first pane


    root = tk.Tk()
    root.geometry("400x250")
    root.title("insert and forget")

    panes = ttk.PanedWindow(root, orient="horizontal")
    panes.pack(fill="both", expand=True)

    help_label = tk.Label(panes, text="Help:\nUse the arrows", bg="lightyellow", width=15)
    game_label = tk.Label(panes, text="Game area", bg="white")
    panes.add(help_label)
    panes.add(game_label, weight=1)

    ttk.Button(root, text="Hide help", command=hide_help).pack(side="left", padx=40, pady=5)
    ttk.Button(root, text="Show help", command=show_help).pack(side="left")

    root.mainloop()

panes
~~~~~~~~~~~~~~~~~~

| ``panes.panes()`` gives a list of the panes. ``len(panes.panes())`` counts them.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("panes")

    panes = ttk.PanedWindow(root, orient="horizontal")
    panes.pack(fill="both", expand=True)

    for colour in ["pink", "lightblue", "lightgreen"]:
        panes.add(tk.Label(panes, text=colour, bg=colour), weight=1)

    ttk.Label(root, text=f"Number of panes: {len(panes.panes())}").pack()

    root.mainloop()

sashpos
~~~~~~~~~~~~~~~~~~

| **What it does:** reads or moves a sash. The first sash is number 0.
| ``panes.sashpos(0)`` gives its position in pixels. ``panes.sashpos(0, 100)`` moves it to 100 pixels.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def half():
        width = panes.winfo_width()
        panes.sashpos(0, width // 2)        # Move the sash to the middle


    root = tk.Tk()
    root.geometry("400x220")
    root.title("sashpos")

    panes = ttk.PanedWindow(root, orient="horizontal")
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Left", bg="lightblue", width=8))
    panes.add(tk.Label(panes, text="Right", bg="lightgreen"), weight=1)

    ttk.Button(root, text="Split in half", command=half).pack(pady=5)

    root.mainloop()

----

Panes inside panes
---------------------

| A PanedWindow can be added to another PanedWindow to make a three-part layout.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("400x250")
    root.title("Panes inside panes")

    outer = ttk.PanedWindow(root, orient="horizontal")
    outer.pack(fill="both", expand=True)

    outer.add(tk.Label(outer, text="Files", bg="lightblue", width=12))

    inner = ttk.PanedWindow(outer, orient="vertical")      # Inside "outer"
    outer.add(inner, weight=1)

    inner.add(tk.Label(inner, text="Code", bg="white"), weight=3)
    inner.add(tk.Label(inner, text="Output", bg="black", fg="white"), weight=1)

    root.mainloop()

----

Styling a ttk PanedWindow
----------------------------

| The style is ``"TPanedwindow"``. ``background`` sets the colour behind the panes, which shows as the sash colour.
| ``"Sash"`` is a separate style; with the ``"clam"`` theme its ``sashthickness`` sets how thick the sash is.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("PanedWindow style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TPanedwindow", background="red")
    style.configure("Sash", sashthickness=10)

    panes = ttk.PanedWindow(root, orient="horizontal")
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Left", bg="white"), weight=1)
    panes.add(tk.Label(panes, text="Right", bg="white"), weight=1)

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
      - ``orient="horizontal"``
    * - ``width``, ``height``
      - Size in pixels
      - ``width=250, height=120``
    * - ``add()``
      - Add a pane
      - ``panes.add(label)``
    * - ``add(..., weight=)``
      - How much the pane grows
      - ``panes.add(label, weight=1)``
    * - ``insert()``
      - Add a pane at a position
      - ``panes.insert(0, label)``
    * - ``forget()``
      - Remove a pane
      - ``panes.forget(label)``
    * - ``panes()``
      - List the panes
      - ``len(panes.panes())``
    * - ``sashpos()``
      - Read or move a sash
      - ``panes.sashpos(0, 100)``
    * - ``"TPanedwindow"``, ``"Sash"``
      - Style names
      - ``style.configure("Sash", sashthickness=10)``

----

All PanedWindow options
---------------------------

| Here is every option a ttk PanedWindow can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``class_``
      - A group name used to style many widgets at once (advanced). Written ``class_`` in Python
      - ``class_="Sidebar"``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``height``
      - How tall it is (in pixels)
      - ``height=200``
    * - ``orient``
      - Panes side by side (``"horizontal"``) or stacked (``"vertical"``)
      - ``orient="horizontal"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TPanedwindow"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``width``
      - How wide it is (in pixels)
      - ``width=300``

| ttk PanedWindow has no ``bg``, ``fg`` or ``font`` options. Change its colours and fonts with a style, e.g. ``style.configure("TPanedwindow", background="lightblue")``.

----

Quiz
--------------------------------

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 20

    .. multichoice::

        What is a ttk PanedWindow?

        [x] A themed container split into panes that can be resized by dragging | Correct. The bar between panes is the sash.
        [ ] A pop-up window | Incorrect. That is a Toplevel.
        [ ] A window with tabs | Incorrect. That is a Notebook.
        [ ] A list | Incorrect. That is a Listbox.

    .. multichoice::

        What does orient="horizontal" do?

        [x] Puts the panes side by side | Correct. horizontal goes across.
        [ ] Stacks the panes | Incorrect. That is "vertical".
        [ ] Hides the sash | Incorrect. It sets direction.
        [ ] Rotates the text | Incorrect. It sets direction.

    .. multichoice::

        What is the default orient for ttk.PanedWindow?

        [ ] "horizontal" | Incorrect. The ttk default is vertical.
        [x] "vertical", so panes are stacked | Correct. Set orient="horizontal" for side by side.
        [ ] "both" | Incorrect. Not a value.
        [ ] "none" | Incorrect. Not a value.

    .. multichoice::

        For a ttk PanedWindow, width and height are measured in:

        [x] Pixels | Correct. It is a container.
        [ ] Characters | Incorrect. Not for containers.
        [ ] Lines | Incorrect. Not lines.
        [ ] Panes | Incorrect. Not panes.

    .. multichoice::

        How is a widget put into a pane?

        [ ] widget.pack() | Incorrect. Panes use add.
        [x] panes.add(widget) | Correct. add puts it in a new pane.
        [ ] panes.insert(widget) | Incorrect. insert needs a position first.
        [ ] widget.grid() | Incorrect. Use add.

    .. multichoice::

        What does weight=1 in panes.add(left, weight=1) do?

        [ ] Makes the pane heavier to drag | Incorrect. It shares space.
        [x] Lets the pane grow when the window gets bigger | Correct. Panes with weight share extra space.
        [ ] Sets the width to 1 | Incorrect. It shares space.
        [ ] Adds one pane | Incorrect. It sets the share.

    .. multichoice::

        If one pane has weight=1 and another weight=3, what happens when the window grows?

        [x] The second pane gets three times as much extra space | Correct. Space is shared by weight.
        [ ] Both get the same | Incorrect. Weights differ.
        [ ] Only the first grows | Incorrect. Both grow.
        [ ] Nothing grows | Incorrect. They grow.

    .. multichoice::

        What does panes.insert(0, widget) do?

        [ ] Adds the widget at the end | Incorrect. 0 is the start.
        [x] Puts the widget in a new first pane | Correct. insert uses a position.
        [ ] Deletes pane 0 | Incorrect. forget does that.
        [ ] Changes pane 0 | Incorrect. It adds a pane.

    .. multichoice::

        What does panes.forget(widget) do?

        [x] Takes the widget out of the PanedWindow | Correct. The widget is not destroyed.
        [ ] Deletes it forever | Incorrect. destroy does that.
        [ ] Hides the sash | Incorrect. It removes a pane.
        [ ] Forgets the size | Incorrect. It removes a pane.

    .. multichoice::

        What does panes.panes() give?

        [ ] The number of panes | Incorrect. It gives a list.
        [x] A list of the panes' widgets | Correct. One for each pane.
        [ ] The sash positions | Incorrect. sashpos does that.
        [ ] The window | Incorrect. It lists panes.

    .. multichoice::

        What does panes.sashpos(0) give?

        [x] The position of the first sash in pixels | Correct. It tells you where the sash is.
        [ ] The number of sashes | Incorrect. It gives a position.
        [ ] The first pane | Incorrect. It gives a position.
        [ ] An error | Incorrect. It is a real method.

    .. multichoice::

        What does panes.sashpos(0, 200) do?

        [ ] Makes 200 sashes | Incorrect. It moves a sash.
        [x] Moves the first sash to 200 pixels | Correct. It sets the position.
        [ ] Makes the first pane 200 high | Incorrect. It moves the sash.
        [ ] Deletes the sash | Incorrect. It moves it.

    .. multichoice::

        What should the parent of each pane's widget be?

        [ ] root | Incorrect. Use the PanedWindow.
        [x] The PanedWindow | Correct. e.g. ttk.Frame(panes).
        [ ] Another pane | Incorrect. Not needed.
        [ ] Nothing | Incorrect. It needs a parent.

    .. multichoice::

        How many widgets go in each pane?

        [x] One, but it can be a Frame holding many widgets | Correct. Use frames for more.
        [ ] As many as you like | Incorrect. One per pane.
        [ ] Two | Incorrect. One per pane.
        [ ] None | Incorrect. One per pane.

    .. multichoice::

        How do you make the PanedWindow fill the window?

        [ ] panes.add(fill="both") | Incorrect. add is for panes.
        [x] panes.pack(fill="both", expand=True) | Correct. It stretches both ways.
        [ ] panes.config(fill="both") | Incorrect. fill is a pack option.
        [ ] panes.grow() | Incorrect. Not a method.

    .. multichoice::

        Which style name is used for every ttk PanedWindow?

        [ ] "PanedWindow" | Incorrect. Use TPanedwindow.
        [x] "TPanedwindow" | Correct. T then the widget name with a small w.
        [ ] "TPane" | Incorrect. Not the name.
        [ ] "Sash" | Incorrect. Not the name.

    .. multichoice::

        Can a PanedWindow be put inside another one?

        [x] Yes, to have side-by-side and stacked panes | Correct. Nest them.
        [ ] No | Incorrect. It can.
        [ ] Only vertical | Incorrect. Any can.
        [ ] Only with grid | Incorrect. Use add.

    .. multichoice::

        Which tk PanedWindow options are missing from ttk?

        [ ] orient | Incorrect. ttk has orient.
        [x] sashwidth and showhandle | Correct. ttk sets the sash look with the theme.
        [ ] width | Incorrect. ttk has width.
        [ ] add | Incorrect. add is a method, not an option.

    .. multichoice::

        What happens when the user drags the sash?

        [x] The panes on each side change size | Correct. That is the point of it.
        [ ] The window moves | Incorrect. The panes resize.
        [ ] A tab opens | Incorrect. That is a Notebook.
        [ ] The panes swap | Incorrect. They resize.

    .. multichoice::

        Which method adds a pane at the end?

        [ ] insert | Incorrect. insert needs a position.
        [x] add | Correct. add puts it at the end.
        [ ] append | Incorrect. Not a method.
        [ ] pack | Incorrect. Not for panes.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a side-by-side PanedWindow.

        panes = ttk.@@PanedWindow | Notebook | Frame@@(root, @@orient | side | direction@@="horizontal")
        panes.pack(fill="both", @@expand | grow | stretch@@=True)

    .. cloze::
        :instructions: Add two panes that share space.

        left = ttk.Frame(@@panes | root | left@@, width=150)
        panes.@@add | pack | insert@@(left, @@weight | width | size@@=1)
        panes.add(right, weight=3)

    .. cloze::
        :instructions: Put a pane at the start and remove one.

        panes.@@insert | add | put@@(0, top_bar)
        panes.@@forget | delete | remove@@(right)

    .. cloze::
        :instructions: Read and move a sash.

        position = panes.@@sashpos | sash | position@@(0)
        panes.sashpos(@@0 | 200 | first@@, 200)

    .. cloze::
        :instructions: List the panes.

        all_panes = panes.@@panes | children | tabs@@()
        print(@@len | count | size@@(all_panes))

----

.. admonition:: Tasks

    #. Make a window titled "Panes" that is 300x200 with a ttk PanedWindow that fills the window and has two labels side by side: "Left" on yellow and "Right" on orange.
    #. Change it so the panes are top and bottom.
    #. Make a side-by-side PanedWindow with a Listbox of three animals (weight 0) and a Text box (weight 1).
    #. Add a button that removes the Listbox pane when clicked.

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
                    root.title("Panes")

                    panes = ttk.PanedWindow(root, orient="horizontal")
                    panes.pack(fill="both", expand=True)

                    panes.add(tk.Label(panes, text="Left", bg="yellow"), weight=1)
                    panes.add(tk.Label(panes, text="Right", bg="orange"), weight=1)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Panes")

                    panes = ttk.PanedWindow(root, orient="vertical")
                    panes.pack(fill="both", expand=True)

                    panes.add(tk.Label(panes, text="Top", bg="yellow"), weight=1)
                    panes.add(tk.Label(panes, text="Bottom", bg="orange"), weight=1)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("400x200")
                    root.title("Animals")

                    panes = ttk.PanedWindow(root, orient="horizontal")
                    panes.pack(fill="both", expand=True)

                    animal_list = tk.Listbox(panes, width=15)
                    for animal in ["Koala", "Wombat", "Platypus"]:
                        animal_list.insert(tk.END, animal)
                    panes.add(animal_list, weight=0)

                    notes_box = tk.Text(panes)
                    panes.add(notes_box, weight=1)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def remove_list():
                        try:
                            panes.forget(animal_list)
                        except tk.TclError:
                            pass            # Already removed


                    root = tk.Tk()
                    root.geometry("400x230")
                    root.title("Animals")

                    panes = ttk.PanedWindow(root, orient="horizontal")
                    panes.pack(fill="both", expand=True)

                    animal_list = tk.Listbox(panes, width=15)
                    for animal in ["Koala", "Wombat", "Platypus"]:
                        animal_list.insert(tk.END, animal)
                    panes.add(animal_list, weight=0)

                    notes_box = tk.Text(panes)
                    panes.add(notes_box, weight=1)

                    ttk.Button(root, text="Remove list", command=remove_list).pack(pady=5)

                    root.mainloop()
