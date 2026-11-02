====================================================
tk Spinbox
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Spinbox>`_

----

What is a Spinbox?
-------------------

| A **Spinbox** is a box with two small arrows on the side.
| Clicking the arrows makes the number go up or down. The user can also type in the box.
| Use a spinbox when the user chooses a number from a range, e.g. how many tickets to buy or an age.

----

Making a Spinbox
-------------------

| Every Spinbox is made in two steps:

#. **Create** the spinbox with ``tk.Spinbox(...)``. Give it the lowest number (``from_``) and the highest number (``to``).
#. **Place** the spinbox in the window with ``.pack()``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first spinbox")  # Words in the title bar

    tickets_spinbox = tk.Spinbox(root, from_=1, to=10)  # 1. Create the spinbox
    tickets_spinbox.pack(pady=20)                       # 2. Place it in the window

    root.mainloop()                 # Keep the window open

| ``from_`` has an underscore at the end. ``from`` on its own is a special Python word, so Tkinter uses ``from_`` instead.

----

Spinbox options
-------------------

| Options are written as ``option=value`` inside ``tk.Spinbox( )``, separated by commas.

from\_ and to
~~~~~~~~~~~~~~~~~~

| **What they do:** set the lowest and highest number the arrows can reach.
| **How to write them:** ``from_=0, to=100``
| The spinbox starts on the ``from_`` number.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("from_ and to")

    age_spinbox = tk.Spinbox(root, from_=5, to=18)
    age_spinbox.pack(pady=20)

    root.mainloop()

increment
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how much the number changes each time an arrow is clicked.
| **How to write it:** ``increment=5`` or ``increment=0.5``
| The default is ``1``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("increment")

    minutes_spinbox = tk.Spinbox(root, from_=0, to=60, increment=5)
    minutes_spinbox.pack(pady=20)

    root.mainloop()

values
~~~~~~~~~~~~~~~~~~

| **What it does:** gives the spinbox a list of choices to step through instead of numbers.
| **How to write it:** ``values=("Small", "Medium", "Large")``
| When ``values`` is used, leave out ``from_`` and ``to``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("values")

    day_spinbox = tk.Spinbox(root, values=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))
    day_spinbox.pack(pady=20)

    root.mainloop()

wrap
~~~~~~~~~~~~~~~~~~

| **What it does:** ``wrap=True`` makes the spinbox go back to the start after the end, like a clock going from 12 back to 1.
| **How to write it:** ``wrap=True``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("wrap")

    hour_spinbox = tk.Spinbox(root, from_=1, to=12, wrap=True)
    hour_spinbox.pack(pady=20)

    root.mainloop()

font and width
~~~~~~~~~~~~~~~~~~

| **What they do:** ``font`` sets the style and size of the text. ``width`` sets how wide the box is in characters.
| **How to write them:** ``font=("Arial", 20)``, ``width=5``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("font and width")

    score_spinbox = tk.Spinbox(root, from_=0, to=99, font=("Arial", 24), width=4)
    score_spinbox.pack(pady=20)

    root.mainloop()

fg, bg and justify
~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``fg`` sets the colour of the text. ``bg`` sets the colour of the box. ``justify`` lines the text up on the ``"left"``, ``"center"`` or ``"right"``.
| **How to write them:** ``fg="white", bg="navy", justify="center"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("fg, bg and justify")

    level_spinbox = tk.Spinbox(root, from_=1, to=10, font=("Arial", 18), width=5,
                               fg="white", bg="navy", justify="center")
    level_spinbox.pack(pady=20)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** controls whether the user can type in the box.
| **How to write it:** ``state="readonly"``
| **Values:**

- ``"normal"`` - the user can use the arrows **and** type (the default).
- ``"readonly"`` - the user can **only** use the arrows. This stops them typing something that is not allowed.
- ``"disabled"`` - greyed out and cannot be used.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    size_spinbox = tk.Spinbox(root, values=("Small", "Medium", "Large"), state="readonly")
    size_spinbox.pack(pady=20)

    root.mainloop()

command
~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function every time an arrow is clicked.
| **How to write it:** ``command=function_name`` (no brackets)

.. code-block:: python

    import tkinter as tk


    def update_price():
        tickets = int(tickets_spinbox.get())
        price_label.config(text=f"Total: ${tickets * 15}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("command")

    tickets_spinbox = tk.Spinbox(root, from_=1, to=10, width=5, font=("Arial", 16),
                                 state="readonly", command=update_price)
    tickets_spinbox.pack(pady=10)

    price_label = tk.Label(root, text="Total: $15", font=("Arial", 16))
    price_label.pack()

    root.mainloop()

textvariable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the spinbox to a Tkinter variable, so you can read or change it with ``.get()`` and ``.set()``.
| **How to write it:** ``amount = tk.IntVar(value=3)`` then ``textvariable=amount``
| This is also the easiest way to choose the **starting** number.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("textvariable")

    players = tk.IntVar(value=4)        # Start on 4

    players_spinbox = tk.Spinbox(root, from_=1, to=8, textvariable=players)
    players_spinbox.pack(pady=20)

    root.mainloop()

----

Spinbox methods
-------------------

| A **method** is an action that a widget can do. Methods are written after a dot, e.g. ``spinbox.get()``.

get
~~~~~~~~~~~~~~~~~~

| **What it does:** reads what is in the box.
| **How to write it:** ``value = spinbox.get()``
| ``get()`` always gives back a **string**. Use ``int()`` or ``float()`` before doing maths.

.. code-block:: python

    import tkinter as tk


    def calculate():
        pizzas = int(pizza_spinbox.get())      # Text -> number
        result_label.config(text=f"{pizzas * 8} slices")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("get")

    question_label = tk.Label(root, text="How many pizzas?")
    question_label.pack(pady=5)

    pizza_spinbox = tk.Spinbox(root, from_=1, to=20, width=5)
    pizza_spinbox.pack()

    slices_button = tk.Button(root, text="How many slices?", command=calculate)
    slices_button.pack(pady=5)

    result_label = tk.Label(root, text="", font=("Arial", 14))
    result_label.pack()

    root.mainloop()

delete and insert
~~~~~~~~~~~~~~~~~~~~~

| **What they do:** change what is in the box from your code. They work the same as in an **Entry**.
| ``spinbox.delete(0, tk.END)`` clears the box. ``spinbox.insert(0, "5")`` puts text in it.
| To **replace** the value, delete first and then insert.

.. code-block:: python

    import tkinter as tk


    def reset():
        lives_spinbox.delete(0, tk.END)
        lives_spinbox.insert(0, "3")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("delete and insert")

    lives_spinbox = tk.Spinbox(root, from_=0, to=9, width=5, font=("Arial", 16))
    lives_spinbox.pack(pady=10)

    reset_button = tk.Button(root, text="Reset to 3 lives", command=reset)
    reset_button.pack()

    root.mainloop()

| If the state is ``"readonly"``, change it to ``"normal"`` first, then back again, or use a ``textvariable`` and ``.set()`` instead.

Checking typed numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~

| When the state is ``"normal"`` the user could type a word. Use ``try`` and ``except ValueError`` so the program does not crash.

.. code-block:: python

    import tkinter as tk


    def double():
        try:
            number = int(number_spinbox.get())
            result_label.config(text=f"Double: {number * 2}")
        except ValueError:
            result_label.config(text="That is not a number!")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Checking")

    number_spinbox = tk.Spinbox(root, from_=1, to=100, width=6, font=("Arial", 16))
    number_spinbox.pack(pady=10)

    double_button = tk.Button(root, text="Double it", command=double)
    double_button.pack()

    result_label = tk.Label(root, text="", font=("Arial", 14))
    result_label.pack(pady=5)

    root.mainloop()

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options **after** the spinbox has been made.
| **How to write it:** ``spinbox.config(option=value)``

.. code-block:: python

    import tkinter as tk


    def adults_only():
        age_spinbox.config(from_=18, to=100, bg="lightyellow")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    age_spinbox = tk.Spinbox(root, from_=0, to=100, width=5)
    age_spinbox.pack(pady=10)

    adults_button = tk.Button(root, text="Adults only", command=adults_only)
    adults_button.pack()

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
      - A list of choices instead of numbers
      - ``values=("S", "M", "L")``
    * - ``wrap``
      - Go back to the start after the end
      - ``wrap=True``
    * - ``font``, ``width``
      - Font, and width in characters
      - ``font=("Arial", 16), width=5``
    * - ``fg``, ``bg``
      - Text colour, box colour
      - ``bg="lightyellow"``
    * - ``justify``
      - Line up the text
      - ``justify="center"``
    * - ``state``
      - Allow typing, arrows only, or off
      - ``state="readonly"``
    * - ``command``
      - Function to run when an arrow is clicked
      - ``command=update``
    * - ``textvariable``
      - Link to a variable
      - ``textvariable=players``
    * - ``get()``
      - Read the value (as a string)
      - ``int(spinbox.get())``
    * - ``delete()``, ``insert()``
      - Clear the box, put text in it
      - ``spinbox.insert(0, "5")``
    * - ``config()``
      - Change options later
      - ``spinbox.config(to=20)``

----

All Spinbox options
---------------------------

| Here is every option a Spinbox can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``activebackground``
      - Background colour of an arrow when the mouse is over it
      - ``activebackground="lightblue"``
    * - ``bg`` or ``background``
      - Background colour
      - ``bg="lavender"``
    * - ``bd`` or ``borderwidth``
      - How thick the border is
      - ``bd=3``
    * - ``buttonbackground``
      - Background colour of the up and down arrows
      - ``buttonbackground="lightgrey"``
    * - ``buttoncursor``
      - Mouse pointer shape over the arrows
      - ``buttoncursor="hand2"``
    * - ``buttondownrelief``
      - Border style of the down arrow
      - ``buttondownrelief="flat"``
    * - ``buttonuprelief``
      - Border style of the up arrow
      - ``buttonuprelief="flat"``
    * - ``command``
      - Function to run when an arrow is clicked
      - ``command=show``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``disabledbackground``
      - Background colour when it is turned off
      - ``disabledbackground="lightgrey"``
    * - ``disabledforeground``
      - Word colour when it is turned off
      - ``disabledforeground="grey"``
    * - ``exportselection``
      - Lets selected text be copied to other programs (``True`` or ``False``)
      - ``exportselection=False``
    * - ``font``
      - Style and size of the words
      - ``font=("Arial", 14)``
    * - ``fg`` or ``foreground``
      - Word colour
      - ``fg="purple"``
    * - ``format``
      - How the number is shown (``"%.2f"`` = 2 decimal places)
      - ``format="%.2f"``
    * - ``from_``
      - Lowest number. Written ``from_`` in Python
      - ``from_=0``
    * - ``highlightbackground``
      - Colour of the focus outline when it is not selected by the keyboard
      - ``highlightbackground="white"``
    * - ``highlightcolor``
      - Colour of the focus outline when it is selected by the keyboard
      - ``highlightcolor="blue"``
    * - ``highlightthickness``
      - How thick the focus outline is
      - ``highlightthickness=2``
    * - ``increment``
      - How much the number goes up or down each click
      - ``increment=5``
    * - ``insertbackground``
      - Colour of the typing cursor
      - ``insertbackground="red"``
    * - ``insertborderwidth``
      - Border thickness of the typing cursor
      - ``insertborderwidth=1``
    * - ``insertofftime``
      - How long the typing cursor hides when it blinks (milliseconds, ``0`` = no blink)
      - ``insertofftime=300``
    * - ``insertontime``
      - How long the typing cursor shows when it blinks (milliseconds)
      - ``insertontime=600``
    * - ``insertwidth``
      - How wide the typing cursor is (in pixels)
      - ``insertwidth=4``
    * - ``invcmd`` or ``invalidcommand``
      - Function to run when ``validatecommand`` says no
      - ``invcmd=beep``
    * - ``justify``
      - Where the words sit in the box: ``"left"``, ``"center"`` or ``"right"``
      - ``justify="center"``
    * - ``readonlybackground``
      - Background colour when ``state="readonly"``
      - ``readonlybackground="lightyellow"``
    * - ``relief``
      - Border style: ``"raised"``, ``"sunken"``, ``"flat"``, ``"ridge"``, ``"groove"`` or ``"solid"``
      - ``relief="sunken"``
    * - ``repeatdelay``
      - How long to hold an arrow before it keeps counting (milliseconds)
      - ``repeatdelay=500``
    * - ``repeatinterval``
      - How often it counts while an arrow is held (milliseconds)
      - ``repeatinterval=100``
    * - ``selectbackground``
      - Background colour of selected text
      - ``selectbackground="yellow"``
    * - ``selectborderwidth``
      - Border thickness around selected text
      - ``selectborderwidth=1``
    * - ``selectforeground``
      - Word colour of selected text
      - ``selectforeground="black"``
    * - ``state``
      - ``"normal"``, ``"readonly"`` (can see but not type) or ``"disabled"`` (greyed out)
      - ``state="readonly"``
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
    * - ``vcmd`` or ``validatecommand``
      - Function that checks what is typed (returns ``True`` or ``False``)
      - ``vcmd=(root.register(check), "%P")``
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

        What is a Spinbox?

        [x] A box with up and down arrows to step through numbers or choices | Correct. The user can also type.
        [ ] A slider | Incorrect. That is a Scale.
        [ ] A spinning picture | Incorrect. It steps through values.
        [ ] A list that shows every item | Incorrect. That is a Listbox.

    .. multichoice::

        How is the lowest number written?

        [ ] from=1 | Incorrect. from is a Python keyword.
        [x] from_=1 | Correct. The underscore is needed.
        [ ] min=1 | Incorrect. Not an option.
        [ ] start=1 | Incorrect. Not an option.

    .. multichoice::

        What does increment=5 do?

        [x] Each arrow click changes the number by 5 | Correct. increment is the step.
        [ ] Starts at 5 | Incorrect. from\_ sets the start.
        [ ] Allows 5 clicks | Incorrect. It sets the step.
        [ ] Shows 5 numbers | Incorrect. It sets the step.

    .. multichoice::

        What does values=("Red", "Green", "Blue") do?

        [ ] Sets the colours of the box | Incorrect. It sets the choices.
        [x] Steps through these words instead of numbers | Correct. values replaces from\_ and to.
        [ ] Adds three Spinboxes | Incorrect. One Spinbox.
        [ ] Shows a list | Incorrect. It steps through them.

    .. multichoice::

        What does wrap=True do?

        [ ] Wraps long text | Incorrect. It is about the values.
        [x] Goes back to the start after the last value | Correct. It loops round.
        [ ] Stops at the end | Incorrect. That is wrap=False.
        [ ] Makes the box wider | Incorrect. width does that.

    .. multichoice::

        What does width=5 mean?

        [x] About 5 characters wide | Correct. Spinbox width counts characters.
        [ ] 5 pixels | Incorrect. It counts characters.
        [ ] 5 values | Incorrect. It sets the width.
        [ ] 5 lines | Incorrect. It has one line.

    .. multichoice::

        What does justify="center" do?

        [ ] Centres the window | Incorrect. Only the text.
        [x] Puts the number in the middle of the box | Correct. justify lines up the text.
        [ ] Centres the arrows | Incorrect. It lines up the text.
        [ ] Removes the arrows | Incorrect. Arrows still show.

    .. multichoice::

        What does state="readonly" do?

        [ ] Hides the Spinbox | Incorrect. It is still shown.
        [x] Stops typing, but the arrows still work | Correct. readonly blocks typing.
        [ ] Stops the arrows | Incorrect. That is "disabled".
        [ ] Deletes the value | Incorrect. Nothing is deleted.

    .. multichoice::

        What does state="disabled" do?

        [x] Greys it out so neither typing nor arrows work | Correct. It is turned off.
        [ ] Only stops typing | Incorrect. That is "readonly".
        [ ] Hides it | Incorrect. It is still shown.
        [ ] Resets it | Incorrect. Nothing changes.

    .. multichoice::

        When does command run on a Spinbox?

        [ ] When the user types | Incorrect. Only the arrows run it.
        [x] When an arrow is clicked | Correct. command runs on each arrow click.
        [ ] When the window opens | Incorrect. Not then.
        [ ] Never | Incorrect. It runs on arrow clicks.

    .. multichoice::

        What does textvariable=amount do?

        [ ] Sets the font | Incorrect. font does that.
        [x] Links the box to a variable, so amount.get() reads it | Correct. The variable updates with the box.
        [ ] Sets the highest number | Incorrect. to does that.
        [ ] Names the box | Incorrect. It links a variable.

    .. multichoice::

        What type does spinbox.get() give?

        [ ] An int | Incorrect. It is always text.
        [x] A string, so use int() for a number | Correct. Change it before doing maths.
        [ ] A list | Incorrect. One value.
        [ ] A float | Incorrect. It is text.

    .. multichoice::

        How do you set the Spinbox to 10 from code?

        [x] spinbox.delete(0, tk.END) then spinbox.insert(0, 10) | Correct. Clear it, then insert the new value.
        [ ] spinbox.set(10) | Incorrect. tk Spinbox has no set method.
        [ ] spinbox.config(value=10) | Incorrect. Not an option.
        [ ] spinbox.get(10) | Incorrect. get reads.

    .. multichoice::

        Why check typed numbers with try and except?

        [ ] Arrows can type letters | Incorrect. The user can type letters.
        [x] The user might type letters, which makes int() fail | Correct. try and except catch the ValueError.
        [ ] Spinboxes cannot hold numbers | Incorrect. They can.
        [ ] It makes it faster | Incorrect. Not about speed.

    .. multichoice::

        Which line changes the highest number later?

        [ ] spinbox.to(20) | Incorrect. Not a method.
        [x] spinbox.config(to=20) | Correct. config changes options.
        [ ] spinbox.set(to=20) | Incorrect. Not a method.
        [ ] spinbox.max = 20 | Incorrect. Use config.

    .. multichoice::

        Can the user type straight into a Spinbox with state="normal"?

        [x] Yes | Correct. Normal Spinboxes allow typing.
        [ ] No | Incorrect. Typing is allowed.
        [ ] Only numbers | Incorrect. Any characters can be typed.
        [ ] Only with values | Incorrect. Typing works either way.

    .. multichoice::

        If from_=1, to=5 and the value is 5, what does the up arrow do with wrap=False?

        [ ] Goes to 1 | Incorrect. That needs wrap=True.
        [x] Stays at 5 | Correct. Without wrap it stops at the end.
        [ ] Goes to 6 | Incorrect. to is 5.
        [ ] Causes an error | Incorrect. No error.

    .. multichoice::

        What do fg and bg change?

        [ ] The arrows only | Incorrect. They change the box.
        [x] The word colour and the box background | Correct. fg is words, bg is background.
        [ ] The window | Incorrect. Only the Spinbox.
        [ ] The step size | Incorrect. increment does that.

    .. multichoice::

        Which widget suits picking a number of tickets from 1 to 10?

        [x] Spinbox | Correct. It steps through a range of numbers.
        [ ] Text | Incorrect. Too big.
        [ ] Canvas | Incorrect. Canvas draws.
        [ ] Menu | Incorrect. Not ideal.

    .. multichoice::

        Which option would you use for a list of sizes instead of numbers?

        [ ] from\_ | Incorrect. from\_ is for numbers.
        [x] values | Correct. values gives a list of choices.
        [ ] increment | Incorrect. That is the step.
        [ ] wrap | Incorrect. wrap loops round.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a Spinbox from 1 to 10.

        tickets = tk.@@Spinbox | Scale | Entry@@(root, @@from_ | from | start@@=1, @@to | end | max@@=10, width=5)
        tickets.pack()

    .. cloze::
        :instructions: Count in fives and loop round.

        score = tk.Spinbox(root, from_=0, to=50, @@increment | step | resolution@@=5, @@wrap | loop | repeat@@=True)

    .. cloze::
        :instructions: Step through words.

        size = tk.Spinbox(root, @@values | choices | items@@=("Small", "Medium", "Large"), state="@@readonly | disabled | normal@@")

    .. cloze::
        :instructions: Read the number and run a function.

        def show():
            count = @@int | str | list@@(tickets.get())
            result_label.config(text="Cost: $" + str(count * 5))

        tickets = tk.Spinbox(root, from_=1, to=10, @@command | click | run@@=show)

    .. cloze::
        :instructions: Set the value from code.

        tickets.@@delete | clear | remove@@(0, tk.END)
        tickets.@@insert | set | add@@(0, 5)

----

.. admonition:: Tasks

    #. Make a window titled "Tickets" that is 300x200. Add a spinbox from 1 to 6 with an Arial size 20 font and a width of 4.
    #. Change your spinbox so the user can only use the arrows, not type.
    #. Make a spinbox that steps through the values "Red", "Orange", "Yellow", "Green" and wraps back to the start.
    #. Make a spinbox from 1 to 10 and a label. Use ``command`` so that every time an arrow is clicked, the label shows the number multiplied by 3.

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
                    root.title("Tickets")

                    tickets_spinbox = tk.Spinbox(root, from_=1, to=6, font=("Arial", 20), width=4)
                    tickets_spinbox.pack(pady=20)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Tickets")

                    tickets_spinbox = tk.Spinbox(root, from_=1, to=6, font=("Arial", 20), width=4,
                                                 state="readonly")
                    tickets_spinbox.pack(pady=20)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Colours")

                    colour_spinbox = tk.Spinbox(root, values=("Red", "Orange", "Yellow", "Green"),
                                                wrap=True)
                    colour_spinbox.pack(pady=20)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def times_three():
                        number = int(number_spinbox.get())
                        answer_label.config(text=f"{number} x 3 = {number * 3}")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Times 3")

                    number_spinbox = tk.Spinbox(root, from_=1, to=10, width=5, command=times_three)
                    number_spinbox.pack(pady=10)

                    answer_label = tk.Label(root, text="1 x 3 = 3", font=("Arial", 16))
                    answer_label.pack()

                    root.mainloop()
