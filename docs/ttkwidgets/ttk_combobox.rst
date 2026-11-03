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

All Combobox options
---------------------------

| Here is every option a ttk Combobox can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``background``
      - Background colour (write ``background``, not ``bg``)
      - ``background="lavender"``
    * - ``class_``
      - A group name used to style many widgets at once (advanced). Written ``class_`` in Python
      - ``class_="Sidebar"``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``exportselection``
      - Lets selected text be copied to other programs (``True`` or ``False``)
      - ``exportselection=False``
    * - ``font``
      - Style and size of the words
      - ``font=("Arial", 14)``
    * - ``foreground``
      - Word colour (write ``foreground``, not ``fg``)
      - ``foreground="purple"``
    * - ``height``
      - How many choices show in the drop-down list at once
      - ``height=5``
    * - ``invalidcommand``
      - Function to run when ``validatecommand`` says no
      - ``invalidcommand=beep``
    * - ``justify``
      - Lines up the words: ``"left"``, ``"center"`` or ``"right"``
      - ``justify="center"``
    * - ``postcommand``
      - Function to run just before the list drops down
      - ``postcommand=update_list``
    * - ``show``
      - Shows this character instead of what is typed (good for passwords)
      - ``show="*"``
    * - ``state``
      - ``"normal"`` (can type), ``"readonly"`` (can only pick from the list) or ``"disabled"``
      - ``state="readonly"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TCombobox"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``textvariable``
      - A variable that holds the chosen or typed item
      - ``textvariable=colour``
    * - ``validate``
      - When to check what is typed: ``"none"``, ``"key"``, ``"focus"``, ``"focusin"``, ``"focusout"`` or ``"all"``
      - ``validate="key"``
    * - ``validatecommand``
      - Function that checks what is typed (returns ``True`` or ``False``)
      - ``validatecommand=(root.register(check), "%P")``
    * - ``values``
      - The list of choices
      - ``values=["Red", "Green", "Blue"]``
    * - ``width``
      - How wide it is (in characters)
      - ``width=15``
    * - ``xscrollcommand``
      - Connects it to a side-to-side scrollbar
      - ``xscrollcommand=x_scrollbar.set``

| Many themes ignore ``background`` for the typing box. Use a style instead, e.g. ``style.configure("TCombobox", fieldbackground="lightyellow")``.

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

        What is a Combobox?

        [x] A box with a drop-down list, where the user can pick or type a choice | Correct. It combines an Entry and a list.
        [ ] A box of buttons | Incorrect. It is a drop-down.
        [ ] A tick box | Incorrect. That is a Checkbutton.
        [ ] A slider | Incorrect. That is a Scale.

    .. multichoice::

        Which option gives the list of choices?

        [ ] choices | Incorrect. Not an option.
        [x] values | Correct. values holds the choices.
        [ ] items | Incorrect. Not an option.
        [ ] list | Incorrect. Not an option.

    .. multichoice::

        What does state="readonly" do?

        [x] The user can only pick from the list, not type | Correct. readonly stops typing.
        [ ] Hides the list | Incorrect. It still drops down.
        [ ] Turns it off | Incorrect. "disabled" turns it off.
        [ ] Lets the user type anything | Incorrect. That is "normal".

    .. multichoice::

        What does state="normal" allow?

        [ ] Only picking from the list | Incorrect. That is readonly.
        [x] Picking from the list or typing a new choice | Correct. normal allows typing.
        [ ] Nothing | Incorrect. It allows typing and picking.
        [ ] Only typing | Incorrect. Picking works too.

    .. multichoice::

        What does height=5 do?

        [ ] Makes the box 5 lines tall | Incorrect. It is one line.
        [x] Shows 5 choices at once in the drop-down | Correct. More choices scroll.
        [ ] Allows only 5 choices | Incorrect. More can be added.
        [ ] Makes it 5 pixels | Incorrect. It counts choices.

    .. multichoice::

        What does width=20 mean?

        [x] About 20 characters wide | Correct. It counts characters.
        [ ] 20 pixels | Incorrect. Characters.
        [ ] 20 choices | Incorrect. It sets width.
        [ ] 20 lines | Incorrect. One line.

    .. multichoice::

        Which option makes the words red?

        [ ] fg="red" | Incorrect. ttk Combobox uses foreground.
        [x] foreground="red" | Correct. Write the full word foreground.
        [ ] colour="red" | Incorrect. Not an option.
        [ ] bg="red" | Incorrect. Not an option, and that is background.

    .. multichoice::

        What does justify="center" do?

        [ ] Centres the window | Incorrect. It centres the text.
        [x] Puts the chosen words in the middle of the box | Correct. justify lines up the text.
        [ ] Centres the list | Incorrect. It lines up the text in the box.
        [ ] Removes the arrow | Incorrect. The arrow stays.

    .. multichoice::

        Which method reads the chosen or typed item?

        [x] combo.get() | Correct. get gives the text in the box.
        [ ] combo.read() | Incorrect. Not a method.
        [ ] combo.value | Incorrect. Not an attribute.
        [ ] combo.choice() | Incorrect. Not a method.

    .. multichoice::

        Which line puts "Blue" in the box from code?

        [ ] combo.get("Blue") | Incorrect. get reads.
        [x] combo.set("Blue") | Correct. set puts text in the box.
        [ ] combo.insert("Blue") | Incorrect. insert needs a position.
        [ ] combo.choose("Blue") | Incorrect. Not a method.

    .. multichoice::

        What does combo.current(0) do?

        [x] Picks the first choice in values | Correct. current chooses by index.
        [ ] Gives the text | Incorrect. It picks a choice.
        [ ] Deletes the first choice | Incorrect. It picks it.
        [ ] Clears the box | Incorrect. It picks a choice.

    .. multichoice::

        What does combo.current() give with no number?

        [ ] The text | Incorrect. It gives an index.
        [x] The index of the chosen item, or -1 if the text is not in the list | Correct. It tells you which one was picked.
        [ ] The number of choices | Incorrect. Use len(values).
        [ ] An error | Incorrect. It is allowed.

    .. multichoice::

        Which event runs a function when a choice is picked?

        [ ] "<Click>" | Incorrect. Not an event.
        [x] "<<ComboboxSelected>>" | Correct. This event fires when a choice is picked.
        [ ] "<Return>" | Incorrect. That is Enter.
        [ ] "<Select>" | Incorrect. Not the right name.

    .. multichoice::

        A function used with bind needs:

        [x] A parameter for the event | Correct. bind sends an event.
        [ ] No parameters | Incorrect. bind sends one.
        [ ] Two parameters | Incorrect. It gets one.
        [ ] The Combobox as a parameter | Incorrect. It gets the event.

    .. multichoice::

        How can a price be found from the chosen item?

        [ ] price = combo | Incorrect. combo is a widget.
        [x] price = prices[combo.get()] | Correct. Use the choice as a dictionary key.
        [ ] price = combo.price | Incorrect. Not an attribute.
        [ ] price = prices(combo.get()) | Incorrect. Dictionaries use square brackets.

    .. multichoice::

        Which line changes the list of choices?

        [ ] combo.values = ["A", "B"] | Incorrect. Use config.
        [x] combo.config(values=["A", "B"]) | Correct. config changes values.
        [ ] combo.set(values=["A", "B"]) | Incorrect. set puts text in the box.
        [ ] combo.add(["A", "B"]) | Incorrect. Not a method.

    .. multichoice::

        How can a typed item be added to the list?

        [x] Get the list from combo["values"], add the new item and set values again | Correct. values must be set as a whole.
        [ ] combo.append(item) | Incorrect. Not a method.
        [ ] combo.insert(item) | Incorrect. Not for the list.
        [ ] It cannot | Incorrect. It can.

    .. multichoice::

        What does textvariable=colour do?

        [ ] Sets the font | Incorrect. font does that.
        [x] Links the box to a StringVar, so colour.get() reads it | Correct. The variable updates with the box.
        [ ] Sets the list | Incorrect. values does that.
        [ ] Names the box | Incorrect. It links a variable.

    .. multichoice::

        Which style name is used for every Combobox?

        [ ] "Combobox" | Incorrect. Use TCombobox.
        [x] "TCombobox" | Correct. T then the widget name.
        [ ] "TCombo" | Incorrect. Not the name.
        [ ] "Drop" | Incorrect. Not the name.

    .. multichoice::

        Which widget suits choosing a country from a long list in a small space?

        [x] Combobox | Correct. It drops down a list.
        [ ] Radiobuttons | Incorrect. Too many buttons.
        [ ] Canvas | Incorrect. Not for choosing.
        [ ] Progressbar | Incorrect. It shows progress.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a Combobox with choices.

        colour_box = ttk.@@Combobox | Entry | Listbox@@(root, @@values | choices | items@@=["Red", "Green", "Blue"], state="readonly")
        colour_box.pack()
        colour_box.@@current | set | get@@(0)

    .. cloze::
        :instructions: Read and set the choice.

        colour = colour_box.@@get | read | value@@()
        colour_box.@@set | get | insert@@("Blue")

    .. cloze::
        :instructions: Run a function when a choice is picked.

        def picked(@@event | choice | self@@):
            result_label.config(text="You chose " + colour_box.get())

        colour_box.@@bind | config | command@@("@@<<ComboboxSelected>> | <Click> | <Return>@@", picked)

    .. cloze::
        :instructions: Show more choices and style the text.

        size_box = ttk.Combobox(root, values=sizes, @@height | lines | rows@@=5, @@justify | anchor | side@@="center", foreground="blue")

    .. cloze::
        :instructions: Change the list of choices.

        colour_box.@@config | set | add@@(@@values | items | text@@=["Pink", "Purple"])

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
