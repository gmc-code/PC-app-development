====================================================
ttk LabelFrame
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk LabelFrame?
----------------------------

| A **ttk LabelFrame** is a frame with a border and a title, just like a tk LabelFrame.
| Use it to show which widgets belong together, e.g. "Your details" or "Choose a size".
| The title's font and colour are set with the ``"TLabelframe.Label"`` style.

----

Making a ttk LabelFrame
--------------------------

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk LabelFrame")

    details = ttk.LabelFrame(root, text="Your details", padding=10)   # 1. Create it
    details.pack(pady=20)                                             # 2. Place it

    ttk.Label(details, text="Name:").pack()          # 3. Widgets go in "details"
    ttk.Entry(details).pack()

    root.mainloop()                 # Keep the window open

----

ttk LabelFrame options
-------------------------

text
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the title shown in the border.
| **How to write it:** ``text="your title"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("text")

    settings = ttk.LabelFrame(root, text="Settings", padding=10)
    settings.pack(pady=20)

    sound = tk.IntVar()
    ttk.Checkbutton(settings, text="Sound on", variable=sound).pack()

    root.mainloop()

padding
~~~~~~~~~~~~~~~~~~

| **What it does:** adds space between the border and the widgets inside.
| **How to write it:** ``padding=15`` or ``padding=(30, 10)`` (left-right, top-bottom)

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("padding")

    squashed = ttk.LabelFrame(root, text="No padding")
    squashed.pack(pady=10)
    ttk.Button(squashed, text="Squashed").pack()

    roomy = ttk.LabelFrame(root, text="Padding", padding=(30, 15))
    roomy.pack(pady=10)
    ttk.Button(roomy, text="Roomy").pack()

    root.mainloop()

labelanchor
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses where the title sits on the border.
| **How to write it:** ``labelanchor="n"``
| **Values:** ``"nw"`` (top left, the default), ``"n"`` (top middle), ``"ne"``, ``"sw"``, ``"s"``, ``"se"``, and ``"w"``, ``"e"`` and others for the sides.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("labelanchor")

    centred = ttk.LabelFrame(root, text="Centred title", labelanchor="n", padding=15)
    centred.pack(pady=30)
    ttk.Label(centred, text="The title is in the middle").pack()

    root.mainloop()

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** change the style and thickness of the border.
| **How to write them:** ``relief="solid", borderwidth=2``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("relief")

    warning = ttk.LabelFrame(root, text="Warning", relief="solid", borderwidth=2, padding=10)
    warning.pack(pady=30)
    ttk.Label(warning, text="Save your work!").pack()

    root.mainloop()

width and height
~~~~~~~~~~~~~~~~~~

| **What they do:** set the size of an **empty** LabelFrame in pixels.
| **How to write them:** ``width=200, height=100``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and height")

    ttk.LabelFrame(root, text="Coming soon", width=200, height=100).pack(pady=30)

    root.mainloop()

----

Using ttk LabelFrames
------------------------

Grouping radiobuttons
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("Order")

    size_box = ttk.LabelFrame(root, text="Size", padding=10)
    size_box.pack(fill="x", padx=10, pady=5)

    size = tk.StringVar(value="Small")
    for choice in ["Small", "Medium", "Large"]:
        ttk.Radiobutton(size_box, text=choice, variable=size, value=choice).pack(anchor="w")

    drink_box = ttk.LabelFrame(root, text="Drink", padding=10)
    drink_box.pack(fill="x", padx=10, pady=5)

    drink = tk.StringVar(value="Water")
    for choice in ["Water", "Juice"]:
        ttk.Radiobutton(drink_box, text=choice, variable=drink, value=choice).pack(anchor="w")

    root.mainloop()

Side-by-side LabelFrames
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("350x200")
    root.title("Scoreboard")

    for team in ["Home", "Away"]:
        box = ttk.LabelFrame(root, text=team, padding=(30, 10))
        box.pack(side="left", padx=15, pady=30)
        ttk.Label(box, text="0", font=("Arial", 30)).pack()

    root.mainloop()

A form with grid
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Form")

    form = ttk.LabelFrame(root, text="Sign up", padding=10)
    form.pack(pady=20)

    ttk.Label(form, text="Name:").grid(row=0, column=0, sticky="e", pady=2)
    ttk.Entry(form).grid(row=0, column=1, pady=2)
    ttk.Label(form, text="Email:").grid(row=1, column=0, sticky="e", pady=2)
    ttk.Entry(form).grid(row=1, column=1, pady=2)

    root.mainloop()

----

ttk LabelFrame methods
-------------------------

config and cget
~~~~~~~~~~~~~~~~~~

| ``labelframe.config(text="New title")`` changes the title. ``labelframe.cget("text")`` reads it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def next_round():
        number = int(game_box.cget("text").replace("Round ", ""))
        game_box.config(text=f"Round {number + 1}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config and cget")

    game_box = ttk.LabelFrame(root, text="Round 1", padding=20)
    game_box.pack(pady=30)
    ttk.Button(game_box, text="Next round", command=next_round).pack()

    root.mainloop()

| ttk LabelFrames also have ``pack_forget()``, ``winfo_children()`` and ``destroy()``, the same as a **ttk Frame**.

----

Styling a ttk LabelFrame
---------------------------

| A ttk LabelFrame uses **two** styles:

- ``"TLabelframe"`` - the box: ``background``, ``bordercolor`` (with ``"clam"``), ``relief``, ``borderwidth``.
- ``"TLabelframe.Label"`` - the title: ``font``, ``foreground``, ``background``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x220")
    root.title("LabelFrame style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabelframe", background="lightyellow", bordercolor="orange")
    style.configure("TLabelframe.Label", font=("Arial", 14, "bold"), foreground="darkorange",
                    background="lightyellow")
    style.configure("TLabel", background="lightyellow")

    notes = ttk.LabelFrame(root, text="Notes", padding=15)
    notes.pack(pady=30)
    ttk.Label(notes, text="Bring a hat tomorrow").pack()

    root.mainloop()

Your own LabelFrame style
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| For a custom style, name **both** parts the same way: ``"Red.TLabelframe"`` and ``"Red.TLabelframe.Label"``, then use ``style="Red.TLabelframe"``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("350x200")
    root.title("Custom LabelFrame style")

    style = ttk.Style()
    style.configure("Red.TLabelframe.Label", foreground="red", font=("Arial", 13, "bold"))
    style.configure("Blue.TLabelframe.Label", foreground="blue", font=("Arial", 13, "bold"))

    red_team = ttk.LabelFrame(root, text="Red team", style="Red.TLabelframe", padding=15)
    red_team.pack(side="left", padx=20, pady=30)
    ttk.Label(red_team, text="Score: 0").pack()

    blue_team = ttk.LabelFrame(root, text="Blue team", style="Blue.TLabelframe", padding=15)
    blue_team.pack(side="left", padx=20, pady=30)
    ttk.Label(blue_team, text="Score: 0").pack()

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
    * - ``text``
      - Title in the border
      - ``text="Settings"``
    * - ``padding``
      - Space inside the border
      - ``padding=10``
    * - ``labelanchor``
      - Where the title sits
      - ``labelanchor="n"``
    * - ``relief``, ``borderwidth``
      - Border style and thickness
      - ``relief="solid", borderwidth=2``
    * - ``width``, ``height``
      - Size of an empty box
      - ``width=200, height=100``
    * - ``style``
      - Use a custom style
      - ``style="Red.TLabelframe"``
    * - ``config()``, ``cget()``
      - Change or read an option
      - ``box.config(text="New title")``
    * - ``"TLabelframe"``
      - Style name of the box
      - ``style.configure("TLabelframe", background="white")``
    * - ``"TLabelframe.Label"``
      - Style name of the title
      - ``style.configure("TLabelframe.Label", font=("Arial", 14))``

----

All LabelFrame options
---------------------------

| Here is every option a ttk LabelFrame can have, for reference. You will only need a few of them most of the time.

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
    * - ``labelanchor``
      - Where the title sits on the border (``"n"`` = top middle, ``"nw"`` = top left)
      - ``labelanchor="n"``
    * - ``labelwidget``
      - Uses another widget (like a Label) as the title
      - ``labelwidget=title_label``
    * - ``padding``
      - Extra space inside the box, around its widgets
      - ``padding=10``
    * - ``relief``
      - Border style: ``"raised"``, ``"sunken"``, ``"flat"``, ``"ridge"``, ``"groove"`` or ``"solid"``
      - ``relief="sunken"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TLabelframe"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``text``
      - Title shown on the border
      - ``text="Settings"``
    * - ``underline``
      - Number of the letter to underline (``0`` = first letter)
      - ``underline=0``
    * - ``width``
      - How wide it is (in pixels)
      - ``width=300``

| ttk LabelFrame has no ``bg``, ``fg`` or ``font`` options. Change its colours and fonts with a style, e.g. ``style.configure("TLabelframe", background="lightblue")``.

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

        What is a ttk LabelFrame?

        [x] A frame with a border and a title, using the ttk theme | Correct. It groups widgets under a heading.
        [ ] A label you can click | Incorrect. That is a Button.
        [ ] A window | Incorrect. Toplevel makes windows.
        [ ] A list | Incorrect. Listbox is a list.

    .. multichoice::

        How is it made?

        [ ] ttk.LabelFrame(root, title="Size") | Incorrect. The option is text.
        [x] ttk.LabelFrame(root, text="Size") | Correct. text sets the title.
        [ ] ttk.Labelframe(root, label="Size") | Incorrect. label is not the option.
        [ ] tk.Frame(root, text="Size") | Incorrect. A Frame has no title.

    .. multichoice::

        What does padding=10 do?

        [x] Adds space inside, between the border and the widgets | Correct. padding pads the inside.
        [ ] Moves the title | Incorrect. labelanchor does that.
        [ ] Makes the title bigger | Incorrect. A style does that.
        [ ] Adds space outside | Incorrect. pack does that.

    .. multichoice::

        What does labelanchor="n" do?

        [ ] Puts the title on the left | Incorrect. That is "w" or "nw".
        [x] Puts the title in the middle of the top border | Correct. n is the top middle.
        [ ] Puts the title at the bottom | Incorrect. That is "s".
        [ ] Hides the title | Incorrect. It moves it.

    .. multichoice::

        Which labelanchor puts the title at the top left?

        [x] "nw" | Correct. n is top, w is left.
        [ ] "ne" | Incorrect. That is top right.
        [ ] "sw" | Incorrect. That is bottom left.
        [ ] "w" | Incorrect. w is the left side, partway down.

    .. multichoice::

        What do relief and borderwidth change?

        [ ] The title font | Incorrect. A style does that.
        [x] The style and thickness of the border | Correct. relief is the style, borderwidth the thickness.
        [ ] The widgets inside | Incorrect. Only the border.
        [ ] The title text | Incorrect. text does that.

    .. multichoice::

        Why might width and height seem to be ignored?

        [x] The LabelFrame shrinks to fit its widgets when they are packed | Correct. Packing resizes it.
        [ ] They only work in tk | Incorrect. They work in ttk too.
        [ ] The numbers are too big | Incorrect. Not the reason.
        [ ] A style is needed | Incorrect. Not the reason.

    .. multichoice::

        How do you put a Radiobutton inside a LabelFrame called box?

        [ ] ttk.Radiobutton(root, ...) | Incorrect. That goes in the window.
        [x] ttk.Radiobutton(box, ...) | Correct. The parent comes first.
        [ ] box.add(radio) | Incorrect. Not a method.
        [ ] ttk.Radiobutton(..., parent=box) | Incorrect. Parent goes first.

    .. multichoice::

        Why group radiobuttons in a LabelFrame?

        [ ] So more than one can be chosen | Incorrect. They still share a variable.
        [x] To show they belong together under a heading | Correct. The title explains the group.
        [ ] They must be in one | Incorrect. They can go anywhere.
        [ ] To make them faster | Incorrect. Not why.

    .. multichoice::

        Which pack option puts LabelFrames side by side?

        [x] side="left" | Correct. side="left" lines them up across.
        [ ] fill="x" | Incorrect. fill stretches.
        [ ] anchor="n" | Incorrect. anchor does not line them up.
        [ ] expand=True | Incorrect. expand uses spare space.

    .. multichoice::

        Which layout makes neat rows of labels and entries in a form?

        [ ] pack only | Incorrect. pack stacks them.
        [x] grid with row and column | Correct. grid lines up rows and columns.
        [ ] place | Incorrect. place uses exact positions.
        [ ] No layout | Incorrect. Widgets need a layout.

    .. multichoice::

        Which line changes the title later?

        [ ] box.title("Options") | Incorrect. title is for windows.
        [x] box.config(text="Options") | Correct. config changes the text.
        [ ] box.set("Options") | Incorrect. Not a method.
        [ ] box.text = "Options" | Incorrect. Use config.

    .. multichoice::

        What does box.cget("text") give?

        [x] The current title | Correct. cget reads an option.
        [ ] The text of the widgets inside | Incorrect. Only its own title.
        [ ] An error | Incorrect. It works.
        [ ] The size | Incorrect. It reads the title.

    .. multichoice::

        Which style name is used for every ttk LabelFrame?

        [ ] "TLabelFrame" | Incorrect. The capital F is not used.
        [x] "TLabelframe" | Correct. The style name has a small f.
        [ ] "LabelFrame" | Incorrect. It needs the T.
        [ ] "TFrame" | Incorrect. That is for plain Frames.

    .. multichoice::

        How is the title of every LabelFrame styled?

        [ ] style.configure("TLabelframe", title_font=...) | Incorrect. Not the way.
        [x] style.configure("TLabelframe.Label", font=("Arial", 12, "bold")) | Correct. The title has its own style part.
        [ ] box.config(font=...) | Incorrect. ttk LabelFrame has no font option.
        [ ] style.configure("Title", ...) | Incorrect. Not the name.

    .. multichoice::

        How is your own LabelFrame style named?

        [x] Something like "Green.TLabelframe" | Correct. Custom names end with the class name.
        [ ] "TLabelframe.Green" | Incorrect. The class name goes last.
        [ ] "Green" | Incorrect. It needs the class name.
        [ ] "LabelframeGreen" | Incorrect. Use a dot and the class name.

    .. multichoice::

        How do you use your own style on one LabelFrame?

        [ ] box.style("Green.TLabelframe") | Incorrect. Not a method.
        [x] ttk.LabelFrame(root, text="Size", style="Green.TLabelframe") | Correct. Pass the style option.
        [ ] box.config(theme="Green") | Incorrect. Not an option.
        [ ] It is not possible | Incorrect. It is.

    .. multichoice::

        Inside one LabelFrame, which rule applies?

        [ ] Use pack and grid together | Incorrect. That can freeze the program.
        [x] Use only pack or only grid for its widgets | Correct. Do not mix them in one container.
        [ ] Only use place | Incorrect. pack and grid work.
        [ ] No layout is needed | Incorrect. A layout is needed.

    .. multichoice::

        What is the difference between ttk.Frame and ttk.LabelFrame?

        [x] LabelFrame has a border with a title | Correct. That is the main difference.
        [ ] Frame has a title | Incorrect. Frames have no title.
        [ ] LabelFrame cannot hold widgets | Incorrect. It can.
        [ ] There is no difference | Incorrect. The title differs.

    .. multichoice::

        Can a LabelFrame be clicked to run a function?

        [ ] Yes, with command | Incorrect. It has no command.
        [x] No, it is only a container | Correct. Put a Button inside.
        [ ] Only with a style | Incorrect. Still no.
        [ ] Only when disabled | Incorrect. Still no.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a ttk LabelFrame with a title.

        size_box = ttk.@@LabelFrame | Label | Frame@@(root, @@text | title | label@@="Size", @@padding | padx | space@@=10)
        size_box.pack(padx=10, pady=10)

    .. cloze::
        :instructions: Put radiobuttons inside it.

        ttk.Radiobutton(@@size_box | root | size@@, text="Small", variable=size, value="Small").pack(anchor="w")
        ttk.Radiobutton(size_box, text="Large", variable=size, @@value | variable | text@@="Large").pack(anchor="w")

    .. cloze::
        :instructions: Move the title and add a border.

        box = ttk.LabelFrame(root, text="Settings", @@labelanchor | anchor | side@@="n", relief="ridge", @@borderwidth | bd | border@@=3)

    .. cloze::
        :instructions: Style the title of every LabelFrame.

        style = ttk.Style()
        style.configure("@@TLabelframe.Label | TLabelFrame | Label@@", font=("Arial", 12, "bold"))

    .. cloze::
        :instructions: Change and read the title.

        box.@@config | cget | title@@(text="Options")
        title = box.@@cget | config | get@@("text")

----

.. admonition:: Tasks

    #. Make a window titled "Profile" that is 300x200 with a ttk LabelFrame "About you" and padding of 10. Put a ttk Label "Name:" and a ttk Entry inside it.
    #. Move the title to the middle of the top border.
    #. Make a ttk LabelFrame "Favourite season" holding four ttk Radiobuttons: "Summer", "Autumn", "Winter" and "Spring".
    #. Style every LabelFrame title in Arial size 14 bold, coloured purple.

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
                    root.title("Profile")

                    about = ttk.LabelFrame(root, text="About you", padding=10)
                    about.pack(pady=20)
                    ttk.Label(about, text="Name:").pack()
                    ttk.Entry(about).pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Profile")

                    about = ttk.LabelFrame(root, text="About you", padding=10, labelanchor="n")
                    about.pack(pady=20)
                    ttk.Label(about, text="Name:").pack()
                    ttk.Entry(about).pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x220")
                    root.title("Seasons")

                    season_box = ttk.LabelFrame(root, text="Favourite season", padding=10)
                    season_box.pack(pady=10)

                    season = tk.StringVar(value="Summer")
                    for choice in ["Summer", "Autumn", "Winter", "Spring"]:
                        ttk.Radiobutton(season_box, text=choice, variable=season,
                                        value=choice).pack(anchor="w")

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x220")
                    root.title("Seasons")

                    style = ttk.Style()
                    style.configure("TLabelframe.Label", font=("Arial", 14, "bold"), foreground="purple")

                    season_box = ttk.LabelFrame(root, text="Favourite season", padding=10)
                    season_box.pack(pady=10)

                    season = tk.StringVar(value="Summer")
                    for choice in ["Summer", "Autumn", "Winter", "Spring"]:
                        ttk.Radiobutton(season_box, text=choice, variable=season,
                                        value=choice).pack(anchor="w")

                    root.mainloop()
