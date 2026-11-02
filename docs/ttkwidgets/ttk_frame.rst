====================================================
ttk Frame
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk Frame?
-----------------------

| A **ttk Frame** is a box that holds and groups other widgets, just like a tk Frame.
| Frames are used to lay out a window, e.g. a row of buttons along the top and a main area underneath.
| A ttk Frame has no ``bg`` option. Its colour is set with the ``"TFrame"`` style.

----

Making a ttk Frame
---------------------

#. **Create** the frame with ``ttk.Frame(root)`` and **place** it with ``.pack()``.
#. **Put widgets in it.** Use the frame's name, not ``root``, as the first thing in the brackets.

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk Frame")

    box = ttk.Frame(root, padding=20, relief="solid", borderwidth=1)   # 1. Create the frame
    box.pack(pady=20)                                                  #    and place it

    ttk.Label(box, text="I am inside the frame").pack()     # 2. "box", not "root"
    ttk.Button(box, text="OK").pack(pady=5)

    root.mainloop()                 # Keep the window open

----

ttk Frame options
--------------------

padding
~~~~~~~~~~~~~~~~~~

| **What it does:** adds space **inside** the frame, between its edge and the widgets.
| **How to write it:** ``padding=20`` (all sides), ``padding=(30, 10)`` (left-right, top-bottom) or ``padding=(left, top, right, bottom)``
| A ttk Frame uses ``padding`` instead of ``padx`` and ``pady``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("padding")

    padded = ttk.Frame(root, padding=(40, 20), relief="solid", borderwidth=1)
    padded.pack(pady=30)
    ttk.Label(padded, text="Lots of space around me").pack()

    root.mainloop()

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** draw a border around the frame.
| **How to write them:** ``relief="groove", borderwidth=3``
| **Styles:** ``"flat"`` (no border, the default), ``"solid"``, ``"raised"``, ``"sunken"``, ``"groove"``, ``"ridge"``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("relief")

    for style_name in ["solid", "raised", "sunken", "groove"]:
        frame = ttk.Frame(root, relief=style_name, borderwidth=3, padding=5)
        frame.pack(pady=4)
        ttk.Label(frame, text=style_name, width=12).pack()

    root.mainloop()

width and height
~~~~~~~~~~~~~~~~~~

| **What they do:** set the size of an **empty** frame in pixels.
| **How to write them:** ``width=200, height=100``
| Once widgets are inside, the frame shrinks or grows to fit them.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and height")

    empty = ttk.Frame(root, width=200, height=100, relief="solid", borderwidth=2)
    empty.pack(pady=40)

    root.mainloop()

style (colour)
~~~~~~~~~~~~~~~~~

| **What it does:** sets the colour of the frame. Use ``style.configure`` with ``background``.
| **How to write it:** ``style.configure("Blue.TFrame", background="lightblue")`` then ``style="Blue.TFrame"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Frame colour")

    style = ttk.Style()
    style.configure("Blue.TFrame", background="lightblue")
    style.configure("Blue.TLabel", background="lightblue")      # Label to match

    blue_box = ttk.Frame(root, style="Blue.TFrame", padding=20)
    blue_box.pack(pady=40)
    ttk.Label(blue_box, text="A blue frame", style="Blue.TLabel").pack()

    root.mainloop()

| Widgets inside a coloured frame keep their own colour, so give them a matching style.

----

Laying out a window with frames
-----------------------------------

side, fill and expand
~~~~~~~~~~~~~~~~~~~~~~~~

| ``pack(side="left")`` puts widgets side by side. ``fill="x"`` stretches across, ``fill="both", expand=True`` uses all the space left.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("400x250")
    root.title("Layout")

    style = ttk.Style()
    style.configure("Top.TFrame", background="navy")
    style.configure("Side.TFrame", background="lightsteelblue")
    style.configure("Main.TFrame", background="white")
    style.configure("Top.TLabel", background="navy", foreground="white", font=("Arial", 18))

    top = ttk.Frame(root, style="Top.TFrame", padding=5)
    top.pack(fill="x")
    ttk.Label(top, text="Science Quiz", style="Top.TLabel").pack()

    side = ttk.Frame(root, style="Side.TFrame", padding=10)
    side.pack(side="left", fill="y")
    ttk.Button(side, text="Start", width=10).pack(pady=5)
    ttk.Button(side, text="Scores", width=10).pack(pady=5)

    main = ttk.Frame(root, style="Main.TFrame")
    main.pack(side="left", fill="both", expand=True)

    root.mainloop()

A row of buttons
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Button row")

    button_row = ttk.Frame(root)
    button_row.pack(pady=30)

    for word in ["Back", "Home", "Next"]:
        ttk.Button(button_row, text=word, width=8).pack(side="left", padx=5)

    root.mainloop()

Using grid inside a frame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Each frame can use its own layout: ``grid`` in one frame and ``pack`` in another. Do **not** mix ``pack`` and ``grid`` inside the **same** frame.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("grid in a frame")

    ttk.Label(root, text="Sign up", font=("Arial", 16)).pack(pady=10)

    form = ttk.Frame(root, padding=10)
    form.pack()

    ttk.Label(form, text="Name:").grid(row=0, column=0, sticky="e", pady=2)
    ttk.Entry(form).grid(row=0, column=1, pady=2)
    ttk.Label(form, text="Email:").grid(row=1, column=0, sticky="e", pady=2)
    ttk.Entry(form).grid(row=1, column=1, pady=2)

    root.mainloop()

----

ttk Frame methods
--------------------

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options after the frame has been made, e.g. swapping its style to change colour.
| **How to write it:** ``frame.config(style="Red.TFrame")``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def light_on():
        room.config(style="On.TFrame")


    def light_off():
        room.config(style="Off.TFrame")


    root = tk.Tk()
    root.geometry("300x220")
    root.title("config")

    style = ttk.Style()
    style.configure("On.TFrame", background="yellow")
    style.configure("Off.TFrame", background="black")

    room = ttk.Frame(root, width=200, height=100, style="Off.TFrame")
    room.pack(pady=10)

    ttk.Button(root, text="Light on", command=light_on).pack()
    ttk.Button(root, text="Light off", command=light_off).pack()

    root.mainloop()

pack_forget
~~~~~~~~~~~~~~~~~~

| **What it does:** hides a frame and everything in it. ``pack()`` shows it again. This is a simple way to swap "screens".

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def show_answer():
        question_frame.pack_forget()
        answer_frame.pack(pady=30)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("pack_forget")

    question_frame = ttk.Frame(root)
    question_frame.pack(pady=30)
    ttk.Label(question_frame, text="What is the largest planet?").pack()
    ttk.Button(question_frame, text="Show answer", command=show_answer).pack(pady=5)

    answer_frame = ttk.Frame(root)          # Not packed yet, so hidden
    ttk.Label(answer_frame, text="Jupiter!", font=("Arial", 24)).pack()

    root.mainloop()

winfo_children and destroy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``frame.winfo_children()`` gives a list of the widgets inside. ``frame.destroy()`` deletes the frame and everything in it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def game_over():
        for widget in controls.winfo_children():
            widget.state(["disabled"])


    root = tk.Tk()
    root.geometry("300x220")
    root.title("winfo_children")

    controls = ttk.Frame(root, padding=10)
    controls.pack()
    for word in ["Up", "Down", "Left", "Right"]:
        ttk.Button(controls, text=word).pack()

    ttk.Button(root, text="Game over", command=game_over).pack(pady=5)
    ttk.Button(root, text="Remove controls", command=controls.destroy).pack()

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
    * - ``ttk.Label(frame, ...)``
      - Put a widget inside the frame
      - ``ttk.Button(box, text="OK")``
    * - ``padding``
      - Space inside the frame
      - ``padding=20``
    * - ``relief``, ``borderwidth``
      - Border style and thickness
      - ``relief="groove", borderwidth=3``
    * - ``width``, ``height``
      - Size of an empty frame
      - ``width=200, height=100``
    * - ``style``
      - Use a style (e.g. for colour)
      - ``style="Blue.TFrame"``
    * - ``pack(side=, fill=, expand=)``
      - Lay out frames
      - ``pack(fill="both", expand=True)``
    * - ``config()``
      - Change options later
      - ``frame.config(style="On.TFrame")``
    * - ``pack_forget()``
      - Hide the frame
      - ``frame.pack_forget()``
    * - ``winfo_children()``
      - List the widgets inside
      - ``frame.winfo_children()``
    * - ``destroy()``
      - Delete the frame
      - ``frame.destroy()``
    * - ``"TFrame"``
      - Style name; use ``background`` for colour
      - ``style.configure("TFrame", background="white")``

----

All Frame options
---------------------------

| Here is every option a ttk Frame can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``borderwidth``
      - How thick the border is (write ``borderwidth``, not ``bd``)
      - ``borderwidth=3``
    * - ``class_``
      - A group name used to style many widgets at once (advanced). Written ``class_`` in Python
      - ``class_="Sidebar"``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``height``
      - How tall it is (in pixels)
      - ``height=200``
    * - ``padding``
      - Extra space inside the frame, around its widgets
      - ``padding=10``
    * - ``relief``
      - Border style: ``"raised"``, ``"sunken"``, ``"flat"``, ``"ridge"``, ``"groove"`` or ``"solid"``
      - ``relief="sunken"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TFrame"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``width``
      - How wide it is (in pixels)
      - ``width=300``

| ttk Frame has no ``bg``, ``fg`` or ``font`` options. Change its colours and fonts with a style, e.g. ``style.configure("TFrame", background="lightblue")``.

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

        What is a ttk Frame?

        [x] A container for grouping widgets that uses the ttk theme | Correct. It works like a tk Frame.
        [ ] A picture frame | Incorrect. It is a container.
        [ ] A window | Incorrect. Toplevel makes windows.
        [ ] A button | Incorrect. It is a container.

    .. multichoice::

        Why does ttk.Frame(root, bg="blue") cause an error?

        [ ] Blue is not allowed | Incorrect. ttk Frames have no bg option.
        [x] ttk widgets do not have bg; colours come from a style | Correct. Use style.configure("TFrame", background=...).
        [ ] Frames cannot be blue | Incorrect. They can with a style.
        [ ] Frames need a size | Incorrect. Not the error.

    .. multichoice::

        What does padding=10 do?

        [x] Adds 10 pixels of space inside the frame around its widgets | Correct. padding pads the inside.
        [ ] Adds space outside | Incorrect. pack does that.
        [ ] Makes 10 frames | Incorrect. It adds space.
        [ ] Moves the frame | Incorrect. It adds space.

    .. multichoice::

        What does padding=(10, 5) mean?

        [ ] 10 pixels on top, 5 on the left | Incorrect. Two numbers mean left and right, then top and bottom.
        [x] 10 pixels left and right, 5 pixels top and bottom | Correct. The first is across, the second is up and down.
        [ ] 10 by 5 frame | Incorrect. It is padding, not size.
        [ ] An error | Incorrect. It is allowed.

    .. multichoice::

        Which pair gives a ttk Frame a border?

        [ ] fg and bg | Incorrect. ttk has neither.
        [x] relief and borderwidth | Correct. relief is the style, borderwidth the thickness.
        [ ] width and height | Incorrect. These are sizes.
        [ ] padding and style | Incorrect. padding adds space.

    .. multichoice::

        For a ttk Frame, width=300 is measured in:

        [x] Pixels | Correct. Frame size is in pixels.
        [ ] Characters | Incorrect. Frames do not hold text.
        [ ] Lines | Incorrect. Not lines.
        [ ] Centimetres | Incorrect. Not used.

    .. multichoice::

        Which line colours every ttk Frame light blue?

        [ ] frame.config(bg="lightblue") | Incorrect. ttk has no bg.
        [x] style.configure("TFrame", background="lightblue") | Correct. TFrame is the style for all frames.
        [ ] style.configure("Frame", bg="lightblue") | Incorrect. Use TFrame and background.
        [ ] frame.colour("lightblue") | Incorrect. Not a method.

    .. multichoice::

        How do you colour only one frame?

        [x] Make a style like "Blue.TFrame" and use style="Blue.TFrame" | Correct. Custom styles affect only the widgets that use them.
        [ ] Use TFrame | Incorrect. That changes every frame.
        [ ] Use bg | Incorrect. ttk has no bg.
        [ ] It is not possible | Incorrect. It is, with a style.

    .. multichoice::

        What does side="left" do in frame.pack(side="left")?

        [ ] Lines up the widgets inside | Incorrect. It places the frame.
        [x] Puts the frame against the left, so frames sit side by side | Correct. side sets where it packs.
        [ ] Moves the words | Incorrect. Frames have no words.
        [ ] Stretches the frame | Incorrect. fill does that.

    .. multichoice::

        What does fill="both" with expand=True do?

        [x] Lets the frame stretch to fill spare space in both directions | Correct. It grows with the window.
        [ ] Fills the frame with colour | Incorrect. Use a style for colour.
        [ ] Adds both widgets | Incorrect. It is about space.
        [ ] Hides the frame | Incorrect. It stretches it.

    .. multichoice::

        Why put a row of buttons in a frame?

        [ ] Buttons must be in a frame | Incorrect. They can go anywhere.
        [x] So they can be packed side by side as one group | Correct. The frame holds the row.
        [ ] To colour the buttons | Incorrect. Not why.
        [ ] To make them faster | Incorrect. Not why.

    .. multichoice::

        Can grid be used inside a frame packed into root?

        [x] Yes, each container can use its own layout | Correct. Do not mix them in the same container.
        [ ] No | Incorrect. Different containers can use different layouts.
        [ ] Only with tk frames | Incorrect. ttk works too.
        [ ] Only if the frame has a style | Incorrect. Not needed.

    .. multichoice::

        Which line changes the padding later?

        [ ] frame.padding(20) | Incorrect. Not a method.
        [x] frame.config(padding=20) | Correct. config changes options.
        [ ] frame.set(padding=20) | Incorrect. Not a method.
        [ ] style.padding(20) | Incorrect. Not how it works.

    .. multichoice::

        What does frame.pack_forget() do?

        [x] Hides the frame so it can be packed again later | Correct. It is not deleted.
        [ ] Deletes it | Incorrect. destroy deletes.
        [ ] Clears its widgets | Incorrect. It hides the frame.
        [ ] Moves it left | Incorrect. It hides it.

    .. multichoice::

        How do you remove every widget inside a frame?

        [ ] frame.clear() | Incorrect. Not a method.
        [x] Loop through frame.winfo_children() and destroy each one | Correct. Each child is removed.
        [ ] frame.delete("all") | Incorrect. That is for Canvas.
        [ ] frame.pack_forget() | Incorrect. That hides the frame itself.

    .. multichoice::

        What does winfo_children() give?

        [ ] The frame size | Incorrect. It lists widgets.
        [x] A list of the widgets inside | Correct. They are its children.
        [ ] The parent | Incorrect. It lists children.
        [ ] The style | Incorrect. It lists widgets.

    .. multichoice::

        What does relief="sunken" make the border look like?

        [x] Pushed in | Correct. sunken looks pressed into the window.
        [ ] Raised | Incorrect. That is "raised".
        [ ] Invisible | Incorrect. That is "flat".
        [ ] Dotted | Incorrect. Not a relief.

    .. multichoice::

        What must be set for relief to show on a ttk Frame?

        [ ] A colour | Incorrect. Not needed.
        [x] A borderwidth bigger than 0 | Correct. With no border, there is nothing to show.
        [ ] padding | Incorrect. Not needed.
        [ ] A width | Incorrect. Not needed.

    .. multichoice::

        Which style name is used for every ttk Frame?

        [ ] "Frame" | Incorrect. Use TFrame.
        [x] "TFrame" | Correct. T then the widget name.
        [ ] "TBox" | Incorrect. Not the name.
        [ ] "Container" | Incorrect. Not the name.

    .. multichoice::

        Which is a good reason to use frames?

        [x] To split the window into parts, like a header and a body | Correct. Frames group related widgets.
        [ ] To make the program faster | Incorrect. Not about speed.
        [ ] To change fonts | Incorrect. Styles do that.
        [ ] Because pack needs them | Incorrect. pack works without frames.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a ttk Frame with padding and a border.

        box = ttk.@@Frame | Label | Style@@(root, @@padding | padx | space@@=10, relief="groove", @@borderwidth | bd | border@@=2)
        box.pack(fill="x")

    .. cloze::
        :instructions: Colour every frame.

        style = ttk.@@Style | style | Theme@@()
        style.configure("@@TFrame | Frame | ttkFrame@@", @@background | bg | colour@@="lightblue")

    .. cloze::
        :instructions: Colour only one frame.

        style.configure("Blue.TFrame", background="lightblue")
        side_bar = ttk.Frame(root, @@style | theme | colour@@="Blue.TFrame", width=150)

    .. cloze::
        :instructions: Put buttons in a row.

        button_row = ttk.Frame(root)
        button_row.pack()
        ttk.Button(@@button_row | root | box@@, text="Back").pack(side="@@left | top | row@@")

    .. cloze::
        :instructions: Hide and clear a frame.

        box.@@pack_forget | destroy | hide@@()
        for widget in box.@@winfo_children | children | widgets@@():
            widget.@@destroy | forget | remove@@()

----

.. admonition:: Tasks

    #. Make a window titled "Frames" that is 300x200. Add a ttk Frame with padding of 20 and a solid border. Put a label "Hello" inside it.
    #. Make a ttk Frame that holds three ttk Buttons, "Red", "Green" and "Blue", side by side.
    #. Make a ``"Pink.TFrame"`` style with a pink background and use it on a frame that is 200 wide and 100 high.
    #. Make a "start" frame with a "Start" button and a "game" frame with the label "Game started!". When "Start" is clicked, hide the start frame and show the game frame.

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
                    root.title("Frames")

                    box = ttk.Frame(root, padding=20, relief="solid", borderwidth=1)
                    box.pack(pady=20)
                    ttk.Label(box, text="Hello").pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Frames")

                    row = ttk.Frame(root)
                    row.pack(pady=20)
                    for colour in ["Red", "Green", "Blue"]:
                        ttk.Button(row, text=colour).pack(side="left", padx=5)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Frames")

                    style = ttk.Style()
                    style.configure("Pink.TFrame", background="pink")

                    pink_box = ttk.Frame(root, width=200, height=100, style="Pink.TFrame")
                    pink_box.pack(pady=40)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def start():
                        start_frame.pack_forget()
                        game_frame.pack(pady=30)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Game")

                    start_frame = ttk.Frame(root)
                    start_frame.pack(pady=30)
                    ttk.Button(start_frame, text="Start", command=start).pack()

                    game_frame = ttk.Frame(root)
                    ttk.Label(game_frame, text="Game started!", font=("Arial", 18)).pack()

                    root.mainloop()
