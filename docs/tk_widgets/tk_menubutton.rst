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
