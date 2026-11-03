====================================================
ttk Spinbox
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#spinbox>`_

----

What is a ttk Spinbox?
-------------------------

| A **ttk Spinbox** is a box with up and down arrows for choosing a number or a choice from a list, just like a tk Spinbox.
| It has one handy extra method: ``set()``, which changes the value without needing ``delete`` and ``insert``.

----

Making a ttk Spinbox
-----------------------

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk Spinbox")

    tickets_spinbox = ttk.Spinbox(root, from_=1, to=10)    # 1. Create it
    tickets_spinbox.set(1)                                 #    and choose the starting value
    tickets_spinbox.pack(pady=30)                          # 2. Place it

    root.mainloop()                 # Keep the window open

.. note::

    A ttk Spinbox starts **empty**. Use ``set()`` or a ``textvariable`` to give it a starting value.

----

ttk Spinbox options
----------------------

from\_, to and increment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``from_`` and ``to`` set the lowest and highest number. ``increment`` sets the size of each step.
| **How to write them:** ``from_=0, to=60, increment=5``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("from_, to and increment")

    minutes = ttk.Spinbox(root, from_=0, to=60, increment=5)
    minutes.set(0)
    minutes.pack(pady=30)

    root.mainloop()

values
~~~~~~~~~~~~~~~~~~

| **What it does:** steps through a list of choices instead of numbers.
| **How to write it:** ``values=("Small", "Medium", "Large")``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("values")

    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

    day_spinbox = ttk.Spinbox(root, values=days)
    day_spinbox.set(days[0])
    day_spinbox.pack(pady=30)

    root.mainloop()

wrap
~~~~~~~~~~~~~~~~~~

| **What it does:** ``wrap=True`` goes back to the start after the end, like a clock.
| **How to write it:** ``wrap=True``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("wrap")

    hour_spinbox = ttk.Spinbox(root, from_=1, to=12, wrap=True)
    hour_spinbox.set(12)
    hour_spinbox.pack(pady=30)

    root.mainloop()

width, font, foreground and justify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``width`` sets the width in characters. ``font`` and ``foreground`` set the style and colour of the text. ``justify`` lines it up ``"left"``, ``"center"`` or ``"right"``.
| **How to write them:** ``width=5, font=("Arial", 20), foreground="navy", justify="center"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and font")

    score_spinbox = ttk.Spinbox(root, from_=0, to=99, width=4, font=("Arial", 24),
                                foreground="navy", justify="center")
    score_spinbox.set(0)
    score_spinbox.pack(pady=30)

    root.mainloop()

format
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses how numbers are shown, e.g. always with two decimal places.
| **How to write it:** ``format="%.2f"`` shows ``1.50``. ``format="%02.0f"`` shows ``05`` (two digits, like a clock).

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("format")

    price = ttk.Spinbox(root, from_=0, to=10, increment=0.5, format="%.2f")
    price.set("0.00")
    price.pack(pady=10)

    minutes = ttk.Spinbox(root, from_=0, to=59, format="%02.0f", wrap=True, width=4)
    minutes.set("00")
    minutes.pack(pady=10)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** controls typing.
| **Values:** ``"normal"`` (arrows and typing), ``"readonly"`` (arrows only, so no wrong typing), ``"disabled"`` (off).
| **How to write it:** ``state="readonly"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    size_spinbox = ttk.Spinbox(root, values=("Small", "Medium", "Large"), state="readonly")
    size_spinbox.set("Small")
    size_spinbox.pack(pady=30)

    root.mainloop()

| ``set()`` still works on a readonly spinbox.

command
~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function every time an arrow is clicked.
| **How to write it:** ``command=function_name``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def update_price():
        tickets = int(tickets_spinbox.get())
        price_label.config(text=f"Total: ${tickets * 15}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("command")

    tickets_spinbox = ttk.Spinbox(root, from_=1, to=10, width=5, state="readonly",
                                  command=update_price)
    tickets_spinbox.set(1)
    tickets_spinbox.pack(pady=20)

    price_label = ttk.Label(root, text="Total: $15", font=("Arial", 16))
    price_label.pack()

    root.mainloop()

textvariable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the spinbox to a variable. It is the easiest way to give a starting value.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("textvariable")

    players = tk.IntVar(value=4)

    ttk.Spinbox(root, from_=1, to=8, textvariable=players).pack(pady=20)
    ttk.Label(root, textvariable=players, font=("Arial", 20)).pack()

    root.mainloop()

----

ttk Spinbox methods
----------------------

get and set
~~~~~~~~~~~~~~~~~~

| ``get()`` reads the value as a **string**, so use ``int()`` or ``float()`` for maths. ``set()`` changes the value.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def calculate():
        pizzas = int(pizza_spinbox.get())
        result_label.config(text=f"{pizzas * 8} slices")


    def reset():
        pizza_spinbox.set(1)
        result_label.config(text="")


    root = tk.Tk()
    root.geometry("300x220")
    root.title("get and set")

    ttk.Label(root, text="How many pizzas?").pack(pady=5)

    pizza_spinbox = ttk.Spinbox(root, from_=1, to=20, width=5)
    pizza_spinbox.set(1)
    pizza_spinbox.pack()

    ttk.Button(root, text="How many slices?", command=calculate).pack(pady=5)
    ttk.Button(root, text="Reset", command=reset).pack()

    result_label = ttk.Label(root, text="", font=("Arial", 14))
    result_label.pack(pady=5)

    root.mainloop()

Checking typed numbers
~~~~~~~~~~~~~~~~~~~~~~~~~

| When the state is ``"normal"``, the user could type a word. Use ``try`` and ``except ValueError``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def double():
        try:
            number = int(number_spinbox.get())
            result_label.config(text=f"Double: {number * 2}")
        except ValueError:
            result_label.config(text="That is not a number!")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Checking")

    number_spinbox = ttk.Spinbox(root, from_=1, to=100, width=6)
    number_spinbox.set(1)
    number_spinbox.pack(pady=10)

    ttk.Button(root, text="Double it", command=double).pack()

    result_label = ttk.Label(root, text="", font=("Arial", 14))
    result_label.pack(pady=5)

    root.mainloop()

bind (Increment and Decrement)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``"<<Increment>>"`` happens when the up arrow is clicked and ``"<<Decrement>>"`` when the down arrow is clicked. The function needs an ``event`` parameter.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def going_up(event):
        result_label.config(text="Up!", foreground="green")


    def going_down(event):
        result_label.config(text="Down!", foreground="red")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("bind")

    level_spinbox = ttk.Spinbox(root, from_=1, to=10, width=5)
    level_spinbox.set(5)
    level_spinbox.pack(pady=20)
    level_spinbox.bind("<<Increment>>", going_up)
    level_spinbox.bind("<<Decrement>>", going_down)

    result_label = ttk.Label(root, text="", font=("Arial", 16))
    result_label.pack()

    root.mainloop()

config
~~~~~~~~~~~~~~~~~~

| ``spinbox.config(option=value)`` changes options later, e.g. a new range.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def adults_only():
        age_spinbox.config(from_=18, to=100)
        age_spinbox.set(18)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    age_spinbox = ttk.Spinbox(root, from_=0, to=100, width=5)
    age_spinbox.set(0)
    age_spinbox.pack(pady=20)

    ttk.Button(root, text="Adults only", command=adults_only).pack()

    root.mainloop()

----

Styling a ttk Spinbox
------------------------

| The style is ``"TSpinbox"``. With ``"clam"``: ``fieldbackground`` (box colour), ``foreground``, ``arrowcolor``, ``arrowsize`` and ``padding``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Spinbox style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TSpinbox", fieldbackground="lightyellow", foreground="darkgreen",
                    arrowcolor="darkgreen", arrowsize=16, padding=5)

    level = ttk.Spinbox(root, from_=1, to=10, width=5, font=("Arial", 16))
    level.set(1)
    level.pack(pady=40)

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
    * - ``from_``, ``to``
      - Lowest and highest number
      - ``from_=1, to=10``
    * - ``increment``
      - Size of each step
      - ``increment=5``
    * - ``values``
      - A list of choices
      - ``values=("S", "M", "L")``
    * - ``wrap``
      - Go back to the start after the end
      - ``wrap=True``
    * - ``width``, ``font``, ``foreground``
      - Size, font and colour
      - ``font=("Arial", 16)``
    * - ``format``
      - How numbers are shown
      - ``format="%.2f"``
    * - ``state``
      - Typing, arrows only, or off
      - ``state="readonly"``
    * - ``command``
      - Function to run when an arrow is clicked
      - ``command=update``
    * - ``textvariable``
      - Link to a variable
      - ``textvariable=players``
    * - ``get()``, ``set()``
      - Read or change the value
      - ``spinbox.set(5)``
    * - ``bind()``
      - ``"<<Increment>>"``, ``"<<Decrement>>"``
      - ``spinbox.bind("<<Increment>>", up)``
    * - ``"TSpinbox"``
      - Style name
      - ``style.configure("TSpinbox", fieldbackground="pink")``

----

All Spinbox options
---------------------------

| Here is every option a ttk Spinbox can have, for reference. You will only need a few of them most of the time.

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
    * - ``command``
      - Function to run when an arrow is clicked
      - ``command=show``
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
    * - ``format``
      - How the number is shown (``"%.2f"`` = 2 decimal places)
      - ``format="%.2f"``
    * - ``from_``
      - Lowest number. Written ``from_`` in Python
      - ``from_=0``
    * - ``increment``
      - How much the number goes up or down each click
      - ``increment=5``
    * - ``invalidcommand``
      - Function to run when ``validatecommand`` says no
      - ``invalidcommand=beep``
    * - ``justify``
      - Lines up the words: ``"left"``, ``"center"`` or ``"right"``
      - ``justify="center"``
    * - ``show``
      - Shows this character instead of what is typed (good for passwords)
      - ``show="*"``
    * - ``state``
      - ``"normal"``, ``"readonly"`` (can see but not type) or ``"disabled"`` (greyed out)
      - ``state="readonly"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TSpinbox"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``textvariable``
      - A variable that holds what is in the box
      - ``textvariable=amount``
    * - ``to``
      - Highest number
      - ``to=100``
    * - ``validate``
      - When to check what is typed: ``"none"``, ``"key"``, ``"focus"``, ``"focusin"``, ``"focusout"`` or ``"all"``
      - ``validate="key"``
    * - ``validatecommand``
      - Function that checks what is typed (returns ``True`` or ``False``)
      - ``validatecommand=(root.register(check), "%P")``
    * - ``values``
      - A list of choices to step through instead of numbers
      - ``values=("Red", "Green", "Blue")``
    * - ``width``
      - How wide it is (in characters)
      - ``width=15``
    * - ``wrap``
      - ``True`` goes back to the start after the last value
      - ``wrap=True``
    * - ``xscrollcommand``
      - Connects it to a side-to-side scrollbar
      - ``xscrollcommand=x_scrollbar.set``

| Many themes ignore ``background`` for the typing box. Use a style instead, e.g. ``style.configure("TSpinbox", fieldbackground="lightyellow")``.

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

        How is a ttk Spinbox made?

        [x] ttk.Spinbox(root, from_=1, to=10) | Correct. It works like the tk Spinbox.
        [ ] tk.Spinbox(root, ttk=True) | Incorrect. Not an option.
        [ ] ttk.spinbox(root) | Incorrect. Needs a capital S.
        [ ] ttk.Spinner(root) | Incorrect. Not a widget.

    .. multichoice::

        How is the lowest number written?

        [ ] from=1 | Incorrect. from is a Python keyword.
        [x] from_=1 | Correct. The underscore is needed.
        [ ] min=1 | Incorrect. Not an option.
        [ ] low=1 | Incorrect. Not an option.

    .. multichoice::

        What does increment=2 do?

        [x] Each arrow click changes the number by 2 | Correct. increment is the step.
        [ ] Starts at 2 | Incorrect. from\_ does that.
        [ ] Allows 2 clicks | Incorrect. It is the step.
        [ ] Shows 2 numbers | Incorrect. It is the step.

    .. multichoice::

        What does values=("S", "M", "L") do?

        [ ] Sets colours | Incorrect. It sets choices.
        [x] Steps through these choices instead of numbers | Correct. values replaces from\_ and to.
        [ ] Makes three Spinboxes | Incorrect. One Spinbox.
        [ ] Shows a list | Incorrect. It steps through them.

    .. multichoice::

        What does wrap=True do?

        [x] Goes back to the start after the last value | Correct. It loops round.
        [ ] Wraps long text | Incorrect. It loops values.
        [ ] Stops at the end | Incorrect. That is wrap=False.
        [ ] Makes it wider | Incorrect. width does that.

    .. multichoice::

        Which option colours the numbers in a ttk Spinbox?

        [ ] fg | Incorrect. ttk uses foreground.
        [x] foreground | Correct. Write the full word.
        [ ] colour | Incorrect. Not an option.
        [ ] textcolour | Incorrect. Not an option.

    .. multichoice::

        What does format="%.2f" do?

        [x] Shows numbers with 2 decimal places, like 2.50 | Correct. Good for money.
        [ ] Rounds to whole numbers | Incorrect. It shows 2 decimal places.
        [ ] Adds a dollar sign | Incorrect. Not by itself.
        [ ] Formats the font | Incorrect. font does that.

    .. multichoice::

        What does state="readonly" do?

        [ ] Stops the arrows | Incorrect. That is "disabled".
        [x] Stops typing, but the arrows still work | Correct. Good for fixed choices.
        [ ] Hides the Spinbox | Incorrect. It is shown.
        [ ] Deletes the value | Incorrect. Nothing is deleted.

    .. multichoice::

        When does command run?

        [ ] When the user types | Incorrect. Typing does not run command.
        [x] When an arrow is clicked | Correct. command runs on arrow clicks.
        [ ] When the window opens | Incorrect. Not then.
        [ ] Never | Incorrect. It runs on arrow clicks.

    .. multichoice::

        What does textvariable=amount do?

        [x] Links the box to a variable, so amount.get() reads it | Correct. It updates with the box.
        [ ] Sets the font | Incorrect. font does that.
        [ ] Sets the highest number | Incorrect. to does that.
        [ ] Names the box | Incorrect. It links a variable.

    .. multichoice::

        Which method reads the value?

        [ ] spinbox.read() | Incorrect. Not a method.
        [x] spinbox.get() | Correct. get gives the text in the box.
        [ ] spinbox.value | Incorrect. Not an attribute.
        [ ] spinbox.number() | Incorrect. Not a method.

    .. multichoice::

        Which line puts 5 in a ttk Spinbox?

        [x] spinbox.set(5) | Correct. ttk Spinbox has a set method.
        [ ] spinbox.get(5) | Incorrect. get reads.
        [ ] spinbox.config(value=5) | Incorrect. Not an option.
        [ ] spinbox.put(5) | Incorrect. Not a method.

    .. multichoice::

        What type does spinbox.get() give?

        [ ] An int | Incorrect. It is always text.
        [x] A string, so use int() or float() for maths | Correct. Change it before maths.
        [ ] A list | Incorrect. One value.
        [ ] A Spinbox | Incorrect. It is the text.

    .. multichoice::

        Why use try and except with the typed value?

        [ ] The arrows make errors | Incorrect. Typing can.
        [x] The user might type letters, which makes int() fail | Correct. except catches the ValueError.
        [ ] ttk Spinboxes cannot hold numbers | Incorrect. They can.
        [ ] It is never needed | Incorrect. It helps with typed text.

    .. multichoice::

        Which event runs when the up arrow is clicked?

        [x] "<<Increment>>" | Correct. ttk Spinbox sends Increment and Decrement events.
        [ ] "<Up>" | Incorrect. That is the arrow key.
        [ ] "<<Up>>" | Incorrect. Not the name.
        [ ] "<Click>" | Incorrect. Not an event.

    .. multichoice::

        Which event runs when the down arrow is clicked?

        [ ] "<<Down>>" | Incorrect. Not the name.
        [x] "<<Decrement>>" | Correct. Decrement means going down.
        [ ] "<Down>" | Incorrect. That is the arrow key.
        [ ] "<<Minus>>" | Incorrect. Not the name.

    .. multichoice::

        Which line changes the highest number later?

        [ ] spinbox.to(20) | Incorrect. Not a method.
        [x] spinbox.config(to=20) | Correct. config changes options.
        [ ] spinbox.set(to=20) | Incorrect. set puts a value in the box.
        [ ] spinbox.max = 20 | Incorrect. Use config.

    .. multichoice::

        Which style name is used for every ttk Spinbox?

        [x] "TSpinbox" | Correct. T then the widget name.
        [ ] "Spinbox" | Incorrect. Needs the T.
        [ ] "TSpin" | Incorrect. Not the name.
        [ ] "TEntry" | Incorrect. That is for Entries.

    .. multichoice::

        If from_=0, to=10, increment=5 and wrap=False, what comes after 10 when up is clicked?

        [ ] 0 | Incorrect. That needs wrap=True.
        [x] It stays at 10 | Correct. Without wrap it stops at the top.
        [ ] 15 | Incorrect. to is 10.
        [ ] An error | Incorrect. No error.

    .. multichoice::

        What does justify="center" do?

        [ ] Centres the window | Incorrect. It centres the text.
        [x] Puts the value in the middle of the box | Correct. justify lines up the text.
        [ ] Centres the arrows | Incorrect. It lines up the text.
        [ ] Hides the arrows | Incorrect. Arrows stay.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a ttk Spinbox.

        tickets = ttk.@@Spinbox | Scale | Entry@@(root, @@from_ | from | start@@=1, to=10, @@increment | step | resolution@@=1, width=5)
        tickets.pack()

    .. cloze::
        :instructions: Show money with two decimal places.

        price = ttk.Spinbox(root, from_=0, to=20, increment=0.5, @@format | style | show@@="%.2f", @@wrap | loop | repeat@@=True)

    .. cloze::
        :instructions: Read and set the value.

        count = @@int | str | list@@(tickets.get())
        tickets.@@set | insert | get@@(5)

    .. cloze::
        :instructions: Step through choices.

        size = ttk.Spinbox(root, @@values | choices | items@@=("Small", "Medium", "Large"), state="@@readonly | disabled | locked@@")

    .. cloze::
        :instructions: Run functions for each arrow.

        tickets.@@bind | config | command@@("@@<<Increment>> | <Up> | <<Up>>@@", went_up)
        tickets.bind("<<Decrement>>", went_down)

----

.. admonition:: Tasks

    #. Make a window titled "Tickets" that is 300x200 with a ttk Spinbox from 1 to 6 that starts on 2.
    #. Make it readonly with Arial size 20 and a width of 4.
    #. Make a ttk Spinbox that steps through "Red", "Orange", "Yellow" and "Green" and wraps back to the start.
    #. Make a ttk Spinbox from 1 to 10 with a ``command`` that shows the number times 3 in a label.

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
                    root.title("Tickets")

                    tickets_spinbox = ttk.Spinbox(root, from_=1, to=6)
                    tickets_spinbox.set(2)
                    tickets_spinbox.pack(pady=30)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Tickets")

                    tickets_spinbox = ttk.Spinbox(root, from_=1, to=6, state="readonly",
                                                  font=("Arial", 20), width=4)
                    tickets_spinbox.set(2)
                    tickets_spinbox.pack(pady=30)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Colours")

                    colour_spinbox = ttk.Spinbox(root, values=("Red", "Orange", "Yellow", "Green"),
                                                 wrap=True)
                    colour_spinbox.set("Red")
                    colour_spinbox.pack(pady=30)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def times_three():
                        number = int(number_spinbox.get())
                        answer_label.config(text=f"{number} x 3 = {number * 3}")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Times 3")

                    number_spinbox = ttk.Spinbox(root, from_=1, to=10, width=5, command=times_three)
                    number_spinbox.set(1)
                    number_spinbox.pack(pady=20)

                    answer_label = ttk.Label(root, text="1 x 3 = 3", font=("Arial", 16))
                    answer_label.pack()

                    root.mainloop()
