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

All Separator options
---------------------------

| Here is every option a ttk Separator can have, for reference. You will only need a few of them most of the time.

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
    * - ``orient``
      - A line across (``"horizontal"``) or a line up and down (``"vertical"``)
      - ``orient="vertical"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TSeparator"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``

| ttk Separator has no ``bg``, ``fg`` or ``font`` options. Change its colours and fonts with a style, e.g. ``style.configure("TSeparator", background="red")``.

----

Quiz
--------------------------------

.. mcqgroup::
    :nav_position: top
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 20

    .. multichoice::

        What is a Separator?

        [x] A thin line used to split parts of a window | Correct. It helps organise the layout.
        [ ] A button | Incorrect. It cannot be clicked.
        [ ] A box for typing | Incorrect. That is an Entry.
        [ ] A scrollbar | Incorrect. It does not scroll.

    .. multichoice::

        What does orient="horizontal" make?

        [x] A line going across | Correct. horizontal goes left to right.
        [ ] A line going up and down | Incorrect. That is vertical.
        [ ] A box | Incorrect. It is a line.
        [ ] Nothing | Incorrect. It makes a line.

    .. multichoice::

        What does orient="vertical" make?

        [ ] A line going across | Incorrect. That is horizontal.
        [x] A line going up and down | Correct. vertical goes up and down.
        [ ] Two lines | Incorrect. One line.
        [ ] A dotted line | Incorrect. It is a plain line.

    .. multichoice::

        What is the default orient?

        [x] "horizontal" | Correct. A line across is the default.
        [ ] "vertical" | Incorrect. That must be set.
        [ ] "both" | Incorrect. Not a value.
        [ ] "none" | Incorrect. Not a value.

    .. multichoice::

        Why might a horizontal Separator not be seen with plain pack()?

        [ ] It is hidden by default | Incorrect. It is shown.
        [x] It has no length of its own, so it needs fill="x" to stretch across | Correct. Without fill it is very short.
        [ ] It needs a colour | Incorrect. Not the reason.
        [ ] It needs text | Incorrect. It has no text.

    .. multichoice::

        Which pack line shows a horizontal Separator across the window?

        [ ] sep.pack() | Incorrect. It may be too short to see.
        [x] sep.pack(fill="x", pady=10) | Correct. fill stretches it across.
        [ ] sep.pack(fill="y") | Incorrect. That is for vertical lines.
        [ ] sep.pack(side="left") | Incorrect. That is for vertical lines.

    .. multichoice::

        Which pack line suits a vertical Separator between two side-by-side parts?

        [x] sep.pack(side="left", fill="y", padx=10) | Correct. It stands up between them.
        [ ] sep.pack(fill="x") | Incorrect. That is for horizontal lines.
        [ ] sep.pack() | Incorrect. It may be too short.
        [ ] sep.pack(side="top") | Incorrect. That stacks it.

    .. multichoice::

        With grid, how does a horizontal Separator stretch across columns?

        [ ] sticky="ns" | Incorrect. That is up and down.
        [x] columnspan for the width and sticky="ew" | Correct. It covers the columns and stretches across.
        [ ] rowspan only | Incorrect. That is for rows.
        [ ] fill="x" | Incorrect. fill is for pack.

    .. multichoice::

        With grid, how does a vertical Separator stretch?

        [x] rowspan for the height and sticky="ns" | Correct. It covers the rows and stretches up and down.
        [ ] sticky="ew" | Incorrect. That is across.
        [ ] columnspan only | Incorrect. That is for columns.
        [ ] fill="y" | Incorrect. fill is for pack.

    .. multichoice::

        What does pady=10 add around a horizontal Separator?

        [ ] 10 lines | Incorrect. It adds space.
        [x] 10 pixels of space above and below it | Correct. It gives the line room.
        [ ] Thickness | Incorrect. It adds space.
        [ ] A colour | Incorrect. It adds space.

    .. multichoice::

        In a form, where is a Separator useful?

        [x] Between the questions and the buttons | Correct. It splits the sections.
        [ ] Inside an Entry | Incorrect. It cannot go inside an Entry.
        [ ] On a Button | Incorrect. Not on a Button.
        [ ] Inside a Menu | Incorrect. Menus use add_separator.

    .. multichoice::

        Which method adds a line inside a Menu instead?

        [ ] ttk.Separator | Incorrect. That is for windows and frames.
        [x] add_separator() | Correct. Menus have their own separator.
        [ ] add_line() | Incorrect. Not a method.
        [ ] menu.separator | Incorrect. Not a method.

    .. multichoice::

        Can a Separator be clicked?

        [ ] Yes | Incorrect. It only draws a line.
        [x] No, it is only for layout | Correct. It does nothing when clicked.
        [ ] Only when vertical | Incorrect. Still no.
        [ ] Only with command | Incorrect. It has no command.

    .. multichoice::

        How do you change a Separator's colour?

        [ ] sep.config(bg="red") | Incorrect. ttk has no bg.
        [x] style.configure("TSeparator", background="red") | Correct. Use a style.
        [ ] sep.colour("red") | Incorrect. Not a method.
        [ ] sep.config(fill="red") | Incorrect. Not an option.

    .. multichoice::

        Which style name is used for every Separator?

        [x] "TSeparator" | Correct. T then the widget name.
        [ ] "Separator" | Incorrect. Needs the T.
        [ ] "TLine" | Incorrect. Not the name.
        [ ] "Line" | Incorrect. Not the name.

    .. multichoice::

        How many options does ttk.Separator have that change its look directly?

        [ ] Many | Incorrect. It has very few.
        [x] Only orient and style really | Correct. Most of its look comes from the style.
        [ ] None at all | Incorrect. orient changes it.
        [ ] width and height | Incorrect. It has no width option.

    .. multichoice::

        Which import is needed for Separator?

        [x] from tkinter import ttk | Correct. Separator is a ttk widget.
        [ ] import separator | Incorrect. Not a module.
        [ ] from tkinter import Separator | Incorrect. It is in ttk.
        [ ] Nothing | Incorrect. ttk must be imported.

    .. multichoice::

        For side-by-side sections, what does the Separator go between?

        [ ] Two Labels in one row | Incorrect. It goes between sections.
        [x] Two frames packed with side="left" | Correct. A vertical line sits between them.
        [ ] Two windows | Incorrect. It goes inside a window.
        [ ] Two menus | Incorrect. Menus use add_separator.

    .. multichoice::

        What happens if fill="y" is used on a horizontal Separator?

        [x] It will not stretch across, so it may not be seen | Correct. Use fill="x" for horizontal.
        [ ] It becomes vertical | Incorrect. orient sets that.
        [ ] It turns red | Incorrect. No colour change.
        [ ] An error happens | Incorrect. No error.

    .. multichoice::

        What is the parent of a Separator inside a frame called form?

        [ ] root | Incorrect. Use the frame.
        [x] form | Correct. e.g. ttk.Separator(form, orient="horizontal").
        [ ] The Separator | Incorrect. It needs a parent.
        [ ] Nothing | Incorrect. It needs a parent.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a horizontal Separator.

        line = ttk.@@Separator | Scrollbar | Frame@@(root, @@orient | side | direction@@="horizontal")
        line.pack(@@fill | side | anchor@@="x", pady=10)

    .. cloze::
        :instructions: Make a vertical Separator between two frames.

        left_frame.pack(side="left")
        divider = ttk.Separator(root, orient="@@vertical | horizontal | up@@")
        divider.pack(side="left", fill="@@y | x | both@@", padx=10)
        right_frame.pack(side="left")

    .. cloze::
        :instructions: Use grid for a Separator in a form.

        sep = ttk.Separator(form, orient="horizontal")
        sep.grid(row=3, column=0, @@columnspan | rowspan | span@@=2, sticky="@@ew | ns | nsew@@", pady=5)

    .. cloze::
        :instructions: Use grid for a vertical Separator.

        divider.grid(row=0, column=1, @@rowspan | columnspan | span@@=4, sticky="@@ns | ew | x@@")

    .. cloze::
        :instructions: Colour every Separator.

        style = ttk.@@Style | style | Theme@@()
        style.configure("@@TSeparator | Separator | TLine@@", background="red")

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
