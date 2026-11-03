====================================================
tk Frame
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Frame>`_

----

What is a Frame?
-------------------

| A **Frame** is an invisible box that holds other widgets.
| Frames are used to **group** widgets together and to **lay out** a window, e.g. a row of buttons along the top and a box of results underneath.
| A frame does nothing by itself. Its job is to hold other widgets.

----

Making a Frame
-------------------

#. **Create** the frame with ``tk.Frame(root)``.
#. **Place** the frame in the window with ``.pack()``.
#. **Put widgets in the frame.** Use the frame's name, not ``root``, as the first thing in the brackets.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first frame")    # Words in the title bar

    box = tk.Frame(root, bg="lightblue", padx=10, pady=10)  # 1. Create the frame
    box.pack(pady=20)                                       # 2. Place it in the window

    hello_label = tk.Label(box, text="I am inside the frame")   # 3. "box", not "root"
    hello_label.pack()

    ok_button = tk.Button(box, text="OK")                       # 3. "box", not "root"
    ok_button.pack()

    root.mainloop()                 # Keep the window open

| The first thing in the brackets is the **parent**: the thing the widget lives inside.
| ``tk.Label(box, ...)`` means "make a label that lives inside **box**".

----

Frame options
-------------------

| Options are written as ``option=value`` inside ``tk.Frame( )``, separated by commas.

bg (background colour)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What it does:** sets the colour of the frame. Without a colour a frame is invisible, so ``bg`` helps you see where it is.
| **How to write it:** ``bg="colour"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("bg")

    top_frame = tk.Frame(root, bg="pink")
    top_frame.pack(fill="x")

    title_label = tk.Label(top_frame, text="My App", bg="pink", font=("Arial", 18))
    title_label.pack()

    root.mainloop()

| Give widgets inside the frame the same ``bg`` so they blend in.

width and height
~~~~~~~~~~~~~~~~~~

| **What they do:** set the size of the frame in **pixels**.
| **How to write them:** ``width=200``, ``height=100``
| An **empty** frame uses this size. Once a frame has widgets inside it, it shrinks or grows to fit them.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and height")

    empty_frame = tk.Frame(root, width=200, height=100, bg="orange")
    empty_frame.pack(pady=20)

    root.mainloop()

padx and pady
~~~~~~~~~~~~~~~~~~

| **What they do:** add empty space **inside** the frame, between its edge and the widgets inside it.
| **How to write them:** ``padx=20``, ``pady=10`` (pixels)

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("padx and pady")

    padded_frame = tk.Frame(root, bg="lightgreen", padx=30, pady=20)
    padded_frame.pack(pady=20)

    name_label = tk.Label(padded_frame, text="Lots of space around me")
    name_label.pack()

    root.mainloop()

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** draw a border around the frame.
| ``relief`` is the border style. ``borderwidth`` is how thick it is in pixels.
| **How to write them:** ``relief="groove", borderwidth=3``
| **Styles:** ``"flat"`` (no border, the default), ``"solid"``, ``"raised"``, ``"sunken"``, ``"groove"``, ``"ridge"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("relief")

    border_frame = tk.Frame(root, relief="groove", borderwidth=3, padx=10, pady=10)
    border_frame.pack(pady=20)

    tk.Label(border_frame, text="Username").pack()
    tk.Entry(border_frame).pack()

    root.mainloop()

| ``tk.Label(...).pack()`` creates and places a widget in one line. Only do this when you never need to use the widget's name again.

cursor
~~~~~~~~~~~~~~~~~~

| **What it does:** changes the mouse pointer when it is over the frame.
| **How to write it:** ``cursor="hand2"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("cursor")

    target_frame = tk.Frame(root, width=150, height=100, bg="yellow", cursor="cross")
    target_frame.pack(pady=40)

    root.mainloop()

----

Laying out a window with frames
-----------------------------------

| ``pack()`` normally stacks widgets from top to bottom.
| ``pack(side="left")`` puts widgets side by side instead.
| By packing widgets into frames, you can have rows **and** columns in the same window.

side
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses which side of the frame (or window) a widget is packed against.
| **How to write it:** ``widget.pack(side="left")``
| **Values:** ``"top"`` (the default), ``"bottom"``, ``"left"``, ``"right"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("A row of buttons")

    button_row = tk.Frame(root)
    button_row.pack(pady=20)

    tk.Button(button_row, text="Back", width=8).pack(side="left", padx=5)
    tk.Button(button_row, text="Home", width=8).pack(side="left", padx=5)
    tk.Button(button_row, text="Next", width=8).pack(side="left", padx=5)

    root.mainloop()

fill and expand
~~~~~~~~~~~~~~~~~~

| **What they do:**
| ``fill="x"`` stretches the frame across the whole width. ``fill="y"`` stretches it down the whole height. ``fill="both"`` does both.
| ``expand=True`` lets the frame use any extra space in the window.
| Resize the window to see the main frame grow.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("fill and expand")

    header = tk.Frame(root, bg="navy", height=40)
    header.pack(fill="x")                       # Full width

    main = tk.Frame(root, bg="white")
    main.pack(fill="both", expand=True)         # Use all the space left

    footer = tk.Frame(root, bg="gray", height=30)
    footer.pack(fill="x")                       # Full width

    root.mainloop()

A full layout example
~~~~~~~~~~~~~~~~~~~~~~~~~

| This window has a title bar along the top, a menu down the left and a main area on the right.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("400x250")
    root.title("Layout")

    # Title bar along the top
    title_frame = tk.Frame(root, bg="darkgreen")
    title_frame.pack(fill="x")
    tk.Label(title_frame, text="Science Quiz", fg="white", bg="darkgreen",
             font=("Arial", 18)).pack(pady=5)

    # Menu down the left side
    menu_frame = tk.Frame(root, bg="lightgreen", padx=10, pady=10)
    menu_frame.pack(side="left", fill="y")
    tk.Button(menu_frame, text="Start", width=10).pack(pady=5)
    tk.Button(menu_frame, text="Scores", width=10).pack(pady=5)
    tk.Button(menu_frame, text="Quit", width=10, command=root.destroy).pack(pady=5)

    # Main area on the right
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(side="left", fill="both", expand=True)
    tk.Label(main_frame, text="Press Start to begin", bg="white",
             font=("Arial", 14)).pack(pady=40)

    root.mainloop()

Using grid inside a frame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``grid()`` places widgets in **rows** and **columns**, like a table.
| Each frame can use a different layout: ``pack`` in one frame and ``grid`` in another.
| Do **not** mix ``pack`` and ``grid`` for widgets that share the **same** parent.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("grid in a frame")

    tk.Label(root, text="Sign up", font=("Arial", 16)).pack(pady=5)    # pack in root

    form = tk.Frame(root)
    form.pack()

    tk.Label(form, text="Name:").grid(row=0, column=0)      # grid in form
    tk.Entry(form).grid(row=0, column=1)
    tk.Label(form, text="Email:").grid(row=1, column=0)
    tk.Entry(form).grid(row=1, column=1)

    root.mainloop()

----

Frame methods
-------------------

| A **method** is an action that a widget can do. Methods are written after a dot.

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options **after** the frame has been made.
| **How to write it:** ``frame.config(option=value)``

.. code-block:: python

    import tkinter as tk


    def light_on():
        room.config(bg="yellow")


    def light_off():
        room.config(bg="black")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    room = tk.Frame(root, width=200, height=100, bg="black")
    room.pack(pady=10)

    tk.Button(root, text="Light on", command=light_on).pack()
    tk.Button(root, text="Light off", command=light_off).pack()

    root.mainloop()

pack_forget
~~~~~~~~~~~~~~~~~~

| **What it does:** hides a frame (and everything in it). It is not deleted, so ``pack()`` shows it again.
| **How to write it:** ``frame.pack_forget()``
| This is a simple way to swap between "screens" in an app.

.. code-block:: python

    import tkinter as tk


    def show_answer():
        question_frame.pack_forget()        # Hide the question
        answer_frame.pack(pady=20)          # Show the answer


    root = tk.Tk()
    root.geometry("300x200")
    root.title("pack_forget")

    question_frame = tk.Frame(root)
    question_frame.pack(pady=20)
    tk.Label(question_frame, text="What is the largest planet?").pack()
    tk.Button(question_frame, text="Show answer", command=show_answer).pack(pady=5)

    answer_frame = tk.Frame(root)           # Not packed yet, so it is hidden
    tk.Label(answer_frame, text="Jupiter!", font=("Arial", 24)).pack()

    root.mainloop()

winfo_children
~~~~~~~~~~~~~~~~~~

| **What it does:** gives back a list of every widget inside the frame.
| **How to write it:** ``frame.winfo_children()``
| Looping through the list lets you change every widget in the frame at once.

.. code-block:: python

    import tkinter as tk


    def disable_all():
        for widget in controls.winfo_children():
            widget.config(state="disabled")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("winfo_children")

    controls = tk.Frame(root)
    controls.pack(pady=10)
    tk.Button(controls, text="Up").pack()
    tk.Button(controls, text="Down").pack()
    tk.Button(controls, text="Left").pack()

    tk.Button(root, text="Game over", command=disable_all).pack(pady=10)

    root.mainloop()

destroy
~~~~~~~~~~~~~~~~~~

| **What it does:** deletes the frame and everything inside it. It cannot be shown again.
| **How to write it:** ``frame.destroy()``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("destroy")

    welcome_frame = tk.Frame(root, bg="lightyellow", padx=20, pady=20)
    welcome_frame.pack(pady=20)
    tk.Label(welcome_frame, text="Welcome!", bg="lightyellow", font=("Arial", 18)).pack()
    tk.Button(welcome_frame, text="Close this message", command=welcome_frame.destroy).pack()

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
    * - ``tk.Label(frame, ...)``
      - Put a widget inside the frame
      - ``tk.Button(box, text="OK")``
    * - ``bg``
      - Colour of the frame
      - ``bg="lightblue"``
    * - ``width``, ``height``
      - Size in pixels (empty frames)
      - ``width=200, height=100``
    * - ``padx``, ``pady``
      - Space inside the frame
      - ``padx=10, pady=10``
    * - ``relief``, ``borderwidth``
      - Border style and thickness
      - ``relief="groove", borderwidth=3``
    * - ``cursor``
      - Mouse pointer over the frame
      - ``cursor="hand2"``
    * - ``pack(side=...)``
      - Pack against a side
      - ``pack(side="left")``
    * - ``pack(fill=...)``
      - Stretch to fill the space
      - ``pack(fill="x")``
    * - ``pack(expand=True)``
      - Use the extra space
      - ``pack(fill="both", expand=True)``
    * - ``config()``
      - Change options later
      - ``frame.config(bg="red")``
    * - ``pack_forget()``
      - Hide the frame
      - ``frame.pack_forget()``
    * - ``winfo_children()``
      - List the widgets inside
      - ``frame.winfo_children()``
    * - ``destroy()``
      - Delete the frame
      - ``frame.destroy()``

----

All Frame options
---------------------------

| Here is every option a Frame can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``bg`` or ``background``
      - Background colour of the frame
      - ``bg="lightblue"``
    * - ``bd`` or ``borderwidth``
      - How thick the border is
      - ``bd=3``
    * - ``class_``
      - A group name used to style many widgets at once (advanced). Written ``class_`` in Python
      - ``class_="Sidebar"``
    * - ``colormap``
      - Which set of colours to use (advanced, rarely needed)
      - ``colormap="new"``
    * - ``container``
      - Lets another program be placed inside it (advanced, rarely needed)
      - ``container=False``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``height``
      - How tall it is (in pixels)
      - ``height=200``
    * - ``highlightbackground``
      - Colour of the focus outline when it is not selected by the keyboard
      - ``highlightbackground="white"``
    * - ``highlightcolor``
      - Colour of the focus outline when it is selected by the keyboard
      - ``highlightcolor="blue"``
    * - ``highlightthickness``
      - How thick the focus outline is
      - ``highlightthickness=2``
    * - ``padx``
      - Extra space inside it, on the left and right
      - ``padx=10``
    * - ``pady``
      - Extra space inside it, at the top and bottom
      - ``pady=10``
    * - ``relief``
      - Border style: ``"raised"``, ``"sunken"``, ``"flat"``, ``"ridge"``, ``"groove"`` or ``"solid"``
      - ``relief="sunken"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``visual``
      - Colour mode for the window (advanced, rarely needed)
      - ``visual="truecolor"``
    * - ``width``
      - How wide it is (in pixels)
      - ``width=300``

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

        What is a Frame used for?

        [x] Holding and grouping other widgets | Correct. A Frame is a container.
        [ ] Showing text | Incorrect. A Label shows text.
        [ ] Drawing shapes | Incorrect. A Canvas draws.
        [ ] Making a menu | Incorrect. A Menu does that.

    .. multichoice::

        To put a button inside frame, what is written first?

        [ ] tk.Button(root, ...) | Incorrect. root puts it in the window.
        [x] tk.Button(frame, ...) | Correct. The first value is the parent.
        [ ] tk.Button(..., parent=frame) | Incorrect. The parent goes first.
        [ ] frame.Button(...) | Incorrect. Widgets are made with tk.Button.

    .. multichoice::

        What does bg="lightblue" do to a frame?

        [x] Colours its background light blue | Correct. bg is the background colour.
        [ ] Colours the buttons inside | Incorrect. Each widget has its own bg.
        [ ] Colours the words | Incorrect. Frames have no words.
        [ ] Nothing | Incorrect. Frames do have a background.

    .. multichoice::

        For a Frame, width=300 is measured in:

        [ ] Characters | Incorrect. Frames do not hold text.
        [x] Pixels | Correct. Frame size is in pixels.
        [ ] Lines | Incorrect. That is for Text.
        [ ] Centimetres | Incorrect. Not used here.

    .. multichoice::

        Why might a frame shrink to fit its widgets even with width set?

        [ ] width does not work | Incorrect. It works until widgets are added.
        [x] pack and grid resize the frame to fit what is inside | Correct. Use pack_propagate(False) to keep the size.
        [ ] The frame is disabled | Incorrect. Frames are not disabled.
        [ ] bg is missing | Incorrect. bg does not affect size.

    .. multichoice::

        What do padx and pady do on a Frame?

        [ ] Add space outside the frame | Incorrect. That is done in pack.
        [x] Add space inside the frame, around its widgets | Correct. They pad the inside edge.
        [ ] Add more frames | Incorrect. They add space.
        [ ] Change the colour | Incorrect. bg changes colour.

    .. multichoice::

        Which pair gives a frame a visible border?

        [ ] fg and bg | Incorrect. These are colours.
        [x] relief and borderwidth | Correct. relief sets style, borderwidth sets thickness.
        [ ] width and height | Incorrect. These set size.
        [ ] padx and pady | Incorrect. These add space.

    .. multichoice::

        What does side="left" do in frame.pack(side="left")?

        [x] Puts the frame on the left, so frames line up side by side | Correct. side sets which edge it packs against.
        [ ] Puts the words on the left | Incorrect. Frames have no words.
        [ ] Aligns the buttons inside | Incorrect. It places the frame itself.
        [ ] Stretches the frame | Incorrect. fill does that.

    .. multichoice::

        What does fill="x" do in pack?

        [ ] Fills the frame with colour | Incorrect. bg sets colour.
        [x] Stretches the widget across the full width | Correct. fill="x" stretches side to side.
        [ ] Stretches it up and down | Incorrect. That is fill="y".
        [ ] Adds x number of widgets | Incorrect. It stretches.

    .. multichoice::

        What does expand=True do in pack?

        [ ] Makes the font bigger | Incorrect. It is about space.
        [x] Lets the widget use spare space when the window grows | Correct. expand gives it extra space.
        [ ] Opens a new window | Incorrect. It does not.
        [ ] Adds a scrollbar | Incorrect. It does not.

    .. multichoice::

        Can grid be used inside a frame while the frame itself uses pack?

        [x] Yes, each container can use its own layout | Correct. Inside one container, use just one of pack or grid.
        [ ] No, never | Incorrect. Different containers can differ.
        [ ] Only with Canvas | Incorrect. Any frame works.
        [ ] Only if bg is set | Incorrect. bg does not matter.

    .. multichoice::

        What is the rule about pack and grid?

        [ ] Never use both in a program | Incorrect. They can be in different containers.
        [x] Do not mix pack and grid inside the same container | Correct. Mixing them in one container can freeze the window.
        [ ] Always use both | Incorrect. That can freeze the program.
        [ ] grid only works in frames | Incorrect. grid works in root too.

    .. multichoice::

        Which line changes a frame's colour later?

        [ ] frame.bg("red") | Incorrect. bg is not a method.
        [x] frame.config(bg="red") | Correct. config changes options.
        [ ] frame.colour = "red" | Incorrect. Options are changed with config.
        [ ] frame.set("red") | Incorrect. Frames do not have set.

    .. multichoice::

        What does frame.pack_forget() do?

        [ ] Deletes the frame forever | Incorrect. destroy deletes it.
        [x] Hides the frame, but it can be packed again | Correct. pack_forget removes it from view.
        [ ] Packs it on the left | Incorrect. That is pack(side="left").
        [ ] Clears its colour | Incorrect. It hides it.

    .. multichoice::

        What does frame.winfo_children() give?

        [x] A list of the widgets inside the frame | Correct. These are its children.
        [ ] The frame's size | Incorrect. winfo_width gives size.
        [ ] The frame's parent | Incorrect. winfo_parent gives that.
        [ ] The number of frames | Incorrect. It lists the widgets inside.

    .. multichoice::

        How do you delete every widget inside a frame?

        [ ] frame.delete("all") | Incorrect. That is for Canvas.
        [x] Loop through frame.winfo_children() and call destroy() on each | Correct. Each child is destroyed.
        [ ] frame.clear() | Incorrect. Frames do not have clear.
        [ ] frame.pack_forget() | Incorrect. That hides the frame itself.

    .. multichoice::

        What does frame.destroy() do?

        [ ] Hides the frame | Incorrect. pack_forget hides.
        [ ] Empties the frame | Incorrect. It removes the frame too.
        [x] Removes the frame and everything inside it | Correct. destroy deletes it for good.
        [ ] Closes the program | Incorrect. Only the frame is removed.

    .. multichoice::

        Why use frames in a layout?

        [x] To split the window into parts, like a top bar and a side bar | Correct. Frames group related widgets.
        [ ] To make widgets faster | Incorrect. They do not change speed.
        [ ] To add colour to words | Incorrect. fg does that.
        [ ] Because widgets must be in a frame | Incorrect. Widgets can go straight in root.

    .. multichoice::

        relief="groove" gives a border that looks:

        [ ] Raised | Incorrect. That is "raised".
        [x] Like a carved line | Correct. groove looks carved in.
        [ ] Invisible | Incorrect. That is "flat".
        [ ] Pushed in | Incorrect. That is "sunken".

    .. multichoice::

        Which pack option places a frame at the bottom?

        [ ] side="down" | Incorrect. down is not a side.
        [x] side="bottom" | Correct. bottom is a pack side.
        [ ] anchor="bottom" | Incorrect. anchor uses compass letters.
        [ ] fill="bottom" | Incorrect. fill uses x, y or both.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a coloured frame with a button inside.

        top_frame = tk.@@Frame | Label | Canvas@@(root, bg="lightblue", @@padx | width | fill@@=10, pady=10)
        top_frame.pack(fill="@@x | y | left@@")
        tk.Button(@@top_frame | root | frame@@, text="Home").pack(side="left")

    .. cloze::
        :instructions: Give a frame a size and a border.

        box = tk.Frame(root, width=300, @@height | length | size@@=200, @@relief | border | style@@="groove", borderwidth=3)
        box.pack()

    .. cloze::
        :instructions: Put two frames side by side.

        left_frame.pack(@@side | fill | anchor@@="left", fill="y")
        right_frame.pack(side="left", fill="both", @@expand | stretch | grow@@=True)

    .. cloze::
        :instructions: Use grid inside a frame.

        form = tk.Frame(root)
        form.pack()
        tk.Label(form, text="Name:").@@grid | pack | place@@(row=0, column=0)
        tk.Entry(form).grid(row=0, @@column | col | side@@=1)

    .. cloze::
        :instructions: Hide a frame, then clear it.

        side_frame.@@pack_forget | destroy | hide@@()
        for widget in side_frame.@@winfo_children | children | widgets@@():
            widget.@@destroy | forget | delete@@()

----

.. admonition:: Tasks

    #. Make a window titled "Frames" that is 300x200. Add a frame with a light blue background and 20 pixels of padding inside it. Put a label "Hello" inside the frame.
    #. Make a frame that holds three buttons, "Red", "Green" and "Blue", side by side.
    #. Make a window with a dark blue frame across the top that holds a white title label "My App", and a white frame underneath that fills the rest of the window.
    #. Make two frames: a "start" frame with a "Start" button, and a "game" frame with the label "Game started!". When "Start" is clicked, hide the start frame and show the game frame.

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
                    root.title("Frames")

                    box = tk.Frame(root, bg="lightblue", padx=20, pady=20)
                    box.pack(pady=20)

                    hello_label = tk.Label(box, text="Hello")
                    hello_label.pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Frames")

                    button_row = tk.Frame(root)
                    button_row.pack(pady=20)

                    tk.Button(button_row, text="Red").pack(side="left", padx=5)
                    tk.Button(button_row, text="Green").pack(side="left", padx=5)
                    tk.Button(button_row, text="Blue").pack(side="left", padx=5)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Frames")

                    top_frame = tk.Frame(root, bg="darkblue")
                    top_frame.pack(fill="x")
                    tk.Label(top_frame, text="My App", fg="white", bg="darkblue",
                             font=("Arial", 16)).pack(pady=5)

                    main_frame = tk.Frame(root, bg="white")
                    main_frame.pack(fill="both", expand=True)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def start():
                        start_frame.pack_forget()
                        game_frame.pack(pady=20)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Game")

                    start_frame = tk.Frame(root)
                    start_frame.pack(pady=20)
                    tk.Button(start_frame, text="Start", command=start).pack()

                    game_frame = tk.Frame(root)
                    tk.Label(game_frame, text="Game started!", font=("Arial", 18)).pack()

                    root.mainloop()
