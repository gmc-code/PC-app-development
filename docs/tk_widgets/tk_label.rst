====================================================
tk Label
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Label>`_

----

What is a Label?
-------------------

| A **Label** shows words (or a picture) in a window.
| The user can read a label but cannot type into it.
| Labels are used for titles, instructions, questions and for showing answers.

----

Making a Label
-------------------

| Every Label is made in two steps:

#. **Create** the label with ``tk.Label(...)``.
#. **Place** the label in the window with ``.pack()``. A label you do not pack will not appear.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first label")    # Words in the title bar

    label = tk.Label(root, text="Hello, world!")   # 1. Create the label
    label.pack()                                    # 2. Place it in the window

    root.mainloop()                 # Keep the window open

| ``root`` is the window. It goes first inside the brackets so Python knows **where** the label belongs.
| Everything after ``root,`` is an **option**. Options change how the label looks. Separate options with commas.

----

Label options
-------------------

| Options are written as ``option=value`` inside ``tk.Label( )``.
| You can use as many options as you like, in any order.

text
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the words shown on the label.
| **How to write it:** ``text="your words"``
| Use ``\n`` inside the words to start a new line.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("text")

    label = tk.Label(root, text="Line one\nLine two")
    label.pack()

    root.mainloop()

font
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the style and size of the letters.
| **How to write it:** ``font=("font name", size)`` or ``font=("font name", size, "style")``
| **Styles you can use:** ``"bold"``, ``"italic"``, ``"underline"``, or more than one, e.g. ``"bold italic"``.
| Common font names: ``"Arial"``, ``"Comic Sans MS"``, ``"Times New Roman"``, ``"Courier New"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("font")

    label_1 = tk.Label(root, text="Arial size 24", font=("Arial", 24))
    label_1.pack()

    label_2 = tk.Label(root, text="Bold and italic", font=("Arial", 18, "bold italic"))
    label_2.pack()

    root.mainloop()

fg (text colour)
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the colour of the letters. ``fg`` is short for **foreground**.
| **How to write it:** ``fg="colour"``
| Use a colour name such as ``"red"``, ``"blue"``, ``"dark green"``, or a hex code such as ``"#0000FF"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("fg")

    label = tk.Label(root, text="Blue words", font=("Arial", 24), fg="blue")
    label.pack()

    root.mainloop()

bg (background colour)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What it does:** sets the colour behind the words. ``bg`` is short for **background**.
| **How to write it:** ``bg="colour"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("bg")

    label = tk.Label(root, text="Yellow background", font=("Arial", 18), bg="yellow")
    label.pack()

    root.mainloop()

width and height
~~~~~~~~~~~~~~~~~~

| **What they do:** set the size of the label.
| ``width`` is measured in **characters** (letters), and ``height`` in **lines** of text.
| **How to write them:** ``width=20``, ``height=3``
| If you leave them out, the label is just big enough to fit its words.
| Give the label a ``bg`` colour so you can see how big it is.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and height")

    label = tk.Label(root, text="Big label", bg="lightblue", width=20, height=3)
    label.pack()

    root.mainloop()

padx and pady
~~~~~~~~~~~~~~~~~~

| **What they do:** add empty space around the words, **inside** the label.
| ``padx`` adds space on the left and right. ``pady`` adds space on the top and bottom.
| **How to write them:** ``padx=20``, ``pady=10`` (measured in pixels)

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("padx and pady")

    label = tk.Label(root, text="Padded", font=("Arial", 18), bg="lightgreen", padx=40, pady=20)
    label.pack()

    root.mainloop()

.. note::

    ``.pack()`` can also have ``padx`` and ``pady``. Those add space **outside** the label,
    pushing it away from other widgets and the edge of the window, e.g. ``label.pack(pady=20)``.

anchor
~~~~~~~~~~~~~~~~~~

| **What it does:** moves the words to a side or corner of the label.
| **How to write it:** ``anchor="position"``
| **Positions:** compass directions ``"n"`` (top), ``"s"`` (bottom), ``"e"`` (right), ``"w"`` (left), ``"ne"``, ``"nw"``, ``"se"``, ``"sw"`` and ``"center"`` (the default).
| The label must be bigger than its words (use ``width`` and ``height``), or there is no room to move them.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("anchor")

    label_1 = tk.Label(root, text="top left", bg="lightyellow", width=25, height=3, anchor="nw")
    label_1.pack(pady=5)

    label_2 = tk.Label(root, text="middle", bg="lightyellow", width=25, height=3, anchor="center")
    label_2.pack(pady=5)

    label_3 = tk.Label(root, text="bottom right", bg="lightyellow", width=25, height=3, anchor="se")
    label_3.pack(pady=5)

    root.mainloop()

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** draw a border around the label.
| ``relief`` is the style of the border. ``borderwidth`` is how thick it is in pixels.
| **How to write them:** ``relief="solid", borderwidth=2``
| **Styles:** ``"flat"`` (no border, the default), ``"solid"``, ``"raised"``, ``"sunken"``, ``"groove"``, ``"ridge"``.
| A border only shows if ``borderwidth`` is 1 or more.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x300")
    root.title("relief")

    for style in ["flat", "solid", "raised", "sunken", "groove", "ridge"]:
        label = tk.Label(root, text=style, width=15, relief=style, borderwidth=3)
        label.pack(pady=5)

    root.mainloop()

wraplength and justify
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``wraplength`` makes long text wrap onto the next line. ``justify`` lines up the wrapped lines.
| **How to write them:** ``wraplength=200`` (pixels), ``justify="left"``
| **justify values:** ``"left"``, ``"center"`` (the default), ``"right"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("wraplength")

    label = tk.Label(
        root,
        text="This is a long sentence that will not fit on one line, so it wraps.",
        font=("Arial", 14),
        wraplength=200,
        justify="left",
    )
    label.pack(pady=20)

    root.mainloop()

image
~~~~~~~~~~~~~~~~~~

| **What it does:** shows a picture in the label.
| **How to write it:** first load the picture with ``tk.PhotoImage(file="name.png")``, then use ``image=picture``.
| The picture must be a **.png** or **.gif** file saved in the **same folder** as your Python file.
| Add ``compound="top"`` to show the picture **and** the text. Other values: ``"bottom"``, ``"left"``, ``"right"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("image")

    picture = tk.PhotoImage(file="logo.png")    # Load the picture

    label = tk.Label(root, image=picture, text="Our logo", compound="top")
    label.pack(pady=20)

    root.mainloop()

textvariable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the label to a **StringVar**, a special Tkinter variable that stores text.
| When the StringVar changes, the label changes by itself.
| **How to write it:** ``message = tk.StringVar(value="start text")`` then ``textvariable=message``
| Change the text with ``message.set("new text")``. Read it with ``message.get()``.

.. code-block:: python

    import tkinter as tk


    def win():
        message.set("You win!")     # The label updates by itself


    root = tk.Tk()
    root.geometry("300x200")
    root.title("textvariable")

    message = tk.StringVar(value="Click the button")

    label = tk.Label(root, textvariable=message, font=("Arial", 18))
    label.pack(pady=20)

    button = tk.Button(root, text="Play", command=win)
    button.pack()

    root.mainloop()

----

Label methods
-------------------

| A **method** is an action that a widget can do. Methods are written after a dot, e.g. ``label.config(...)``.
| Label methods are used to change a label **while the program is running**, e.g. to show an answer.

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes one or more options **after** the label has been made.
| **How to write it:** ``label.config(option=value)``
| Any option from the list above can be changed this way.

.. code-block:: python

    import tkinter as tk


    def change():
        label.config(text="Changed!", fg="white", bg="green")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    label = tk.Label(root, text="Not changed yet", font=("Arial", 18), bg="lightgray")
    label.pack(pady=20)

    button = tk.Button(root, text="Change the label", command=change)
    button.pack()

    root.mainloop()

| You may also see a shorter way to change one option: ``label["text"] = "Changed!"``

cget
~~~~~~~~~~~~~~~~~~

| **What it does:** reads (gets) the current value of an option.
| **How to write it:** ``value = label.cget("option")``
| The text from a label is always a **string**. Use ``int()`` to turn it into a number before doing maths.

.. code-block:: python

    import tkinter as tk


    def add_one():
        number = int(label.cget("text"))    # Read the label and turn it into a number
        label.config(text=number + 1)       # Show the new number


    root = tk.Tk()
    root.geometry("300x200")
    root.title("cget")

    label = tk.Label(root, text="0", font=("Arial", 40))
    label.pack(pady=20)

    button = tk.Button(root, text="Add 1", command=add_one)
    button.pack()

    root.mainloop()

----

Options quick reference
---------------------------

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``text``
      - Words shown on the label
      - ``text="Hello"``
    * - ``font``
      - Font name, size and style
      - ``font=("Arial", 16, "bold")``
    * - ``fg``
      - Colour of the words
      - ``fg="blue"``
    * - ``bg``
      - Colour behind the words
      - ``bg="yellow"``
    * - ``width``
      - Width in characters
      - ``width=20``
    * - ``height``
      - Height in lines
      - ``height=2``
    * - ``padx``, ``pady``
      - Space inside the label around the words
      - ``padx=10, pady=5``
    * - ``anchor``
      - Where the words sit inside the label
      - ``anchor="w"``
    * - ``relief``
      - Border style
      - ``relief="solid"``
    * - ``borderwidth``
      - Border thickness in pixels
      - ``borderwidth=2``
    * - ``wraplength``
      - Wrap text longer than this many pixels
      - ``wraplength=200``
    * - ``justify``
      - Line up wrapped lines
      - ``justify="left"``
    * - ``image``
      - Show a picture
      - ``image=picture``
    * - ``textvariable``
      - Link the label to a StringVar
      - ``textvariable=message``

----

All Label options
---------------------------

| Here is every option a Label can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``activebackground``
      - Background colour when ``state="active"``
      - ``activebackground="lightblue"``
    * - ``activeforeground``
      - Word colour when ``state="active"``
      - ``activeforeground="red"``
    * - ``anchor``
      - Where the words sit inside it (``"w"`` = left, ``"center"`` = middle)
      - ``anchor="w"``
    * - ``bg`` or ``background``
      - Background colour
      - ``bg="lavender"``
    * - ``bitmap``
      - Shows a small built-in picture
      - ``bitmap="question"``
    * - ``bd`` or ``borderwidth``
      - How thick the border is
      - ``bd=3``
    * - ``compound``
      - Where the picture goes compared to the words
      - ``compound="left"``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``disabledforeground``
      - Word colour when it is turned off
      - ``disabledforeground="grey"``
    * - ``font``
      - Style and size of the words
      - ``font=("Arial", 14)``
    * - ``fg`` or ``foreground``
      - Word colour
      - ``fg="purple"``
    * - ``height``
      - How tall it is (in lines of text)
      - ``height=2``
    * - ``highlightbackground``
      - Colour of the focus outline when it is not selected by the keyboard
      - ``highlightbackground="white"``
    * - ``highlightcolor``
      - Colour of the focus outline when it is selected by the keyboard
      - ``highlightcolor="blue"``
    * - ``highlightthickness``
      - How thick the focus outline is
      - ``highlightthickness=2``
    * - ``image``
      - Shows a picture instead of (or with) the words
      - ``image=dog_picture``
    * - ``justify``
      - Lines up many lines of words: ``"left"``, ``"center"`` or ``"right"``
      - ``justify="left"``
    * - ``padx``
      - Extra space on the left and right of the words
      - ``padx=10``
    * - ``pady``
      - Extra space above and below the words
      - ``pady=5``
    * - ``relief``
      - Border style: ``"raised"``, ``"sunken"``, ``"flat"``, ``"ridge"``, ``"groove"`` or ``"solid"``
      - ``relief="sunken"``
    * - ``state``
      - ``"normal"``, ``"active"`` or ``"disabled"`` (greyed out)
      - ``state="disabled"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``text``
      - Words shown on the label
      - ``text="Hello"``
    * - ``textvariable``
      - A variable that holds the words, so they can change
      - ``textvariable=label_words``
    * - ``underline``
      - Number of the letter to underline (``0`` = first letter)
      - ``underline=0``
    * - ``width``
      - How wide it is (in characters)
      - ``width=15``
    * - ``wraplength``
      - Starts a new line when the words get this long (in pixels)
      - ``wraplength=100``

| The picture option (``image``) needs a picture made first, e.g. ``dog_picture = tk.PhotoImage(file="dog.png")``.

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

        What is a Label used for?

        [x] Showing text or a picture | Correct. Labels display information.
        [ ] Typing text | Incorrect. An Entry is for typing.
        [ ] Running a function when clicked | Incorrect. A Button does that.
        [ ] Choosing from a list | Incorrect. A Listbox or OptionMenu does that.

    .. multichoice::

        Which option sets the words on a label?

        [ ] words | Incorrect. words is not an option.
        [x] text | Correct. text sets the words.
        [ ] label | Incorrect. label is not an option.
        [ ] value | Incorrect. value is not a Label option.

    .. multichoice::

        What does font=("Arial", 20, "bold") make?

        [x] Bold Arial text, size 20 | Correct. Name, size, then style.
        [ ] Arial text in 20 colours | Incorrect. 20 is the size.
        [ ] A label 20 characters wide | Incorrect. width sets that.
        [ ] Italic text | Incorrect. "italic" would make it italic.

    .. multichoice::

        Which option changes the colour of the words?

        [ ] bg | Incorrect. bg is the background.
        [ ] colour | Incorrect. colour is not an option.
        [x] fg | Correct. fg is the foreground (word) colour.
        [ ] text | Incorrect. text sets the words.

    .. multichoice::

        What does bg="yellow" do on a label?

        [ ] Makes the words yellow | Incorrect. fg makes the words yellow.
        [x] Makes the label's background yellow | Correct. bg is the background colour.
        [ ] Makes the window yellow | Incorrect. Only the label changes.
        [ ] Nothing | Incorrect. Labels have a background.

    .. multichoice::

        For a text label, what does width=20 mean?

        [ ] 20 pixels | Incorrect. With text, width is in characters.
        [x] About 20 characters wide | Correct. Text labels count characters.
        [ ] 20 lines | Incorrect. height counts lines.
        [ ] 20 labels | Incorrect. It sets one label's width.

    .. multichoice::

        What does height=3 mean on a text label?

        [x] 3 lines of text tall | Correct. height counts lines for text labels.
        [ ] 3 pixels tall | Incorrect. It counts lines, not pixels.
        [ ] 3 labels | Incorrect. It sets one label.
        [ ] 3 characters | Incorrect. width counts characters.

    .. multichoice::

        What do padx and pady do?

        [ ] Move the label | Incorrect. pack and grid place it.
        [x] Add space inside the label around the words | Correct. They make the label bigger around its text.
        [ ] Change the font | Incorrect. font does that.
        [ ] Add a border | Incorrect. relief does that.

    .. multichoice::

        What does anchor="w" do in a wide label?

        [ ] Moves the window west | Incorrect. It only affects the label.
        [x] Puts the words on the left side of the label | Correct. w means west, the left.
        [ ] Puts the words on the right | Incorrect. That would be "e".
        [ ] Makes the words bold | Incorrect. font does that.

    .. multichoice::

        Which anchor value puts the words at the top right?

        [ ] "nw" | Incorrect. nw is top left.
        [ ] "se" | Incorrect. se is bottom right.
        [x] "ne" | Correct. n is top and e is right.
        [ ] "sw" | Incorrect. sw is bottom left.

    .. multichoice::

        What does relief="ridge" with borderwidth=3 do?

        [x] Adds a raised-edge border 3 pixels thick | Correct. relief sets the style and borderwidth the thickness.
        [ ] Makes the words 3 times bigger | Incorrect. font does that.
        [ ] Adds 3 lines | Incorrect. It adds a border.
        [ ] Hides the label | Incorrect. It is still shown.

    .. multichoice::

        What does wraplength=150 do?

        [ ] Makes the label 150 characters wide | Incorrect. width does that.
        [x] Starts a new line when the words reach 150 pixels | Correct. wraplength wraps long text.
        [ ] Shows only 150 letters | Incorrect. All the text still shows.
        [ ] Sets the font size | Incorrect. font does that.

    .. multichoice::

        What does justify="left" do?

        [ ] Moves the label to the left | Incorrect. pack or grid move it.
        [x] Lines up several lines of words on the left | Correct. justify lines up wrapped lines.
        [ ] Puts one word on the left | Incorrect. It lines up all the lines.
        [ ] Changes the font | Incorrect. font does that.

    .. multichoice::

        What must be made before a label can show a picture?

        [ ] A Canvas | Incorrect. A Canvas is not needed.
        [x] A PhotoImage, e.g. tk.PhotoImage(file="cat.png") | Correct. Then use image=picture.
        [ ] A Button | Incorrect. Not needed.
        [ ] A Frame | Incorrect. Not needed.

    .. multichoice::

        What does textvariable=message do?

        [ ] Sets the font | Incorrect. font does that.
        [x] Links the label to a StringVar, so message.set() changes the words | Correct. The label updates by itself.
        [ ] Names the label | Incorrect. It links a variable.
        [ ] Hides the label | Incorrect. It does not hide it.

    .. multichoice::

        Which line changes a label's text after it is made?

        [x] result_label.config(text="Done") | Correct. config changes options.
        [ ] result_label.text = "Done" | Incorrect. Options are changed with config.
        [ ] result_label.set("Done") | Incorrect. Labels do not have set.
        [ ] result_label.cget(text="Done") | Incorrect. cget only reads.

    .. multichoice::

        What does result_label.cget("fg") give?

        [ ] It changes fg | Incorrect. config changes it.
        [x] The current word colour of the label | Correct. cget reads an option.
        [ ] The label text | Incorrect. It reads fg, not text.
        [ ] An error | Incorrect. cget works on any option.

    .. multichoice::

        Can the user type into a Label?

        [ ] Yes | Incorrect. Labels only display.
        [x] No, labels only show text or pictures | Correct. Use an Entry for typing.
        [ ] Only if state="normal" | Incorrect. Labels still cannot be typed in.
        [ ] Only with textvariable | Incorrect. textvariable does not allow typing.

    .. multichoice::

        Which line makes and places a label in one line?

        [ ] tk.Label(root, text="Hi").show() | Incorrect. show is not a method.
        [x] tk.Label(root, text="Hi").pack() | Correct. Make it, then pack it.
        [ ] tk.Label.pack(root, text="Hi") | Incorrect. Make the label first.
        [ ] root.Label(text="Hi") | Incorrect. Use tk.Label.

    .. multichoice::

        Why should a label used for results be given a name like result_label?

        [x] So it can be changed later with config | Correct. You need its name to change it.
        [ ] Labels must always have names | Incorrect. One-line labels work too.
        [ ] It makes the font bigger | Incorrect. Names do not change fonts.
        [ ] It is faster | Incorrect. Names do not change speed.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a label with big blue words.

        title_label = tk.@@Label | Entry | Button@@(root, text="My App", font=("Arial", @@24 | Arial | bold@@), @@fg | bg | colour@@="blue")
        title_label.pack()

    .. cloze::
        :instructions: Give a label a background, size and space.

        info_label = tk.Label(root, text="Info", @@bg | fg | fill@@="yellow", width=20, @@height | length | lines@@=2, padx=10)
        info_label.pack()

    .. cloze::
        :instructions: Wrap long text and line it up on the left.

        long_label = tk.Label(root, text=long_text, @@wraplength | width | wrap@@=200, @@justify | anchor | side@@="left")
        long_label.pack()

    .. cloze::
        :instructions: Show a picture in a label.

        cat_picture = tk.@@PhotoImage | Picture | Image@@(file="cat.png")
        cat_label = tk.Label(root, @@image | picture | file@@=cat_picture)
        cat_label.pack()

    .. cloze::
        :instructions: Change and read a label.

        result_label.@@config | cget | set@@(text="Well done!")
        colour = result_label.@@cget | config | get@@("fg")

----

.. admonition:: Tasks

    #. Make a window titled "About me" that is 400x200. Add a label that shows your name in Arial size 24, with white text on a blue background.
    #. Add a second label below the first that shows your favourite food. Give it a solid border with a borderwidth of 2, and 10 pixels of padding inside the label on every side.
    #. Make a label with a width of 20, a height of 3, a light green background and the words "Score: 0" anchored to the top left ("nw").
    #. Make a label that shows "0" and a button labelled "Add 5". When the button is clicked, use ``cget`` and ``config`` to add 5 to the number on the label.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("400x200")
                    root.title("About me")

                    name_label = tk.Label(root, text="Sam", font=("Arial", 24), fg="white", bg="blue")
                    name_label.pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("400x200")
                    root.title("About me")

                    name_label = tk.Label(root, text="Sam", font=("Arial", 24), fg="white", bg="blue")
                    name_label.pack()

                    food_label = tk.Label(root, text="Pizza", relief="solid", borderwidth=2,
                                          padx=10, pady=10)
                    food_label.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("400x200")
                    root.title("Score")

                    score_label = tk.Label(root, text="Score: 0", width=20, height=3,
                                           bg="lightgreen", anchor="nw")
                    score_label.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def add_five():
                        number = int(number_label.cget("text"))
                        number_label.config(text=number + 5)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Add 5")

                    number_label = tk.Label(root, text="0", font=("Arial", 40))
                    number_label.pack(pady=20)

                    add_button = tk.Button(root, text="Add 5", command=add_five)
                    add_button.pack()

                    root.mainloop()
