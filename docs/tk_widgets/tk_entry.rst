====================================================
tk Entry
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Entry>`_

----

What is an Entry?
-------------------

| An **Entry** is a box the user can type into.
| It holds **one line** of text, so it is good for short answers like a name, a password or a number.
| For several lines of text, use a **Text** widget instead.

----

Making an Entry
-------------------

| Every Entry is made in two steps:

#. **Create** the entry with ``tk.Entry(...)``.
#. **Place** the entry in the window with ``.pack()``.

| An Entry starts empty. Run the code below and click in the box to type.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first entry")    # Words in the title bar

    entry = tk.Entry(root)          # 1. Create the entry
    entry.pack(pady=20)             # 2. Place it in the window, 20 pixels from the top

    root.mainloop()                 # Keep the window open

| An Entry has no words next to it, so the user will not know what to type.
| Put a **Label** above it as an instruction:

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Entry with a label")

    name_label = tk.Label(root, text="Type your name:")
    name_label.pack(pady=5)

    name_entry = tk.Entry(root)
    name_entry.pack()

    root.mainloop()

----

Entry options
-------------------

| Options are written as ``option=value`` inside ``tk.Entry( )``, separated by commas.

font
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the style and size of the letters the user types.
| **How to write it:** ``font=("font name", size)`` or ``font=("font name", size, "style")``
| A bigger font also makes the box taller.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("font")

    entry = tk.Entry(root, font=("Arial", 24))
    entry.pack(pady=20)

    root.mainloop()

width
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how wide the box is, measured in **characters** (letters).
| **How to write it:** ``width=10``
| If you leave it out, the box is 20 characters wide. The user can still type more than fits; the text scrolls sideways.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width")

    short_entry = tk.Entry(root, width=5)
    short_entry.pack(pady=10)

    long_entry = tk.Entry(root, width=40)
    long_entry.pack(pady=10)

    root.mainloop()

fg and bg (colours)
~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``fg`` sets the colour of the typed letters. ``bg`` sets the colour of the box.
| **How to write them:** ``fg="colour"``, ``bg="colour"``
| Use a colour name such as ``"navy"`` or a hex code such as ``"#ffffcc"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("fg and bg")

    entry = tk.Entry(root, font=("Arial", 18), fg="navy", bg="lightyellow")
    entry.pack(pady=20)

    root.mainloop()

justify
~~~~~~~~~~~~~~~~~~

| **What it does:** lines up the typed text on the left, in the centre, or on the right of the box.
| **How to write it:** ``justify="center"``
| **Values:** ``"left"`` (the default), ``"center"``, ``"right"``. Numbers often look best on the ``"right"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("justify")

    left_entry = tk.Entry(root, font=("Arial", 16), justify="left")
    left_entry.pack(pady=5)

    centre_entry = tk.Entry(root, font=("Arial", 16), justify="center")
    centre_entry.pack(pady=5)

    right_entry = tk.Entry(root, font=("Arial", 16), justify="right")
    right_entry.pack(pady=5)

    root.mainloop()

show
~~~~~~~~~~~~~~~~~~

| **What it does:** hides what the user types by showing another character instead. Used for **passwords**.
| **How to write it:** ``show="*"``
| ``get()`` still reads the real letters that were typed.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("show")

    password_label = tk.Label(root, text="Password:")
    password_label.pack(pady=5)

    password_entry = tk.Entry(root, font=("Arial", 16), show="*")
    password_entry.pack()

    root.mainloop()

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** change the border around the box.
| ``relief`` is the border style. ``borderwidth`` is how thick it is in pixels.
| **How to write them:** ``relief="solid", borderwidth=2``
| **Styles:** ``"sunken"`` (the usual look), ``"solid"``, ``"flat"``, ``"raised"``, ``"groove"``, ``"ridge"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("relief")

    entry = tk.Entry(root, font=("Arial", 16), relief="solid", borderwidth=2)
    entry.pack(pady=20)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** controls whether the user can type in the box.
| **How to write it:** ``state="readonly"``
| **Values:**

- ``"normal"`` - the user can type (the default).
- ``"readonly"`` - the user can see and copy the text but cannot change it. Good for showing an answer.
- ``"disabled"`` - the box is greyed out and cannot be used.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    normal_entry = tk.Entry(root, state="normal")
    normal_entry.pack(pady=5)

    readonly_entry = tk.Entry(root, state="readonly")
    readonly_entry.pack(pady=5)

    disabled_entry = tk.Entry(root, state="disabled")
    disabled_entry.pack(pady=5)

    root.mainloop()

textvariable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the entry to a **StringVar**, a special Tkinter variable that stores text.
| Whatever is typed in the box is stored in the StringVar, and changing the StringVar changes the box.
| **How to write it:** ``answer = tk.StringVar()`` then ``textvariable=answer``
| Read the text with ``answer.get()``. Change it with ``answer.set("new text")``.

.. code-block:: python

    import tkinter as tk


    def make_capitals():
        word.set(word.get().upper())    # Read the word, make it CAPITALS, put it back


    root = tk.Tk()
    root.geometry("300x200")
    root.title("textvariable")

    word = tk.StringVar(value="hello")

    entry = tk.Entry(root, textvariable=word, font=("Arial", 16))
    entry.pack(pady=20)

    button = tk.Button(root, text="CAPITALS", command=make_capitals)
    button.pack()

    root.mainloop()

----

Entry methods
-------------------

| A **method** is an action that a widget can do. Methods are written after a dot, e.g. ``entry.get()``.

get
~~~~~~~~~~~~~~~~~~

| **What it does:** reads what the user has typed.
| **How to write it:** ``text = entry.get()``
| ``get()`` is usually used inside a function that runs when a button is clicked.

.. code-block:: python

    import tkinter as tk


    def say_hello():
        name = name_entry.get()                     # Read the typed name
        answer_label.config(text="Hello " + name)   # Show it on the label


    root = tk.Tk()
    root.geometry("300x200")
    root.title("get")

    name_entry = tk.Entry(root, font=("Arial", 16))
    name_entry.pack(pady=10)

    hello_button = tk.Button(root, text="Say hello", command=say_hello)
    hello_button.pack()

    answer_label = tk.Label(root, text="", font=("Arial", 16))
    answer_label.pack(pady=10)

    root.mainloop()

Getting a number
~~~~~~~~~~~~~~~~~~

| ``get()`` always gives back a **string** (text), even if the user typed a number.
| Text cannot be used in maths, so turn it into a number first:

- ``int(entry.get())`` for whole numbers, e.g. ``7``
- ``float(entry.get())`` for decimal numbers, e.g. ``2.5``

| If the user types something that is not a number, Python shows a ``ValueError``.
| ``try`` and ``except`` catch the error and show a friendly message instead of crashing.

.. code-block:: python

    import tkinter as tk


    def double_it():
        try:
            number = float(number_entry.get())          # Text -> number
            answer_label.config(text=number * 2)
        except ValueError:
            answer_label.config(text="Please type a number")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Getting a number")

    number_entry = tk.Entry(root, font=("Arial", 16), width=10)
    number_entry.pack(pady=10)

    double_button = tk.Button(root, text="Double it", command=double_it)
    double_button.pack()

    answer_label = tk.Label(root, text="", font=("Arial", 16))
    answer_label.pack(pady=10)

    root.mainloop()

delete
~~~~~~~~~~~~~~~~~~

| **What it does:** removes text from the box.
| **How to write it:** ``entry.delete(0, tk.END)``
| ``0`` means the first character and ``tk.END`` means the end, so this clears **everything**.

.. code-block:: python

    import tkinter as tk


    def clear():
        entry.delete(0, tk.END)     # Remove all the text


    root = tk.Tk()
    root.geometry("300x200")
    root.title("delete")

    entry = tk.Entry(root, font=("Arial", 16))
    entry.pack(pady=20)

    clear_button = tk.Button(root, text="Clear", command=clear)
    clear_button.pack()

    root.mainloop()

insert
~~~~~~~~~~~~~~~~~~

| **What it does:** puts text into the box from your code.
| **How to write it:** ``entry.insert(0, "text")``
| ``0`` puts the text at the start. Use ``tk.END`` to add it to the end instead.
| To **replace** the text, ``delete`` it first and then ``insert``.

.. code-block:: python

    import tkinter as tk


    def fill_in():
        entry.delete(0, tk.END)         # Clear the box first
        entry.insert(0, "Parade")       # Then put in the new text


    root = tk.Tk()
    root.geometry("300x200")
    root.title("insert")

    entry = tk.Entry(root, font=("Arial", 16))
    entry.insert(0, "Type here")        # Starting text
    entry.pack(pady=20)

    fill_button = tk.Button(root, text="Fill in", command=fill_in)
    fill_button.pack()

    root.mainloop()

focus_set
~~~~~~~~~~~~~~~~~~

| **What it does:** puts the flashing typing cursor in the box, so the user can type straight away without clicking.
| **How to write it:** ``entry.focus_set()``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("focus_set")

    first_entry = tk.Entry(root, font=("Arial", 16))
    first_entry.pack(pady=10)

    second_entry = tk.Entry(root, font=("Arial", 16))
    second_entry.pack(pady=10)

    second_entry.focus_set()        # The cursor starts in the second box

    root.mainloop()

select_range
~~~~~~~~~~~~~~~~~~

| **What it does:** highlights (selects) text in the box. Whatever the user types next replaces the highlighted text.
| **How to write it:** ``entry.select_range(0, tk.END)`` highlights everything.
| It is often used with ``focus_set()`` to let the user quickly retype a wrong answer.

.. code-block:: python

    import tkinter as tk


    def check():
        if answer_entry.get() == "12":
            result_label.config(text="Correct!", fg="green")
        else:
            result_label.config(text="Try again", fg="red")
            answer_entry.focus_set()                    # Cursor back in the box
            answer_entry.select_range(0, tk.END)        # Highlight the wrong answer


    root = tk.Tk()
    root.geometry("300x200")
    root.title("select_range")

    question_label = tk.Label(root, text="What is 3 x 4?", font=("Arial", 16))
    question_label.pack(pady=5)

    answer_entry = tk.Entry(root, font=("Arial", 16), width=5)
    answer_entry.pack()

    check_button = tk.Button(root, text="Check", command=check)
    check_button.pack(pady=5)

    result_label = tk.Label(root, text="", font=("Arial", 16))
    result_label.pack()

    root.mainloop()

bind (pressing Enter)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function when a key is pressed in the box.
| **How to write it:** ``entry.bind("<Return>", function_name)``
| ``"<Return>"`` is the Enter key.
| A function run by ``bind`` is given extra information about the key press, so the function needs a parameter called ``event``.
| Writing ``event=None`` lets the same function work for a button too.

.. code-block:: python

    import tkinter as tk


    def say_hello(event=None):
        answer_label.config(text="Hello " + name_entry.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("bind")

    name_entry = tk.Entry(root, font=("Arial", 16))
    name_entry.pack(pady=10)
    name_entry.bind("<Return>", say_hello)      # Press Enter to run say_hello

    hello_button = tk.Button(root, text="Say hello", command=say_hello)
    hello_button.pack()

    answer_label = tk.Label(root, text="", font=("Arial", 16))
    answer_label.pack(pady=10)

    root.mainloop()

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes one or more options **after** the entry has been made.
| **How to write it:** ``entry.config(option=value)``
| A program cannot ``insert`` or ``delete`` while the state is ``"readonly"``, so change it to ``"normal"`` first, then back again.

.. code-block:: python

    import tkinter as tk


    def show_answer():
        answer_entry.config(state="normal")         # Unlock the box
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, "Canberra")
        answer_entry.config(state="readonly")       # Lock it again


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    question_label = tk.Label(root, text="Capital of Australia?", font=("Arial", 14))
    question_label.pack(pady=5)

    answer_entry = tk.Entry(root, font=("Arial", 16), state="readonly")
    answer_entry.pack()

    show_button = tk.Button(root, text="Show answer", command=show_answer)
    show_button.pack(pady=10)

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
    * - ``font``
      - Font name, size and style
      - ``font=("Arial", 16)``
    * - ``width``
      - Width of the box in characters
      - ``width=10``
    * - ``fg``
      - Colour of the typed letters
      - ``fg="navy"``
    * - ``bg``
      - Colour of the box
      - ``bg="lightyellow"``
    * - ``justify``
      - Line up the text left, centre or right
      - ``justify="center"``
    * - ``show``
      - Hide typing (passwords)
      - ``show="*"``
    * - ``relief``, ``borderwidth``
      - Border style and thickness
      - ``relief="solid", borderwidth=2``
    * - ``state``
      - Allow or stop typing
      - ``state="readonly"``
    * - ``textvariable``
      - Link the box to a StringVar
      - ``textvariable=word``
    * - ``get()``
      - Read the typed text
      - ``name = entry.get()``
    * - ``delete()``
      - Clear the box
      - ``entry.delete(0, tk.END)``
    * - ``insert()``
      - Put text in the box
      - ``entry.insert(0, "hi")``
    * - ``focus_set()``
      - Put the cursor in the box
      - ``entry.focus_set()``
    * - ``select_range()``
      - Highlight the text
      - ``entry.select_range(0, tk.END)``
    * - ``bind()``
      - Run a function when a key is pressed
      - ``entry.bind("<Return>", go)``
    * - ``config()``
      - Change options later
      - ``entry.config(bg="pink")``

----

.. admonition:: Tasks

    #. Make a window titled "Sign in" that is 300x200. Add a label "Username:" and an Entry below it using Arial size 16, with a light blue background.
    #. Add a label "Password:" and a password Entry that shows ``"*"`` instead of the letters typed.
    #. Make an Entry and a button labelled "Clear". When the button is clicked, the Entry is emptied.
    #. Make an Entry where the user types their age, and a button labelled "Next year". When it is clicked, a label shows how old they will be next year. Use ``try`` and ``except`` so the program does not crash if a word is typed.

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
                    root.title("Sign in")

                    user_label = tk.Label(root, text="Username:")
                    user_label.pack()

                    user_entry = tk.Entry(root, font=("Arial", 16), bg="lightblue")
                    user_entry.pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Sign in")

                    user_label = tk.Label(root, text="Username:")
                    user_label.pack()

                    user_entry = tk.Entry(root, font=("Arial", 16), bg="lightblue")
                    user_entry.pack()

                    password_label = tk.Label(root, text="Password:")
                    password_label.pack()

                    password_entry = tk.Entry(root, font=("Arial", 16), bg="lightblue", show="*")
                    password_entry.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk


                    def clear():
                        entry.delete(0, tk.END)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Clear")

                    entry = tk.Entry(root, font=("Arial", 16))
                    entry.pack(pady=20)

                    clear_button = tk.Button(root, text="Clear", command=clear)
                    clear_button.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def next_year():
                        try:
                            age = int(age_entry.get())
                            answer_label.config(text=f"Next year you will be {age + 1}")
                        except ValueError:
                            answer_label.config(text="Please type a whole number")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Age")

                    age_label = tk.Label(root, text="How old are you?")
                    age_label.pack(pady=5)

                    age_entry = tk.Entry(root, font=("Arial", 16), width=5)
                    age_entry.pack()

                    next_button = tk.Button(root, text="Next year", command=next_year)
                    next_button.pack(pady=5)

                    answer_label = tk.Label(root, text="", font=("Arial", 14))
                    answer_label.pack()

                    root.mainloop()
