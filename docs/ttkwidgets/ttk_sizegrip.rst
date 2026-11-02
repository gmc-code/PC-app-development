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

All Sizegrip options
---------------------------

| Here is every option a ttk Sizegrip can have, for reference. You will only need a few of them most of the time.

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
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TSizegrip"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``

| ttk Sizegrip has no ``bg``, ``fg`` or ``font`` options. Change its colours and fonts with a style, e.g. ``style.configure("TSizegrip", background="lightblue")``.

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

        What is a Sizegrip?

        [x] The small dotted corner the user drags to resize the window | Correct. It sits in the bottom right.
        [ ] A scrollbar | Incorrect. It resizes, not scrolls.
        [ ] A button | Incorrect. It is dragged.
        [ ] A frame | Incorrect. It is a grip.

    .. multichoice::

        Where is a Sizegrip usually placed?

        [ ] Top left | Incorrect. It goes bottom right.
        [x] The bottom right corner of the window | Correct. That is where users expect it.
        [ ] The middle | Incorrect. Not usually.
        [ ] On a button | Incorrect. Not on a button.

    .. multichoice::

        Which pack line puts a Sizegrip in the bottom right?

        [x] grip.pack(side="bottom", anchor="se") | Correct. se is south-east, the bottom right.
        [ ] grip.pack(side="top") | Incorrect. That puts it at the top.
        [ ] grip.pack(anchor="nw") | Incorrect. nw is top left.
        [ ] grip.pack(fill="x") | Incorrect. That stretches it.

    .. multichoice::

        What does anchor="se" mean?

        [ ] South-west, bottom left | Incorrect. sw is bottom left.
        [x] South-east, bottom right | Correct. s is bottom, e is right.
        [ ] North-east, top right | Incorrect. ne is top right.
        [ ] Centre | Incorrect. se is a corner.

    .. multichoice::

        With grid, how is a Sizegrip put in the corner?

        [x] Put it in the last row and column with sticky="se" | Correct. It sticks to the bottom right of its cell.
        [ ] sticky="nw" | Incorrect. That is top left.
        [ ] row=0, column=0 | Incorrect. That is the top left cell.
        [ ] columnspan=10 | Incorrect. Not needed.

    .. multichoice::

        What does cursor="sizing" do?

        [ ] Makes the window bigger | Incorrect. It changes the pointer.
        [x] Shows a resize pointer when the mouse is over the grip | Correct. It hints that it can be dragged.
        [ ] Hides the grip | Incorrect. It changes the pointer.
        [ ] Locks the window | Incorrect. Not related.

    .. multichoice::

        What does a Sizegrip do if the window cannot be resized?

        [x] It does nothing useful, so it is usually left out | Correct. The window size is locked.
        [ ] It still resizes the window | Incorrect. resizable stops it.
        [ ] It causes an error | Incorrect. No error.
        [ ] It unlocks the window | Incorrect. It cannot.

    .. multichoice::

        Which line stops the user resizing the window?

        [ ] root.sizegrip(False) | Incorrect. Not a method.
        [x] root.resizable(False, False) | Correct. Width and height are locked.
        [ ] grip.state(["disabled"]) | Incorrect. That only changes the grip.
        [ ] root.geometry("fixed") | Incorrect. Not valid.

    .. multichoice::

        What is a status bar?

        [ ] A progress bar | Incorrect. It shows messages.
        [x] A strip along the bottom of the window showing messages | Correct. A Sizegrip often sits at its right end.
        [ ] A menu | Incorrect. It shows messages.
        [ ] A title bar | Incorrect. It is at the bottom.

    .. multichoice::

        How is a Sizegrip added to a status bar frame?

        [x] ttk.Sizegrip(status_bar).pack(side="right") | Correct. The status bar is the parent.
        [ ] status_bar.add(Sizegrip) | Incorrect. Not a method.
        [ ] ttk.Sizegrip(root, status_bar) | Incorrect. The parent goes first.
        [ ] status_bar.sizegrip() | Incorrect. Not a method.

    .. multichoice::

        Which pack line puts a status bar along the bottom?

        [ ] status_bar.pack(side="top") | Incorrect. That is the top.
        [x] status_bar.pack(side="bottom", fill="x") | Correct. It stretches across the bottom.
        [ ] status_bar.pack(fill="y") | Incorrect. That stretches up and down.
        [ ] status_bar.pack(anchor="n") | Incorrect. That is the top.

    .. multichoice::

        Which import is needed?

        [x] from tkinter import ttk | Correct. Sizegrip is a ttk widget.
        [ ] import sizegrip | Incorrect. Not a module.
        [ ] from tkinter import Sizegrip | Incorrect. It is in ttk.
        [ ] Nothing | Incorrect. ttk must be imported.

    .. multichoice::

        How many options does a Sizegrip have?

        [ ] Many | Incorrect. It has very few.
        [x] Very few: mainly cursor, style and takefocus | Correct. It has one job.
        [ ] None | Incorrect. It has some.
        [ ] The same as a Button | Incorrect. Far fewer.

    .. multichoice::

        Can a Sizegrip be clicked to run a function?

        [ ] Yes, with command | Incorrect. It has no command.
        [x] No, it is only dragged to resize | Correct. It has no command option.
        [ ] Only when enabled | Incorrect. Still no.
        [ ] Only on Windows | Incorrect. Still no.

    .. multichoice::

        Which style name is used for a Sizegrip?

        [x] "TSizegrip" | Correct. T then the widget name.
        [ ] "Sizegrip" | Incorrect. Needs the T.
        [ ] "TGrip" | Incorrect. Not the name.
        [ ] "Grip" | Incorrect. Not the name.

    .. multichoice::

        Why does the order of packing matter for a bottom status bar?

        [ ] It does not matter | Incorrect. It matters.
        [x] Pack the status bar before the big widgets so it keeps its place at the bottom | Correct. Earlier packed widgets claim space first.
        [ ] The Sizegrip must be packed first in root | Incorrect. It goes in the status bar.
        [ ] Only grid can do it | Incorrect. pack can.

    .. multichoice::

        What does root.geometry("400x300") do?

        [x] Sets the starting size of the window | Correct. The user can still resize it with the grip.
        [ ] Locks the size | Incorrect. resizable does that.
        [ ] Adds a Sizegrip | Incorrect. It sets size.
        [ ] Moves the grip | Incorrect. It sets window size.

    .. multichoice::

        What does root.minsize(300, 200) do?

        [ ] Sets the starting size | Incorrect. geometry does that.
        [x] Stops the window being dragged smaller than 300 by 200 | Correct. It sets the smallest size.
        [ ] Removes the Sizegrip | Incorrect. Not related.
        [ ] Hides the window | Incorrect. Not related.

    .. multichoice::

        In grid, why give the main widget weight=1 with columnconfigure and rowconfigure?

        [x] So it grows when the window is resized with the grip | Correct. Weight shares extra space.
        [ ] So it is heavier | Incorrect. It shares space.
        [ ] So the Sizegrip moves | Incorrect. The main widget grows.
        [ ] It is not needed | Incorrect. Without weight, nothing grows.

    .. multichoice::

        Is a Sizegrip needed to resize a window?

        [ ] Yes, always | Incorrect. Windows can be resized by their edges.
        [x] No, it just makes resizing easier to find | Correct. Window edges also resize.
        [ ] Only on Windows | Incorrect. It is optional.
        [ ] Only with grid | Incorrect. It is optional.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Add a Sizegrip in the bottom right corner.

        grip = ttk.@@Sizegrip | Scrollbar | Separator@@(root)
        grip.pack(side="@@bottom | top | left@@", anchor="@@se | nw | ne@@")

    .. cloze::
        :instructions: Make a status bar with a Sizegrip.

        status_bar = ttk.Frame(root)
        status_bar.pack(side="@@bottom | top | left@@", fill="@@x | y | both@@")
        ttk.Label(status_bar, text="Ready").pack(side="left")
        ttk.@@Sizegrip | Separator | Label@@(status_bar).pack(side="right")

    .. cloze::
        :instructions: Place a Sizegrip with grid.

        text.grid(row=0, column=0, sticky="nsew")
        grip.grid(row=1, column=1, @@sticky | anchor | side@@="se")
        root.@@columnconfigure | rowconfigure | config@@(0, weight=1)

    .. cloze::
        :instructions: Show a resize pointer.

        grip = ttk.Sizegrip(root, @@cursor | pointer | mouse@@="sizing")

    .. cloze::
        :instructions: Stop the window being resized.

        root.@@resizable | sizegrip | geometry@@(False, @@False | True | 0@@)

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
