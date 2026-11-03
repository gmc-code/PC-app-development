====================================================
tk Scrollbar
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Scrollbar>`_

----

What is a Scrollbar?
-----------------------

| A **Scrollbar** is the bar down the side (or along the bottom) of a box that lets the user move through content that does not fit.
| A scrollbar is always used **with** another widget, such as a **Listbox**, **Text** or **Canvas**.

----

Making a Scrollbar
---------------------

| A scrollbar must be **linked** to the widget it scrolls. The link goes both ways:

- The **widget** tells the scrollbar when its content moves, so the scrollbar's handle moves too.
- The **scrollbar** tells the widget to move when the user drags the handle.

#. **Create** the scrollbar and **pack** it on the right with ``side="right", fill="y"``.
#. **Create** the widget with ``yscrollcommand=scrollbar.set`` and pack it on the left.
#. **Link** the scrollbar back with ``scrollbar.config(command=widget.yview)``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first scrollbar")

    scrollbar = tk.Scrollbar(root)                      # 1. Create the scrollbar
    scrollbar.pack(side="right", fill="y")              #    down the right side

    number_list = tk.Listbox(root, yscrollcommand=scrollbar.set)    # 2. Widget -> scrollbar
    number_list.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=number_list.yview)         # 3. Scrollbar -> widget

    for number in range(1, 101):
        number_list.insert(tk.END, f"Item {number}")

    root.mainloop()                 # Keep the window open

| ``yview`` means "the up-and-down view". ``fill="y"`` stretches the scrollbar the full height.

----

Scrollbar options
--------------------

| Options are written as ``option=value`` inside ``tk.Scrollbar( )``, separated by commas.

orient
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses whether the scrollbar goes up-and-down or side-to-side.
| **How to write it:** ``orient="horizontal"``
| **Values:** ``"vertical"`` (the default) and ``"horizontal"``.
| A horizontal scrollbar uses ``xscrollcommand`` and ``xview`` instead of ``yscrollcommand`` and ``yview``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("orient")

    scrollbar = tk.Scrollbar(root, orient="horizontal")
    scrollbar.pack(side="bottom", fill="x")             # Along the bottom, full width

    long_text = tk.Text(root, wrap="none", xscrollcommand=scrollbar.set)
    long_text.pack(fill="both", expand=True)

    scrollbar.config(command=long_text.xview)

    long_text.insert("1.0", "This line is much too long to fit in the window, "
                            "so you need to scroll sideways to read all of it.")

    root.mainloop()

| ``wrap="none"`` stops the Text widget wrapping lines, so they run off the side and need scrolling.

width
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how thick the scrollbar is, in pixels.
| **How to write it:** ``width=25``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width")

    scrollbar = tk.Scrollbar(root, width=30)
    scrollbar.pack(side="right", fill="y")

    word_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
    word_list.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=word_list.yview)

    for number in range(1, 51):
        word_list.insert(tk.END, f"Word {number}")

    root.mainloop()

Colours
~~~~~~~~~~~~~~~~~~

| ``bg``, ``troughcolor`` and ``activebackground`` change the colours of the scrollbar.
| **Note:** on Windows, the scrollbar uses the normal Windows look and these colours are ignored. They work on Linux and some other computers.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("colours")

    scrollbar = tk.Scrollbar(root, bg="orange", troughcolor="lightyellow",
                             activebackground="red")
    scrollbar.pack(side="right", fill="y")

    item_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
    item_list.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=item_list.yview)

    for number in range(1, 51):
        item_list.insert(tk.END, f"Item {number}")

    root.mainloop()

----

Using scrollbars with other widgets
---------------------------------------

With a Text widget
~~~~~~~~~~~~~~~~~~~~~

| The same three steps work for a **Text** widget.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Text with a scrollbar")

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side="right", fill="y")

    story_box = tk.Text(root, wrap="word", yscrollcommand=scrollbar.set)
    story_box.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=story_box.yview)

    for number in range(1, 31):
        story_box.insert(tk.END, f"This is line {number} of the story.\n")

    root.mainloop()

Inside a Frame
~~~~~~~~~~~~~~~~~

| Put the widget and its scrollbar in a **Frame** to keep them together. Then other widgets can go above or below without getting mixed up.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("In a frame")

    tk.Label(root, text="Countries", font=("Arial", 14)).pack()

    list_frame = tk.Frame(root)
    list_frame.pack(pady=5)

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side="right", fill="y")

    country_list = tk.Listbox(list_frame, height=6, yscrollcommand=scrollbar.set)
    country_list.pack(side="left")
    scrollbar.config(command=country_list.yview)

    for country in ["Australia", "Brazil", "Canada", "Denmark", "Egypt", "France",
                    "Germany", "India", "Japan", "Kenya", "Mexico", "Norway"]:
        country_list.insert(tk.END, country)

    tk.Button(root, text="Choose").pack()

    root.mainloop()

Two scrollbars
~~~~~~~~~~~~~~~~~

| A widget can have both an up-and-down **and** a side-to-side scrollbar. Pack the scrollbars **before** the widget.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Two scrollbars")

    down_bar = tk.Scrollbar(root, orient="vertical")
    down_bar.pack(side="right", fill="y")

    across_bar = tk.Scrollbar(root, orient="horizontal")
    across_bar.pack(side="bottom", fill="x")

    grid_box = tk.Text(root, wrap="none",
                       yscrollcommand=down_bar.set, xscrollcommand=across_bar.set)
    grid_box.pack(side="left", fill="both", expand=True)

    down_bar.config(command=grid_box.yview)
    across_bar.config(command=grid_box.xview)

    for row in range(1, 41):
        grid_box.insert(tk.END, f"Row {row}: " + "x " * 60 + "\n")

    root.mainloop()

With a Canvas
~~~~~~~~~~~~~~~~

| A Canvas needs one extra option: ``scrollregion``. It tells the canvas how big the **whole** drawing is, including the part you cannot see.
| **How to write it:** ``scrollregion=(0, 0, width, height)``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Canvas with a scrollbar")

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side="right", fill="y")

    canvas = tk.Canvas(root, bg="white", scrollregion=(0, 0, 300, 1000),
                       yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=canvas.yview)

    for y in range(0, 1000, 100):
        canvas.create_text(100, y + 50, text=f"{y} pixels down", font=("Arial", 14))

    root.mainloop()

----

Scrollbar methods
--------------------

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options **after** the scrollbar has been made. It is mostly used to link the scrollbar to its widget.
| **How to write it:** ``scrollbar.config(command=widget.yview)``

| See the examples above: every one uses ``config`` as step 3.

Scrolling from code
~~~~~~~~~~~~~~~~~~~~~~

| These are methods of the **widget** (not the scrollbar), but they make the scrollbar move:

- ``widget.yview_moveto(0)`` jumps to the **top**. ``widget.yview_moveto(1)`` jumps to the **bottom**.
- ``widget.see(index)`` scrolls so an item can be seen (Listbox and Text).

.. code-block:: python

    import tkinter as tk


    def go_top():
        name_list.yview_moveto(0)


    def go_bottom():
        name_list.yview_moveto(1)


    root = tk.Tk()
    root.geometry("300x250")
    root.title("yview_moveto")

    list_frame = tk.Frame(root)
    list_frame.pack(pady=5)

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side="right", fill="y")

    name_list = tk.Listbox(list_frame, height=8, yscrollcommand=scrollbar.set)
    name_list.pack(side="left")
    scrollbar.config(command=name_list.yview)

    for number in range(1, 101):
        name_list.insert(tk.END, f"Student {number}")

    tk.Button(root, text="Top", command=go_top).pack(side="left", padx=60)
    tk.Button(root, text="Bottom", command=go_bottom).pack(side="left")

    root.mainloop()

get
~~~~~~~~~~~~~~~~~~

| **What it does:** tells you where the handle is, as two decimals between 0 and 1.
| The first number is the top of what you can see, and the second is the bottom. ``(0.0, 0.1)`` means you can see the first tenth of the list.
| **How to write it:** ``top, bottom = scrollbar.get()``

.. code-block:: python

    import tkinter as tk


    def where():
        top, bottom = scrollbar.get()
        result_label.config(text=f"You have scrolled {round(bottom * 100)}% of the way")


    root = tk.Tk()
    root.geometry("300x250")
    root.title("get")

    list_frame = tk.Frame(root)
    list_frame.pack(pady=5)

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side="right", fill="y")

    item_list = tk.Listbox(list_frame, height=8, yscrollcommand=scrollbar.set)
    item_list.pack(side="left")
    scrollbar.config(command=item_list.yview)

    for number in range(1, 51):
        item_list.insert(tk.END, f"Item {number}")

    tk.Button(root, text="How far?", command=where).pack()
    result_label = tk.Label(root, text="")
    result_label.pack()

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
    * - ``pack(side=, fill=)``
      - Put a vertical scrollbar down the right
      - ``pack(side="right", fill="y")``
    * - ``yscrollcommand``
      - Widget tells the scrollbar it moved
      - ``yscrollcommand=scrollbar.set``
    * - ``command``
      - Scrollbar tells the widget to move
      - ``scrollbar.config(command=box.yview)``
    * - ``orient``
      - Up-and-down or side-to-side
      - ``orient="horizontal"``
    * - ``xscrollcommand``, ``xview``
      - Linking a horizontal scrollbar
      - ``xscrollcommand=bar.set``
    * - ``width``
      - Thickness in pixels
      - ``width=25``
    * - ``scrollregion``
      - Size of the whole drawing (Canvas only)
      - ``scrollregion=(0, 0, 300, 1000)``
    * - ``yview_moveto()``
      - Jump to the top (0) or bottom (1)
      - ``box.yview_moveto(1)``
    * - ``get()``
      - Where the handle is (0 to 1)
      - ``scrollbar.get()``

----

All Scrollbar options
---------------------------

| Here is every option a Scrollbar can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``activebackground``
      - Colour of the arrows and slider when the mouse is over them
      - ``activebackground="lightblue"``
    * - ``activerelief``
      - Border style of the part the mouse is over
      - ``activerelief="sunken"``
    * - ``bg`` or ``background``
      - Background colour
      - ``bg="lavender"``
    * - ``bd`` or ``borderwidth``
      - How thick the border is
      - ``bd=3``
    * - ``command``
      - Connects it to the widget it scrolls
      - ``command=listbox.yview``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``elementborderwidth``
      - Border thickness of the arrows and slider
      - ``elementborderwidth=2``
    * - ``highlightbackground``
      - Colour of the focus outline when it is not selected by the keyboard
      - ``highlightbackground="white"``
    * - ``highlightcolor``
      - Colour of the focus outline when it is selected by the keyboard
      - ``highlightcolor="blue"``
    * - ``highlightthickness``
      - How thick the focus outline is
      - ``highlightthickness=2``
    * - ``jump``
      - ``True`` waits until you let go of the slider before scrolling
      - ``jump=True``
    * - ``orient``
      - Up and down (``"vertical"``) or side to side (``"horizontal"``)
      - ``orient="horizontal"``
    * - ``relief``
      - Border style: ``"raised"``, ``"sunken"``, ``"flat"``, ``"ridge"``, ``"groove"`` or ``"solid"``
      - ``relief="sunken"``
    * - ``repeatdelay``
      - How long to hold an arrow before it keeps scrolling (milliseconds)
      - ``repeatdelay=500``
    * - ``repeatinterval``
      - How often it scrolls while an arrow is held (milliseconds)
      - ``repeatinterval=100``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``troughcolor``
      - Colour of the track the slider moves along
      - ``troughcolor="lightgrey"``
    * - ``width``
      - How thick the scrollbar is (in pixels)
      - ``width=20``

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

        What is a Scrollbar used for?

        [x] Moving through content that does not fit, like a long list | Correct. It scrolls another widget.
        [ ] Picking a number | Incorrect. That is a Scale.
        [ ] Typing | Incorrect. That is an Entry.
        [ ] Drawing | Incorrect. That is a Canvas.

    .. multichoice::

        Can a Scrollbar scroll by itself, without another widget?

        [ ] Yes | Incorrect. It needs another widget.
        [x] No, it must be connected to a widget like Text, Listbox or Canvas | Correct. It controls that widget's view.
        [ ] Only when vertical | Incorrect. It always needs a widget.
        [ ] Only with bg set | Incorrect. It needs a widget.

    .. multichoice::

        What is the default orient for a Scrollbar?

        [x] "vertical" | Correct. Up and down is the default.
        [ ] "horizontal" | Incorrect. That must be set.
        [ ] "both" | Incorrect. Not a value.
        [ ] "none" | Incorrect. Not a value.

    .. multichoice::

        What does width=20 do on a Scrollbar?

        [ ] Makes it 20 long | Incorrect. It sets the thickness.
        [x] Makes it 20 pixels thick | Correct. width is the thickness.
        [ ] Scrolls 20 lines | Incorrect. It sets size.
        [ ] Shows 20 items | Incorrect. Not related.

    .. multichoice::

        Two steps connect a Scrollbar to a Text box. One is command=text.yview. What is the other?

        [x] text.config(yscrollcommand=scrollbar.set) | Correct. The Text tells the Scrollbar where it is.
        [ ] text.config(command=scrollbar) | Incorrect. Text has no command option.
        [ ] scrollbar.pack(text) | Incorrect. Not how it connects.
        [ ] scrollbar.set(text) | Incorrect. Not how it connects.

    .. multichoice::

        What does command=listbox.yview do?

        [ ] Deletes the list | Incorrect. It scrolls the list.
        [x] Makes moving the Scrollbar scroll the Listbox up and down | Correct. yview moves the view up and down.
        [ ] Adds an item | Incorrect. It scrolls.
        [ ] Changes the colour | Incorrect. It scrolls.

    .. multichoice::

        For a horizontal Scrollbar, which pair is used?

        [ ] yview and yscrollcommand | Incorrect. Those are for up and down.
        [x] xview and xscrollcommand | Correct. x is side to side.
        [ ] view and scrollcommand | Incorrect. Not the names.
        [ ] left and right | Incorrect. Not the names.

    .. multichoice::

        Where is a vertical Scrollbar usually packed?

        [ ] side="top" | Incorrect. It goes beside the widget.
        [x] side="right", fill="y" | Correct. It sits on the right and stretches up and down.
        [ ] side="bottom", fill="x" | Incorrect. That is for horizontal ones.
        [ ] side="left", fill="x" | Incorrect. fill="x" is wrong for vertical.

    .. multichoice::

        Why put a Text and its Scrollbar inside a Frame?

        [x] So they stay together as one part of the layout | Correct. The frame groups them.
        [ ] Scrollbars only work in frames | Incorrect. They work anywhere.
        [ ] To make it scroll faster | Incorrect. No change.
        [ ] To colour them | Incorrect. Not why.

    .. multichoice::

        With grid, how is a vertical Scrollbar made to stretch the full height?

        [ ] sticky="ew" | Incorrect. That stretches side to side.
        [x] sticky="ns" | Correct. North and south stretches it up and down.
        [ ] fill="y" | Incorrect. fill is for pack.
        [ ] expand=True | Incorrect. That is for pack.

    .. multichoice::

        What must a Canvas have before a Scrollbar can scroll it?

        [ ] A Text widget | Incorrect. Not needed.
        [x] A scrollregion setting the full drawing size | Correct. e.g. scrollregion=(0, 0, 1000, 1000).
        [ ] A Listbox | Incorrect. Not needed.
        [ ] A frame | Incorrect. Not required.

    .. multichoice::

        Which line scrolls a Text box to the end from code?

        [x] text.see(tk.END) or text.yview_moveto(1) | Correct. Both move the view to the end.
        [ ] scrollbar.end() | Incorrect. Not a method.
        [ ] text.scroll("end") | Incorrect. Not a method.
        [ ] scrollbar.set(1) | Incorrect. That only moves the bar.

    .. multichoice::

        What does scrollbar.get() give?

        [ ] The text | Incorrect. It gives positions.
        [x] Two numbers showing where the visible part starts and ends (0 to 1) | Correct. e.g. (0.0, 0.5) means the top half is shown.
        [ ] The widget it scrolls | Incorrect. It gives positions.
        [ ] The colour | Incorrect. It gives positions.

    .. multichoice::

        What does yview_moveto(0) do?

        [ ] Scrolls to the end | Incorrect. 0 is the top.
        [x] Scrolls to the top | Correct. 0 is the start.
        [ ] Deletes the text | Incorrect. It only scrolls.
        [ ] Moves 0 lines | Incorrect. It moves to the top.

    .. multichoice::

        Which line changes a Scrollbar's thickness later?

        [ ] scrollbar.width(20) | Incorrect. Not a method.
        [x] scrollbar.config(width=20) | Correct. config changes options.
        [ ] scrollbar.set(width=20) | Incorrect. set moves the slider.
        [ ] scrollbar.size = 20 | Incorrect. Use config.

    .. multichoice::

        Which widgets have yview, so they can use a vertical Scrollbar?

        [x] Text, Listbox and Canvas | Correct. They all scroll.
        [ ] Label and Button | Incorrect. They do not scroll.
        [ ] Scale | Incorrect. It is already a slider.
        [ ] Frame | Incorrect. Frames do not scroll by themselves.

    .. multichoice::

        What does troughcolor change?

        [ ] The arrows | Incorrect. It colours the track.
        [x] The track the slider moves in | Correct. The trough is the track.
        [ ] The scrolled widget | Incorrect. Only the Scrollbar.
        [ ] Nothing | Incorrect. It colours the track.

    .. multichoice::

        How do you make a horizontal Scrollbar?

        [ ] tk.Scrollbar(root, side="x") | Incorrect. Not an option.
        [x] tk.Scrollbar(root, orient="horizontal") | Correct. orient sets the direction.
        [ ] tk.Scrollbar(root, across=True) | Incorrect. Not an option.
        [ ] tk.Scrollbar(root, width="horizontal") | Incorrect. width is thickness.

    .. multichoice::

        Why might text need wrap="none" for a horizontal Scrollbar?

        [x] So long lines do not wrap and can be scrolled sideways | Correct. Wrapped lines never need sideways scrolling.
        [ ] So it scrolls faster | Incorrect. Not about speed.
        [ ] So the colours show | Incorrect. Not related.
        [ ] It is never needed | Incorrect. It is needed for sideways scrolling.

    .. multichoice::

        If the Scrollbar moves but the widget does not, what is missing?

        [ ] The bg colour | Incorrect. Not related.
        [x] command=widget.yview on the Scrollbar | Correct. That links the Scrollbar to the widget.
        [ ] A Frame | Incorrect. Not required.
        [ ] tickinterval | Incorrect. Not a Scrollbar option.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Connect a Scrollbar to a Text box.

        scrollbar = tk.@@Scrollbar | Scale | Frame@@(root, @@command | scroll | link@@=text.yview)
        text.config(@@yscrollcommand | command | xscrollcommand@@=scrollbar.set)

    .. cloze::
        :instructions: Place the Scrollbar beside the Text box.

        scrollbar.pack(side="@@right | top | bottom@@", fill="@@y | x | both@@")
        text.pack(side="left", fill="both", expand=True)

    .. cloze::
        :instructions: Make a horizontal Scrollbar.

        x_scroll = tk.Scrollbar(root, @@orient | side | direction@@="horizontal", command=text.@@xview | yview | view@@)
        text.config(xscrollcommand=x_scroll.set, @@wrap | width | fill@@="none")

    .. cloze::
        :instructions: Use grid for a Listbox and Scrollbar.

        listbox.grid(row=0, column=0)
        scrollbar.grid(row=0, column=@@1 | 0 | 2@@, sticky="@@ns | ew | nsew@@")

    .. cloze::
        :instructions: Scroll a Canvas.

        canvas.config(@@scrollregion | scrollsize | region@@=(0, 0, 1000, 1000), yscrollcommand=scrollbar.set)
        scrollbar.config(command=canvas.@@yview | xview | scroll@@)

----

.. admonition:: Tasks

    #. Make a window titled "Numbers" that is 300x200. Add a Listbox with the numbers 1 to 200 and a vertical scrollbar linked to it.
    #. Make your scrollbar 25 pixels thick and add a "Bottom" button that jumps to the end of the list.
    #. Make a Text widget with ``wrap="none"`` and a horizontal scrollbar along the bottom. Insert one very long line of text.
    #. Put a Listbox of ten fruits and its scrollbar inside a Frame. Put a label "Fruit" above the frame and a "Choose" button below it.

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
                    root.title("Numbers")

                    scrollbar = tk.Scrollbar(root)
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


                    def bottom():
                        number_list.yview_moveto(1)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Numbers")

                    tk.Button(root, text="Bottom", command=bottom).pack(side="bottom")

                    scrollbar = tk.Scrollbar(root, width=25)
                    scrollbar.pack(side="right", fill="y")

                    number_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
                    number_list.pack(side="left", fill="both", expand=True)
                    scrollbar.config(command=number_list.yview)

                    for number in range(1, 201):
                        number_list.insert(tk.END, number)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Long line")

                    scrollbar = tk.Scrollbar(root, orient="horizontal")
                    scrollbar.pack(side="bottom", fill="x")

                    long_text = tk.Text(root, wrap="none", xscrollcommand=scrollbar.set)
                    long_text.pack(fill="both", expand=True)
                    scrollbar.config(command=long_text.xview)

                    long_text.insert("1.0", "This is a very very very long line of text " * 5)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x250")
                    root.title("Fruit")

                    tk.Label(root, text="Fruit", font=("Arial", 14)).pack()

                    list_frame = tk.Frame(root)
                    list_frame.pack(pady=5)

                    scrollbar = tk.Scrollbar(list_frame)
                    scrollbar.pack(side="right", fill="y")

                    fruit_list = tk.Listbox(list_frame, height=5, yscrollcommand=scrollbar.set)
                    fruit_list.pack(side="left")
                    scrollbar.config(command=fruit_list.yview)

                    for fruit in ["Apple", "Banana", "Cherry", "Grape", "Kiwi",
                                  "Lemon", "Mango", "Orange", "Peach", "Pear"]:
                        fruit_list.insert(tk.END, fruit)

                    tk.Button(root, text="Choose").pack()

                    root.mainloop()
