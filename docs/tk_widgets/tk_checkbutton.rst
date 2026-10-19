====================================================
tk Checkbutton
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Checkbutton>`_

----

What is a Checkbutton?
-------------------------

| A **Checkbutton** is a small tick box with words next to it.
| The user clicks it to tick it, and clicks again to untick it.
| Use checkbuttons when the user can choose **any number** of options, e.g. pizza toppings.
| To choose **only one** option from a group, use **Radiobuttons** instead.

----

Making a Checkbutton
-------------------------

| A checkbutton needs a **variable** to remember whether it is ticked.
| An ``IntVar`` is a Tkinter variable that stores a whole number: **1** when ticked and **0** when not ticked.

#. **Create** the variable with ``tk.IntVar()``.
#. **Create** the checkbutton with ``tk.Checkbutton(...)`` and link it to the variable.
#. **Place** the checkbutton in the window with ``.pack()``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first checkbutton")

    cheese = tk.IntVar()            # 1. Variable: 1 = ticked, 0 = not ticked

    cheese_check = tk.Checkbutton(root, text="Cheese", variable=cheese)   # 2. Create it
    cheese_check.pack(pady=20)      # 3. Place it in the window

    root.mainloop()                 # Keep the window open

| Each checkbutton needs its **own** variable.

----

Checkbutton options
-----------------------

| Options are written as ``option=value`` inside ``tk.Checkbutton( )``, separated by commas.

text
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the words next to the tick box.
| **How to write it:** ``text="your words"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("text")

    agree = tk.IntVar()

    agree_check = tk.Checkbutton(root, text="I agree to the rules", variable=agree)
    agree_check.pack(pady=20)

    root.mainloop()

variable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the checkbutton to a variable that remembers if it is ticked.
| **How to write it:** ``variable=name_of_variable``
| Read the variable with ``.get()``: it gives **1** if ticked, **0** if not.

.. code-block:: python

    import tkinter as tk


    def check():
        if homework.get() == 1:
            result_label.config(text="Well done!")
        else:
            result_label.config(text="Better get started...")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("variable")

    homework = tk.IntVar()

    homework_check = tk.Checkbutton(root, text="Homework done", variable=homework)
    homework_check.pack(pady=10)

    check_button = tk.Button(root, text="Check", command=check)
    check_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()

onvalue and offvalue
~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** choose what the variable stores when the box is ticked (``onvalue``) and unticked (``offvalue``).
| **How to write them:** ``onvalue="Yes", offvalue="No"``
| To store words instead of numbers, use a ``tk.StringVar()`` as the variable.

.. code-block:: python

    import tkinter as tk


    def show():
        result_label.config(text="Sauce: " + sauce.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("onvalue and offvalue")

    sauce = tk.StringVar(value="No")

    sauce_check = tk.Checkbutton(root, text="Tomato sauce", variable=sauce,
                                 onvalue="Yes", offvalue="No", command=show)
    sauce_check.pack(pady=20)

    result_label = tk.Label(root, text="Sauce: No")
    result_label.pack()

    root.mainloop()

command
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses a function to run **every time** the box is ticked or unticked.
| **How to write it:** ``command=function_name`` (no brackets)

.. code-block:: python

    import tkinter as tk


    def change_colour():
        if dark.get() == 1:
            root.config(bg="black")
        else:
            root.config(bg="white")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("command")
    root.config(bg="white")

    dark = tk.IntVar()

    dark_check = tk.Checkbutton(root, text="Dark mode", variable=dark, command=change_colour)
    dark_check.pack(pady=20)

    root.mainloop()

font, fg and bg
~~~~~~~~~~~~~~~~~~

| **What they do:** ``font`` sets the style and size of the words, ``fg`` sets the colour of the words and ``bg`` sets the background colour.
| **How to write them:** ``font=("Arial", 16)``, ``fg="blue"``, ``bg="lightyellow"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("font, fg and bg")

    music = tk.IntVar()

    music_check = tk.Checkbutton(root, text="Play music", variable=music,
                                 font=("Arial", 16), fg="blue", bg="lightyellow")
    music_check.pack(pady=20)

    root.mainloop()

selectcolor
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the colour **inside** the tick box.
| **How to write it:** ``selectcolor="colour"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("selectcolor")

    sport = tk.IntVar()

    sport_check = tk.Checkbutton(root, text="Sport", variable=sport,
                                 font=("Arial", 16), selectcolor="lightgreen")
    sport_check.pack(pady=20)

    root.mainloop()

anchor and width
~~~~~~~~~~~~~~~~~~

| **What they do:** ``width`` sets how wide the checkbutton is (in characters). ``anchor="w"`` lines it up on the **left**.
| Using the same ``width`` and ``anchor="w"`` on every checkbutton makes a neat list with the boxes lined up.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("anchor and width")

    ham = tk.IntVar()
    pineapple = tk.IntVar()
    mushrooms = tk.IntVar()

    ham_check = tk.Checkbutton(root, text="Ham", variable=ham, width=15, anchor="w")
    ham_check.pack()

    pineapple_check = tk.Checkbutton(root, text="Pineapple", variable=pineapple, width=15, anchor="w")
    pineapple_check.pack()

    mushrooms_check = tk.Checkbutton(root, text="Mushrooms", variable=mushrooms, width=15, anchor="w")
    mushrooms_check.pack()

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** turns the checkbutton on or off.
| **How to write it:** ``state="disabled"``
| **Values:** ``"normal"`` (can be clicked, the default) and ``"disabled"`` (greyed out).

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    free = tk.IntVar()
    sold_out = tk.IntVar()

    free_check = tk.Checkbutton(root, text="Chips", variable=free)
    free_check.pack(pady=5)

    sold_out_check = tk.Checkbutton(root, text="Ice cream (sold out)", variable=sold_out,
                                    state="disabled")
    sold_out_check.pack(pady=5)

    root.mainloop()

----

Checkbutton methods
-----------------------

| A **method** is an action that a widget can do. Methods are written after a dot.

get and set (the variable)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``variable.get()`` reads the value. ``variable.set(1)`` ticks the box from your code, and ``variable.set(0)`` unticks it.
| **How to write them:** ``ticked = cheese.get()``, ``cheese.set(1)``
| ``set`` is useful for having a box ticked when the program starts.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("get and set")

    sound = tk.IntVar()
    sound.set(1)            # Start with the box ticked

    sound_check = tk.Checkbutton(root, text="Sound on", variable=sound)
    sound_check.pack(pady=20)

    root.mainloop()

select, deselect and toggle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:**
| ``select()`` ticks the box.
| ``deselect()`` unticks the box.
| ``toggle()`` swaps it: ticked becomes unticked, and unticked becomes ticked.

.. code-block:: python

    import tkinter as tk


    def tick_all():
        for box in all_boxes:
            box.select()


    def clear_all():
        for box in all_boxes:
            box.deselect()


    root = tk.Tk()
    root.geometry("300x220")
    root.title("select and deselect")

    red = tk.IntVar()
    green = tk.IntVar()
    blue = tk.IntVar()

    red_check = tk.Checkbutton(root, text="Red", variable=red)
    red_check.pack()
    green_check = tk.Checkbutton(root, text="Green", variable=green)
    green_check.pack()
    blue_check = tk.Checkbutton(root, text="Blue", variable=blue)
    blue_check.pack()

    all_boxes = [red_check, green_check, blue_check]

    tick_button = tk.Button(root, text="Tick all", command=tick_all)
    tick_button.pack(pady=5)

    clear_button = tk.Button(root, text="Clear all", command=clear_all)
    clear_button.pack()

    root.mainloop()

Counting ticked boxes
~~~~~~~~~~~~~~~~~~~~~~~~~

| Because a ticked box stores **1** and an unticked box stores **0**, adding the variables together counts how many are ticked.

.. code-block:: python

    import tkinter as tk


    def count():
        total = cheese.get() + ham.get() + olives.get()
        result_label.config(text=f"Toppings: {total}   Price: ${10 + total * 2}")


    root = tk.Tk()
    root.geometry("300x220")
    root.title("Pizza")

    cheese = tk.IntVar()
    ham = tk.IntVar()
    olives = tk.IntVar()

    tk.Checkbutton(root, text="Cheese", variable=cheese, command=count).pack()
    tk.Checkbutton(root, text="Ham", variable=ham, command=count).pack()
    tk.Checkbutton(root, text="Olives", variable=olives, command=count).pack()

    result_label = tk.Label(root, text="Toppings: 0   Price: $10", font=("Arial", 14))
    result_label.pack(pady=10)

    root.mainloop()

| ``tk.Checkbutton(...).pack()`` creates and places a widget in one line. Only do this when you never need to use the widget's name again.

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options **after** the checkbutton has been made.
| **How to write it:** ``check.config(option=value)``

.. code-block:: python

    import tkinter as tk


    def lock():
        rules_check.config(state="disabled", text="Rules accepted")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    rules = tk.IntVar()

    rules_check = tk.Checkbutton(root, text="Accept the rules", variable=rules, command=lock)
    rules_check.pack(pady=20)

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
      - Words next to the box
      - ``text="Cheese"``
    * - ``variable``
      - Variable that remembers ticked (1) or not (0)
      - ``variable=cheese``
    * - ``onvalue``, ``offvalue``
      - What the variable stores when ticked / unticked
      - ``onvalue="Yes", offvalue="No"``
    * - ``command``
      - Function to run when clicked
      - ``command=update``
    * - ``font``, ``fg``, ``bg``
      - Font, word colour, background colour
      - ``font=("Arial", 14)``
    * - ``selectcolor``
      - Colour inside the box
      - ``selectcolor="lightgreen"``
    * - ``width``, ``anchor``
      - Width, and where it sits
      - ``width=15, anchor="w"``
    * - ``state``
      - Turn it on or off
      - ``state="disabled"``
    * - ``variable.get()``
      - Read the value
      - ``cheese.get()``
    * - ``variable.set()``
      - Tick (1) or untick (0) from code
      - ``cheese.set(1)``
    * - ``select()``, ``deselect()``
      - Tick or untick the box
      - ``cheese_check.select()``
    * - ``toggle()``
      - Swap ticked and unticked
      - ``cheese_check.toggle()``
    * - ``config()``
      - Change options later
      - ``cheese_check.config(state="disabled")``

----

.. admonition:: Tasks

    #. Make a window titled "Hobbies" that is 300x200. Add three checkbuttons: "Sport", "Music" and "Art", each with its own ``IntVar``.
    #. Make the "Music" checkbutton start ticked by using ``set``.
    #. Add a button labelled "How many?" and a label. When clicked, the label shows how many hobbies are ticked.
    #. Make a checkbutton "Big text". Use ``command`` so that when it is ticked a label's font changes to size 30, and when it is unticked it goes back to size 12.

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
                    root.title("Hobbies")

                    sport = tk.IntVar()
                    music = tk.IntVar()
                    art = tk.IntVar()

                    sport_check = tk.Checkbutton(root, text="Sport", variable=sport)
                    sport_check.pack()
                    music_check = tk.Checkbutton(root, text="Music", variable=music)
                    music_check.pack()
                    art_check = tk.Checkbutton(root, text="Art", variable=art)
                    art_check.pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Hobbies")

                    sport = tk.IntVar()
                    music = tk.IntVar()
                    art = tk.IntVar()
                    music.set(1)

                    sport_check = tk.Checkbutton(root, text="Sport", variable=sport)
                    sport_check.pack()
                    music_check = tk.Checkbutton(root, text="Music", variable=music)
                    music_check.pack()
                    art_check = tk.Checkbutton(root, text="Art", variable=art)
                    art_check.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk


                    def how_many():
                        total = sport.get() + music.get() + art.get()
                        count_label.config(text=f"Hobbies ticked: {total}")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Hobbies")

                    sport = tk.IntVar()
                    music = tk.IntVar()
                    art = tk.IntVar()
                    music.set(1)

                    sport_check = tk.Checkbutton(root, text="Sport", variable=sport)
                    sport_check.pack()
                    music_check = tk.Checkbutton(root, text="Music", variable=music)
                    music_check.pack()
                    art_check = tk.Checkbutton(root, text="Art", variable=art)
                    art_check.pack()

                    count_button = tk.Button(root, text="How many?", command=how_many)
                    count_button.pack(pady=5)

                    count_label = tk.Label(root, text="")
                    count_label.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def change_size():
                        if big.get() == 1:
                            word_label.config(font=("Arial", 30))
                        else:
                            word_label.config(font=("Arial", 12))


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Big text")

                    big = tk.IntVar()

                    big_check = tk.Checkbutton(root, text="Big text", variable=big, command=change_size)
                    big_check.pack(pady=10)

                    word_label = tk.Label(root, text="Hello", font=("Arial", 12))
                    word_label.pack()

                    root.mainloop()
