====================================================
ttk Scrollbar
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk Scrollbar?
---------------------------

| A **ttk Scrollbar** lets the user scroll through content that does not fit, just like a tk Scrollbar.
| It is linked to another widget, such as a **Listbox**, **Text**, **Canvas** or **ttk Treeview**.
| A ttk Scrollbar matches the theme. Unlike a tk Scrollbar, its colours **can** be changed on Windows using a style with the ``"clam"`` theme.

----

Making a ttk Scrollbar
-------------------------

| The link goes both ways:

#. **Create** the scrollbar and pack it down the right with ``side="right", fill="y"``.
#. **Create** the widget with ``yscrollcommand=scrollbar.set`` so it tells the scrollbar when it moves.
#. **Link** back with ``scrollbar.config(command=widget.yview)`` so dragging the scrollbar moves the widget.

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk Scrollbar")

    scrollbar = ttk.Scrollbar(root, orient="vertical")              # 1. Create it
    scrollbar.pack(side="right", fill="y")

    item_list = tk.Listbox(root, yscrollcommand=scrollbar.set)      # 2. Widget -> scrollbar
    item_list.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=item_list.yview)                       # 3. Scrollbar -> widget

    for number in range(1, 101):
        item_list.insert(tk.END, f"Item {number}")

    root.mainloop()                 # Keep the window open

----

ttk Scrollbar options
------------------------

orient
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses up-and-down (``"vertical"``, the default) or side-to-side (``"horizontal"``).
| A horizontal scrollbar uses ``xscrollcommand`` and ``xview`` instead of ``yscrollcommand`` and ``yview``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("orient")

    across = ttk.Scrollbar(root, orient="horizontal")
    across.pack(side="bottom", fill="x")

    long_text = tk.Text(root, wrap="none", xscrollcommand=across.set)
    long_text.pack(fill="both", expand=True)
    across.config(command=long_text.xview)

    long_text.insert("1.0", "This line is much too long to fit, so you need to scroll sideways "
                            "to read all of it. Keep going... nearly there... the end!")

    root.mainloop()

command
~~~~~~~~~~~~~~~~~~

| **What it does:** tells the scrollbar which widget to move. Use the widget's ``yview`` (or ``xview``) **without** brackets.
| **How to write it:** ``command=text_box.yview``, or ``scrollbar.config(command=text_box.yview)`` after the widget is made.

----

Using ttk Scrollbars
-----------------------

With a Text widget
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Text")

    scrollbar = ttk.Scrollbar(root)
    scrollbar.pack(side="right", fill="y")

    story_box = tk.Text(root, wrap="word", yscrollcommand=scrollbar.set)
    story_box.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=story_box.yview)

    for number in range(1, 31):
        story_box.insert(tk.END, f"This is line {number} of the story.\n")

    root.mainloop()

With grid
~~~~~~~~~~~~~~~~~~

| With ``grid``, put the scrollbar in the next column and use ``sticky="ns"`` to stretch it from top (north) to bottom (south).

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("grid")

    ttk.Label(root, text="Countries").grid(row=0, column=0)

    country_list = tk.Listbox(root, height=6)
    country_list.grid(row=1, column=0)

    scrollbar = ttk.Scrollbar(root, command=country_list.yview)
    scrollbar.grid(row=1, column=1, sticky="ns")
    country_list.config(yscrollcommand=scrollbar.set)

    for country in ["Australia", "Brazil", "Canada", "Denmark", "Egypt", "France",
                    "Germany", "India", "Japan", "Kenya"]:
        country_list.insert(tk.END, country)

    root.mainloop()

| Here the scrollbar is made **after** the listbox, so ``command`` can go straight in ``ttk.Scrollbar(...)``, and ``yscrollcommand`` is added with ``config``.

Two scrollbars
~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Two scrollbars")

    down_bar = ttk.Scrollbar(root, orient="vertical")
    down_bar.pack(side="right", fill="y")
    across_bar = ttk.Scrollbar(root, orient="horizontal")
    across_bar.pack(side="bottom", fill="x")

    grid_box = tk.Text(root, wrap="none", yscrollcommand=down_bar.set,
                       xscrollcommand=across_bar.set)
    grid_box.pack(side="left", fill="both", expand=True)

    down_bar.config(command=grid_box.yview)
    across_bar.config(command=grid_box.xview)

    for row in range(1, 41):
        grid_box.insert(tk.END, f"Row {row}: " + "o " * 60 + "\n")

    root.mainloop()

With a Canvas
~~~~~~~~~~~~~~~~

| A Canvas also needs ``scrollregion``: the size of the **whole** drawing, including the part you cannot see.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Canvas")

    scrollbar = ttk.Scrollbar(root)
    scrollbar.pack(side="right", fill="y")

    canvas = tk.Canvas(root, bg="white", scrollregion=(0, 0, 300, 1000),
                       yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=canvas.yview)

    for y in range(0, 1000, 100):
        canvas.create_text(120, y + 50, text=f"{y} pixels down", font=("Arial", 14))

    root.mainloop()

----

ttk Scrollbar methods
------------------------

get
~~~~~~~~~~~~~~~~~~

| **What it does:** tells you where the handle is, as two decimals from 0 to 1 (the top and bottom of what you can see).
| **How to write it:** ``top, bottom = scrollbar.get()``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def how_far():
        top, bottom = scrollbar.get()
        result_label.config(text=f"You have scrolled {round(bottom * 100)}% of the way")


    root = tk.Tk()
    root.geometry("300x250")
    root.title("get")

    box = ttk.Frame(root)
    box.pack(pady=5)

    scrollbar = ttk.Scrollbar(box)
    scrollbar.pack(side="right", fill="y")

    item_list = tk.Listbox(box, height=8, yscrollcommand=scrollbar.set)
    item_list.pack(side="left")
    scrollbar.config(command=item_list.yview)

    for number in range(1, 51):
        item_list.insert(tk.END, f"Item {number}")

    ttk.Button(root, text="How far?", command=how_far).pack()
    result_label = ttk.Label(root, text="")
    result_label.pack()

    root.mainloop()

Scrolling from code
~~~~~~~~~~~~~~~~~~~~~~

| These are methods of the **widget**, but they move the scrollbar too:
| ``widget.yview_moveto(0)`` jumps to the top, ``widget.yview_moveto(1)`` jumps to the bottom.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("yview_moveto")

    box = ttk.Frame(root)
    box.pack(pady=5)

    scrollbar = ttk.Scrollbar(box)
    scrollbar.pack(side="right", fill="y")

    name_list = tk.Listbox(box, height=8, yscrollcommand=scrollbar.set)
    name_list.pack(side="left")
    scrollbar.config(command=name_list.yview)

    for number in range(1, 101):
        name_list.insert(tk.END, f"Student {number}")

    ttk.Button(root, text="Top", command=lambda: name_list.yview_moveto(0)).pack(side="left", padx=50)
    ttk.Button(root, text="Bottom", command=lambda: name_list.yview_moveto(1)).pack(side="left")

    root.mainloop()

----

Styling a ttk Scrollbar
--------------------------

| The style is ``"Vertical.TScrollbar"`` or ``"Horizontal.TScrollbar"``. With the ``"clam"`` theme:

- ``background`` - colour of the handle and arrows
- ``troughcolor`` - colour of the track
- ``arrowcolor`` - colour of the arrow shapes
- ``arrowsize`` - size of the arrows (also makes the scrollbar thicker)

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Scrollbar style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Vertical.TScrollbar", background="orange", troughcolor="lightyellow",
                    arrowcolor="white", arrowsize=20)
    style.map("Vertical.TScrollbar", background=[("active", "darkorange")])

    scrollbar = ttk.Scrollbar(root)
    scrollbar.pack(side="right", fill="y")

    item_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
    item_list.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=item_list.yview)

    for number in range(1, 51):
        item_list.insert(tk.END, f"Item {number}")

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
      - Up and down or side to side
      - ``orient="horizontal"``
    * - ``command``
      - Scrollbar tells the widget to move
      - ``command=box.yview``
    * - ``yscrollcommand``
      - Widget tells the scrollbar it moved
      - ``yscrollcommand=scrollbar.set``
    * - ``xscrollcommand``, ``xview``
      - Linking a horizontal scrollbar
      - ``xscrollcommand=bar.set``
    * - ``pack(side=, fill=)``
      - Put it down the right side
      - ``pack(side="right", fill="y")``
    * - ``grid(sticky="ns")``
      - Stretch it in a grid
      - ``grid(row=1, column=1, sticky="ns")``
    * - ``get()``
      - Where the handle is (0 to 1)
      - ``scrollbar.get()``
    * - ``yview_moveto()``
      - Jump to the top (0) or bottom (1)
      - ``box.yview_moveto(1)``
    * - ``"Vertical.TScrollbar"``
      - Style name
      - ``style.configure("Vertical.TScrollbar", troughcolor="pink")``

----

All Scrollbar options
---------------------------

| Here is every option a ttk Scrollbar can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``class_``
      - A group name used to style many widgets at once (advanced). Written ``class_`` in Python
      - ``class_="Sidebar"``
    * - ``command``
      - Connects it to the widget it scrolls
      - ``command=tree.yview``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``orient``
      - Up and down (``"vertical"``) or side to side (``"horizontal"``)
      - ``orient="vertical"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TScrollbar"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``

| ttk Scrollbar has no ``bg``, ``fg`` or ``font`` options. Change its colours and fonts with a style, e.g. ``style.configure("Vertical.TScrollbar", background="lightblue")``.

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

        What is a ttk Scrollbar for?

        [x] Scrolling a widget whose content does not fit, like Text or Treeview | Correct. It is the themed version.
        [ ] Picking a number | Incorrect. That is a Scale.
        [ ] Showing progress | Incorrect. That is a Progressbar.
        [ ] Drawing | Incorrect. That is a Canvas.

    .. multichoice::

        What is the default orient?

        [x] "vertical" | Correct. Up and down is the default.
        [ ] "horizontal" | Incorrect. That must be set.
        [ ] "both" | Incorrect. Not a value.
        [ ] "none" | Incorrect. Not a value.

    .. multichoice::

        What does command=text.yview do?

        [ ] Deletes the text | Incorrect. It scrolls it.
        [x] Makes moving the Scrollbar scroll the Text up and down | Correct. yview moves the view.
        [ ] Adds text | Incorrect. It scrolls.
        [ ] Changes the colour | Incorrect. It scrolls.

    .. multichoice::

        Two steps connect a Scrollbar. One is command=tree.yview. What is the other?

        [x] tree.config(yscrollcommand=scrollbar.set) | Correct. The widget tells the Scrollbar where it is.
        [ ] tree.config(scroll=True) | Incorrect. Not an option.
        [ ] scrollbar.pack(tree) | Incorrect. Not how it connects.
        [ ] tree.add(scrollbar) | Incorrect. Not a method.

    .. multichoice::

        For a horizontal Scrollbar, which pair is used?

        [ ] yview and yscrollcommand | Incorrect. Those are vertical.
        [x] xview and xscrollcommand | Correct. x is side to side.
        [ ] view and command | Incorrect. Not the names.
        [ ] left and right | Incorrect. Not the names.

    .. multichoice::

        Where is a vertical Scrollbar usually packed?

        [x] side="right", fill="y" | Correct. It stretches up and down on the right.
        [ ] side="top" | Incorrect. It goes beside the widget.
        [ ] side="bottom", fill="x" | Incorrect. That is horizontal.
        [ ] side="left", fill="x" | Incorrect. fill="x" is wrong here.

    .. multichoice::

        With grid, how is a vertical Scrollbar stretched to full height?

        [ ] sticky="ew" | Incorrect. That is side to side.
        [x] sticky="ns" | Correct. North and south.
        [ ] fill="y" | Incorrect. fill is for pack.
        [ ] expand=True | Incorrect. That is for pack.

    .. multichoice::

        With grid, how is a horizontal Scrollbar stretched?

        [x] sticky="ew" | Correct. East and west stretches it across.
        [ ] sticky="ns" | Incorrect. That is up and down.
        [ ] fill="x" | Incorrect. fill is for pack.
        [ ] side="bottom" | Incorrect. side is for pack.

    .. multichoice::

        What must a Canvas have before it can be scrolled?

        [ ] A Text widget | Incorrect. Not needed.
        [x] A scrollregion giving the full size of the drawing | Correct. e.g. scrollregion=(0, 0, 1000, 1000).
        [ ] A Listbox | Incorrect. Not needed.
        [ ] A style | Incorrect. Not needed.

    .. multichoice::

        What does scrollbar.get() give?

        [x] Two numbers from 0 to 1 showing which part is visible | Correct. e.g. (0.0, 0.5) is the top half.
        [ ] The text | Incorrect. It gives positions.
        [ ] The widget | Incorrect. It gives positions.
        [ ] The style | Incorrect. It gives positions.

    .. multichoice::

        What does text.yview_moveto(1) do?

        [ ] Scrolls to the top | Incorrect. 0 is the top.
        [x] Scrolls to the bottom | Correct. 1 is the end.
        [ ] Moves one line | Incorrect. It moves to the end.
        [ ] Deletes the text | Incorrect. It scrolls.

    .. multichoice::

        What does text.yview_scroll(1, "units") do?

        [x] Scrolls down by one line | Correct. units are small steps.
        [ ] Scrolls to the end | Incorrect. yview_moveto(1) does that.
        [ ] Scrolls up | Incorrect. 1 is down; -1 is up.
        [ ] Deletes a line | Incorrect. It scrolls.

    .. multichoice::

        What does text.yview_scroll(-1, "pages") do?

        [ ] Scrolls down one page | Incorrect. -1 goes up.
        [x] Scrolls up one page | Correct. pages are big steps.
        [ ] Deletes a page | Incorrect. It scrolls.
        [ ] Goes to the top | Incorrect. It moves one page.

    .. multichoice::

        Why does a Text widget need wrap="none" for sideways scrolling?

        [x] So long lines stay on one line and can be scrolled across | Correct. Wrapped lines never need it.
        [ ] So it is faster | Incorrect. Not about speed.
        [ ] So the colour shows | Incorrect. Not related.
        [ ] It is not needed | Incorrect. It is needed.

    .. multichoice::

        If the Scrollbar slider does not move when the text is scrolled, what is missing?

        [ ] command | Incorrect. That handles the other direction.
        [x] yscrollcommand=scrollbar.set on the widget | Correct. The widget must tell the Scrollbar.
        [ ] A style | Incorrect. Not needed.
        [ ] A Frame | Incorrect. Not needed.

    .. multichoice::

        Which widgets can use a vertical ttk Scrollbar?

        [x] Text, Listbox, Canvas and Treeview | Correct. They all have yview.
        [ ] Label and Button | Incorrect. They do not scroll.
        [ ] Progressbar | Incorrect. It does not scroll.
        [ ] Separator | Incorrect. It does not scroll.

    .. multichoice::

        Which line makes a horizontal Scrollbar?

        [ ] ttk.Scrollbar(root, side="x") | Incorrect. Not an option.
        [x] ttk.Scrollbar(root, orient="horizontal") | Correct. orient sets direction.
        [ ] ttk.Scrollbar(root, across=True) | Incorrect. Not an option.
        [ ] ttk.Scrollbar(root, width="horizontal") | Incorrect. Not an option.

    .. multichoice::

        Which style name is used for a vertical ttk Scrollbar?

        [ ] "TScrollbar" | Incorrect. It needs the direction.
        [x] "Vertical.TScrollbar" | Correct. The direction is part of the name.
        [ ] "Scroll" | Incorrect. Not the name.
        [ ] "TScroll" | Incorrect. Not the name.

    .. multichoice::

        Can a Scrollbar work without being connected to a widget?

        [ ] Yes | Incorrect. It needs a widget.
        [x] No, it must be connected both ways to a widget | Correct. Use command and the widget's scroll command.
        [ ] Only horizontal ones | Incorrect. Both need a widget.
        [ ] Only with a style | Incorrect. It needs a widget.

    .. multichoice::

        Why use two scrollbars on one Text widget?

        [x] To scroll both up and down and side to side | Correct. One vertical, one horizontal.
        [ ] To scroll faster | Incorrect. Not why.
        [ ] To colour it | Incorrect. Not why.
        [ ] It is not possible | Incorrect. It is.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Connect a ttk Scrollbar to a Text box.

        scrollbar = ttk.@@Scrollbar | Scale | Progressbar@@(root, @@command | scroll | link@@=text.yview)
        text.config(@@yscrollcommand | xscrollcommand | command@@=scrollbar.set)
        scrollbar.pack(side="right", fill="@@y | x | both@@")

    .. cloze::
        :instructions: Use grid with a Treeview.

        tree.grid(row=0, column=0)
        scrollbar.grid(row=0, column=1, @@sticky | fill | side@@="@@ns | ew | nsew@@")

    .. cloze::
        :instructions: Make a horizontal Scrollbar.

        x_scroll = ttk.Scrollbar(root, @@orient | side | direction@@="horizontal", command=text.@@xview | yview | view@@)
        text.config(xscrollcommand=x_scroll.set)

    .. cloze::
        :instructions: Scroll a Canvas.

        canvas.config(@@scrollregion | region | size@@=(0, 0, 1000, 1000))
        canvas.config(yscrollcommand=scrollbar.set)

    .. cloze::
        :instructions: Scroll from code.

        text.@@yview_moveto | yview_scroll | see@@(1)
        text.yview_scroll(1, "@@units | lines | steps@@")

----

.. admonition:: Tasks

    #. Make a window titled "Numbers" that is 300x200 with a Listbox of the numbers 1 to 200 and a ttk Scrollbar linked to it.
    #. Make a Text widget with ``wrap="none"``, a horizontal ttk Scrollbar, and one very long line of text.
    #. Use ``grid`` to put a Listbox of ten fruits in row 0, column 0 and its ttk Scrollbar in row 0, column 1.
    #. Style the scrollbar from Q1 with a green handle and a light green track.

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
                    root.title("Numbers")

                    scrollbar = ttk.Scrollbar(root)
                    scrollbar.pack(side="right", fill="y")

                    number_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
                    number_list.pack(side="left", fill="both", expand=True)
                    scrollbar.config(command=number_list.yview)

                    for number in range(1, 201):
                        number_list.insert(tk.END, number)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Long line")

                    scrollbar = ttk.Scrollbar(root, orient="horizontal")
                    scrollbar.pack(side="bottom", fill="x")

                    long_text = tk.Text(root, wrap="none", xscrollcommand=scrollbar.set)
                    long_text.pack(fill="both", expand=True)
                    scrollbar.config(command=long_text.xview)

                    long_text.insert("1.0", "This is a very very long line of text " * 6)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Fruit")

                    fruit_list = tk.Listbox(root, height=5)
                    fruit_list.grid(row=0, column=0)

                    scrollbar = ttk.Scrollbar(root, command=fruit_list.yview)
                    scrollbar.grid(row=0, column=1, sticky="ns")
                    fruit_list.config(yscrollcommand=scrollbar.set)

                    for fruit in ["Apple", "Banana", "Cherry", "Grape", "Kiwi",
                                  "Lemon", "Mango", "Orange", "Peach", "Pear"]:
                        fruit_list.insert(tk.END, fruit)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Numbers")

                    style = ttk.Style()
                    style.theme_use("clam")
                    style.configure("Vertical.TScrollbar", background="green", troughcolor="lightgreen")

                    scrollbar = ttk.Scrollbar(root)
                    scrollbar.pack(side="right", fill="y")

                    number_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
                    number_list.pack(side="left", fill="both", expand=True)
                    scrollbar.config(command=number_list.yview)

                    for number in range(1, 201):
                        number_list.insert(tk.END, number)

                    root.mainloop()
