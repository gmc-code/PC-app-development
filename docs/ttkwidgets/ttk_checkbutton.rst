====================================================
ttk Checkbutton
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk Checkbutton?
-----------------------------

| A **ttk Checkbutton** is a tick box with words next to it, just like a tk Checkbutton.
| The user can tick **any number** of checkbuttons.
| Colours and fonts are set with the ``"TCheckbutton"`` style.

----

Making a ttk Checkbutton
---------------------------

| Each checkbutton needs its **own** ``IntVar``: **1** when ticked, **0** when not.

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk Checkbutton")

    cheese = tk.IntVar()            # 1. Variable: 1 = ticked, 0 = not ticked

    cheese_check = ttk.Checkbutton(root, text="Cheese", variable=cheese)   # 2. Create it
    cheese_check.pack(pady=20)      # 3. Place it

    root.mainloop()                 # Keep the window open

.. note::

    Always give a ttk Checkbutton a ``variable``. Without one, it can start in a half-ticked "alternate" state.

----

ttk Checkbutton options
--------------------------

text
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the words next to the tick box.
| **How to write it:** ``text="your words"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("text")

    agree = tk.IntVar()
    ttk.Checkbutton(root, text="I agree to the rules", variable=agree).pack(pady=20)

    root.mainloop()

variable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the checkbutton to a variable. ``variable.get()`` gives **1** if ticked and **0** if not.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def check():
        if homework.get() == 1:
            result_label.config(text="Well done!")
        else:
            result_label.config(text="Better get started...")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("variable")

    homework = tk.IntVar()

    ttk.Checkbutton(root, text="Homework done", variable=homework).pack(pady=10)
    ttk.Button(root, text="Check", command=check).pack()

    result_label = ttk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()

onvalue and offvalue
~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** choose what the variable stores when ticked and unticked. Use a ``StringVar`` to store words.
| **How to write them:** ``onvalue="Yes", offvalue="No"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def show():
        result_label.config(text="Extra cheese: " + extra.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("onvalue and offvalue")

    extra = tk.StringVar(value="No")

    ttk.Checkbutton(root, text="Extra cheese", variable=extra, onvalue="Yes",
                    offvalue="No", command=show).pack(pady=20)

    result_label = ttk.Label(root, text="Extra cheese: No")
    result_label.pack()

    root.mainloop()

command
~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function every time the box is ticked or unticked.
| **How to write it:** ``command=function_name``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def update():
        if big.get() == 1:
            word_label.config(font=("Arial", 30))
        else:
            word_label.config(font=("Arial", 12))


    root = tk.Tk()
    root.geometry("300x200")
    root.title("command")

    big = tk.IntVar()

    ttk.Checkbutton(root, text="Big text", variable=big, command=update).pack(pady=10)

    word_label = ttk.Label(root, text="Hello", font=("Arial", 12))
    word_label.pack()

    root.mainloop()

width and padding
~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``width`` sets the width in characters, so a list of checkbuttons lines up. ``padding`` adds space around it.
| **How to write them:** ``width=15``, ``padding=5``
| Use ``pack(anchor="w")`` to line them up on the left.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and padding")

    toppings = []                       # Keep every variable in a list
    for topping in ["Ham", "Pineapple", "Mushrooms"]:
        choice = tk.IntVar()
        toppings.append(choice)
        ttk.Checkbutton(root, text=topping, variable=choice, width=15,
                        padding=5).pack(anchor="w", padx=80)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** turns the checkbutton off (greyed out) or on.
| **How to write it:** ``state="disabled"``, or later ``check.state(["disabled"])`` and ``check.state(["!disabled"])``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    chips = tk.IntVar()
    ice_cream = tk.IntVar()

    ttk.Checkbutton(root, text="Chips", variable=chips).pack(pady=5)
    ttk.Checkbutton(root, text="Ice cream (sold out)", variable=ice_cream,
                    state="disabled").pack(pady=5)

    root.mainloop()

----

ttk Checkbutton methods
--------------------------

get and set (the variable)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``variable.get()`` reads 1 or 0. ``variable.set(1)`` ticks the box from your code and ``variable.set(0)`` unticks it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def tick_all():
        for option in [red, green, blue]:
            option.set(1)


    def clear_all():
        for option in [red, green, blue]:
            option.set(0)


    root = tk.Tk()
    root.geometry("300x220")
    root.title("get and set")

    red = tk.IntVar()
    green = tk.IntVar(value=1)          # Starts ticked
    blue = tk.IntVar()

    ttk.Checkbutton(root, text="Red", variable=red).pack()
    ttk.Checkbutton(root, text="Green", variable=green).pack()
    ttk.Checkbutton(root, text="Blue", variable=blue).pack()

    ttk.Button(root, text="Tick all", command=tick_all).pack(pady=5)
    ttk.Button(root, text="Clear all", command=clear_all).pack()

    root.mainloop()

instate (is it ticked?)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| A ticked ttk Checkbutton is in the ``"selected"`` state. ``check.instate(["selected"])`` gives ``True`` if it is ticked.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def check():
        if sound_check.instate(["selected"]):
            result_label.config(text="Sound is on")
        else:
            result_label.config(text="Sound is off")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("instate")

    sound = tk.IntVar()

    sound_check = ttk.Checkbutton(root, text="Sound", variable=sound)
    sound_check.pack(pady=10)

    ttk.Button(root, text="Check", command=check).pack()

    result_label = ttk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()

invoke
~~~~~~~~~~~~~~~~~~

| ``check.invoke()`` clicks the checkbutton from code: it swaps ticked/unticked and runs its command.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def show():
        result_label.config(text=f"Dark mode: {dark.get()}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("invoke")

    dark = tk.IntVar()

    dark_check = ttk.Checkbutton(root, text="Dark mode", variable=dark, command=show)
    dark_check.pack(pady=10)

    result_label = ttk.Label(root, text="")
    result_label.pack()

    dark_check.invoke()             # Tick it and run show() at the start

    root.mainloop()

Counting ticked boxes
~~~~~~~~~~~~~~~~~~~~~~~~

| Ticked boxes store **1**, so adding the variables counts how many are ticked.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def count():
        total = cheese.get() + ham.get() + olives.get()
        result_label.config(text=f"Price: ${10 + total * 2}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Pizza")

    cheese = tk.IntVar()
    ham = tk.IntVar()
    olives = tk.IntVar()

    ttk.Checkbutton(root, text="Cheese", variable=cheese, command=count).pack()
    ttk.Checkbutton(root, text="Ham", variable=ham, command=count).pack()
    ttk.Checkbutton(root, text="Olives", variable=olives, command=count).pack()

    result_label = ttk.Label(root, text="Price: $10", font=("Arial", 14))
    result_label.pack(pady=10)

    root.mainloop()

----

Styling a ttk Checkbutton
----------------------------

| The style for every ttk Checkbutton is ``"TCheckbutton"``.
| ``indicatorbackground`` (with the ``"clam"`` theme) sets the colour inside the tick box.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Checkbutton style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TCheckbutton", font=("Arial", 14), foreground="navy",
                    background="lightyellow", indicatorbackground="white")
    style.map("TCheckbutton", foreground=[("selected", "green")],
              indicatorbackground=[("selected", "lightgreen")])

    sports = []
    for sport in ["Soccer", "Netball", "Tennis"]:
        choice = tk.IntVar()
        sports.append(choice)
        ttk.Checkbutton(root, text=sport, variable=choice).pack(pady=3)

    root.mainloop()

| ``style.map`` with ``"selected"`` makes ticked boxes green.

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
      - Remembers ticked (1) or not (0)
      - ``variable=cheese``
    * - ``onvalue``, ``offvalue``
      - Values stored when ticked / unticked
      - ``onvalue="Yes", offvalue="No"``
    * - ``command``
      - Function to run when clicked
      - ``command=update``
    * - ``width``, ``padding``
      - Width and space around it
      - ``width=15, padding=5``
    * - ``state``
      - Turn on or off
      - ``state="disabled"``
    * - ``variable.get()``, ``.set()``
      - Read, tick or untick
      - ``cheese.set(1)``
    * - ``instate(["selected"])``
      - Is it ticked?
      - ``check.instate(["selected"])``
    * - ``invoke()``
      - Click from code
      - ``check.invoke()``
    * - ``"TCheckbutton"``
      - Style name
      - ``style.configure("TCheckbutton", font=("Arial", 14))``

----

All Checkbutton options
---------------------------

| Here is every option a ttk Checkbutton can have, for reference. You will only need a few of them most of the time.

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
      - Function to run when it is ticked or unticked
      - ``command=show``
    * - ``compound``
      - Where the picture goes compared to the words
      - ``compound="left"``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``image``
      - Shows a picture instead of (or with) the words
      - ``image=dog_picture``
    * - ``offvalue``
      - What is stored in the variable when it is not ticked
      - ``offvalue="no"``
    * - ``onvalue``
      - What is stored in the variable when it is ticked
      - ``onvalue="yes"``
    * - ``padding``
      - Extra space inside it, around the words (one number, or left, top, right, bottom)
      - ``padding=10``
    * - ``state``
      - ``"normal"`` or ``"disabled"`` (greyed out)
      - ``state="disabled"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TCheckbutton"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``text``
      - Words next to the tick box
      - ``text="I agree"``
    * - ``textvariable``
      - A variable that holds the words, so they can change
      - ``textvariable=label_words``
    * - ``underline``
      - Number of the letter to underline (``0`` = first letter)
      - ``underline=0``
    * - ``variable``
      - Variable that stores ``onvalue`` or ``offvalue``
      - ``variable=agree``
    * - ``width``
      - How wide it is (in characters)
      - ``width=15``

| The ``image`` option needs a picture made first, e.g. ``dog_picture = tk.PhotoImage(file="dog.png")``.
| ttk Checkbutton has no ``bg``, ``fg`` or ``font`` options. Change its colours and fonts with a style, e.g. ``style.configure("TCheckbutton", foreground="purple")``.

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

        How is a ttk Checkbutton made?

        [x] ttk.Checkbutton(root, text="Agree", variable=agree) | Correct. It is made like the tk one.
        [ ] tk.Checkbutton(root, ttk=True) | Incorrect. Not an option.
        [ ] ttk.checkbutton(root) | Incorrect. Needs a capital C.
        [ ] ttk.Tickbox(root) | Incorrect. Not a widget.

    .. multichoice::

        What does a Checkbutton let the user do?

        [ ] Choose only one of many | Incorrect. That is Radiobuttons.
        [x] Tick or untick a box, with any number ticked | Correct. Each box is separate.
        [ ] Type text | Incorrect. That is an Entry.
        [ ] Pick a number | Incorrect. That is a Scale.

    .. multichoice::

        What is variable used for?

        [x] Storing whether the box is ticked | Correct. It holds onvalue or offvalue.
        [ ] Setting the text | Incorrect. text does that.
        [ ] Running a function | Incorrect. command does that.
        [ ] Setting the colour | Incorrect. Use a style.

    .. multichoice::

        With tk.IntVar(), what is stored when ticked (by default)?

        [ ] 0 | Incorrect. 0 means unticked.
        [x] 1 | Correct. 1 means ticked.
        [ ] True | Incorrect. IntVars hold numbers.
        [ ] "on" | Incorrect. Not by default.

    .. multichoice::

        What does onvalue="yes" do?

        [ ] Ticks the box | Incorrect. It sets the stored value.
        [x] Stores "yes" when the box is ticked | Correct. onvalue is the ticked value.
        [ ] Shows yes | Incorrect. text shows words.
        [ ] Stores yes when unticked | Incorrect. offvalue does that.

    .. multichoice::

        What does offvalue="no" do?

        [x] Stores "no" when the box is not ticked | Correct. offvalue is the unticked value.
        [ ] Unticks the box | Incorrect. It sets the stored value.
        [ ] Hides the box | Incorrect. It sets a value.
        [ ] Turns the box off | Incorrect. state does that.

    .. multichoice::

        When does command run?

        [ ] Only when ticked | Incorrect. It runs on every click.
        [x] Each time the box is ticked or unticked | Correct. command runs on every change from a click.
        [ ] When the window opens | Incorrect. Not then.
        [ ] Never | Incorrect. It runs on click.

    .. multichoice::

        What does padding=5 do?

        [ ] Adds 5 boxes | Incorrect. It adds space.
        [x] Adds space inside the widget around the box and words | Correct. padding pads the inside.
        [ ] Moves it 5 pixels | Incorrect. pack moves it.
        [ ] Makes it 5 wide | Incorrect. width does that.

    .. multichoice::

        Which line greys out a ttk Checkbutton?

        [x] check.state(["disabled"]) | Correct. ttk uses the state method.
        [ ] check.config(bg="grey") | Incorrect. ttk has no bg.
        [ ] check.grey() | Incorrect. Not a method.
        [ ] check.state("off") | Incorrect. Not right.

    .. multichoice::

        How do you find out if the box is ticked?

        [ ] check.get() | Incorrect. Read the variable.
        [x] agree.get(), where agree is its variable | Correct. The variable holds the value.
        [ ] check.ticked | Incorrect. Not an attribute.
        [ ] check.value() | Incorrect. Not a method.

    .. multichoice::

        What does agree.set(1) do?

        [ ] Unticks the box | Incorrect. 0 unticks it.
        [x] Ticks the box | Correct. 1 is the default onvalue.
        [ ] Adds a box | Incorrect. It changes the value.
        [ ] Deletes the box | Incorrect. It changes the value.

    .. multichoice::

        What does check.instate(["selected"]) give?

        [x] True if the box is ticked | Correct. selected is the ticked state.
        [ ] It ticks the box | Incorrect. It only checks.
        [ ] The text | Incorrect. It checks state.
        [ ] An error | Incorrect. It is a real method.

    .. multichoice::

        What does check.invoke() do?

        [ ] Deletes it | Incorrect. destroy does that.
        [x] Swaps the tick and runs its command, like a click | Correct. invoke acts like a click.
        [ ] Only ticks it | Incorrect. It swaps it.
        [ ] Disables it | Incorrect. state does that.

    .. multichoice::

        How can you count ticked boxes using IntVars?

        [ ] len(boxes) | Incorrect. That counts all boxes.
        [x] Add up each variable's get() | Correct. Each ticked box adds 1.
        [ ] check.count() | Incorrect. Not a method.
        [ ] style.count() | Incorrect. Not a method.

    .. multichoice::

        Which style name changes every ttk Checkbutton?

        [ ] "Checkbutton" | Incorrect. The style is TCheckbutton.
        [x] "TCheckbutton" | Correct. T then the widget name.
        [ ] "TCheck" | Incorrect. Not the name.
        [ ] "ttk.Checkbutton" | Incorrect. Not a style name.

    .. multichoice::

        How do you change the font of ttk Checkbuttons?

        [x] style.configure("TCheckbutton", font=("Arial", 14)) | Correct. ttk uses styles.
        [ ] check.config(font=("Arial", 14)) | Incorrect. ttk Checkbutton has no font option.
        [ ] check.font = 14 | Incorrect. Not how it works.
        [ ] check.state(["big"]) | Incorrect. Not a state.

    .. multichoice::

        What does width=20 mean?

        [ ] 20 pixels | Incorrect. It counts characters.
        [x] About 20 characters wide | Correct. Text widgets count characters.
        [ ] 20 boxes | Incorrect. One box.
        [ ] 20 lines | Incorrect. Not lines.

    .. multichoice::

        Which widget suits "Tick every subject you like"?

        [x] Checkbuttons | Correct. Many can be ticked.
        [ ] Radiobuttons | Incorrect. Only one could be chosen.
        [ ] A Label | Incorrect. Labels cannot be ticked.
        [ ] A Progressbar | Incorrect. It shows progress.

    .. multichoice::

        Can a ttk Checkbutton be ticked from code?

        [ ] No | Incorrect. It can.
        [x] Yes, by setting its variable to the onvalue | Correct. e.g. agree.set(1).
        [ ] Only with invoke | Incorrect. set works too.
        [ ] Only if disabled | Incorrect. Not related.

    .. multichoice::

        What type of variable stores text like "yes" and "no"?

        [ ] tk.IntVar() | Incorrect. That stores numbers.
        [x] tk.StringVar() | Correct. StringVar stores text.
        [ ] tk.DoubleVar() | Incorrect. That stores decimals.
        [ ] tk.BooleanVar() | Incorrect. That stores True or False.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a ttk Checkbutton.

        agree = tk.@@IntVar | Label | Style@@()
        agree_check = ttk.@@Checkbutton | Radiobutton | Button@@(root, text="I agree", @@variable | value | text@@=agree)
        agree_check.pack()

    .. cloze::
        :instructions: Store words when ticked and unticked.

        choice = tk.StringVar(value="no")
        ttk.Checkbutton(root, text="Cheese", variable=choice, @@onvalue | ticked | value@@="yes", @@offvalue | unticked | novalue@@="no").pack()

    .. cloze::
        :instructions: Run a function when clicked.

        def show():
            result_label.config(text="Value: " + str(agree.@@get | set | read@@()))

        ttk.Checkbutton(root, text="Agree", variable=agree, @@command | click | run@@=show).pack()

    .. cloze::
        :instructions: Turn the box off and check if it is ticked.

        agree_check.@@state | config | set@@(["disabled"])
        ticked = agree_check.@@instate | state | get@@(["selected"])

    .. cloze::
        :instructions: Change the font of every Checkbutton.

        style = ttk.Style()
        style.configure("@@TCheckbutton | Checkbutton | TCheck@@", @@font | size | text@@=("Arial", 14))

----

.. admonition:: Tasks

    #. Make a window titled "Subjects" that is 300x200 with three ttk Checkbuttons: "Maths", "Science" and "Art", each with its own ``IntVar``.
    #. Make "Science" start ticked.
    #. Add a button "How many?" and a label that shows how many subjects are ticked.
    #. Style the checkbuttons with Arial size 14 and make ticked ones turn purple.

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
                    root.title("Subjects")

                    maths = tk.IntVar()
                    science = tk.IntVar()
                    art = tk.IntVar()

                    ttk.Checkbutton(root, text="Maths", variable=maths).pack()
                    ttk.Checkbutton(root, text="Science", variable=science).pack()
                    ttk.Checkbutton(root, text="Art", variable=art).pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Subjects")

                    maths = tk.IntVar()
                    science = tk.IntVar(value=1)
                    art = tk.IntVar()

                    ttk.Checkbutton(root, text="Maths", variable=maths).pack()
                    ttk.Checkbutton(root, text="Science", variable=science).pack()
                    ttk.Checkbutton(root, text="Art", variable=art).pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def how_many():
                        total = maths.get() + science.get() + art.get()
                        count_label.config(text=f"Subjects ticked: {total}")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Subjects")

                    maths = tk.IntVar()
                    science = tk.IntVar(value=1)
                    art = tk.IntVar()

                    ttk.Checkbutton(root, text="Maths", variable=maths).pack()
                    ttk.Checkbutton(root, text="Science", variable=science).pack()
                    ttk.Checkbutton(root, text="Art", variable=art).pack()

                    ttk.Button(root, text="How many?", command=how_many).pack(pady=5)
                    count_label = ttk.Label(root, text="")
                    count_label.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Subjects")

                    style = ttk.Style()
                    style.theme_use("clam")
                    style.configure("TCheckbutton", font=("Arial", 14))
                    style.map("TCheckbutton", foreground=[("selected", "purple")])

                    maths = tk.IntVar()
                    science = tk.IntVar(value=1)
                    art = tk.IntVar()

                    ttk.Checkbutton(root, text="Maths", variable=maths).pack()
                    ttk.Checkbutton(root, text="Science", variable=science).pack()
                    ttk.Checkbutton(root, text="Art", variable=art).pack()

                    root.mainloop()
