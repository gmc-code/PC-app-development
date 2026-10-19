====================================================
tk Button
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Button>`_

----

What is a Button?
-------------------

| A **Button** is something the user clicks to make the program do something.
| Each button is linked to a **function**. When the button is clicked, the function runs.

----

Making a Button
-------------------

| Every Button is made in two steps:

#. **Create** the button with ``tk.Button(...)``.
#. **Place** the button in the window with ``.pack()``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first button")   # Words in the title bar

    button = tk.Button(root, text="Click me")   # 1. Create the button
    button.pack(pady=20)                        # 2. Place it in the window

    root.mainloop()                 # Keep the window open

| This button can be clicked, but nothing happens yet. The ``command`` option below makes it do something.

----

Button options
-------------------

| Options are written as ``option=value`` inside ``tk.Button( )``, separated by commas.

text
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the words on the button.
| **How to write it:** ``text="your words"``
| Keep button words short and clear, e.g. ``"Start"``, ``"Check answer"``, ``"Quit"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("text")

    button = tk.Button(root, text="Start the game")
    button.pack(pady=20)

    root.mainloop()

command
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses the function that runs when the button is clicked.
| **How to write it:** ``command=function_name``
| The function must be written (defined with ``def``) **above** the button.

.. warning::

    Do **not** put brackets after the function name.

    - ``command=say_hello`` ✔ runs the function when the button is clicked.
    - ``command=say_hello()`` ✘ runs the function straight away, before anyone clicks.

.. code-block:: python

    import tkinter as tk


    def say_hello():
        message_label.config(text="Hello!")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("command")

    hello_button = tk.Button(root, text="Say hello", command=say_hello)
    hello_button.pack(pady=20)

    message_label = tk.Label(root, text="", font=("Arial", 20))
    message_label.pack()

    root.mainloop()

font
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the style and size of the words on the button.
| **How to write it:** ``font=("font name", size)`` or ``font=("font name", size, "style")``
| **Styles:** ``"bold"``, ``"italic"``, ``"underline"``, or more than one, e.g. ``"bold italic"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("font")

    button = tk.Button(root, text="Big button", font=("Arial", 20, "bold"))
    button.pack(pady=20)

    root.mainloop()

fg and bg (colours)
~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``fg`` sets the colour of the words. ``bg`` sets the colour of the button.
| **How to write them:** ``fg="colour"``, ``bg="colour"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("fg and bg")

    go_button = tk.Button(root, text="GO", font=("Arial", 16), fg="white", bg="green")
    go_button.pack(pady=10)

    stop_button = tk.Button(root, text="STOP", font=("Arial", 16), fg="white", bg="red")
    stop_button.pack(pady=10)

    root.mainloop()

.. note::

    On a Mac, buttons ignore ``bg``. These colours work on Windows.

activebackground and activeforeground
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** set the colours **while the button is being pressed**.
| ``activebackground`` is the button colour and ``activeforeground`` is the word colour while pressed.
| **How to write them:** ``activebackground="colour"``, ``activeforeground="colour"``
| Hold the mouse button down on the button to see the change.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("active colours")

    button = tk.Button(
        root,
        text="Press and hold",
        font=("Arial", 16),
        bg="lightblue",             # Normal colour
        activebackground="navy",    # Colour while pressed
        activeforeground="white",   # Word colour while pressed
    )
    button.pack(pady=20)

    root.mainloop()

width and height
~~~~~~~~~~~~~~~~~~

| **What they do:** set the size of the button.
| ``width`` is measured in **characters** (letters), and ``height`` in **lines** of text.
| **How to write them:** ``width=15``, ``height=2``
| Giving several buttons the same width makes them line up neatly.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and height")

    yes_button = tk.Button(root, text="Yes", width=15)
    yes_button.pack(pady=5)

    no_button = tk.Button(root, text="No", width=15)
    no_button.pack(pady=5)

    tall_button = tk.Button(root, text="Tall", width=15, height=3)
    tall_button.pack(pady=5)

    root.mainloop()

padx and pady
~~~~~~~~~~~~~~~~~~

| **What they do:** add empty space around the words, **inside** the button, making it bigger.
| ``padx`` adds space on the left and right. ``pady`` adds space on the top and bottom.
| **How to write them:** ``padx=20``, ``pady=10`` (measured in pixels)

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("padx and pady")

    button = tk.Button(root, text="Padded", padx=40, pady=15)
    button.pack(pady=20)

    root.mainloop()

.. note::

    ``.pack()`` can also have ``padx`` and ``pady``. Those add space **outside** the button,
    pushing it away from other widgets, e.g. ``button.pack(pady=20)``.

relief, borderwidth and overrelief
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** change the border of the button.
| ``relief`` is the border style. ``borderwidth`` is how thick it is in pixels.
| ``overrelief`` is the border style while the mouse is **over** the button.
| **How to write them:** ``relief="raised", borderwidth=3, overrelief="sunken"``
| **Styles:** ``"raised"`` (the default), ``"sunken"``, ``"flat"``, ``"solid"``, ``"groove"``, ``"ridge"``.
| Move the mouse over the button below to see ``overrelief`` working.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("relief")

    button = tk.Button(root, text="Hover over me", font=("Arial", 14),
                       relief="raised", borderwidth=4, overrelief="sunken")
    button.pack(pady=20)

    root.mainloop()

cursor
~~~~~~~~~~~~~~~~~~

| **What it does:** changes the mouse pointer when it is over the button.
| **How to write it:** ``cursor="hand2"``
| **Some values:** ``"hand2"`` (a pointing hand), ``"arrow"``, ``"cross"``, ``"watch"``, ``"heart"``, ``"star"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("cursor")

    button = tk.Button(root, text="Point at me", font=("Arial", 14), cursor="hand2")
    button.pack(pady=20)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** turns the button on or off.
| **How to write it:** ``state="disabled"``
| **Values:** ``"normal"`` (can be clicked, the default) and ``"disabled"`` (greyed out, cannot be clicked).

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    on_button = tk.Button(root, text="I work", state="normal")
    on_button.pack(pady=10)

    off_button = tk.Button(root, text="I am turned off", state="disabled")
    off_button.pack(pady=10)

    root.mainloop()

----

Button methods and tricks
-----------------------------

| A **method** is an action that a widget can do. Methods are written after a dot, e.g. ``button.config(...)``.

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes one or more options **after** the button has been made.
| **How to write it:** ``button.config(option=value)``
| A common use is to turn a button off after it has been clicked, so it can only be used once.

.. code-block:: python

    import tkinter as tk


    def vote():
        vote_button.config(text="Thanks for voting!", state="disabled")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    vote_button = tk.Button(root, text="Vote", font=("Arial", 16), command=vote)
    vote_button.pack(pady=20)

    root.mainloop()

cget
~~~~~~~~~~~~~~~~~~

| **What it does:** reads (gets) the current value of an option.
| **How to write it:** ``value = button.cget("option")``
| Below, ``cget("text")`` checks what the button says, so one button can switch between ON and OFF.

.. code-block:: python

    import tkinter as tk


    def switch():
        if light_button.cget("text") == "ON":
            light_button.config(text="OFF", bg="gray")
        else:
            light_button.config(text="ON", bg="yellow")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("cget")

    light_button = tk.Button(root, text="OFF", bg="gray", font=("Arial", 20), width=6,
                             command=switch)
    light_button.pack(pady=20)

    root.mainloop()

invoke
~~~~~~~~~~~~~~~~~~

| **What it does:** "clicks" the button from your code, so its command runs.
| **How to write it:** ``button.invoke()``
| Below, pressing the **Enter** key invokes the button. ``root.bind("<Return>", ...)`` watches for the Enter key.

.. code-block:: python

    import tkinter as tk


    def say_hello():
        message_label.config(text="Hello!")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("invoke")

    hello_button = tk.Button(root, text="Say hello", command=say_hello)
    hello_button.pack(pady=20)

    message_label = tk.Label(root, text="Click or press Enter", font=("Arial", 16))
    message_label.pack()

    root.bind("<Return>", lambda event: hello_button.invoke())

    root.mainloop()

A Quit button
~~~~~~~~~~~~~~~~~~

| ``root.destroy`` closes the window, so it can be used as a button's command.
| Remember: no brackets after ``destroy``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Quit")

    quit_button = tk.Button(root, text="Quit", bg="salmon", command=root.destroy)
    quit_button.pack(pady=20)

    root.mainloop()

Sending a value with lambda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Sometimes you want several buttons to use **one** function, but each button sends a different value.
| ``command=change_colour("red")`` would not work, because the brackets run the function straight away.
| Put ``lambda:`` in front. It means "wait until the button is clicked, then run this".
| **How to write it:** ``command=lambda: function_name(value)``

.. code-block:: python

    import tkinter as tk


    def change_colour(colour):
        root.config(bg=colour)      # Change the window's background colour


    root = tk.Tk()
    root.geometry("300x200")
    root.title("lambda")

    red_button = tk.Button(root, text="Red", width=10, command=lambda: change_colour("red"))
    red_button.pack(pady=5)

    green_button = tk.Button(root, text="Green", width=10, command=lambda: change_colour("green"))
    green_button.pack(pady=5)

    blue_button = tk.Button(root, text="Blue", width=10, command=lambda: change_colour("blue"))
    blue_button.pack(pady=5)

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
      - Words on the button
      - ``text="Start"``
    * - ``command``
      - Function to run when clicked (no brackets)
      - ``command=start``
    * - ``font``
      - Font name, size and style
      - ``font=("Arial", 16)``
    * - ``fg``
      - Colour of the words
      - ``fg="white"``
    * - ``bg``
      - Colour of the button
      - ``bg="green"``
    * - ``activebackground``
      - Button colour while pressed
      - ``activebackground="navy"``
    * - ``activeforeground``
      - Word colour while pressed
      - ``activeforeground="white"``
    * - ``width``, ``height``
      - Size in characters and lines
      - ``width=15, height=2``
    * - ``padx``, ``pady``
      - Space inside the button around the words
      - ``padx=20, pady=10``
    * - ``relief``, ``borderwidth``
      - Border style and thickness
      - ``relief="solid", borderwidth=2``
    * - ``overrelief``
      - Border style when the mouse is over it
      - ``overrelief="sunken"``
    * - ``cursor``
      - Mouse pointer shape over the button
      - ``cursor="hand2"``
    * - ``state``
      - Turn the button on or off
      - ``state="disabled"``
    * - ``config()``
      - Change options later
      - ``button.config(text="Done")``
    * - ``cget()``
      - Read an option
      - ``button.cget("text")``
    * - ``invoke()``
      - Click the button from code
      - ``button.invoke()``

----

.. admonition:: Tasks

    #. Make a window titled "Buttons" that is 300x200. Add a button that says "Press me" in Arial size 16, with white words on a purple background, and a width of 15.
    #. Change your button so it turns black while being pressed and shows a hand pointer when the mouse is over it.
    #. Add a label below the button. When the button is clicked, the label shows "You pressed the button!".
    #. Make a "Roll" button and a label. When the button is clicked, the label shows a random number from 1 to 6. (Hint: ``import random`` and use ``random.randint(1, 6)``.)
    #. Make three buttons, "Small", "Medium" and "Large", that all use **one** function to change the font size of a label to 10, 20 or 30. Use ``lambda``.

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
                    root.title("Buttons")

                    button = tk.Button(root, text="Press me", font=("Arial", 16),
                                       fg="white", bg="purple", width=15)
                    button.pack(pady=20)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Buttons")

                    button = tk.Button(root, text="Press me", font=("Arial", 16),
                                       fg="white", bg="purple", width=15,
                                       activebackground="black", activeforeground="white",
                                       cursor="hand2")
                    button.pack(pady=20)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk


                    def pressed():
                        message_label.config(text="You pressed the button!")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Buttons")

                    button = tk.Button(root, text="Press me", font=("Arial", 16),
                                       fg="white", bg="purple", width=15,
                                       activebackground="black", activeforeground="white",
                                       cursor="hand2", command=pressed)
                    button.pack(pady=20)

                    message_label = tk.Label(root, text="", font=("Arial", 14))
                    message_label.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    import random


                    def roll():
                        dice_label.config(text=random.randint(1, 6))


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Dice")

                    roll_button = tk.Button(root, text="Roll", font=("Arial", 16), command=roll)
                    roll_button.pack(pady=10)

                    dice_label = tk.Label(root, text="?", font=("Arial", 40))
                    dice_label.pack()

                    root.mainloop()

            .. tab-item:: Q5

                .. code-block:: python

                    import tkinter as tk


                    def set_size(size):
                        word_label.config(font=("Arial", size))


                    root = tk.Tk()
                    root.geometry("300x250")
                    root.title("Sizes")

                    small_button = tk.Button(root, text="Small", width=10, command=lambda: set_size(10))
                    small_button.pack(pady=2)

                    medium_button = tk.Button(root, text="Medium", width=10, command=lambda: set_size(20))
                    medium_button.pack(pady=2)

                    large_button = tk.Button(root, text="Large", width=10, command=lambda: set_size(30))
                    large_button.pack(pady=2)

                    word_label = tk.Label(root, text="Hello", font=("Arial", 20))
                    word_label.pack(pady=10)

                    root.mainloop()
