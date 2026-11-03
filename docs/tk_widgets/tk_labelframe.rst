====================================================
tk LabelFrame
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.LabelFrame>`_

----

What is a LabelFrame?
------------------------

| A **LabelFrame** is a **Frame** with a border and a title.
| It draws a box around a group of widgets and puts a heading in the border, like a section on a paper form.
| Use it to show which widgets belong together, e.g. "Personal details" or "Choose a size".

----

Making a LabelFrame
------------------------

#. **Create** the LabelFrame with ``tk.LabelFrame(root, text="Title")``.
#. **Place** it in the window with ``.pack()``.
#. **Put widgets in it.** Use the LabelFrame's name, not ``root``, as the first thing in the brackets.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first LabelFrame")

    details = tk.LabelFrame(root, text="Your details", padx=10, pady=10)  # 1. Create it
    details.pack(pady=20)                                                 # 2. Place it

    name_label = tk.Label(details, text="Name:")        # 3. "details", not "root"
    name_label.pack()

    name_entry = tk.Entry(details)                      # 3. "details", not "root"
    name_entry.pack()

    root.mainloop()                 # Keep the window open

----

LabelFrame options
---------------------

| Options are written as ``option=value`` inside ``tk.LabelFrame( )``, separated by commas.

text
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the title shown in the border.
| **How to write it:** ``text="your title"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("text")

    settings = tk.LabelFrame(root, text="Settings", padx=10, pady=10)
    settings.pack(pady=20)

    tk.Checkbutton(settings, text="Sound on").pack()

    root.mainloop()

| ``tk.Checkbutton(...).pack()`` creates and places a widget in one line. Only do this when you never need to use the widget's name again.

font and fg
~~~~~~~~~~~~~~~~~~

| **What they do:** ``font`` sets the style and size of the title. ``fg`` sets the colour of the title.
| **How to write them:** ``font=("Arial", 14, "bold")``, ``fg="darkblue"``
| These change the **title** only, not the widgets inside.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("font and fg")

    scores = tk.LabelFrame(root, text="High scores", font=("Arial", 14, "bold"), fg="darkblue",
                           padx=10, pady=10)
    scores.pack(pady=20)

    tk.Label(scores, text="Ava: 120").pack()
    tk.Label(scores, text="Ben: 95").pack()

    root.mainloop()

bg (background colour)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What it does:** sets the colour inside the box.
| **How to write it:** ``bg="colour"``
| Give the widgets inside the same ``bg`` so they blend in.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("bg")

    notes = tk.LabelFrame(root, text="Notes", bg="lightyellow", padx=10, pady=10)
    notes.pack(pady=20)

    tk.Label(notes, text="Bring a hat tomorrow", bg="lightyellow").pack()

    root.mainloop()

padx and pady
~~~~~~~~~~~~~~~~~~

| **What they do:** add empty space between the border and the widgets inside.
| **How to write them:** ``padx=15``, ``pady=10`` (pixels)
| Without padding, the widgets touch the border.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("padx and pady")

    no_pad = tk.LabelFrame(root, text="No padding")
    no_pad.pack(pady=10)
    tk.Button(no_pad, text="Squashed").pack()

    padded = tk.LabelFrame(root, text="Padding", padx=30, pady=15)
    padded.pack(pady=10)
    tk.Button(padded, text="Roomy").pack()

    root.mainloop()

labelanchor
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses where the title sits on the border.
| **How to write it:** ``labelanchor="n"``
| **Values:** ``"nw"`` (top left, the default), ``"n"`` (top middle), ``"ne"`` (top right), and ``"sw"``, ``"s"``, ``"se"`` for the bottom.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("labelanchor")

    centred = tk.LabelFrame(root, text="Centred title", labelanchor="n", padx=20, pady=10)
    centred.pack(pady=20)

    tk.Label(centred, text="The title is in the middle").pack()

    root.mainloop()

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** change the style and thickness of the border.
| **How to write them:** ``relief="solid", borderwidth=2``
| **Styles:** ``"groove"`` (the default), ``"solid"``, ``"ridge"``, ``"raised"``, ``"sunken"``, ``"flat"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("relief")

    warning = tk.LabelFrame(root, text="Warning", relief="solid", borderwidth=2,
                            fg="red", padx=10, pady=10)
    warning.pack(pady=20)

    tk.Label(warning, text="Save your work!").pack()

    root.mainloop()

width and height
~~~~~~~~~~~~~~~~~~

| **What they do:** set the size of an **empty** LabelFrame in pixels.
| **How to write them:** ``width=200``, ``height=100``
| Once widgets are put inside, the LabelFrame shrinks or grows to fit them.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and height")

    empty_box = tk.LabelFrame(root, text="Coming soon", width=200, height=100)
    empty_box.pack(pady=20)

    root.mainloop()

----

Using LabelFrames
---------------------

Grouping radiobuttons
~~~~~~~~~~~~~~~~~~~~~~~~

| LabelFrames are perfect for showing that a set of radiobuttons is **one** question.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("Order")

    size_box = tk.LabelFrame(root, text="Size", padx=10, pady=5)
    size_box.pack(fill="x", padx=10, pady=5)

    size = tk.StringVar(value="Small")
    for choice in ["Small", "Medium", "Large"]:
        tk.Radiobutton(size_box, text=choice, variable=size, value=choice).pack(anchor="w")

    drink_box = tk.LabelFrame(root, text="Drink", padx=10, pady=5)
    drink_box.pack(fill="x", padx=10, pady=5)

    drink = tk.StringVar(value="Water")
    for choice in ["Water", "Juice"]:
        tk.Radiobutton(drink_box, text=choice, variable=drink, value=choice).pack(anchor="w")

    root.mainloop()

| ``pack(anchor="w")`` lines each radiobutton up on the left of the LabelFrame.

Side-by-side LabelFrames
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Use ``pack(side="left")`` to put LabelFrames next to each other.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("350x200")
    root.title("Side by side")

    player_1 = tk.LabelFrame(root, text="Player 1", padx=20, pady=10)
    player_1.pack(side="left", padx=10, pady=20)
    tk.Label(player_1, text="Score: 0", font=("Arial", 14)).pack()

    player_2 = tk.LabelFrame(root, text="Player 2", padx=20, pady=10)
    player_2.pack(side="left", padx=10, pady=20)
    tk.Label(player_2, text="Score: 0", font=("Arial", 14)).pack()

    root.mainloop()

A form with grid
~~~~~~~~~~~~~~~~~~~

| ``grid()`` lines up labels and entries in rows and columns inside the LabelFrame.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Form")

    form = tk.LabelFrame(root, text="Sign up", padx=10, pady=10)
    form.pack(pady=20)

    tk.Label(form, text="Name:").grid(row=0, column=0, sticky="e")
    tk.Entry(form).grid(row=0, column=1, pady=2)
    tk.Label(form, text="Email:").grid(row=1, column=0, sticky="e")
    tk.Entry(form).grid(row=1, column=1, pady=2)

    root.mainloop()

| ``sticky="e"`` pushes each label to the right (east) of its cell, so it sits next to its entry.

----

LabelFrame methods
---------------------

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options **after** the LabelFrame has been made, e.g. its title.
| **How to write it:** ``labelframe.config(option=value)``

.. code-block:: python

    import tkinter as tk

    round_number = 1


    def next_round():
        global round_number             # Allow the function to change round_number
        round_number = round_number + 1
        game_box.config(text=f"Round {round_number}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    game_box = tk.LabelFrame(root, text="Round 1", font=("Arial", 14), padx=20, pady=10)
    game_box.pack(pady=20)

    tk.Button(game_box, text="Next round", command=next_round).pack()

    root.mainloop()

cget
~~~~~~~~~~~~~~~~~~

| **What it does:** reads the current value of an option.
| **How to write it:** ``title = labelframe.cget("text")``

.. code-block:: python

    import tkinter as tk


    def show_title():
        result_label.config(text="This box is called: " + box.cget("text"))


    root = tk.Tk()
    root.geometry("300x200")
    root.title("cget")

    box = tk.LabelFrame(root, text="Mystery box", padx=20, pady=10)
    box.pack(pady=10)
    tk.Button(box, text="What is my title?", command=show_title).pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

| LabelFrames also have the same ``pack_forget()``, ``winfo_children()`` and ``destroy()`` methods as a **Frame**.

----

Quick reference
-------------------

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option or method
      - What it does
      - Example
    * - ``text``
      - Title in the border
      - ``text="Settings"``
    * - ``font``, ``fg``
      - Font and colour of the title
      - ``font=("Arial", 14), fg="blue"``
    * - ``bg``
      - Colour inside the box
      - ``bg="lightyellow"``
    * - ``padx``, ``pady``
      - Space between the border and the widgets
      - ``padx=10, pady=10``
    * - ``labelanchor``
      - Where the title sits
      - ``labelanchor="n"``
    * - ``relief``, ``borderwidth``
      - Border style and thickness
      - ``relief="solid", borderwidth=2``
    * - ``width``, ``height``
      - Size of an empty box in pixels
      - ``width=200, height=100``
    * - ``config()``
      - Change options later
      - ``box.config(text="New title")``
    * - ``cget()``
      - Read an option
      - ``box.cget("text")``

----

All LabelFrame options
---------------------------

| Here is every option a LabelFrame can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``bg`` or ``background``
      - Background colour
      - ``bg="lavender"``
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
    * - ``font``
      - Style and size of the title
      - ``font=("Arial", 12, "bold")``
    * - ``fg`` or ``foreground``
      - Colour of the title
      - ``fg="blue"``
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
    * - ``labelanchor``
      - Where the title sits on the border (``"n"`` = top middle, ``"nw"`` = top left)
      - ``labelanchor="n"``
    * - ``labelwidget``
      - Uses another widget (like a Label) as the title
      - ``labelwidget=title_label``
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
    * - ``text``
      - Title shown on the border
      - ``text="Settings"``
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

        What is a LabelFrame?

        [x] A frame with a border and a title | Correct. It groups widgets with a heading.
        [ ] A label that can be clicked | Incorrect. That is a Button.
        [ ] A box to type in | Incorrect. That is an Entry.
        [ ] A drawing area | Incorrect. That is a Canvas.

    .. multichoice::

        Which option sets the title on the border?

        [ ] title | Incorrect. title is for windows.
        [x] text | Correct. text sets the LabelFrame title.
        [ ] label | Incorrect. label is not an option here.
        [ ] heading | Incorrect. heading is not an option.

    .. multichoice::

        What do font and fg change on a LabelFrame?

        [ ] The widgets inside | Incorrect. Each widget has its own font.
        [x] The title on the border | Correct. They style the title.
        [ ] The border thickness | Incorrect. borderwidth does that.
        [ ] The background | Incorrect. bg does that.

    .. multichoice::

        What does bg="lightyellow" colour?

        [x] The inside of the LabelFrame | Correct. bg is its background.
        [ ] Only the title | Incorrect. The title is styled with fg and font.
        [ ] The whole window | Incorrect. Only the LabelFrame.
        [ ] The buttons inside | Incorrect. Each widget has its own bg.

    .. multichoice::

        What do padx and pady do on a LabelFrame?

        [ ] Move the title | Incorrect. labelanchor moves the title.
        [x] Add space inside, between the border and the widgets | Correct. They pad the inside.
        [ ] Add space outside | Incorrect. That is done in pack or grid.
        [ ] Make the title bigger | Incorrect. font does that.

    .. multichoice::

        What does labelanchor="n" do?

        [ ] Puts the title on the left | Incorrect. That is "w".
        [x] Puts the title in the middle of the top border | Correct. n is the top middle.
        [ ] Puts the title at the bottom | Incorrect. That is "s".
        [ ] Hides the title | Incorrect. It moves it.

    .. multichoice::

        Which labelanchor puts the title at the top left (the default)?

        [x] "nw" | Correct. n is top and w is left.
        [ ] "ne" | Incorrect. ne is top right.
        [ ] "sw" | Incorrect. sw is bottom left.
        [ ] "center" | Incorrect. center is not used for the title.

    .. multichoice::

        What do relief and borderwidth change?

        [ ] The title colour | Incorrect. fg does that.
        [x] The style and thickness of the border | Correct. relief is the style, borderwidth the thickness.
        [ ] The size of the widgets inside | Incorrect. They only affect the border.
        [ ] The window title | Incorrect. root.title does that.

    .. multichoice::

        Why is width or height sometimes ignored on a LabelFrame?

        [ ] The values are too small | Incorrect. It is about packing.
        [x] It shrinks to fit the widgets inside when they are packed | Correct. Packing resizes it to fit.
        [ ] LabelFrames have no size | Incorrect. They do.
        [ ] bg must be set first | Incorrect. bg does not affect size.

    .. multichoice::

        How do you put a Radiobutton inside a LabelFrame called box?

        [ ] tk.Radiobutton(root, ...) | Incorrect. That puts it in the window.
        [x] tk.Radiobutton(box, ...) | Correct. The parent comes first.
        [ ] box.add(tk.Radiobutton()) | Incorrect. LabelFrames do not use add.
        [ ] tk.Radiobutton(..., frame=box) | Incorrect. The parent goes first.

    .. multichoice::

        Why put radiobuttons in a LabelFrame?

        [x] To group them under a heading like "Size" | Correct. It shows they belong together.
        [ ] So more than one can be chosen | Incorrect. They still share a variable.
        [ ] To make them faster | Incorrect. No change in speed.
        [ ] Radiobuttons must be in a LabelFrame | Incorrect. They can go anywhere.

    .. multichoice::

        Which pack option puts two LabelFrames side by side?

        [ ] fill="x" | Incorrect. fill stretches.
        [x] side="left" | Correct. side="left" lines them up across.
        [ ] anchor="n" | Incorrect. anchor does not line them up.
        [ ] expand=False | Incorrect. expand is about spare space.

    .. multichoice::

        In a form inside a LabelFrame, which layout lines up labels and entries in rows?

        [ ] pack only | Incorrect. pack puts one under another.
        [x] grid with row and column | Correct. grid makes neat rows and columns.
        [ ] place only | Incorrect. place uses exact positions.
        [ ] No layout is needed | Incorrect. Widgets need a layout.

    .. multichoice::

        Which line changes the title later?

        [ ] box.title("New") | Incorrect. title is for windows.
        [x] box.config(text="New") | Correct. config changes the text option.
        [ ] box.set("New") | Incorrect. LabelFrames do not have set.
        [ ] box.text = "New" | Incorrect. Use config.

    .. multichoice::

        What does box.cget("text") give?

        [x] The current title | Correct. cget reads an option.
        [ ] The words in the widgets inside | Incorrect. Only the LabelFrame's own text.
        [ ] An error | Incorrect. It is a real method.
        [ ] The size of the frame | Incorrect. That is winfo_width.

    .. multichoice::

        Can a LabelFrame be clicked to run a function?

        [ ] Yes, with command | Incorrect. It has no command option.
        [x] No, it is only a container | Correct. Put a Button inside instead.
        [ ] Only if text is set | Incorrect. Still no.
        [ ] Only with relief="raised" | Incorrect. Still no.

    .. multichoice::

        What is the difference between a Frame and a LabelFrame?

        [ ] A LabelFrame cannot hold widgets | Incorrect. It can.
        [x] A LabelFrame has a border with a title | Correct. That is the main difference.
        [ ] A Frame has a title | Incorrect. Frames have no title.
        [ ] There is no difference | Incorrect. The title and border differ.

    .. multichoice::

        Which relief value gives a carved-in line border?

        [ ] "flat" | Incorrect. flat shows no border style.
        [ ] "raised" | Incorrect. raised sticks out.
        [x] "groove" | Correct. groove looks carved in.
        [ ] "solid" | Incorrect. solid is a plain line.

    .. multichoice::

        Inside one LabelFrame, which rule applies?

        [x] Use only pack or only grid for its widgets | Correct. Mixing them in one container can freeze the program.
        [ ] Use pack and grid together | Incorrect. That can freeze the program.
        [ ] Only use place | Incorrect. pack and grid work too.
        [ ] Do not use any layout | Incorrect. Widgets need a layout.

    .. multichoice::

        What does padx=10 add?

        [ ] 10 more widgets | Incorrect. It adds space.
        [ ] A border 10 pixels thick | Incorrect. borderwidth does that.
        [x] 10 pixels of space on the left and right inside | Correct. padx pads the sides.
        [ ] Ten characters to the title | Incorrect. It adds space.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a LabelFrame with a title.

        size_box = tk.@@LabelFrame | Label | Button@@(root, @@text | title | label@@="Size", padx=10, pady=10)
        size_box.pack(padx=10, pady=10)

    .. cloze::
        :instructions: Put radiobuttons inside the LabelFrame.

        size = tk.StringVar(value="Small")
        tk.Radiobutton(@@size_box | root | size@@, text="Small", variable=size, value="Small").pack(anchor="w")
        tk.Radiobutton(size_box, text="Large", @@variable | value | text@@=size, value="Large").pack(anchor="@@w | left | west@@")

    .. cloze::
        :instructions: Move and style the title.

        box = tk.LabelFrame(root, text="Settings", @@labelanchor | anchor | side@@="n", font=("Arial", 12, "bold"), @@fg | bg | colour@@="blue")
        box.pack()

    .. cloze::
        :instructions: Put two LabelFrames side by side.

        left_box.pack(@@side | fill | anchor@@="left", padx=10)
        right_box.pack(side="@@left | top | across@@", padx=10)

    .. cloze::
        :instructions: Change and read the title.

        box.@@config | cget | title@@(text="Options")
        title = box.@@cget | config | get@@("text")

----

.. admonition:: Tasks

    #. Make a window titled "Profile" that is 300x200. Add a LabelFrame with the title "About you" and padding of 10. Put a label "Name:" and an Entry inside it.
    #. Change your LabelFrame so the title is in the middle of the top border, in Arial size 14 bold, coloured purple.
    #. Make a LabelFrame titled "Favourite season" that holds four radiobuttons: "Summer", "Autumn", "Winter" and "Spring".
    #. Make two LabelFrames side by side titled "Home" and "Away", each with a label showing "0".

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
                    root.title("Profile")

                    about = tk.LabelFrame(root, text="About you", padx=10, pady=10)
                    about.pack(pady=20)

                    name_label = tk.Label(about, text="Name:")
                    name_label.pack()
                    name_entry = tk.Entry(about)
                    name_entry.pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Profile")

                    about = tk.LabelFrame(root, text="About you", padx=10, pady=10,
                                          labelanchor="n", font=("Arial", 14, "bold"), fg="purple")
                    about.pack(pady=20)

                    name_label = tk.Label(about, text="Name:")
                    name_label.pack()
                    name_entry = tk.Entry(about)
                    name_entry.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x250")
                    root.title("Seasons")

                    season_box = tk.LabelFrame(root, text="Favourite season", padx=10, pady=5)
                    season_box.pack(pady=10)

                    season = tk.StringVar(value="Summer")
                    for choice in ["Summer", "Autumn", "Winter", "Spring"]:
                        tk.Radiobutton(season_box, text=choice, variable=season,
                                       value=choice).pack(anchor="w")

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Scoreboard")

                    home = tk.LabelFrame(root, text="Home", padx=20, pady=10)
                    home.pack(side="left", padx=10, pady=20)
                    tk.Label(home, text="0", font=("Arial", 24)).pack()

                    away = tk.LabelFrame(root, text="Away", padx=20, pady=10)
                    away.pack(side="left", padx=10, pady=20)
                    tk.Label(away, text="0", font=("Arial", 24)).pack()

                    root.mainloop()
