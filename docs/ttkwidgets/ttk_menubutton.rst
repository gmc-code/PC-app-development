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
