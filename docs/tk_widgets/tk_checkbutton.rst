====================================================
tk Checkbutton
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Checkbutton>`_

----

What is a Checkbutton?
-------------------------

| A **Checkbutton** is a small tick box with words next to it.
| The user clicks it to tick it, and clicks again to untick it.
| Use checkbuttons when the user can choose **any number** of options, e.g. pizza toppings.
| To choose **only one** option from a group, use **Radiobuttons** instead.

----

Making a Checkbutton
-------------------------

| A checkbutton needs a **variable** to remember whether it is ticked.
| An ``IntVar`` is a Tkinter variable that stores a whole number: **1** when ticked and **0** when not ticked.

#. **Create** the variable with ``tk.IntVar()``.
#. **Create** the checkbutton with ``tk.Checkbutton(...)`` and link it to the variable.
#. **Place** the checkbutton in the window with ``.pack()``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first checkbutton")

    cheese = tk.IntVar()            # 1. Variable: 1 = ticked, 0 = not ticked

    cheese_check = tk.Checkbutton(root, text="Cheese", variable=cheese)   # 2. Create it
    cheese_check.pack(pady=20)      # 3. Place it in the window

    root.mainloop()                 # Keep the window open

| Each checkbutton needs its **own** variable.

----

Checkbutton options
-----------------------

| Options are written as ``option=value`` inside ``tk.Checkbutton( )``, separated by commas.

text
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the words next to the tick box.
| **How to write it:** ``text="your words"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("text")

    agree = tk.IntVar()

    agree_check = tk.Checkbutton(root, text="I agree to the rules", variable=agree)
    agree_check.pack(pady=20)

    root.mainloop()

variable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the checkbutton to a variable that remembers if it is ticked.
| **How to write it:** ``variable=name_of_variable``
| Read the variable with ``.get()``: it gives **1** if ticked, **0** if not.

.. code-block:: python

    import tkinter as tk


    def check():
        if homework.get() == 1:
            result_label.config(text="Well done!")
        else:
            result_label.config(text="Better get started...")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("variable")

    homework = tk.IntVar()

    homework_check = tk.Checkbutton(root, text="Homework done", variable=homework)
    homework_check.pack(pady=10)

    check_button = tk.Button(root, text="Check", command=check)
    check_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()

onvalue and offvalue
~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** choose what the variable stores when the box is ticked (``onvalue``) and unticked (``offvalue``).
| **How to write them:** ``onvalue="Yes", offvalue="No"``
| To store words instead of numbers, use a ``tk.StringVar()`` as the variable.

.. code-block:: python

    import tkinter as tk


    def show():
        result_label.config(text="Sauce: " + sauce.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("onvalue and offvalue")

    sauce = tk.StringVar(value="No")

    sauce_check = tk.Checkbutton(root, text="Tomato sauce", variable=sauce,
                                 onvalue="Yes", offvalue="No", command=show)
    sauce_check.pack(pady=20)

    result_label = tk.Label(root, text="Sauce: No")
    result_label.pack()

    root.mainloop()

command
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses a function to run **every time** the box is ticked or unticked.
| **How to write it:** ``command=function_name`` (no brackets)

.. code-block:: python

    import tkinter as tk


    def change_colour():
        if dark.get() == 1:
            root.config(bg="black")
        else:
            root.config(bg="white")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("command")
    root.config(bg="white")

    dark = tk.IntVar()

    dark_check = tk.Checkbutton(root, text="Dark mode", variable=dark, command=change_colour)
    dark_check.pack(pady=20)

    root.mainloop()

font, fg and bg
~~~~~~~~~~~~~~~~~~

| **What they do:** ``font`` sets the style and size of the words, ``fg`` sets the colour of the words and ``bg`` sets the background colour.
| **How to write them:** ``font=("Arial", 16)``, ``fg="blue"``, ``bg="lightyellow"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("font, fg and bg")

    music = tk.IntVar()

    music_check = tk.Checkbutton(root, text="Play music", variable=music,
                                 font=("Arial", 16), fg="blue", bg="lightyellow")
    music_check.pack(pady=20)

    root.mainloop()

selectcolor
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the colour **inside** the tick box.
| **How to write it:** ``selectcolor="colour"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("selectcolor")

    sport = tk.IntVar()

    sport_check = tk.Checkbutton(root, text="Sport", variable=sport,
                                 font=("Arial", 16), selectcolor="lightgreen")
    sport_check.pack(pady=20)

    root.mainloop()

anchor and width
~~~~~~~~~~~~~~~~~~

| **What they do:** ``width`` sets how wide the checkbutton is (in characters). ``anchor="w"`` lines it up on the **left**.
| Using the same ``width`` and ``anchor="w"`` on every checkbutton makes a neat list with the boxes lined up.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("anchor and width")

    ham = tk.IntVar()
    pineapple = tk.IntVar()
    mushrooms = tk.IntVar()

    ham_check = tk.Checkbutton(root, text="Ham", variable=ham, width=15, anchor="w")
    ham_check.pack()

    pineapple_check = tk.Checkbutton(root, text="Pineapple", variable=pineapple, width=15, anchor="w")
    pineapple_check.pack()

    mushrooms_check = tk.Checkbutton(root, text="Mushrooms", variable=mushrooms, width=15, anchor="w")
    mushrooms_check.pack()

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** turns the checkbutton on or off.
| **How to write it:** ``state="disabled"``
| **Values:** ``"normal"`` (can be clicked, the default) and ``"disabled"`` (greyed out).

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    free = tk.IntVar()
    sold_out = tk.IntVar()

    free_check = tk.Checkbutton(root, text="Chips", variable=free)
    free_check.pack(pady=5)

    sold_out_check = tk.Checkbutton(root, text="Ice cream (sold out)", variable=sold_out,
                                    state="disabled")
    sold_out_check.pack(pady=5)

    root.mainloop()

----

Checkbutton methods
-----------------------

| A **method** is an action that a widget can do. Methods are written after a dot.

get and set (the variable)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``variable.get()`` reads the value. ``variable.set(1)`` ticks the box from your code, and ``variable.set(0)`` unticks it.
| **How to write them:** ``ticked = cheese.get()``, ``cheese.set(1)``
| ``set`` is useful for having a box ticked when the program starts.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("get and set")

    sound = tk.IntVar()
    sound.set(1)            # Start with the box ticked

    sound_check = tk.Checkbutton(root, text="Sound on", variable=sound)
    sound_check.pack(pady=20)

    root.mainloop()

select, deselect and toggle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:**
| ``select()`` ticks the box.
| ``deselect()`` unticks the box.
| ``toggle()`` swaps it: ticked becomes unticked, and unticked becomes ticked.

.. code-block:: python

    import tkinter as tk


    def tick_all():
        for box in all_boxes:
            box.select()


    def clear_all():
        for box in all_boxes:
            box.deselect()


    root = tk.Tk()
    root.geometry("300x220")
    root.title("select and deselect")

    red = tk.IntVar()
    green = tk.IntVar()
    blue = tk.IntVar()

    red_check = tk.Checkbutton(root, text="Red", variable=red)
    red_check.pack()
    green_check = tk.Checkbutton(root, text="Green", variable=green)
    green_check.pack()
    blue_check = tk.Checkbutton(root, text="Blue", variable=blue)
    blue_check.pack()

    all_boxes = [red_check, green_check, blue_check]

    tick_button = tk.Button(root, text="Tick all", command=tick_all)
    tick_button.pack(pady=5)

    clear_button = tk.Button(root, text="Clear all", command=clear_all)
    clear_button.pack()

    root.mainloop()

Counting ticked boxes
~~~~~~~~~~~~~~~~~~~~~~~~~

| Because a ticked box stores **1** and an unticked box stores **0**, adding the variables together counts how many are ticked.

.. code-block:: python

    import tkinter as tk


    def count():
        total = cheese.get() + ham.get() + olives.get()
        result_label.config(text=f"Toppings: {total}   Price: ${10 + total * 2}")


    root = tk.Tk()
    root.geometry("300x220")
    root.title("Pizza")

    cheese = tk.IntVar()
    ham = tk.IntVar()
    olives = tk.IntVar()

    tk.Checkbutton(root, text="Cheese", variable=cheese, command=count).pack()
    tk.Checkbutton(root, text="Ham", variable=ham, command=count).pack()
    tk.Checkbutton(root, text="Olives", variable=olives, command=count).pack()

    result_label = tk.Label(root, text="Toppings: 0   Price: $10", font=("Arial", 14))
    result_label.pack(pady=10)

    root.mainloop()

| ``tk.Checkbutton(...).pack()`` creates and places a widget in one line. Only do this when you never need to use the widget's name again.

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options **after** the checkbutton has been made.
| **How to write it:** ``check.config(option=value)``

.. code-block:: python

    import tkinter as tk


    def lock():
        rules_check.config(state="disabled", text="Rules accepted")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    rules = tk.IntVar()

    rules_check = tk.Checkbutton(root, text="Accept the rules", variable=rules, command=lock)
    rules_check.pack(pady=20)

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
      - Words next to the box
      - ``text="Cheese"``
    * - ``variable``
      - Variable that remembers ticked (1) or not (0)
      - ``variable=cheese``
    * - ``onvalue``, ``offvalue``
      - What the variable stores when ticked / unticked
      - ``onvalue="Yes", offvalue="No"``
    * - ``command``
      - Function to run when clicked
      - ``command=update``
    * - ``font``, ``fg``, ``bg``
      - Font, word colour, background colour
      - ``font=("Arial", 14)``
    * - ``selectcolor``
      - Colour inside the box
      - ``selectcolor="lightgreen"``
    * - ``width``, ``anchor``
      - Width, and where it sits
      - ``width=15, anchor="w"``
    * - ``state``
      - Turn it on or off
      - ``state="disabled"``
    * - ``variable.get()``
      - Read the value
      - ``cheese.get()``
    * - ``variable.set()``
      - Tick (1) or untick (0) from code
      - ``cheese.set(1)``
    * - ``select()``, ``deselect()``
      - Tick or untick the box
      - ``cheese_check.select()``
    * - ``toggle()``
      - Swap ticked and unticked
      - ``cheese_check.toggle()``
    * - ``config()``
      - Change options later
      - ``cheese_check.config(state="disabled")``

----

All Checkbutton options
---------------------------

| Here is every option a Checkbutton can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``activebackground``
      - Background colour when the mouse is over it
      - ``activebackground="lightblue"``
    * - ``activeforeground``
      - Word colour when the mouse is over it
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
    * - ``command``
      - Function to run when it is ticked or unticked
      - ``command=show``
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
    * - ``indicatoron``
      - ``0`` hides the tick box so it looks like a normal button
      - ``indicatoron=0``
    * - ``justify``
      - Lines up many lines of words: ``"left"``, ``"center"`` or ``"right"``
      - ``justify="left"``
    * - ``offrelief``
      - Border style when not chosen (used with ``indicatoron=0``)
      - ``offrelief="flat"``
    * - ``offvalue``
      - What is stored in the variable when it is not ticked
      - ``offvalue="no"``
    * - ``onvalue``
      - What is stored in the variable when it is ticked
      - ``onvalue="yes"``
    * - ``overrelief``
      - Border style when the mouse is over it
      - ``overrelief="raised"``
    * - ``padx``
      - Extra space on the left and right of the words
      - ``padx=10``
    * - ``pady``
      - Extra space above and below the words
      - ``pady=5``
    * - ``relief``
      - Border style: ``"raised"``, ``"sunken"``, ``"flat"``, ``"ridge"``, ``"groove"`` or ``"solid"``
      - ``relief="sunken"``
    * - ``selectcolor``
      - Colour inside the tick box
      - ``selectcolor="yellow"``
    * - ``selectimage``
      - Picture to show when it is ticked
      - ``selectimage=tick_picture``
    * - ``state``
      - ``"normal"`` (can click), ``"active"`` or ``"disabled"`` (greyed out)
      - ``state="disabled"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``text``
      - Words next to the tick box
      - ``text="I agree"``
    * - ``textvariable``
      - A variable that holds the words, so they can change
      - ``textvariable=label_words``
    * - ``tristateimage``
      - Picture to show when it is half-ticked
      - ``tristateimage=half_picture``
    * - ``tristatevalue``
      - The variable value that makes it look half-ticked (default ``""``)
      - ``tristatevalue="maybe"``
    * - ``underline``
      - Number of the letter to underline (``0`` = first letter)
      - ``underline=0``
    * - ``variable``
      - Variable that stores ``onvalue`` or ``offvalue``
      - ``variable=agree``
    * - ``width``
      - How wide it is (in characters)
      - ``width=15``
    * - ``wraplength``
      - Starts a new line when the words get this long (in pixels)
      - ``wraplength=100``

| The picture options (``image``, ``selectimage``, ``tristateimage``) need a picture made first, e.g. ``dog_picture = tk.PhotoImage(file="dog.png")``.

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

        What is a Checkbutton?

        [x] A tick box that can be ticked or unticked | Correct. Each Checkbutton can be on or off.
        [ ] A round button where only one can be chosen | Incorrect. That is a Radiobutton.
        [ ] A box for typing | Incorrect. That is an Entry.
        [ ] A drop-down list | Incorrect. That is an OptionMenu.

    .. multichoice::

        Can the user tick more than one Checkbutton at the same time?

        [x] Yes, each one is separate | Correct. Checkbuttons work on their own.
        [ ] No, only one at a time | Incorrect. That is how Radiobuttons work.
        [ ] Only two at a time | Incorrect. There is no limit.
        [ ] Only if they share a variable | Incorrect. Each usually has its own variable.

    .. multichoice::

        Which option sets the words next to the tick box?

        [ ] label | Incorrect. label is not an option.
        [x] text | Correct. text sets the words.
        [ ] words | Incorrect. words is not an option.
        [ ] value | Incorrect. value is used by Radiobuttons.

    .. multichoice::

        What is variable used for?

        [ ] Setting the colour | Incorrect. Colours use fg and bg.
        [ ] Running a function | Incorrect. command runs a function.
        [x] Storing whether the box is ticked | Correct. The variable holds onvalue or offvalue.
        [ ] Setting the font | Incorrect. font sets the font.

    .. multichoice::

        With tk.IntVar(), what is stored when the box is ticked (by default)?

        [ ] 0 | Incorrect. 0 means not ticked.
        [x] 1 | Correct. By default, ticked stores 1.
        [ ] True | Incorrect. An IntVar stores numbers.
        [ ] "yes" | Incorrect. That needs onvalue="yes".

    .. multichoice::

        What does onvalue="yes" do?

        [x] Stores "yes" in the variable when the box is ticked | Correct. onvalue is the ticked value.
        [ ] Ticks the box at the start | Incorrect. Set the variable to tick it.
        [ ] Shows yes next to the box | Incorrect. text sets the words.
        [ ] Stores "yes" when unticked | Incorrect. That is offvalue.

    .. multichoice::

        Which option sets the value stored when the box is NOT ticked?

        [ ] onvalue | Incorrect. That is for ticked.
        [ ] novalue | Incorrect. This option does not exist.
        [x] offvalue | Correct. offvalue is the unticked value.
        [ ] untick | Incorrect. This option does not exist.

    .. multichoice::

        What does command do on a Checkbutton?

        [ ] Ticks the box | Incorrect. Clicking ticks the box.
        [x] Runs a function each time the box is ticked or unticked | Correct. command runs on every click.
        [ ] Stores the value | Incorrect. variable stores the value.
        [ ] Sets the text | Incorrect. text sets the words.

    .. multichoice::

        What does selectcolor="yellow" change?

        [x] The colour inside the tick box | Correct. selectcolor is the box colour.
        [ ] The words | Incorrect. fg sets the word colour.
        [ ] The window | Incorrect. It only changes the tick box.
        [ ] The border | Incorrect. relief and borderwidth change the border.

    .. multichoice::

        Why use anchor="w" and the same width on each Checkbutton?

        [ ] To make them bigger | Incorrect. width alone sets size.
        [x] So the tick boxes line up neatly on the left | Correct. Same width and left anchor line them up.
        [ ] To tick them all | Incorrect. anchor does not tick boxes.
        [ ] To change the colour | Incorrect. anchor is about position.

    .. multichoice::

        What does state="disabled" do?

        [ ] Unticks the box | Incorrect. It does not change the value.
        [ ] Deletes it | Incorrect. destroy deletes widgets.
        [x] Greys it out so it cannot be clicked | Correct. Disabled widgets cannot be used.
        [ ] Ticks the box | Incorrect. It only turns the box off.

    .. multichoice::

        How do you find out if a box is ticked?

        [ ] check.get() | Incorrect. Read the variable, not the widget.
        [x] agree.get(), where agree is its variable | Correct. The variable holds the value.
        [ ] check.ticked | Incorrect. That does not exist.
        [ ] check.cget("value") | Incorrect. value is not a Checkbutton option.

    .. multichoice::

        What does agree.set(1) do for an IntVar linked to a Checkbutton?

        [x] Ticks the box | Correct. 1 is the default onvalue.
        [ ] Unticks the box | Incorrect. 0 would untick it.
        [ ] Deletes the box | Incorrect. set only changes the value.
        [ ] Adds one more box | Incorrect. It does not make widgets.

    .. multichoice::

        What does check.select() do?

        [ ] Unticks it | Incorrect. deselect() unticks it.
        [x] Ticks it | Correct. select ticks the box.
        [ ] Swaps it | Incorrect. toggle swaps it.
        [ ] Runs command | Incorrect. invoke runs command.

    .. multichoice::

        What does check.toggle() do?

        [ ] Always ticks it | Incorrect. select always ticks.
        [ ] Always unticks it | Incorrect. deselect always unticks.
        [x] Swaps it: ticked becomes unticked and unticked becomes ticked | Correct. toggle flips the box.
        [ ] Deletes it | Incorrect. destroy deletes widgets.

    .. multichoice::

        What does check.deselect() do?

        [x] Unticks the box | Correct. deselect unticks it.
        [ ] Ticks the box | Incorrect. select ticks it.
        [ ] Greys it out | Incorrect. state="disabled" greys it.
        [ ] Changes its text | Incorrect. config changes text.

    .. multichoice::

        How can you count how many boxes are ticked (IntVars with 0 and 1)?

        [ ] Count the Checkbuttons | Incorrect. That counts all boxes.
        [x] Add up the .get() of each variable | Correct. Each ticked box adds 1.
        [ ] Use len() on one variable | Incorrect. A variable is not a list.
        [ ] Use check.count() | Incorrect. This method does not exist.

    .. multichoice::

        Which line changes a Checkbutton's text later?

        [ ] check.text("New") | Incorrect. text is not a method.
        [ ] check.set(text="New") | Incorrect. Checkbuttons do not have set.
        [x] check.config(text="New") | Correct. config changes options.
        [ ] check.cget(text="New") | Incorrect. cget reads options.

    .. multichoice::

        Which variable type stores whole numbers?

        [ ] tk.StringVar() | Incorrect. StringVar stores text.
        [x] tk.IntVar() | Correct. IntVar stores whole numbers.
        [ ] tk.BooleanVar() | Incorrect. That stores True or False.
        [ ] tk.DoubleVar() | Incorrect. That stores decimal numbers.

    .. multichoice::

        Which widget would suit "Choose all the toppings you want"?

        [x] Checkbuttons | Correct. The user may want many toppings.
        [ ] Radiobuttons | Incorrect. Radiobuttons allow only one choice.
        [ ] A Label | Incorrect. Labels cannot be clicked.
        [ ] A Scale | Incorrect. A Scale picks a number.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a Checkbutton with its own variable.

        agree = tk.@@IntVar | StringVar | Label@@()
        agree_check = tk.@@Checkbutton | Radiobutton | Button@@(root, text="I agree", @@variable | value | text@@=agree)
        agree_check.pack()

    .. cloze::
        :instructions: Store words instead of numbers.

        choice = tk.@@StringVar | IntVar | Entry@@(value="no")
        cheese_check = tk.Checkbutton(root, text="Cheese", variable=choice, @@onvalue | value | ticked@@="yes", offvalue="@@no | yes | off@@")

    .. cloze::
        :instructions: Run a function when the box is clicked.

        def show():
            result_label.config(text=agree.@@get | set | read@@())

        tk.Checkbutton(root, text="Agree", variable=agree, @@command | click | run@@=show).pack()

    .. cloze::
        :instructions: Tick, untick and swap the box from code.

        agree_check.@@select | tick | set@@()
        agree_check.@@deselect | untick | clear@@()
        agree_check.@@toggle | swap | flip@@()

    .. cloze::
        :instructions: Count the ticked boxes.

        total = cheese.get() @@+ | - | *@@ ham.get() + tomato.get()
        count_label.config(@@text | value | count@@="Ticked: " + str(total))

----

.. admonition:: Tasks

    #. Make a window titled "Hobbies" that is 300x200. Add three checkbuttons: "Sport", "Music" and "Art", each with its own ``IntVar``.
    #. Make the "Music" checkbutton start ticked by using ``set``.
    #. Add a button labelled "How many?" and a label. When clicked, the label shows how many hobbies are ticked.
    #. Make a checkbutton "Big text". Use ``command`` so that when it is ticked a label's font changes to size 30, and when it is unticked it goes back to size 12.

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
                    root.title("Hobbies")

                    sport = tk.IntVar()
                    music = tk.IntVar()
                    art = tk.IntVar()

                    sport_check = tk.Checkbutton(root, text="Sport", variable=sport)
                    sport_check.pack()
                    music_check = tk.Checkbutton(root, text="Music", variable=music)
                    music_check.pack()
                    art_check = tk.Checkbutton(root, text="Art", variable=art)
                    art_check.pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Hobbies")

                    sport = tk.IntVar()
                    music = tk.IntVar()
                    art = tk.IntVar()
                    music.set(1)

                    sport_check = tk.Checkbutton(root, text="Sport", variable=sport)
                    sport_check.pack()
                    music_check = tk.Checkbutton(root, text="Music", variable=music)
                    music_check.pack()
                    art_check = tk.Checkbutton(root, text="Art", variable=art)
                    art_check.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk


                    def how_many():
                        total = sport.get() + music.get() + art.get()
                        count_label.config(text=f"Hobbies ticked: {total}")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Hobbies")

                    sport = tk.IntVar()
                    music = tk.IntVar()
                    art = tk.IntVar()
                    music.set(1)

                    sport_check = tk.Checkbutton(root, text="Sport", variable=sport)
                    sport_check.pack()
                    music_check = tk.Checkbutton(root, text="Music", variable=music)
                    music_check.pack()
                    art_check = tk.Checkbutton(root, text="Art", variable=art)
                    art_check.pack()

                    count_button = tk.Button(root, text="How many?", command=how_many)
                    count_button.pack(pady=5)

                    count_label = tk.Label(root, text="")
                    count_label.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def change_size():
                        if big.get() == 1:
                            word_label.config(font=("Arial", 30))
                        else:
                            word_label.config(font=("Arial", 12))


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Big text")

                    big = tk.IntVar()

                    big_check = tk.Checkbutton(root, text="Big text", variable=big, command=change_size)
                    big_check.pack(pady=10)

                    word_label = tk.Label(root, text="Hello", font=("Arial", 12))
                    word_label.pack()

                    root.mainloop()
