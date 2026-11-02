====================================================
ttk Radiobutton
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk Radiobutton?
-----------------------------

| A **ttk Radiobutton** is a round button in a **group**. The user can choose **only one** button in the group, just like tk Radiobuttons.
| Colours and fonts are set with the ``"TRadiobutton"`` style.
| The special ``"Toolbutton"`` style makes radiobuttons look like normal buttons.

----

Making a group of ttk Radiobuttons
-------------------------------------

| All the radiobuttons in a group share **one variable**. Each one has its own **value**.

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk Radiobuttons")

    drink = tk.StringVar(value="Water")     # 1. One shared variable; "Water" is chosen at the start

    ttk.Radiobutton(root, text="Water", variable=drink, value="Water").pack()   # 2. Create
    ttk.Radiobutton(root, text="Juice", variable=drink, value="Juice").pack()   #    and place
    ttk.Radiobutton(root, text="Milk", variable=drink, value="Milk").pack()

    root.mainloop()                 # Keep the window open

----

ttk Radiobutton options
--------------------------

text, variable and value
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``text`` is the words shown. ``variable`` is the shared variable for the group. ``value`` is what is stored when **this** button is chosen.
| **How to write them:** ``text="Year 7", variable=year, value="Year 7"``
| Read the chosen value with ``variable.get()``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def show():
        result_label.config(text="You chose " + year.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("text, variable and value")

    year = tk.StringVar(value="Year 7")

    for choice in ["Year 7", "Year 8", "Year 9"]:
        ttk.Radiobutton(root, text=choice, variable=year, value=choice).pack()

    ttk.Button(root, text="Show", command=show).pack(pady=5)

    result_label = ttk.Label(root, text="")
    result_label.pack()

    root.mainloop()

command
~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function as soon as a radiobutton is clicked. Give every button in the group the same command.
| **How to write it:** ``command=function_name``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def change_colour():
        root.config(bg=colour.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("command")

    colour = tk.StringVar(value="white")

    for name in ["white", "pink", "lightblue", "lightgreen"]:
        ttk.Radiobutton(root, text=name, variable=colour, value=name,
                        command=change_colour).pack(pady=2)

    root.mainloop()

width and padding
~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``width`` sets the width in characters. ``padding`` adds space around the button.
| Use the same ``width`` on each button and ``pack(anchor="w")`` to line them up neatly.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and padding")

    sport = tk.StringVar(value="Soccer")

    for choice in ["Soccer", "Netball", "Basketball"]:
        ttk.Radiobutton(root, text=choice, variable=sport, value=choice,
                        width=15, padding=5).pack(anchor="w", padx=80)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** turns a radiobutton off (greyed out) or on.
| **How to write it:** ``state="disabled"``, or later ``radio.state(["disabled"])`` and ``radio.state(["!disabled"])``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    seat = tk.StringVar(value="Window")

    ttk.Radiobutton(root, text="Window seat", variable=seat, value="Window").pack()
    ttk.Radiobutton(root, text="Aisle seat (full)", variable=seat, value="Aisle",
                    state="disabled").pack()

    root.mainloop()

style="Toolbutton"
~~~~~~~~~~~~~~~~~~~~~

| **What it does:** makes each radiobutton look like a normal button. The chosen one stays pressed in.
| **How to write it:** ``style="Toolbutton"``
| This does the same job as ``indicatoron=0`` on a tk Radiobutton.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Toolbutton")

    level = tk.StringVar(value="Easy")

    row = ttk.Frame(root)
    row.pack(pady=40)
    for choice in ["Easy", "Medium", "Hard"]:
        ttk.Radiobutton(row, text=choice, variable=level, value=choice,
                        style="Toolbutton", width=8).pack(side="left", padx=2)

    root.mainloop()

----

ttk Radiobutton methods
--------------------------

get and set (the variable)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``variable.get()`` reads the chosen value. ``variable.set(value)`` chooses a button from code.
| Setting a value that matches **no** button, e.g. ``"none"``, means nothing is chosen.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def reset():
        drink.set("none")           # Matches no button, so nothing is chosen


    root = tk.Tk()
    root.geometry("300x200")
    root.title("get and set")

    drink = tk.StringVar(value="Juice")

    for choice in ["Water", "Juice", "Milk"]:
        ttk.Radiobutton(root, text=choice, variable=drink, value=choice).pack()

    ttk.Button(root, text="Reset", command=reset).pack(pady=10)

    root.mainloop()

Checking a quiz answer
~~~~~~~~~~~~~~~~~~~~~~~~~

| Compare ``variable.get()`` with the right answer.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def check():
        if answer.get() == "Mars":
            result_label.config(text="Correct!", foreground="green")
        else:
            result_label.config(text="Try again", foreground="red")


    root = tk.Tk()
    root.geometry("300x220")
    root.title("Quiz")

    ttk.Label(root, text="Which planet is red?", font=("Arial", 14)).pack(pady=5)

    answer = tk.StringVar(value="none")

    for planet in ["Venus", "Mars", "Jupiter"]:
        ttk.Radiobutton(root, text=planet, variable=answer, value=planet).pack()

    ttk.Button(root, text="Check", command=check).pack(pady=5)

    result_label = ttk.Label(root, text="", font=("Arial", 14))
    result_label.pack()

    root.mainloop()

invoke and instate
~~~~~~~~~~~~~~~~~~~~~

| ``radio.invoke()`` chooses the radiobutton and runs its command, like a click.
| ``radio.instate(["selected"])`` gives ``True`` if this radiobutton is the chosen one.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def show():
        if large_radio.instate(["selected"]):
            result_label.config(text="Large chosen: $5")
        else:
            result_label.config(text="Small chosen: $3")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("invoke and instate")

    size = tk.StringVar(value="none")

    small_radio = ttk.Radiobutton(root, text="Small", variable=size, value="Small", command=show)
    small_radio.pack()
    large_radio = ttk.Radiobutton(root, text="Large", variable=size, value="Large", command=show)
    large_radio.pack()

    result_label = ttk.Label(root, text="")
    result_label.pack(pady=10)

    small_radio.invoke()            # Choose Small and run show() at the start

    root.mainloop()

----

Styling ttk Radiobuttons
---------------------------

| The style for every ttk Radiobutton is ``"TRadiobutton"``.
| ``indicatorbackground`` (with ``"clam"``) sets the colour inside the round button. ``style.map`` with ``"selected"`` changes the chosen one.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Radiobutton style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TRadiobutton", font=("Arial", 14), background="lavender")
    style.map("TRadiobutton", foreground=[("selected", "purple")],
              indicatorbackground=[("selected", "violet")])

    pet = tk.StringVar(value="Dog")
    for choice in ["Dog", "Cat", "Rabbit"]:
        ttk.Radiobutton(root, text=choice, variable=pet, value=choice).pack(pady=3)

    root.mainloop()

Styling Toolbuttons
~~~~~~~~~~~~~~~~~~~~~~

| Make your own style based on ``"Toolbutton"``, e.g. ``"Level.Toolbutton"``, to colour the chosen button.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Toolbutton style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Level.Toolbutton", font=("Arial", 12), padding=8)
    style.map("Level.Toolbutton", background=[("selected", "gold")])

    level = tk.StringVar(value="Medium")

    row = ttk.Frame(root)
    row.pack(pady=40)
    for choice in ["Easy", "Medium", "Hard"]:
        ttk.Radiobutton(row, text=choice, variable=level, value=choice,
                        style="Level.Toolbutton").pack(side="left", padx=2)

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
      - Words next to the button
      - ``text="Year 7"``
    * - ``variable``
      - Shared variable for the group
      - ``variable=year``
    * - ``value``
      - Stored when this button is chosen
      - ``value="Year 7"``
    * - ``command``
      - Function to run when clicked
      - ``command=show``
    * - ``width``, ``padding``
      - Width and space around it
      - ``width=15, padding=5``
    * - ``state``
      - Turn on or off
      - ``state="disabled"``
    * - ``style="Toolbutton"``
      - Look like normal buttons
      - ``style="Toolbutton"``
    * - ``variable.get()``, ``.set()``
      - Read or choose a value
      - ``year.set("Year 8")``
    * - ``invoke()``
      - Choose and run the command
      - ``radio.invoke()``
    * - ``instate(["selected"])``
      - Is this one chosen?
      - ``radio.instate(["selected"])``
    * - ``"TRadiobutton"``
      - Style name
      - ``style.configure("TRadiobutton", font=("Arial", 14))``

----

All Radiobutton options
---------------------------

| Here is every option a ttk Radiobutton can have, for reference. You will only need a few of them most of the time.

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
      - Function to run when it is clicked
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
    * - ``padding``
      - Extra space inside it, around the words (one number, or left, top, right, bottom)
      - ``padding=10``
    * - ``state``
      - ``"normal"`` or ``"disabled"`` (greyed out)
      - ``state="disabled"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TRadiobutton"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``text``
      - Words next to the round button
      - ``text="Year 7"``
    * - ``textvariable``
      - A variable that holds the words, so they can change
      - ``textvariable=label_words``
    * - ``underline``
      - Number of the letter to underline (``0`` = first letter)
      - ``underline=0``
    * - ``value``
      - What is stored in the variable when this one is chosen
      - ``value="Year 7"``
    * - ``variable``
      - Shared variable for the whole group
      - ``variable=year``
    * - ``width``
      - How wide it is (in characters)
      - ``width=15``

| The ``image`` option needs a picture made first, e.g. ``dog_picture = tk.PhotoImage(file="dog.png")``.
| ttk Radiobutton has no ``bg``, ``fg`` or ``font`` options. Change its colours and fonts with a style, e.g. ``style.configure("TRadiobutton", foreground="purple")``.

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

        How is a ttk Radiobutton made?

        [x] ttk.Radiobutton(root, text="Small", variable=size, value="Small") | Correct. text, variable and value are set.
        [ ] tk.Radiobutton(root, ttk=True) | Incorrect. Not an option.
        [ ] ttk.radiobutton(root) | Incorrect. Needs a capital R.
        [ ] ttk.Radio(root) | Incorrect. Not a widget.

    .. multichoice::

        What groups radiobuttons together?

        [ ] The same text | Incorrect. Text can differ.
        [x] The same variable | Correct. One shared variable makes a group.
        [ ] Being in the same row | Incorrect. Position does not group them.
        [ ] The same value | Incorrect. Values must differ.

    .. multichoice::

        What must each radiobutton in a group have that is different?

        [x] Its value | Correct. Each stores its own value.
        [ ] Its variable | Incorrect. That is shared.
        [ ] Its parent | Incorrect. They can share a parent.
        [ ] Its style | Incorrect. Styles can be the same.

    .. multichoice::

        How many radiobuttons in a group can be chosen at once?

        [ ] Any number | Incorrect. That is Checkbuttons.
        [x] One | Correct. Choosing one un-chooses the others.
        [ ] Two | Incorrect. Only one.
        [ ] None | Incorrect. One can be chosen.

    .. multichoice::

        When does command run?

        [x] As soon as the radiobutton is clicked | Correct. Give the group the same command.
        [ ] When the window opens | Incorrect. Not then.
        [ ] Only when unchosen | Incorrect. Radiobuttons are not unclicked.
        [ ] Never | Incorrect. It runs on click.

    .. multichoice::

        What does width=12 mean?

        [ ] 12 pixels | Incorrect. It counts characters.
        [x] About 12 characters wide | Correct. Text widgets count characters.
        [ ] 12 buttons | Incorrect. One button.
        [ ] 12 lines | Incorrect. Not lines.

    .. multichoice::

        What does padding=5 do?

        [x] Adds space inside the widget around the circle and words | Correct. padding pads the inside.
        [ ] Adds 5 buttons | Incorrect. It adds space.
        [ ] Moves it | Incorrect. pack moves it.
        [ ] Makes the circle bigger | Incorrect. It adds space.

    .. multichoice::

        Which line greys out a ttk Radiobutton?

        [ ] radio.config(bg="grey") | Incorrect. ttk has no bg.
        [x] radio.state(["disabled"]) | Correct. ttk uses the state method.
        [ ] radio.disable() | Incorrect. Not a method.
        [ ] radio.grey() | Incorrect. Not a method.

    .. multichoice::

        What does style="Toolbutton" do?

        [x] Hides the circle so each choice looks like a button that stays pressed when chosen | Correct. A built-in ttk style.
        [ ] Makes a toolbar | Incorrect. It changes the look.
        [ ] Adds tools | Incorrect. It changes the look.
        [ ] Disables the button | Incorrect. It changes the look.

    .. multichoice::

        How do you find which radiobutton is chosen?

        [ ] radio.get() | Incorrect. Read the variable.
        [x] size.get(), where size is the shared variable | Correct. The variable holds the value.
        [ ] radio.chosen | Incorrect. Not an attribute.
        [ ] radio.instate() | Incorrect. That checks one button's state.

    .. multichoice::

        What does size.set("Large") do?

        [x] Chooses the radiobutton whose value is "Large" | Correct. set chooses from code.
        [ ] Adds a Large button | Incorrect. It changes the variable.
        [ ] Changes the text | Incorrect. It changes the value.
        [ ] Deletes Large | Incorrect. Nothing is deleted.

    .. multichoice::

        How do you start with no radiobutton chosen?

        [ ] Do not make a variable | Incorrect. It is needed.
        [x] Set the variable to a value no button has, like "none" | Correct. No button matches.
        [ ] Use state(["disabled"]) | Incorrect. That turns them off.
        [ ] Use padding=0 | Incorrect. Not related.

    .. multichoice::

        How is a quiz answer checked?

        [x] if answer.get() == "Mars": | Correct. Compare the variable with the right answer.
        [ ] if answer == "Mars": | Incorrect. answer is a variable object.
        [ ] if radio.text == "Mars": | Incorrect. Read the variable.
        [ ] if answer.set("Mars"): | Incorrect. set changes it.

    .. multichoice::

        What does radio.invoke() do?

        [ ] Only greys it out | Incorrect. state does that.
        [x] Chooses it and runs its command, like a click | Correct. invoke acts like a click.
        [ ] Deletes it | Incorrect. destroy deletes.
        [ ] Changes its style | Incorrect. config does that.

    .. multichoice::

        What does radio.instate(["selected"]) give?

        [x] True if this radiobutton is chosen | Correct. selected is the chosen state.
        [ ] It chooses it | Incorrect. It only checks.
        [ ] The value | Incorrect. It checks the state.
        [ ] An error | Incorrect. It is a real method.

    .. multichoice::

        Which style name changes every ttk Radiobutton?

        [ ] "Radiobutton" | Incorrect. Use TRadiobutton.
        [x] "TRadiobutton" | Correct. T then the widget name.
        [ ] "TRadio" | Incorrect. Not the name.
        [ ] "Toolbutton" | Incorrect. That is a different style.

    .. multichoice::

        How can Toolbuttons get a colour when chosen?

        [x] style.map("Toolbutton", background=[("selected", "lightgreen")]) | Correct. map sets colours for states.
        [ ] radio.config(bg="lightgreen") | Incorrect. ttk has no bg.
        [ ] style.configure("Toolbutton", selected="green") | Incorrect. Use map for states.
        [ ] It is not possible | Incorrect. It is.

    .. multichoice::

        Which variable type suits whole-number values like 1, 2 and 3?

        [ ] tk.StringVar() | Incorrect. That is for text.
        [x] tk.IntVar() | Correct. IntVar holds whole numbers.
        [ ] tk.BooleanVar() | Incorrect. True or False only.
        [ ] A list | Incorrect. Use a tkinter variable.

    .. multichoice::

        Which widget suits "Choose your year level"?

        [x] Radiobuttons | Correct. Only one answer.
        [ ] Checkbuttons | Incorrect. Those allow many.
        [ ] Progressbar | Incorrect. It shows progress.
        [ ] Separator | Incorrect. It draws a line.

    .. multichoice::

        How do you change the font of every ttk Radiobutton?

        [ ] radio.config(font=14) | Incorrect. ttk Radiobutton has no font option.
        [x] style.configure("TRadiobutton", font=("Arial", 14)) | Correct. Use a style.
        [ ] root.font(14) | Incorrect. Not a method.
        [ ] radio.font = 14 | Incorrect. Not how it works.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a group of ttk radiobuttons.

        size = tk.@@StringVar | IntVar | Style@@(value="Small")
        ttk.@@Radiobutton | Checkbutton | Button@@(root, text="Small", @@variable | value | group@@=size, value="Small").pack()
        ttk.Radiobutton(root, text="Large", variable=size, @@value | text | onvalue@@="Large").pack()

    .. cloze::
        :instructions: Run a function when a choice is clicked.

        def show():
            result_label.config(text="Size: " + size.@@get | set | value@@())

        ttk.Radiobutton(root, text="Medium", variable=size, value="Medium", @@command | click | run@@=show).pack()

    .. cloze::
        :instructions: Make choices look like buttons.

        ttk.Radiobutton(root, text="Easy", variable=level, value="Easy", @@style | theme | look@@="@@Toolbutton | TRadiobutton | Button@@").pack(side="left")

    .. cloze::
        :instructions: Choose and check from code.

        size.@@set | get | select@@("Large")
        chosen = large_radio.@@instate | state | get@@(["selected"])

    .. cloze::
        :instructions: Colour chosen Toolbuttons.

        style = ttk.Style()
        style.@@map | configure | set@@("Toolbutton", background=[("@@selected | active | chosen@@", "lightgreen")])

----

.. admonition:: Tasks

    #. Make a window titled "Transport" that is 300x200 with three ttk Radiobuttons, "Bus", "Car" and "Walk", sharing one ``StringVar``. Start on "Walk".
    #. Add a "Show" button and a label that shows "You travel by" and the choice.
    #. Make a question "What is 4 x 5?" with the choices 15, 20 and 25. Use ``command`` to check the answer as soon as one is clicked.
    #. Make three Toolbutton-style radiobuttons side by side, "Small", "Medium" and "Large", where the chosen one turns light green.

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
                    root.title("Transport")

                    transport = tk.StringVar(value="Walk")

                    for choice in ["Bus", "Car", "Walk"]:
                        ttk.Radiobutton(root, text=choice, variable=transport, value=choice).pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def show():
                        result_label.config(text="You travel by " + transport.get())


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Transport")

                    transport = tk.StringVar(value="Walk")

                    for choice in ["Bus", "Car", "Walk"]:
                        ttk.Radiobutton(root, text=choice, variable=transport, value=choice).pack()

                    ttk.Button(root, text="Show", command=show).pack(pady=5)
                    result_label = ttk.Label(root, text="")
                    result_label.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def check():
                        if answer.get() == 20:
                            result_label.config(text="Correct!", foreground="green")
                        else:
                            result_label.config(text="Try again", foreground="red")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Quiz")

                    ttk.Label(root, text="What is 4 x 5?", font=("Arial", 14)).pack()

                    answer = tk.IntVar(value=0)
                    for number in [15, 20, 25]:
                        ttk.Radiobutton(root, text=number, variable=answer, value=number,
                                        command=check).pack()

                    result_label = ttk.Label(root, text="", font=("Arial", 14))
                    result_label.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Sizes")

                    style = ttk.Style()
                    style.theme_use("clam")
                    style.map("Size.Toolbutton", background=[("selected", "lightgreen")])

                    size = tk.StringVar(value="Medium")

                    row = ttk.Frame(root)
                    row.pack(pady=40)
                    for choice in ["Small", "Medium", "Large"]:
                        ttk.Radiobutton(row, text=choice, variable=size, value=choice,
                                        style="Size.Toolbutton").pack(side="left", padx=2)

                    root.mainloop()
