====================================================
ttk Menubutton
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk Menubutton?
----------------------------

| A **ttk Menubutton** is a button that opens a drop-down **Menu** when clicked.
| A ttk Menubutton already shows a small arrow, so the user knows a list will drop down.
| The drop-down list is a normal **tk Menu** (there is no ttk Menu). See the **Menu** page for all the Menu methods.

----

Making a ttk Menubutton
--------------------------

#. **Create** the Menubutton with ``ttk.Menubutton(root, text="...")``.
#. **Create** a tk Menu that belongs to it: ``tk.Menu(menubutton, tearoff=0)``.
#. **Add** commands to the Menu.
#. **Link** them with ``menubutton.config(menu=the_menu)``, then **place** the Menubutton.

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets


    def say(word):
        message_label.config(text=word)


    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk Menubutton")

    greet_button = ttk.Menubutton(root, text="Greetings")                  # 1. Create it

    greet_menu = tk.Menu(greet_button, tearoff=0)                          # 2. Its menu
    greet_menu.add_command(label="Hello", command=lambda: say("Hello!"))   # 3. Commands
    greet_menu.add_command(label="Goodbye", command=lambda: say("Goodbye!"))

    greet_button.config(menu=greet_menu)                                   # 4. Link them
    greet_button.pack(pady=20)                                             #    and place

    message_label = ttk.Label(root, text="", font=("Arial", 16))
    message_label.pack()

    root.mainloop()                 # Keep the window open

| ``lambda:`` lets each command send different words to the same function.

----

ttk Menubutton options
-------------------------

text and width
~~~~~~~~~~~~~~~~~

| **What they do:** ``text`` sets the words on the Menubutton. ``width`` sets its width in characters.
| **How to write them:** ``text="Options", width=15``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("text and width")

    options_button = ttk.Menubutton(root, text="Options", width=15)
    options_menu = tk.Menu(options_button, tearoff=0)
    options_menu.add_command(label="Settings")
    options_menu.add_command(label="Help")
    options_button.config(menu=options_menu)
    options_button.pack(pady=40)

    root.mainloop()

direction
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses where the menu opens.
| **How to write it:** ``direction="above"``
| **Values:** ``"below"`` (the default), ``"above"``, ``"left"``, ``"right"``, ``"flush"`` (over the button).

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("direction")

    up_button = ttk.Menubutton(root, text="Opens upwards", direction="above")
    up_menu = tk.Menu(up_button, tearoff=0)
    up_menu.add_command(label="First")
    up_menu.add_command(label="Second")
    up_button.config(menu=up_menu)
    up_button.pack(side="bottom", pady=10)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** turns the Menubutton off (the menu will not open) or on.
| **How to write it:** ``state="disabled"``, or later ``menubutton.state(["disabled"])`` and ``menubutton.state(["!disabled"])``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    locked_button = ttk.Menubutton(root, text="Locked", state="disabled")
    locked_menu = tk.Menu(locked_button, tearoff=0)
    locked_menu.add_command(label="Secret")
    locked_button.config(menu=locked_menu)
    locked_button.pack(pady=40)

    root.mainloop()

padding
~~~~~~~~~~~~~~~~~~

| **What it does:** adds space inside the Menubutton around the words.
| **How to write it:** ``padding=(20, 8)``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("padding")

    big_button = ttk.Menubutton(root, text="Big menu", padding=(20, 8))
    big_menu = tk.Menu(big_button, tearoff=0)
    big_menu.add_command(label="Item")
    big_button.config(menu=big_menu)
    big_button.pack(pady=40)

    root.mainloop()

----

ttk Menubutton methods
-------------------------

Showing the choice with config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``menubutton.config(text=...)`` can show the user's choice on the Menubutton itself.
| ``lambda sport=sport:`` makes each command in the loop remember its own sport.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def choose(sport):
        sport_button.config(text=sport)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    sport_button = ttk.Menubutton(root, text="Choose a sport", width=18)
    sport_menu = tk.Menu(sport_button, tearoff=0)
    for sport in ["Cricket", "Netball", "Soccer", "Tennis"]:
        sport_menu.add_command(label=sport, command=lambda sport=sport: choose(sport))
    sport_button.config(menu=sport_menu)
    sport_button.pack(pady=40)

    root.mainloop()

add_checkbutton
~~~~~~~~~~~~~~~~~~

| Menu items that can be ticked on and off. Each needs its own ``IntVar``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def show():
        result_label.config(text=f"Sound: {sound.get()}   Music: {music.get()}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("add_checkbutton")

    sound = tk.IntVar(value=1)
    music = tk.IntVar()

    extras_button = ttk.Menubutton(root, text="Extras")
    extras_menu = tk.Menu(extras_button, tearoff=0)
    extras_menu.add_checkbutton(label="Sound", variable=sound, command=show)
    extras_menu.add_checkbutton(label="Music", variable=music, command=show)
    extras_button.config(menu=extras_menu)
    extras_button.pack(pady=30)

    result_label = ttk.Label(root, text="Sound: 1   Music: 0")
    result_label.pack()

    root.mainloop()

add_radiobutton
~~~~~~~~~~~~~~~~~~

| A group of menu items where only **one** can be chosen. They share one variable.
| A ttk Menubutton can show the variable with ``textvariable``, so its words change by themselves.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("add_radiobutton")

    size = tk.StringVar(value="Medium")

    size_button = ttk.Menubutton(root, textvariable=size, width=12)   # Shows the choice
    size_menu = tk.Menu(size_button, tearoff=0)
    for choice in ["Small", "Medium", "Large"]:
        size_menu.add_radiobutton(label=choice, variable=size, value=choice)
    size_button.config(menu=size_menu)
    size_button.pack(pady=40)

    root.mainloop()

----

Styling a ttk Menubutton
---------------------------

| The style for every ttk Menubutton is ``"TMenubutton"``. The drop-down list is a tk Menu, so give the **Menu** its own ``font``, ``bg`` and ``fg``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Menubutton style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TMenubutton", font=("Arial", 14), foreground="white",
                    background="seagreen", padding=8)
    style.map("TMenubutton", background=[("active", "mediumseagreen")])

    food_button = ttk.Menubutton(root, text="Food")
    food_menu = tk.Menu(food_button, tearoff=0, font=("Arial", 14), bg="honeydew")
    food_menu.add_command(label="Pizza")
    food_menu.add_command(label="Pasta")
    food_button.config(menu=food_menu)
    food_button.pack(pady=40)

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
    * - ``text``, ``textvariable``
      - Words on the button
      - ``text="Options"``
    * - ``menu``
      - The tk Menu that drops down
      - ``mb.config(menu=my_menu)``
    * - ``width``, ``padding``
      - Width and space inside
      - ``width=15, padding=8``
    * - ``direction``
      - Where the menu opens
      - ``direction="above"``
    * - ``state``
      - Turn on or off
      - ``state="disabled"``
    * - ``add_command()``
      - Add a command to the menu
      - ``my_menu.add_command(label="Hi")``
    * - ``add_checkbutton()``
      - Add a tick-on/off item
      - ``add_checkbutton(label="Sound", variable=sound)``
    * - ``add_radiobutton()``
      - Add a choose-one item
      - ``add_radiobutton(label="S", variable=size, value="S")``
    * - ``config()``
      - Change options later
      - ``mb.config(text="New")``
    * - ``"TMenubutton"``
      - Style name
      - ``style.configure("TMenubutton", font=("Arial", 14))``

----

All Menubutton options
---------------------------

| Here is every option a ttk Menubutton can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``class_``
      - A group name used to style many widgets at once (advanced). Written ``class_`` in Python
      - ``class_="Sidebar"``
    * - ``compound``
      - Where the picture goes compared to the words
      - ``compound="left"``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``direction``
      - Where the menu appears: ``"below"``, ``"above"``, ``"left"``, ``"right"`` or ``"flush"``
      - ``direction="above"``
    * - ``image``
      - Shows a picture instead of (or with) the words
      - ``image=dog_picture``
    * - ``menu``
      - The menu that drops down when it is clicked
      - ``menu=food_menu``
    * - ``padding``
      - Extra space inside it, around the words (one number, or left, top, right, bottom)
      - ``padding=10``
    * - ``state``
      - ``"normal"`` or ``"disabled"`` (greyed out)
      - ``state="disabled"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TMenubutton"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``text``
      - Words shown on the button
      - ``text="Food"``
    * - ``textvariable``
      - A variable that holds the words, so they can change
      - ``textvariable=label_words``
    * - ``underline``
      - Number of the letter to underline (``0`` = first letter)
      - ``underline=0``
    * - ``width``
      - How wide it is (in characters)
      - ``width=15``

| The ``image`` option needs a picture made first, e.g. ``dog_picture = tk.PhotoImage(file="dog.png")``.
| ttk Menubutton has no ``bg``, ``fg`` or ``font`` options. Change its colours and fonts with a style, e.g. ``style.configure("TMenubutton", foreground="purple")``.

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

        What is a ttk Menubutton?

        [x] A themed button that opens a drop-down menu | Correct. It holds a tk Menu.
        [ ] A menu bar | Incorrect. That is a Menu on the window.
        [ ] A button that runs one function | Incorrect. That is a Button.
        [ ] A list | Incorrect. That is a Listbox.

    .. multichoice::

        What kind of menu goes with a ttk Menubutton?

        [ ] ttk.Menu | Incorrect. There is no ttk Menu.
        [x] tk.Menu | Correct. ttk uses the normal tk Menu.
        [ ] ttk.Combobox | Incorrect. That is a different widget.
        [ ] A Frame | Incorrect. It needs a Menu.

    .. multichoice::

        Which line links the menu to the Menubutton?

        [x] food_button["menu"] = food_menu | Correct. Or food_button.config(menu=food_menu).
        [ ] food_menu.pack(food_button) | Incorrect. Menus are not packed.
        [ ] food_button.add(food_menu) | Incorrect. Not a method.
        [ ] food_button.link(food_menu) | Incorrect. Not a method.

    .. multichoice::

        What is the parent of the menu?

        [ ] root | Incorrect. The Menubutton is its parent.
        [x] The Menubutton | Correct. tk.Menu(food_button, tearoff=0).
        [ ] Another Menu | Incorrect. Not here.
        [ ] Nothing | Incorrect. It needs a parent.

    .. multichoice::

        What does width=12 mean?

        [x] About 12 characters wide | Correct. Text widgets count characters.
        [ ] 12 pixels | Incorrect. Characters.
        [ ] 12 items | Incorrect. It sets width.
        [ ] 12 lines | Incorrect. Not lines.

    .. multichoice::

        What does direction="above" do?

        [ ] Moves the button up | Incorrect. It moves the menu.
        [x] Opens the menu above the button | Correct. direction sets where the menu appears.
        [ ] Opens it on the right | Incorrect. That is "right".
        [ ] Hides the menu | Incorrect. It moves it.

    .. multichoice::

        What is the default direction?

        [ ] "above" | Incorrect. The default is below.
        [x] "below" | Correct. Menus open below by default.
        [ ] "left" | Incorrect. Not the default.
        [ ] "flush" | Incorrect. Not the default.

    .. multichoice::

        Which line greys out a ttk Menubutton?

        [x] food_button.state(["disabled"]) | Correct. ttk uses the state method.
        [ ] food_button.config(bg="grey") | Incorrect. ttk has no bg.
        [ ] food_button.disable() | Incorrect. Not a method.
        [ ] food_menu.state(["disabled"]) | Incorrect. Change the button.

    .. multichoice::

        What does padding=5 do?

        [ ] Adds 5 menu items | Incorrect. It adds space.
        [x] Adds space inside the button around the words | Correct. padding pads the inside.
        [ ] Moves the menu | Incorrect. direction does that.
        [ ] Makes the menu bigger | Incorrect. It pads the button.

    .. multichoice::

        How can the button show the chosen item?

        [ ] It happens by itself | Incorrect. You must change it.
        [x] Run food_button.config(text=choice) when an item is chosen | Correct. Use the item's command.
        [ ] Use text= on the menu | Incorrect. Menu items use label.
        [ ] Use direction= | Incorrect. That moves the menu.

    .. multichoice::

        What does add_checkbutton add?

        [x] A menu item with a tick that turns on and off | Correct. Each has its own variable.
        [ ] A ttk Checkbutton widget | Incorrect. It is a menu item.
        [ ] A separator | Incorrect. add_separator does that.
        [ ] A new menu | Incorrect. add_cascade does that.

    .. multichoice::

        What does add_radiobutton add?

        [ ] A tick item | Incorrect. add_checkbutton does that.
        [x] A menu item where only one in the group can be chosen | Correct. They share a variable.
        [ ] A new Menubutton | Incorrect. It adds an item.
        [ ] A line | Incorrect. add_separator does that.

    .. multichoice::

        For add_radiobutton items in one group, what is the same?

        [x] The variable | Correct. The shared variable groups them.
        [ ] The value | Incorrect. Values differ.
        [ ] The label | Incorrect. Labels differ.
        [ ] Nothing | Incorrect. The variable is shared.

    .. multichoice::

        Which style name is used for every ttk Menubutton?

        [ ] "Menubutton" | Incorrect. Use TMenubutton.
        [x] "TMenubutton" | Correct. T then the widget name.
        [ ] "TMenu" | Incorrect. Not the name.
        [ ] "TButton" | Incorrect. That is for Buttons.

    .. multichoice::

        How do you change the font of every Menubutton?

        [x] style.configure("TMenubutton", font=("Arial", 14)) | Correct. ttk uses styles.
        [ ] food_button.config(font=14) | Incorrect. ttk Menubutton has no font option.
        [ ] food_menu.config(font=14) | Incorrect. That changes the menu.
        [ ] root.font(14) | Incorrect. Not a method.

    .. multichoice::

        Can the menu's own colours and font be changed?

        [ ] No | Incorrect. They can.
        [x] Yes, with food_menu.config(bg=..., font=...) because it is a tk Menu | Correct. tk Menus do have these options.
        [ ] Only with a ttk style | Incorrect. tk Menus use config.
        [ ] Only on Windows | Incorrect. It works generally.

    .. multichoice::

        What does tearoff=0 do?

        [ ] Hides the button | Incorrect. It changes the menu.
        [x] Removes the dashed tear-off line at the top of the menu | Correct. Menus look cleaner.
        [ ] Disables the menu | Incorrect. state does that.
        [ ] Opens the menu | Incorrect. Clicking opens it.

    .. multichoice::

        Which method adds a plain clickable item?

        [x] add_command | Correct. It adds an item that runs a function.
        [ ] add_item | Incorrect. Not a method.
        [ ] add_cascade | Incorrect. That adds a sub-menu.
        [ ] add_separator | Incorrect. That adds a line.

    .. multichoice::

        Which widget does a similar job and shows the choice by itself?

        [ ] ttk.Label | Incorrect. Labels do not open menus.
        [x] ttk.Combobox | Correct. A readonly Combobox picks one choice and shows it.
        [ ] ttk.Progressbar | Incorrect. It shows progress.
        [ ] ttk.Separator | Incorrect. It draws a line.

    .. multichoice::

        What happens when the Menubutton is clicked?

        [x] Its menu drops down | Correct. That is its job.
        [ ] A function runs straight away | Incorrect. Menu items run functions.
        [ ] The window closes | Incorrect. Not unless an item does that.
        [ ] Nothing | Incorrect. The menu opens.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a ttk Menubutton and its menu.

        food_button = ttk.@@Menubutton | Button | Combobox@@(root, text="Food", width=12)
        food_menu = tk.@@Menu | Menubutton | Frame@@(food_button, tearoff=0)
        food_button["@@menu | items | list@@"] = food_menu

    .. cloze::
        :instructions: Add items that show the choice.

        food_menu.@@add_command | add_cascade | add_item@@(label="Pizza", command=lambda: food_button.config(@@text | label | value@@="Pizza"))

    .. cloze::
        :instructions: Add tick items.

        cheese = tk.IntVar()
        food_menu.@@add_checkbutton | add_radiobutton | add_command@@(label="Extra cheese", variable=cheese)

    .. cloze::
        :instructions: Add choice items that share a variable.

        size = tk.StringVar(value="Small")
        size_menu.@@add_radiobutton | add_checkbutton | add_choice@@(label="Small", variable=size, @@value | label | text@@="Small")

    .. cloze::
        :instructions: Open the menu above and turn the button off.

        food_button.config(@@direction | side | anchor@@="above")
        food_button.@@state | config | set@@(["disabled"])

----

.. admonition:: Tasks

    #. Make a window titled "Pets" that is 300x200 with a ttk Menubutton "Pets" whose menu has the commands "Dog", "Cat" and "Fish".
    #. Make each command change a label to show "You chose" and the pet.
    #. Make a ttk Menubutton that uses ``textvariable`` and ``add_radiobutton`` to choose a colour: "Red", "Green" or "Blue".
    #. Style your Menubuttons with Arial size 14 and padding of 10.

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
                    root.title("Pets")

                    pet_button = ttk.Menubutton(root, text="Pets")
                    pet_menu = tk.Menu(pet_button, tearoff=0)
                    for pet in ["Dog", "Cat", "Fish"]:
                        pet_menu.add_command(label=pet)
                    pet_button.config(menu=pet_menu)
                    pet_button.pack(pady=30)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def choose(pet):
                        result_label.config(text="You chose " + pet)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Pets")

                    pet_button = ttk.Menubutton(root, text="Pets")
                    pet_menu = tk.Menu(pet_button, tearoff=0)
                    for pet in ["Dog", "Cat", "Fish"]:
                        pet_menu.add_command(label=pet, command=lambda pet=pet: choose(pet))
                    pet_button.config(menu=pet_menu)
                    pet_button.pack(pady=30)

                    result_label = ttk.Label(root, text="", font=("Arial", 14))
                    result_label.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Colours")

                    colour = tk.StringVar(value="Red")

                    colour_button = ttk.Menubutton(root, textvariable=colour, width=10)
                    colour_menu = tk.Menu(colour_button, tearoff=0)
                    for choice in ["Red", "Green", "Blue"]:
                        colour_menu.add_radiobutton(label=choice, variable=colour, value=choice)
                    colour_button.config(menu=colour_menu)
                    colour_button.pack(pady=40)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Colours")

                    style = ttk.Style()
                    style.configure("TMenubutton", font=("Arial", 14), padding=10)

                    colour = tk.StringVar(value="Red")

                    colour_button = ttk.Menubutton(root, textvariable=colour, width=10)
                    colour_menu = tk.Menu(colour_button, tearoff=0)
                    for choice in ["Red", "Green", "Blue"]:
                        colour_menu.add_radiobutton(label=choice, variable=colour, value=choice)
                    colour_button.config(menu=colour_menu)
                    colour_button.pack(pady=40)

                    root.mainloop()
