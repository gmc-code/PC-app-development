====================================================
ttk Combobox
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#combobox>`_

----

What is a Combobox?
----------------------

| A **Combobox** is a drop-down list. It is an **Entry** box with an arrow: clicking the arrow shows a list of choices.
| The user can pick a choice from the list, and (unless it is readonly) can also type their own answer.
| Use it for picking one item from a list, e.g. a country, a year level or a colour. tk has no Combobox; it only comes with ttk.

----

Making a Combobox
--------------------

#. **Create** the Combobox with ``ttk.Combobox(root, values=[...])``.
#. **Choose** the starting item with ``.set()`` or ``.current()``.
#. **Place** it with ``.pack()``.

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first Combobox")

    fruit_box = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"])   # 1. Create it
    fruit_box.set("Apple")                                                 # 2. Starting item
    fruit_box.pack(pady=30)                                                # 3. Place it

    root.mainloop()                 # Keep the window open

----

Combobox options
-------------------

values
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the list of choices.
| **How to write it:** ``values=["one", "two", "three"]`` or ``values=my_list``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("values")

    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    planet_box = ttk.Combobox(root, values=planets)
    planet_box.set("Earth")
    planet_box.pack(pady=30)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** controls whether the user can type their own answer.
| **Values:**

- ``"normal"`` - pick from the list **or** type (the default).
- ``"readonly"`` - pick from the list only. Use this when only the listed choices are allowed.
- ``"disabled"`` - greyed out.

| **How to write it:** ``state="readonly"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    ttk.Label(root, text="Type or pick:").pack()
    any_box = ttk.Combobox(root, values=["Red", "Green", "Blue"])
    any_box.pack(pady=5)

    ttk.Label(root, text="Pick only:").pack()
    pick_box = ttk.Combobox(root, values=["Red", "Green", "Blue"], state="readonly")
    pick_box.set("Red")
    pick_box.pack(pady=5)

    root.mainloop()

width and font
~~~~~~~~~~~~~~~~~

| **What they do:** ``width`` sets the width in characters. ``font`` sets the style and size of the text in the box.
| **How to write them:** ``width=25, font=("Arial", 14)``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and font")

    country_box = ttk.Combobox(root, values=["Australia", "New Zealand", "Fiji"],
                               width=20, font=("Arial", 14))
    country_box.set("Australia")
    country_box.pack(pady=30)

    root.mainloop()

| ``font`` only changes the box. To change the drop-down list too, see **Styling a Combobox** below.

height
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how many choices the drop-down list shows before it needs scrolling.
| **How to write it:** ``height=5``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("height")

    numbers = list(range(1, 51))

    number_box = ttk.Combobox(root, values=numbers, height=5)
    number_box.set(1)
    number_box.pack(pady=30)

    root.mainloop()

justify and foreground
~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``justify`` lines the text up ``"left"``, ``"center"`` or ``"right"``. ``foreground`` sets the text colour.
| **How to write them:** ``justify="center", foreground="purple"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("justify")

    size_box = ttk.Combobox(root, values=["Small", "Medium", "Large"], justify="center",
                            foreground="purple", font=("Arial", 14))
    size_box.set("Medium")
    size_box.pack(pady=30)

    root.mainloop()

textvariable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the Combobox to a ``StringVar``. ``.get()`` reads the choice and ``.set()`` changes it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("textvariable")

    pet = tk.StringVar(value="Dog")

    ttk.Combobox(root, textvariable=pet, values=["Dog", "Cat", "Fish"],
                 state="readonly").pack(pady=20)
    ttk.Label(root, textvariable=pet, font=("Arial", 20)).pack()     # Shows the choice

    root.mainloop()

----

Combobox methods
-------------------

get
~~~~~~~~~~~~~~~~~~

| **What it does:** reads the chosen (or typed) text.
| **How to write it:** ``choice = combobox.get()``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def show():
        result_label.config(text="You chose " + year_box.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("get")

    year_box = ttk.Combobox(root, values=["Year 7", "Year 8", "Year 9"], state="readonly")
    year_box.set("Year 7")
    year_box.pack(pady=10)

    ttk.Button(root, text="Show", command=show).pack()

    result_label = ttk.Label(root, text="", font=("Arial", 14))
    result_label.pack(pady=10)

    root.mainloop()

set
~~~~~~~~~~~~~~~~~~

| **What it does:** changes the text in the box from code.
| **How to write it:** ``combobox.set("choice")``. ``combobox.set("")`` clears it.

current
~~~~~~~~~~~~~~~~~~

| **What it does:**
| ``combobox.current(0)`` chooses an item by its **number** (0 is the first).
| ``combobox.current()`` with nothing in the brackets tells you the number of the chosen item (``-1`` if the text is not in the list).

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def show_position():
        number = month_box.current()
        result_label.config(text=f"{month_box.get()} is month number {number + 1}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("current")

    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]

    month_box = ttk.Combobox(root, values=months, state="readonly")
    month_box.current(0)                    # Choose the first month
    month_box.pack(pady=10)

    ttk.Button(root, text="Which number?", command=show_position).pack()

    result_label = ttk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()

bind (when a choice is picked)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function as soon as the user picks a choice from the list. A Combobox has **no** ``command`` option, so use ``bind``.
| **How to write it:** ``combobox.bind("<<ComboboxSelected>>", function_name)``
| The function needs an ``event`` parameter.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def change_colour(event):
        root.config(bg=colour_box.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("ComboboxSelected")

    colour_box = ttk.Combobox(root, values=["white", "pink", "lightblue", "lightgreen"],
                              state="readonly")
    colour_box.set("white")
    colour_box.pack(pady=30)
    colour_box.bind("<<ComboboxSelected>>", change_colour)

    root.mainloop()

Using the choice in a calculation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| A **dictionary** links each choice to a number.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    prices = {"Small": 3, "Medium": 4, "Large": 5}


    def show_price(event):
        price_label.config(text=f"Price: ${prices[size_box.get()]}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Drink sizes")

    size_box = ttk.Combobox(root, values=list(prices), state="readonly")
    size_box.set("Small")
    size_box.pack(pady=20)
    size_box.bind("<<ComboboxSelected>>", show_price)

    price_label = ttk.Label(root, text="Price: $3", font=("Arial", 16))
    price_label.pack()

    root.mainloop()

| ``list(prices)`` makes a list of the dictionary's keys: ``["Small", "Medium", "Large"]``.

config (changing the list)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``combobox.config(values=new_list)`` changes the choices while the program runs.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    foods = {
        "Fruit": ["Apple", "Banana", "Mango"],
        "Vegetables": ["Carrot", "Pea", "Potato"],
    }


    def change_list(event):
        group = group_box.get()
        food_box.config(values=foods[group])
        food_box.current(0)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Changing the list")

    group_box = ttk.Combobox(root, values=list(foods), state="readonly")
    group_box.set("Fruit")
    group_box.pack(pady=10)
    group_box.bind("<<ComboboxSelected>>", change_list)

    food_box = ttk.Combobox(root, values=foods["Fruit"], state="readonly")
    food_box.current(0)
    food_box.pack(pady=10)

    root.mainloop()

Adding typed items to the list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``cget("values")`` reads the current list. Add the typed word and put the new list back with ``config``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def add_name(event=None):
        new_name = name_box.get()
        names = list(name_box.cget("values"))
        if new_name and new_name not in names:
            names.append(new_name)
            name_box.config(values=names)
            result_label.config(text=f"{new_name} added")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Adding items")

    name_box = ttk.Combobox(root, values=["Ava", "Ben"])
    name_box.pack(pady=10)
    name_box.bind("<Return>", add_name)

    ttk.Button(root, text="Add name", command=add_name).pack()

    result_label = ttk.Label(root, text="Type a name and press Enter")
    result_label.pack(pady=10)

    root.mainloop()

----

Styling a Combobox
---------------------

| The style is ``"TCombobox"``. With ``"clam"``: ``fieldbackground`` (box colour), ``foreground``, ``arrowcolor``, ``background`` (arrow button) and ``padding``.
| Use ``style.map`` with ``"readonly"`` to colour readonly boxes, because readonly has its own colour.
| The **drop-down list** is not a ttk widget. Change its font and colours with ``root.option_add`` **before** making the Combobox.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Combobox style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TCombobox", foreground="navy", arrowcolor="white", background="navy",
                    padding=5)
    style.map("TCombobox", fieldbackground=[("readonly", "lightyellow")])

    root.option_add("*TCombobox*Listbox.font", ("Arial", 14))            # The drop-down list
    root.option_add("*TCombobox*Listbox.background", "lightyellow")

    animal_box = ttk.Combobox(root, values=["Koala", "Kangaroo", "Wombat"], state="readonly",
                              font=("Arial", 14))
    animal_box.set("Koala")
    animal_box.pack(pady=40)

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
    * - ``values``
      - The list of choices
      - ``values=["S", "M", "L"]``
    * - ``state``
      - Typing allowed, pick only, or off
      - ``state="readonly"``
    * - ``width``, ``font``
      - Width and font of the box
      - ``width=20, font=("Arial", 14)``
    * - ``height``
      - Choices shown in the drop-down
      - ``height=5``
    * - ``justify``, ``foreground``
      - Line up the text, text colour
      - ``justify="center"``
    * - ``textvariable``
      - Link to a StringVar
      - ``textvariable=pet``
    * - ``get()``
      - Read the choice
      - ``box.get()``
    * - ``set()``
      - Change the text
      - ``box.set("Large")``
    * - ``current()``
      - Choose by number / find the number
      - ``box.current(0)``
    * - ``bind("<<ComboboxSelected>>")``
      - Run a function when a choice is picked
      - ``box.bind("<<ComboboxSelected>>", show)``
    * - ``config(values=...)``
      - Change the list
      - ``box.config(values=new_list)``
    * - ``"TCombobox"``
      - Style name
      - ``style.configure("TCombobox", foreground="navy")``

----

.. admonition:: Tasks

    #. Make a window titled "Holidays" that is 300x200 with a readonly Combobox of "Beach", "Snow", "City" and "Camping", starting on "Beach".
    #. Add a "Show" button and a label that shows "You picked" and the choice.
    #. Make a readonly Combobox of five colours that changes the window's background as soon as a colour is picked.
    #. Make a Combobox of the numbers 1 to 12 and a label. When a number is picked, the label shows that number times 7.

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
                    root.title("Holidays")

                    holiday_box = ttk.Combobox(root, values=["Beach", "Snow", "City", "Camping"],
                                               state="readonly")
                    holiday_box.set("Beach")
                    holiday_box.pack(pady=30)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def show():
                        result_label.config(text="You picked " + holiday_box.get())


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Holidays")

                    holiday_box = ttk.Combobox(root, values=["Beach", "Snow", "City", "Camping"],
                                               state="readonly")
                    holiday_box.set("Beach")
                    holiday_box.pack(pady=10)

                    ttk.Button(root, text="Show", command=show).pack()
                    result_label = ttk.Label(root, text="")
                    result_label.pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def change_colour(event):
                        root.config(bg=colour_box.get())


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Colours")

                    colour_box = ttk.Combobox(root, values=["white", "pink", "orange", "lightgreen",
                                                            "skyblue"], state="readonly")
                    colour_box.set("white")
                    colour_box.pack(pady=30)
                    colour_box.bind("<<ComboboxSelected>>", change_colour)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def times_seven(event):
                        number = int(number_box.get())
                        answer_label.config(text=f"{number} x 7 = {number * 7}")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Times 7")

                    number_box = ttk.Combobox(root, values=list(range(1, 13)), state="readonly",
                                              width=5)
                    number_box.pack(pady=20)
                    number_box.bind("<<ComboboxSelected>>", times_seven)

                    answer_label = ttk.Label(root, text="Pick a number", font=("Arial", 16))
                    answer_label.pack()

                    root.mainloop()
