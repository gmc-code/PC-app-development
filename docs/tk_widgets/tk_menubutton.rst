====================================================
tk Menubutton
====================================================

| See: `<https://www.tcl-lang.org/man/tcl8.6/TkCmd/menubutton.htm>`_

----

What is a Menubutton?
------------------------

| A **Menubutton** is a button that opens a drop-down **Menu** when it is clicked.
| Unlike a menu bar, a Menubutton can be placed **anywhere** in the window, like any other widget.
| Use it when you want a small drop-down list of commands or choices next to other widgets.

----

Making a Menubutton
----------------------

| A Menubutton and its Menu are made together:

#. **Create** the Menubutton with ``tk.Menubutton(root, text="...")``.
#. **Create** a Menu that belongs to the Menubutton: ``tk.Menu(menubutton, tearoff=0)``.
#. **Add** commands to the Menu.
#. **Link** the Menu to the Menubutton with ``menubutton.config(menu=the_menu)``.
#. **Place** the Menubutton with ``.pack()``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library


    def say(word):
        message_label.config(text=word)


    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first Menubutton")

    greet_button = tk.Menubutton(root, text="Greetings", relief="raised")   # 1. Create it

    greet_menu = tk.Menu(greet_button, tearoff=0)                           # 2. Its menu
    greet_menu.add_command(label="Hello", command=lambda: say("Hello!"))    # 3. Add commands
    greet_menu.add_command(label="Goodbye", command=lambda: say("Goodbye!"))

    greet_button.config(menu=greet_menu)                                    # 4. Link them
    greet_button.pack(pady=20)                                              # 5. Place it

    message_label = tk.Label(root, text="", font=("Arial", 16))
    message_label.pack()

    root.mainloop()                 # Keep the window open

| ``lambda:`` lets each command send different words to the same function. See the **Button** page for more about ``lambda``.

----

Menubutton options
---------------------

| Options are written as ``option=value`` inside ``tk.Menubutton( )``, separated by commas.

text
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the words on the Menubutton.
| **How to write it:** ``text="your words"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("text")

    options_button = tk.Menubutton(root, text="Options ▼", relief="raised")
    options_menu = tk.Menu(options_button, tearoff=0)
    options_menu.add_command(label="Settings")
    options_menu.add_command(label="Help")
    options_button.config(menu=options_menu)
    options_button.pack(pady=20)

    root.mainloop()

| Adding ``▼`` to the words shows the user that a list will drop down.

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** set the border style and thickness.
| **How to write them:** ``relief="raised", borderwidth=2``
| A Menubutton is ``"flat"`` by default, so it looks like a label. ``relief="raised"`` makes it look like a button the user can click.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("relief")

    flat_button = tk.Menubutton(root, text="Flat (default)")
    flat_button.pack(pady=10)

    raised_button = tk.Menubutton(root, text="Raised", relief="raised", borderwidth=2)
    raised_button.pack(pady=10)

    root.mainloop()

font, fg and bg
~~~~~~~~~~~~~~~~~~

| **What they do:** ``font`` sets the style and size of the words. ``fg`` and ``bg`` set the word and background colours.
| **How to write them:** ``font=("Arial", 14)``, ``fg="white"``, ``bg="green"``
| These change the **button**. Give the Menu its own ``font``, ``fg`` and ``bg`` to change the drop-down list.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("font, fg and bg")

    food_button = tk.Menubutton(root, text="Food ▼", relief="raised",
                                font=("Arial", 14), fg="white", bg="green")
    food_menu = tk.Menu(food_button, tearoff=0, font=("Arial", 14), bg="lightgreen")
    food_menu.add_command(label="Pizza")
    food_menu.add_command(label="Pasta")
    food_button.config(menu=food_menu)
    food_button.pack(pady=20)

    root.mainloop()

activebackground and activeforeground
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** set the colours of the Menubutton while the mouse is over it.
| **How to write them:** ``activebackground="gold"``, ``activeforeground="black"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("active colours")

    pick_button = tk.Menubutton(root, text="Hover over me", relief="raised", bg="lightgray",
                                activebackground="gold", activeforeground="black")
    pick_menu = tk.Menu(pick_button, tearoff=0)
    pick_menu.add_command(label="One")
    pick_menu.add_command(label="Two")
    pick_button.config(menu=pick_menu)
    pick_button.pack(pady=20)

    root.mainloop()

width, height, padx and pady
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``width`` and ``height`` set the size in characters and lines. ``padx`` and ``pady`` add space inside around the words.
| **How to write them:** ``width=15``, ``height=2``, ``padx=10``, ``pady=5``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("size")

    big_button = tk.Menubutton(root, text="Big menu", relief="raised",
                               width=15, height=2, padx=10, pady=5)
    big_menu = tk.Menu(big_button, tearoff=0)
    big_menu.add_command(label="Item")
    big_button.config(menu=big_menu)
    big_button.pack(pady=20)

    root.mainloop()

direction
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses where the menu appears when it opens.
| **How to write it:** ``direction="above"``
| **Values:** ``"below"`` (the default), ``"above"``, ``"left"``, ``"right"``.
| ``"above"`` is useful for a Menubutton near the bottom of the window.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("direction")

    up_button = tk.Menubutton(root, text="Opens upwards ▲", relief="raised", direction="above")
    up_menu = tk.Menu(up_button, tearoff=0)
    up_menu.add_command(label="First")
    up_menu.add_command(label="Second")
    up_button.config(menu=up_menu)
    up_button.pack(side="bottom", pady=10)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** turns the Menubutton on or off.
| **How to write it:** ``state="disabled"``
| **Values:** ``"normal"`` (the default) and ``"disabled"`` (greyed out; the menu will not open).

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    locked_button = tk.Menubutton(root, text="Locked ▼", relief="raised", state="disabled")
    locked_menu = tk.Menu(locked_button, tearoff=0)
    locked_menu.add_command(label="Secret")
    locked_button.config(menu=locked_menu)
    locked_button.pack(pady=20)

    root.mainloop()

----

Menubutton methods
---------------------

| A Menubutton uses the **Menu** methods for the commands in its list. The most useful are below. See the **Menu** page for all of them.

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options **after** the Menubutton has been made, e.g. its words.
| **How to write it:** ``menubutton.config(option=value)``
| A common use is to show the user's choice on the Menubutton itself.

.. code-block:: python

    import tkinter as tk


    def choose(sport):
        sport_button.config(text=sport + " ▼")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    sport_button = tk.Menubutton(root, text="Choose a sport ▼", relief="raised", width=18)
    sport_menu = tk.Menu(sport_button, tearoff=0)
    for sport in ["Cricket", "Netball", "Soccer", "Tennis"]:
        sport_menu.add_command(label=sport, command=lambda sport=sport: choose(sport))
    sport_button.config(menu=sport_menu)
    sport_button.pack(pady=20)

    root.mainloop()

| ``lambda sport=sport:`` makes each command remember its own sport. Without ``sport=sport``, every command would use the **last** sport in the loop.

add_checkbutton
~~~~~~~~~~~~~~~~~~

| **What it does:** adds items that can be ticked on and off. Each needs its own ``IntVar``.
| **How to write it:** ``menu.add_checkbutton(label="words", variable=int_var)``

.. code-block:: python

    import tkinter as tk


    def show():
        chosen = []
        if cheese.get() == 1:
            chosen.append("cheese")
        if ham.get() == 1:
            chosen.append("ham")
        if olives.get() == 1:
            chosen.append("olives")
        result_label.config(text="Toppings: " + ", ".join(chosen))


    root = tk.Tk()
    root.geometry("300x200")
    root.title("add_checkbutton")

    cheese = tk.IntVar()
    ham = tk.IntVar()
    olives = tk.IntVar()

    topping_button = tk.Menubutton(root, text="Toppings ▼", relief="raised")
    topping_menu = tk.Menu(topping_button, tearoff=0)
    topping_menu.add_checkbutton(label="Cheese", variable=cheese, command=show)
    topping_menu.add_checkbutton(label="Ham", variable=ham, command=show)
    topping_menu.add_checkbutton(label="Olives", variable=olives, command=show)
    topping_button.config(menu=topping_menu)
    topping_button.pack(pady=20)

    result_label = tk.Label(root, text="Toppings: ")
    result_label.pack()

    root.mainloop()

add_radiobutton
~~~~~~~~~~~~~~~~~~

| **What it does:** adds a group of items where only **one** can be chosen. They share one variable.
| **How to write it:** ``menu.add_radiobutton(label="words", variable=string_var, value="value")``

.. code-block:: python

    import tkinter as tk


    def show():
        size_button.config(text="Size: " + size.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("add_radiobutton")

    size = tk.StringVar(value="Medium")

    size_button = tk.Menubutton(root, text="Size: Medium", relief="raised", width=15)
    size_menu = tk.Menu(size_button, tearoff=0)
    for choice in ["Small", "Medium", "Large"]:
        size_menu.add_radiobutton(label=choice, variable=size, value=choice, command=show)
    size_button.config(menu=size_menu)
    size_button.pack(pady=20)

    root.mainloop()

----

Menubutton, OptionMenu or menu bar?
---------------------------------------

.. list-table::
    :header-rows: 1
    :widths: 30 70

    * - Widget
      - Best for
    * - Menu bar
      - Commands for the whole app (File, Edit, Help) along the top of the window
    * - Menubutton
      - A drop-down list of **commands** placed anywhere in the window
    * - OptionMenu
      - Choosing **one value** from a list; it always shows the current choice

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
      - Words on the button
      - ``text="Options ▼"``
    * - ``menu``
      - The Menu that drops down
      - ``mb.config(menu=my_menu)``
    * - ``relief``, ``borderwidth``
      - Border style and thickness
      - ``relief="raised"``
    * - ``font``, ``fg``, ``bg``
      - Font and colours of the button
      - ``font=("Arial", 14)``
    * - ``activebackground``
      - Colour when the mouse is over it
      - ``activebackground="gold"``
    * - ``width``, ``height``
      - Size in characters and lines
      - ``width=15``
    * - ``direction``
      - Where the menu opens
      - ``direction="above"``
    * - ``state``
      - Turn it on or off
      - ``state="disabled"``
    * - ``add_command()``
      - Add a command to the menu
      - ``my_menu.add_command(label="Hi")``
    * - ``add_checkbutton()``
      - Add a tick-on/tick-off item
      - ``add_checkbutton(label="Ham", variable=ham)``
    * - ``add_radiobutton()``
      - Add a choose-one item
      - ``add_radiobutton(label="S", variable=size, value="S")``
    * - ``config()``
      - Change options later
      - ``mb.config(text="New")``

----

All Menubutton options
---------------------------

| Here is every option a Menubutton can have, for reference. You will only need a few of them most of the time.

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
    * - ``compound``
      - Where the picture goes compared to the words
      - ``compound="left"``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``direction``
      - Where the menu appears: ``"below"``, ``"above"``, ``"left"``, ``"right"`` or ``"flush"``
      - ``direction="above"``
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
      - ``True`` shows a small box that tells you a menu drops down
      - ``indicatoron=True``
    * - ``justify``
      - Lines up many lines of words: ``"left"``, ``"center"`` or ``"right"``
      - ``justify="left"``
    * - ``menu``
      - The menu that drops down when it is clicked
      - ``menu=food_menu``
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
      - ``"normal"`` (can click), ``"active"`` or ``"disabled"`` (greyed out)
      - ``state="disabled"``
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
    * - ``wraplength``
      - Starts a new line when the words get this long (in pixels)
      - ``wraplength=100``

| The picture option (``image``) needs a picture made first, e.g. ``dog_picture = tk.PhotoImage(file="dog.png")``.

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

        What is a Menubutton?

        [x] A button that opens a drop-down menu when clicked | Correct. It holds a menu.
        [ ] A button that runs one function | Incorrect. That is a Button.
        [ ] A menu bar | Incorrect. That is a Menu on the window.
        [ ] A tick box | Incorrect. That is a Checkbutton.

    .. multichoice::

        What two things are needed to make a Menubutton work?

        [ ] A Label and a Frame | Incorrect. They are not needed.
        [x] The Menubutton and a Menu linked with menu= | Correct. The menu holds the items.
        [ ] Two Buttons | Incorrect. Not needed.
        [ ] An Entry and a Button | Incorrect. Not needed.

    .. multichoice::

        Which line links a menu to a Menubutton called food_button?

        [x] food_button.config(menu=food_menu) | Correct. The menu option links them.
        [ ] food_menu.pack(food_button) | Incorrect. Menus are not packed.
        [ ] food_button.add(food_menu) | Incorrect. Not a method.
        [ ] food_button.menu(food_menu) | Incorrect. Not a method.

    .. multichoice::

        When making the Menu, what is its parent?

        [ ] root | Incorrect. The Menubutton is the parent.
        [x] The Menubutton | Correct. tk.Menu(food_button, tearoff=0).
        [ ] Another Menu | Incorrect. Not here.
        [ ] Nothing | Incorrect. It needs a parent.

    .. multichoice::

        Which option sets the words on the Menubutton?

        [ ] label | Incorrect. label is for menu items.
        [x] text | Correct. text sets the button words.
        [ ] title | Incorrect. title is for windows.
        [ ] name | Incorrect. Not used.

    .. multichoice::

        Why use relief="raised" on a Menubutton?

        [x] So it looks like a button that can be clicked | Correct. By default it can look flat.
        [ ] To open the menu | Incorrect. Clicking opens it.
        [ ] To colour it | Incorrect. bg colours it.
        [ ] To make it bigger | Incorrect. width does that.

    .. multichoice::

        What does direction="above" do?

        [ ] Moves the button up | Incorrect. It moves the menu.
        [x] Opens the menu above the button | Correct. direction sets where the menu appears.
        [ ] Opens the menu below | Incorrect. That is "below", the default.
        [ ] Hides the menu | Incorrect. It changes where it shows.

    .. multichoice::

        What does activebackground change on a Menubutton?

        [ ] The menu items | Incorrect. The menu has its own options.
        [x] The button colour when the mouse is over it | Correct. It is the hover colour.
        [ ] The window | Incorrect. Only the Menubutton.
        [ ] The word colour when disabled | Incorrect. disabledforeground does that.

    .. multichoice::

        What does state="disabled" do?

        [x] Greys out the Menubutton so the menu will not open | Correct. It cannot be used.
        [ ] Deletes the menu | Incorrect. It just turns it off.
        [ ] Opens the menu | Incorrect. It stops it opening.
        [ ] Changes the text | Incorrect. config(text=) does that.

    .. multichoice::

        Which line changes the Menubutton's words to show the choice?

        [ ] food_button.set("Pizza") | Incorrect. Not a method.
        [x] food_button.config(text="Pizza") | Correct. config changes text.
        [ ] food_menu.config(text="Pizza") | Incorrect. That changes the menu, not the button.
        [ ] food_button.text = "Pizza" | Incorrect. Use config.

    .. multichoice::

        What does add_checkbutton add to the menu?

        [ ] A Button | Incorrect. It adds a menu item.
        [x] An item with a tick that turns on and off | Correct. Each one has its own variable.
        [ ] A separator | Incorrect. add_separator does that.
        [ ] A new Menubutton | Incorrect. It adds an item.

    .. multichoice::

        What does add_radiobutton add?

        [ ] A tick item | Incorrect. add_checkbutton does that.
        [x] An item where only one in the group can be chosen | Correct. They share a variable.
        [ ] A Radiobutton widget | Incorrect. It is a menu item.
        [ ] A line | Incorrect. add_separator does that.

    .. multichoice::

        For add_radiobutton items, what must be the same?

        [x] The variable | Correct. The shared variable groups them.
        [ ] The value | Incorrect. Each needs a different value.
        [ ] The label | Incorrect. Each has its own label.
        [ ] Nothing | Incorrect. They must share a variable.

    .. multichoice::

        For add_radiobutton items, what must be different?

        [ ] The variable | Incorrect. That must be the same.
        [x] The value | Correct. Each item stores its own value.
        [ ] The menu | Incorrect. They are in the same menu.
        [ ] The parent | Incorrect. Same parent.

    .. multichoice::

        What do padx and pady do on a Menubutton?

        [ ] Move the menu | Incorrect. direction does that.
        [x] Add space inside the button around the words | Correct. They make it bigger.
        [ ] Add items | Incorrect. add_command does that.
        [ ] Change colours | Incorrect. bg and fg do that.

    .. multichoice::

        How can a menu item update the Menubutton text when chosen?

        [x] Give it command=lambda: food_button.config(text="Pizza") | Correct. The command runs when chosen.
        [ ] It happens by itself | Incorrect. You must change it.
        [ ] Use text= on the menu item | Incorrect. Menu items use label.
        [ ] Use direction= | Incorrect. direction moves the menu.

    .. multichoice::

        What does tearoff=0 do in tk.Menu(food_button, tearoff=0)?

        [ ] Hides the Menubutton | Incorrect. It removes the dashed line.
        [x] Removes the dashed tear-off line at the top of the menu | Correct. Cleaner menus.
        [ ] Opens the menu | Incorrect. Clicking opens it.
        [ ] Disables the menu | Incorrect. state does that.

    .. multichoice::

        Which widget is most like a Menubutton, but shows the chosen item automatically?

        [ ] Label | Incorrect. Labels do not open menus.
        [x] OptionMenu | Correct. OptionMenu is a ready-made Menubutton with choices.
        [ ] Entry | Incorrect. Entries are for typing.
        [ ] Canvas | Incorrect. Canvas is for drawing.

    .. multichoice::

        What does font=("Arial", 14) change?

        [ ] The menu items | Incorrect. The menu has its own font.
        [x] The words on the Menubutton | Correct. It styles the button text.
        [ ] The window title | Incorrect. root.title does that.
        [ ] Nothing | Incorrect. It changes the button font.

    .. multichoice::

        What does width=12 mean on a text Menubutton?

        [x] About 12 characters wide | Correct. Text widgets count characters.
        [ ] 12 pixels | Incorrect. It counts characters.
        [ ] 12 menu items | Incorrect. It sets width.
        [ ] 12 lines | Incorrect. height counts lines.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a Menubutton and its menu.

        food_button = tk.@@Menubutton | Button | Menu@@(root, text="Food", @@relief | border | style@@="raised")
        food_menu = tk.@@Menu | Menubutton | Frame@@(food_button, tearoff=0)
        food_button.@@config | pack | add@@(menu=food_menu)

    .. cloze::
        :instructions: Add items to the menu.

        food_menu.@@add_command | add_cascade | add_item@@(label="Pizza", command=pick_pizza)
        food_menu.add_command(@@label | text | name@@="Pasta", command=pick_pasta)

    .. cloze::
        :instructions: Add tick items.

        cheese = tk.IntVar()
        food_menu.@@add_checkbutton | add_radiobutton | add_tick@@(label="Extra cheese", @@variable | value | text@@=cheese)

    .. cloze::
        :instructions: Add choice items that share a variable.

        size = tk.StringVar(value="Small")
        size_menu.add_radiobutton(label="Small", variable=@@size | value | Small@@, value="Small")
        size_menu.add_radiobutton(label="Large", variable=size, @@value | variable | label@@="Large")

    .. cloze::
        :instructions: Open the menu above and show the choice.

        food_button.config(@@direction | side | anchor@@="above")
        food_button.config(@@text | label | menu@@="Pizza")

----

.. admonition:: Tasks

    #. Make a window titled "Pets" that is 300x200. Add a raised Menubutton with the words "Pets ▼" whose menu has the commands "Dog", "Cat" and "Fish".
    #. Make each command change a label to show "You chose" and the pet.
    #. Give your Menubutton a light blue background, Arial size 14 and a gold colour when the mouse is over it.
    #. Make a Menubutton "Extras ▼" with two tick-on/tick-off items, "Sound" and "Music", each with its own ``IntVar``.

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
                    root.title("Pets")

                    pet_button = tk.Menubutton(root, text="Pets ▼", relief="raised")
                    pet_menu = tk.Menu(pet_button, tearoff=0)
                    pet_menu.add_command(label="Dog")
                    pet_menu.add_command(label="Cat")
                    pet_menu.add_command(label="Fish")
                    pet_button.config(menu=pet_menu)
                    pet_button.pack(pady=20)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk


                    def choose(pet):
                        result_label.config(text="You chose " + pet)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Pets")

                    pet_button = tk.Menubutton(root, text="Pets ▼", relief="raised")
                    pet_menu = tk.Menu(pet_button, tearoff=0)
                    pet_menu.add_command(label="Dog", command=lambda: choose("Dog"))
                    pet_menu.add_command(label="Cat", command=lambda: choose("Cat"))
                    pet_menu.add_command(label="Fish", command=lambda: choose("Fish"))
                    pet_button.config(menu=pet_menu)
                    pet_button.pack(pady=20)

                    result_label = tk.Label(root, text="", font=("Arial", 14))
                    result_label.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk


                    def choose(pet):
                        result_label.config(text="You chose " + pet)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Pets")

                    pet_button = tk.Menubutton(root, text="Pets ▼", relief="raised",
                                               bg="lightblue", font=("Arial", 14),
                                               activebackground="gold")
                    pet_menu = tk.Menu(pet_button, tearoff=0)
                    pet_menu.add_command(label="Dog", command=lambda: choose("Dog"))
                    pet_menu.add_command(label="Cat", command=lambda: choose("Cat"))
                    pet_menu.add_command(label="Fish", command=lambda: choose("Fish"))
                    pet_button.config(menu=pet_menu)
                    pet_button.pack(pady=20)

                    result_label = tk.Label(root, text="", font=("Arial", 14))
                    result_label.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Extras")

                    sound = tk.IntVar()
                    music = tk.IntVar()

                    extras_button = tk.Menubutton(root, text="Extras ▼", relief="raised")
                    extras_menu = tk.Menu(extras_button, tearoff=0)
                    extras_menu.add_checkbutton(label="Sound", variable=sound)
                    extras_menu.add_checkbutton(label="Music", variable=music)
                    extras_button.config(menu=extras_menu)
                    extras_button.pack(pady=20)

                    root.mainloop()
