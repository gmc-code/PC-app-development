====================================================
tk OptionMenu
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.OptionMenu>`_

----

What is an OptionMenu?
-------------------------

| An **OptionMenu** is a drop-down list. It shows one choice. Clicking it opens a list of all the choices.
| Use an OptionMenu when the user picks **one** item from a list, but you want to save space in the window, e.g. choosing a country or a year level.

----

Making an OptionMenu
-------------------------

| An OptionMenu needs a **variable** to remember the chosen item.

#. **Create** a ``tk.StringVar()`` and set the starting choice.
#. **Create** the OptionMenu with ``tk.OptionMenu(root, variable, choice1, choice2, ...)``.
#. **Place** it in the window with ``.pack()``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first OptionMenu")

    flavour = tk.StringVar(value="Vanilla")     # 1. Variable with the starting choice

    flavour_menu = tk.OptionMenu(root, flavour, "Vanilla", "Chocolate", "Strawberry")   # 2. Create
    flavour_menu.pack(pady=20)                  # 3. Place it in the window

    root.mainloop()                 # Keep the window open

| The OptionMenu is different from other widgets: the **variable** and the **choices** are written straight after ``root``, not as ``option=value``.

----

Using a Python list of choices
---------------------------------

| If the choices are in a Python list, put a ``*`` in front of the list name.
| The ``*`` "unpacks" the list, so each item becomes a separate choice.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("List of choices")

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    day = tk.StringVar(value=days[0])           # Start on the first item in the list

    day_menu = tk.OptionMenu(root, day, *days)
    day_menu.pack(pady=20)

    root.mainloop()

----

OptionMenu options
---------------------

command
~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function as soon as the user picks a choice.
| **How to write it:** add ``command=function_name`` at the **end**, after the choices.
| The OptionMenu sends the chosen item to the function, so the function needs a **parameter** to receive it.

.. code-block:: python

    import tkinter as tk


    def change_colour(choice):
        root.config(bg=choice)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("command")

    colour = tk.StringVar(value="white")

    colour_menu = tk.OptionMenu(root, colour, "white", "pink", "lightblue", "lightgreen",
                                command=change_colour)
    colour_menu.pack(pady=20)

    root.mainloop()

Changing the look with config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Other options **cannot** go inside ``tk.OptionMenu( )``. Use ``.config()`` after it has been made.
| Useful options:

- ``font`` - style and size of the words.
- ``width`` - width in characters.
- ``fg`` and ``bg`` - word colour and background colour.
- ``activebackground`` - colour when the mouse is over it.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    size = tk.StringVar(value="Medium")

    size_menu = tk.OptionMenu(root, size, "Small", "Medium", "Large")
    size_menu.config(font=("Arial", 16), width=10, bg="lightyellow", activebackground="gold")
    size_menu.pack(pady=20)

    root.mainloop()

Changing the drop-down list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The list that drops down is a separate **Menu**. Reach it with ``option_menu["menu"]``.
| Use ``.config()`` on it to change the font and colours of the list.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("drop-down list")

    animal = tk.StringVar(value="Koala")

    animal_menu = tk.OptionMenu(root, animal, "Koala", "Kangaroo", "Wombat", "Emu")
    animal_menu.config(font=("Arial", 16))
    animal_menu["menu"].config(font=("Arial", 16), bg="lightgreen")     # The list that drops down
    animal_menu.pack(pady=20)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** turns the OptionMenu on or off.
| **How to write it:** ``option_menu.config(state="disabled")``
| **Values:** ``"normal"`` (the default) and ``"disabled"`` (greyed out).

.. code-block:: python

    import tkinter as tk


    def lock():
        year_menu.config(state="disabled")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    year = tk.StringVar(value="Year 7")

    year_menu = tk.OptionMenu(root, year, "Year 7", "Year 8", "Year 9")
    year_menu.pack(pady=10)

    lock_button = tk.Button(root, text="Lock my choice", command=lock)
    lock_button.pack()

    root.mainloop()

----

OptionMenu methods
---------------------

| A **method** is an action that a widget can do. Methods are written after a dot.

get (the variable)
~~~~~~~~~~~~~~~~~~~~~

| **What it does:** reads the chosen item.
| **How to write it:** ``choice = variable.get()``

.. code-block:: python

    import tkinter as tk


    def show():
        result_label.config(text="You picked " + pet.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("get")

    pet = tk.StringVar(value="Dog")

    pet_menu = tk.OptionMenu(root, pet, "Dog", "Cat", "Rabbit")
    pet_menu.pack(pady=10)

    show_button = tk.Button(root, text="Show", command=show)
    show_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()

set (the variable)
~~~~~~~~~~~~~~~~~~~~~

| **What it does:** chooses an item from your code.
| **How to write it:** ``variable.set("choice")``

.. code-block:: python

    import tkinter as tk


    def reset():
        team.set("Red")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("set")

    team = tk.StringVar(value="Red")

    team_menu = tk.OptionMenu(root, team, "Red", "Blue", "Green", "Yellow")
    team_menu.pack(pady=10)

    reset_button = tk.Button(root, text="Reset", command=reset)
    reset_button.pack()

    root.mainloop()

Using the choice in a calculation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| A **dictionary** can link each choice to a number. Use the chosen item to look up its number.

.. code-block:: python

    import tkinter as tk

    prices = {"Small": 3, "Medium": 4, "Large": 5}


    def show_price(choice):
        price_label.config(text=f"Price: ${prices[choice]}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Drink sizes")

    size = tk.StringVar(value="Small")

    size_menu = tk.OptionMenu(root, size, *prices, command=show_price)
    size_menu.pack(pady=10)

    price_label = tk.Label(root, text="Price: $3", font=("Arial", 16))
    price_label.pack()

    root.mainloop()

| ``*prices`` unpacks the **keys** of the dictionary: "Small", "Medium" and "Large".

Changing the choices while the program runs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| To change the list of choices:

#. ``menu.delete(0, "end")`` removes all the old choices.
#. ``menu.add_command(label=..., command=...)`` adds each new choice.

| ``lambda item=item: food.set(item)`` makes each choice set the variable to its own word when clicked.

.. code-block:: python

    import tkinter as tk


    def show_fruit():
        change_choices(["Apple", "Banana", "Mango"])


    def show_vegetables():
        change_choices(["Carrot", "Pea", "Potato"])


    def change_choices(new_choices):
        menu = food_menu["menu"]
        menu.delete(0, "end")                   # 1. Remove the old choices
        for item in new_choices:                # 2. Add the new ones
            menu.add_command(label=item, command=lambda item=item: food.set(item))
        food.set(new_choices[0])                # Show the first new choice


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Changing choices")

    food = tk.StringVar(value="Apple")

    food_menu = tk.OptionMenu(root, food, "Apple", "Banana", "Mango")
    food_menu.pack(pady=10)

    fruit_button = tk.Button(root, text="Fruit", command=show_fruit)
    fruit_button.pack(pady=2)

    veg_button = tk.Button(root, text="Vegetables", command=show_vegetables)
    veg_button.pack(pady=2)

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
    * - ``tk.OptionMenu(root, var, ...)``
      - Make the drop-down list
      - ``tk.OptionMenu(root, size, "S", "M")``
    * - ``*list``
      - Use every item in a Python list
      - ``tk.OptionMenu(root, day, *days)``
    * - ``command``
      - Function to run when a choice is picked
      - ``command=show_price``
    * - ``config(font=...)``
      - Font of the button
      - ``menu.config(font=("Arial", 14))``
    * - ``config(width=...)``
      - Width in characters
      - ``menu.config(width=10)``
    * - ``config(bg=...)``
      - Background colour
      - ``menu.config(bg="lightyellow")``
    * - ``["menu"].config()``
      - Change the list that drops down
      - ``menu["menu"].config(bg="pink")``
    * - ``config(state=...)``
      - Turn it on or off
      - ``menu.config(state="disabled")``
    * - ``variable.get()``
      - Read the chosen item
      - ``size.get()``
    * - ``variable.set()``
      - Choose an item from code
      - ``size.set("Large")``

----

.. admonition:: Tasks

    #. Make a window titled "Holidays" that is 300x200. Add an OptionMenu with the choices "Beach", "Snow", "City" and "Camping". Start on "Beach".
    #. Change your OptionMenu to use Arial size 14, a width of 12 and a light blue background.
    #. Make a Python list of five colours and use ``*`` to put them in an OptionMenu. Use ``command`` so the window background changes to the colour picked.
    #. Make an OptionMenu with the choices "Year 7", "Year 8" and "Year 9", a "Show" button and a label. When clicked, the label shows "Welcome to" followed by the chosen year.

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
                    root.title("Holidays")

                    holiday = tk.StringVar(value="Beach")

                    holiday_menu = tk.OptionMenu(root, holiday, "Beach", "Snow", "City", "Camping")
                    holiday_menu.pack(pady=20)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Holidays")

                    holiday = tk.StringVar(value="Beach")

                    holiday_menu = tk.OptionMenu(root, holiday, "Beach", "Snow", "City", "Camping")
                    holiday_menu.config(font=("Arial", 14), width=12, bg="lightblue")
                    holiday_menu.pack(pady=20)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk


                    def change_colour(choice):
                        root.config(bg=choice)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Colours")

                    colours = ["white", "pink", "orange", "lightgreen", "skyblue"]

                    colour = tk.StringVar(value=colours[0])

                    colour_menu = tk.OptionMenu(root, colour, *colours, command=change_colour)
                    colour_menu.pack(pady=20)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def show():
                        result_label.config(text="Welcome to " + year.get())


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Year level")

                    year = tk.StringVar(value="Year 7")

                    year_menu = tk.OptionMenu(root, year, "Year 7", "Year 8", "Year 9")
                    year_menu.pack(pady=10)

                    show_button = tk.Button(root, text="Show", command=show)
                    show_button.pack()

                    result_label = tk.Label(root, text="", font=("Arial", 14))
                    result_label.pack(pady=10)

                    root.mainloop()
