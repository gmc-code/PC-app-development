====================================================
tk Listbox
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Listbox>`_

----

What is a Listbox?
-------------------

| A **Listbox** shows a list of words, one on each line.
| The user clicks an item to choose (select) it.
| Use a listbox for a list of choices, e.g. a list of countries, or to show a list the program builds, e.g. a shopping list.

----

Making a Listbox
-------------------

| Every Listbox is made in three steps:

#. **Create** the listbox with ``tk.Listbox(...)``.
#. **Add** items with ``.insert(tk.END, "item")``. ``tk.END`` means "add it to the end of the list".
#. **Place** the listbox in the window with ``.pack()``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x250")        # Window size: 300 wide, 250 high
    root.title("My first listbox")  # Words in the title bar

    fruit_list = tk.Listbox(root)           # 1. Create the listbox

    fruit_list.insert(tk.END, "Apple")      # 2. Add items
    fruit_list.insert(tk.END, "Banana")
    fruit_list.insert(tk.END, "Cherry")

    fruit_list.pack(pady=10)                # 3. Place it in the window

    root.mainloop()                 # Keep the window open

----

Item numbers (indexes)
-------------------------

| Each item in a listbox has a number called an **index**. Like a Python list, counting starts at **0**.

.. list-table::
    :header-rows: 1
    :widths: 30 70

    * - Index
      - Item
    * - ``0``
      - Apple (the first item)
    * - ``1``
      - Banana
    * - ``2``
      - Cherry
    * - ``tk.END``
      - The end of the list

----

Listbox options
-------------------

| Options are written as ``option=value`` inside ``tk.Listbox( )``, separated by commas.

height and width
~~~~~~~~~~~~~~~~~~

| **What they do:** ``height`` sets how many **lines** (items) show at once. ``width`` sets how wide it is in **characters**.
| **How to write them:** ``height=5``, ``width=20``
| If there are more items than the height, the user can scroll with the mouse wheel.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("height and width")

    number_list = tk.Listbox(root, height=4, width=15)
    for number in range(1, 11):
        number_list.insert(tk.END, f"Number {number}")
    number_list.pack(pady=10)

    root.mainloop()

font
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the style and size of the words in the list.
| **How to write it:** ``font=("font name", size)``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("font")

    pet_list = tk.Listbox(root, font=("Arial", 16), height=4)
    for pet in ["Dog", "Cat", "Fish", "Bird"]:
        pet_list.insert(tk.END, pet)
    pet_list.pack(pady=10)

    root.mainloop()

| A ``for`` loop is a quick way to add every item from a Python list.

fg and bg (colours)
~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``fg`` sets the colour of the words. ``bg`` sets the colour of the box.
| **How to write them:** ``fg="white", bg="darkblue"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("fg and bg")

    planet_list = tk.Listbox(root, fg="white", bg="darkblue", height=5)
    for planet in ["Mercury", "Venus", "Earth", "Mars"]:
        planet_list.insert(tk.END, planet)
    planet_list.pack(pady=10)

    root.mainloop()

selectbackground and selectforeground
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** set the colours of the **chosen** item. ``selectbackground`` is the highlight colour and ``selectforeground`` is the word colour.
| **How to write them:** ``selectbackground="orange", selectforeground="black"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("select colours")

    team_list = tk.Listbox(root, selectbackground="orange", selectforeground="black", height=4)
    for team in ["Red team", "Blue team", "Green team"]:
        team_list.insert(tk.END, team)
    team_list.pack(pady=10)

    root.mainloop()

selectmode
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses how many items the user can select.
| **How to write it:** ``selectmode="multiple"``
| **Values:**

- ``"browse"`` - one item at a time (the default).
- ``"multiple"`` - click items to choose several; click again to un-choose.
- ``"extended"`` - hold **Ctrl** or **Shift** while clicking to choose several, like in File Explorer.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("selectmode")

    topping_list = tk.Listbox(root, selectmode="multiple", height=6)
    for topping in ["Cheese", "Ham", "Pineapple", "Olives", "Mushrooms"]:
        topping_list.insert(tk.END, topping)
    topping_list.pack(pady=10)

    root.mainloop()

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** change the border around the box.
| **How to write them:** ``relief="solid", borderwidth=2``
| **Styles:** ``"sunken"`` (the default), ``"solid"``, ``"flat"``, ``"raised"``, ``"groove"``, ``"ridge"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("relief")

    day_list = tk.Listbox(root, relief="solid", borderwidth=2, height=5)
    for day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
        day_list.insert(tk.END, day)
    day_list.pack(pady=10)

    root.mainloop()

----

Listbox methods
-------------------

| A **method** is an action that a widget can do. Methods are written after a dot, e.g. ``listbox.insert(...)``.

insert
~~~~~~~~~~~~~~~~~~

| **What it does:** adds an item to the list.
| **How to write it:** ``listbox.insert(tk.END, "item")`` adds to the end. ``listbox.insert(0, "item")`` adds to the top.

.. code-block:: python

    import tkinter as tk


    def add_item():
        shopping_list.insert(tk.END, item_entry.get())     # Add what was typed
        item_entry.delete(0, tk.END)                        # Clear the entry


    root = tk.Tk()
    root.geometry("300x300")
    root.title("insert")

    item_entry = tk.Entry(root)
    item_entry.pack(pady=5)

    add_button = tk.Button(root, text="Add to list", command=add_item)
    add_button.pack()

    shopping_list = tk.Listbox(root, height=8)
    shopping_list.pack(pady=5)

    root.mainloop()

curselection
~~~~~~~~~~~~~~~~~~

| **What it does:** finds which item the user has chosen. It gives back the **index** (item number), not the words.
| **How to write it:** ``chosen = listbox.curselection()``
| The answer is a **tuple** of index numbers, e.g. ``(2,)``. Use ``chosen[0]`` to get the first one.
| If nothing is chosen, the tuple is empty, ``()``.

get
~~~~~~~~~~~~~~~~~~

| **What it does:** gives back the words of an item.
| **How to write it:** ``words = listbox.get(index)``
| ``curselection`` and ``get`` are used together: first find the index, then get the words.

.. code-block:: python

    import tkinter as tk


    def show_choice():
        chosen = country_list.curselection()        # e.g. (2,)
        if chosen:                                  # Check something is chosen
            country = country_list.get(chosen[0])   # Get the words
            result_label.config(text="You chose " + country)
        else:
            result_label.config(text="Please choose a country")


    root = tk.Tk()
    root.geometry("300x250")
    root.title("curselection and get")

    country_list = tk.Listbox(root, height=5)
    for country in ["Australia", "Japan", "Kenya", "Brazil", "Canada"]:
        country_list.insert(tk.END, country)
    country_list.pack(pady=5)

    show_button = tk.Button(root, text="Show choice", command=show_choice)
    show_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack(pady=5)

    root.mainloop()

Getting several choices
~~~~~~~~~~~~~~~~~~~~~~~~~~

| With ``selectmode="multiple"``, ``curselection()`` gives back every chosen index. Loop through them to get each item.

.. code-block:: python

    import tkinter as tk


    def order():
        toppings = []
        for index in topping_list.curselection():
            toppings.append(topping_list.get(index))
        result_label.config(text="Your toppings: " + ", ".join(toppings))


    root = tk.Tk()
    root.geometry("300x250")
    root.title("Several choices")

    topping_list = tk.Listbox(root, selectmode="multiple", height=5)
    for topping in ["Cheese", "Ham", "Pineapple", "Olives", "Mushrooms"]:
        topping_list.insert(tk.END, topping)
    topping_list.pack(pady=5)

    order_button = tk.Button(root, text="Order", command=order)
    order_button.pack()

    result_label = tk.Label(root, text="", wraplength=250)
    result_label.pack(pady=5)

    root.mainloop()

delete
~~~~~~~~~~~~~~~~~~

| **What it does:** removes items from the list.
| **How to write it:**
| ``listbox.delete(index)`` removes one item.
| ``listbox.delete(0, tk.END)`` removes **every** item.

.. code-block:: python

    import tkinter as tk


    def delete_chosen():
        chosen = job_list.curselection()
        if chosen:
            job_list.delete(chosen[0])


    def clear_all():
        job_list.delete(0, tk.END)


    root = tk.Tk()
    root.geometry("300x280")
    root.title("delete")

    job_list = tk.Listbox(root, height=5)
    for job in ["Feed the dog", "Do homework", "Tidy room", "Practise piano"]:
        job_list.insert(tk.END, job)
    job_list.pack(pady=5)

    done_button = tk.Button(root, text="Done (delete chosen)", command=delete_chosen)
    done_button.pack(pady=2)

    clear_button = tk.Button(root, text="Clear all", command=clear_all)
    clear_button.pack(pady=2)

    root.mainloop()

size
~~~~~~~~~~~~~~~~~~

| **What it does:** counts how many items are in the list.
| **How to write it:** ``count = listbox.size()``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("size")

    name_list = tk.Listbox(root, height=5)
    for name in ["Ava", "Ben", "Chloe", "Dev"]:
        name_list.insert(tk.END, name)
    name_list.pack(pady=5)

    count_label = tk.Label(root, text=f"There are {name_list.size()} names")
    count_label.pack()

    root.mainloop()

selection_set and selection_clear
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** choose or un-choose items from your code.
| ``listbox.selection_set(0)`` chooses the first item.
| ``listbox.selection_clear(0, tk.END)`` un-chooses everything.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("selection_set")

    size_list = tk.Listbox(root, height=3)
    for size in ["Small", "Medium", "Large"]:
        size_list.insert(tk.END, size)
    size_list.selection_set(1)          # "Medium" is chosen at the start
    size_list.pack(pady=10)

    root.mainloop()

bind (clicking an item)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function as soon as the user clicks an item, without needing a button.
| **How to write it:** ``listbox.bind("<<ListboxSelect>>", function_name)``
| The function needs an ``event`` parameter.

.. code-block:: python

    import tkinter as tk


    def show_colour(event):
        chosen = colour_list.curselection()
        if chosen:
            colour = colour_list.get(chosen[0])
            colour_label.config(bg=colour, text=colour)


    root = tk.Tk()
    root.geometry("300x250")
    root.title("bind")

    colour_list = tk.Listbox(root, height=5)
    for colour in ["red", "orange", "yellow", "green", "blue"]:
        colour_list.insert(tk.END, colour)
    colour_list.pack(pady=5)
    colour_list.bind("<<ListboxSelect>>", show_colour)

    colour_label = tk.Label(root, text="Click a colour", width=20, height=2)
    colour_label.pack(pady=5)

    root.mainloop()

itemconfig
~~~~~~~~~~~~~~~~~~

| **What it does:** changes the colour of **one** item.
| **How to write it:** ``listbox.itemconfig(index, fg="red", bg="yellow")``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("itemconfig")

    result_list = tk.Listbox(root, height=4)
    for result in ["Maths: pass", "English: pass", "Science: fail"]:
        result_list.insert(tk.END, result)
    result_list.itemconfig(2, fg="red")        # Make item 2 red
    result_list.pack(pady=10)

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
    * - ``height``, ``width``
      - Lines shown, width in characters
      - ``height=5, width=20``
    * - ``font``
      - Font name and size
      - ``font=("Arial", 14)``
    * - ``fg``, ``bg``
      - Word colour, box colour
      - ``bg="lightyellow"``
    * - ``selectbackground``
      - Highlight colour of the chosen item
      - ``selectbackground="orange"``
    * - ``selectmode``
      - Choose one or several items
      - ``selectmode="multiple"``
    * - ``relief``, ``borderwidth``
      - Border style and thickness
      - ``relief="solid", borderwidth=2``
    * - ``insert()``
      - Add an item
      - ``listbox.insert(tk.END, "Apple")``
    * - ``curselection()``
      - Index numbers of chosen items
      - ``chosen = listbox.curselection()``
    * - ``get()``
      - Words of an item
      - ``listbox.get(chosen[0])``
    * - ``delete()``
      - Remove items
      - ``listbox.delete(0, tk.END)``
    * - ``size()``
      - Count the items
      - ``listbox.size()``
    * - ``selection_set()``
      - Choose an item from code
      - ``listbox.selection_set(0)``
    * - ``bind()``
      - Run a function when an item is clicked
      - ``listbox.bind("<<ListboxSelect>>", show)``
    * - ``itemconfig()``
      - Colour one item
      - ``listbox.itemconfig(2, fg="red")``

----

.. admonition:: Tasks

    #. Make a window titled "Sports" that is 300x250. Add a listbox with a height of 5 and Arial size 14, containing "Cricket", "Football", "Netball", "Swimming" and "Tennis". Use a ``for`` loop.
    #. Add a button labelled "Choose" and a label. When clicked, the label shows the sport that was chosen.
    #. Make an Entry, an "Add" button and a listbox. When the button is clicked, the text in the Entry is added to the end of the listbox.
    #. Add a "Remove" button to your answer for Q3 that deletes the chosen item from the listbox.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x250")
                    root.title("Sports")

                    sport_list = tk.Listbox(root, height=5, font=("Arial", 14))
                    for sport in ["Cricket", "Football", "Netball", "Swimming", "Tennis"]:
                        sport_list.insert(tk.END, sport)
                    sport_list.pack(pady=5)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk


                    def choose():
                        chosen = sport_list.curselection()
                        if chosen:
                            result_label.config(text="You chose " + sport_list.get(chosen[0]))


                    root = tk.Tk()
                    root.geometry("300x250")
                    root.title("Sports")

                    sport_list = tk.Listbox(root, height=5, font=("Arial", 14))
                    for sport in ["Cricket", "Football", "Netball", "Swimming", "Tennis"]:
                        sport_list.insert(tk.END, sport)
                    sport_list.pack(pady=5)

                    choose_button = tk.Button(root, text="Choose", command=choose)
                    choose_button.pack()

                    result_label = tk.Label(root, text="")
                    result_label.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk


                    def add():
                        name_list.insert(tk.END, name_entry.get())


                    root = tk.Tk()
                    root.geometry("300x300")
                    root.title("Names")

                    name_entry = tk.Entry(root)
                    name_entry.pack(pady=5)

                    add_button = tk.Button(root, text="Add", command=add)
                    add_button.pack()

                    name_list = tk.Listbox(root, height=8)
                    name_list.pack(pady=5)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def add():
                        name_list.insert(tk.END, name_entry.get())


                    def remove():
                        chosen = name_list.curselection()
                        if chosen:
                            name_list.delete(chosen[0])


                    root = tk.Tk()
                    root.geometry("300x320")
                    root.title("Names")

                    name_entry = tk.Entry(root)
                    name_entry.pack(pady=5)

                    add_button = tk.Button(root, text="Add", command=add)
                    add_button.pack()

                    name_list = tk.Listbox(root, height=8)
                    name_list.pack(pady=5)

                    remove_button = tk.Button(root, text="Remove", command=remove)
                    remove_button.pack()

                    root.mainloop()
