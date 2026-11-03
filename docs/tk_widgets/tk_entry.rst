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

All Entry options
---------------------------

| Here is every option an Entry can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``bg`` or ``background``
      - Background colour
      - ``bg="lavender"``
    * - ``bd`` or ``borderwidth``
      - How thick the border is
      - ``bd=3``
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
    * - ``highlightbackground``
      - Colour of the focus outline when it is not selected by the keyboard
      - ``highlightbackground="white"``
    * - ``highlightcolor``
      - Colour of the focus outline when it is selected by the keyboard
      - ``highlightcolor="blue"``
    * - ``highlightthickness``
      - How thick the focus outline is
      - ``highlightthickness=2``
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
    * - ``selectbackground``
      - Background colour of selected text
      - ``selectbackground="yellow"``
    * - ``selectborderwidth``
      - Border thickness around selected text
      - ``selectborderwidth=1``
    * - ``selectforeground``
      - Word colour of selected text
      - ``selectforeground="black"``
    * - ``show``
      - Shows this character instead of what is typed (good for passwords)
      - ``show="*"``
    * - ``state``
      - ``"normal"``, ``"readonly"`` (can see but not type) or ``"disabled"`` (greyed out)
      - ``state="readonly"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``textvariable``
      - A variable that holds what is typed in the box
      - ``textvariable=name``
    * - ``validate``
      - When to check what is typed: ``"none"``, ``"key"``, ``"focus"``, ``"focusin"``, ``"focusout"`` or ``"all"``
      - ``validate="key"``
    * - ``vcmd`` or ``validatecommand``
      - Function that checks what is typed (returns ``True`` or ``False``)
      - ``vcmd=(root.register(check), "%P")``
    * - ``width``
      - How wide it is (in characters)
      - ``width=15``
    * - ``xscrollcommand``
      - Connects it to a side-to-side scrollbar
      - ``xscrollcommand=x_scrollbar.set``

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

        What is an Entry?

        [x] A box where the user can type one line | Correct. Entry is for one line of typing.
        [ ] A box for many lines | Incorrect. The Text widget is for many lines.
        [ ] A button | Incorrect. Buttons are clicked.
        [ ] A picture | Incorrect. Images use Label or Canvas.

    .. multichoice::

        For an Entry, what does width=20 mean?

        [ ] 20 pixels | Incorrect. Entry width is in characters.
        [x] About 20 characters wide | Correct. Entry width counts characters.
        [ ] 20 lines | Incorrect. Entry has one line.
        [ ] 20 words | Incorrect. It counts characters.

    .. multichoice::

        Which option makes the typed words red?

        [x] fg="red" | Correct. fg sets the word colour.
        [ ] bg="red" | Incorrect. bg sets the box colour.
        [ ] colour="red" | Incorrect. colour is not an option.
        [ ] text="red" | Incorrect. Entry has no text option.

    .. multichoice::

        What does justify="center" do?

        [ ] Makes the box bigger | Incorrect. width sets the size.
        [ ] Centres the window | Incorrect. It only affects the Entry.
        [x] Puts the typed words in the middle of the box | Correct. justify lines up the words.
        [ ] Clears the box | Incorrect. delete clears the box.

    .. multichoice::

        What does show="\*" do?

        [x] Shows a star for each letter typed, good for passwords | Correct. The real letters are still stored.
        [ ] Shows the letters normally | Incorrect. show hides them behind stars.
        [ ] Stops typing | Incorrect. state does that.
        [ ] Adds a star at the end | Incorrect. Each letter shows as a star.

    .. multichoice::

        What does state="readonly" mean?

        [ ] The box is hidden | Incorrect. It is still shown.
        [x] The user can see the words but cannot type | Correct. readonly stops typing.
        [ ] The words are deleted | Incorrect. It does not delete.
        [ ] The box turns red | Incorrect. It does not change colour.

    .. multichoice::

        Which method reads what was typed?

        [ ] entry.read() | Incorrect. This method does not exist.
        [x] entry.get() | Correct. get gives the typed text.
        [ ] entry.text() | Incorrect. This method does not exist.
        [ ] entry.value | Incorrect. That is not used.

    .. multichoice::

        What type is the result of entry.get()?

        [ ] A whole number | Incorrect. It is always text.
        [ ] A decimal number | Incorrect. It is always text.
        [x] A string (text) | Correct. Use int() or float() to make a number.
        [ ] A list | Incorrect. It is one piece of text.

    .. multichoice::

        How do you turn the typed text into a whole number?

        [ ] str(entry.get()) | Incorrect. str makes text.
        [x] int(entry.get()) | Correct. int changes text to a whole number.
        [ ] entry.get().number | Incorrect. That does not exist.
        [ ] number(entry.get()) | Incorrect. number is not a Python function.

    .. multichoice::

        What happens if int(entry.get()) is used when "abc" was typed?

        [ ] It gives 0 | Incorrect. Python cannot change abc to a number.
        [x] A ValueError | Correct. abc is not a number.
        [ ] It gives "abc" | Incorrect. int must give a number.
        [ ] It ignores it | Incorrect. An error happens.

    .. multichoice::

        Which line clears everything in the Entry?

        [x] entry.delete(0, tk.END) | Correct. Delete from the first character to the end.
        [ ] entry.clear() | Incorrect. Entries do not have clear.
        [ ] entry.delete() | Incorrect. delete needs a start.
        [ ] entry.insert(0, "") | Incorrect. That adds nothing; it does not clear.

    .. multichoice::

        What does entry.insert(0, "Hello") do?

        [ ] Deletes Hello | Incorrect. insert adds text.
        [ ] Adds Hello at the end | Incorrect. 0 means the start.
        [x] Puts Hello at the start of the box | Correct. 0 is the first position.
        [ ] Replaces the window title | Incorrect. It only changes the Entry.

    .. multichoice::

        What does entry.focus_set() do?

        [x] Puts the typing cursor in the box so the user can type straight away | Correct. focus_set selects the box.
        [ ] Highlights the text | Incorrect. select_range does that.
        [ ] Clears the box | Incorrect. delete clears.
        [ ] Makes the box bigger | Incorrect. width does that.

    .. multichoice::

        What does entry.select_range(0, tk.END) do?

        [ ] Deletes all the text | Incorrect. delete does that.
        [x] Highlights all the text | Correct. select_range selects text.
        [ ] Moves the box | Incorrect. pack or grid move widgets.
        [ ] Reads the text | Incorrect. get reads text.

    .. multichoice::

        Which event runs a function when Enter is pressed?

        [ ] "<Enter>" | Incorrect. That is the mouse moving onto a widget.
        [ ] "<Key-Enter>" | Incorrect. This is not the event name.
        [x] "<Return>" | Correct. Return is the Enter key.
        [ ] "<Button-1>" | Incorrect. That is a mouse click.

    .. multichoice::

        A function used with bind needs:

        [x] A parameter, such as event | Correct. bind sends an event to the function.
        [ ] No parameters | Incorrect. bind always sends an event.
        [ ] Two parameters | Incorrect. It gets one event.
        [ ] A return value | Incorrect. It does not need to return.

    .. multichoice::

        What does textvariable=name do?

        [ ] Sets the font | Incorrect. font sets the font.
        [x] Links the box to a StringVar, so name.get() reads it | Correct. Changes in the box update the variable.
        [ ] Sets the box name | Incorrect. It links a variable.
        [ ] Hides the text | Incorrect. show hides text.

    .. multichoice::

        Which line makes the box pink later?

        [ ] entry.bg = "pink" | Incorrect. Options are changed with config.
        [x] entry.config(bg="pink") | Correct. config changes options.
        [ ] entry.set(bg="pink") | Incorrect. Entries do not have set.
        [ ] entry.pink() | Incorrect. That does not exist.

    .. multichoice::

        Which tk constant means "the end of the text"?

        [ ] tk.LAST | Incorrect. That is not used here.
        [ ] tk.STOP | Incorrect. That does not exist.
        [x] tk.END | Correct. END means the end.
        [ ] tk.FINISH | Incorrect. That does not exist.

    .. multichoice::

        Which widget suits typing a name?

        [x] Entry | Correct. A name fits on one line.
        [ ] Label | Incorrect. Labels cannot be typed in.
        [ ] Scale | Incorrect. Scale is a slider.
        [ ] Canvas | Incorrect. Canvas is for drawing.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make an Entry and read what was typed.

        name_entry = tk.@@Entry | Label | Text@@(root, width=20, font=("Arial", 14))
        name_entry.pack()
        name = name_entry.@@get | read | text@@()

    .. cloze::
        :instructions: Make a password box.

        password_entry = tk.Entry(root, @@show | hide | text@@="@@* | password | 0@@")
        password_entry.pack()

    .. cloze::
        :instructions: Get a number from the box.

        age = @@int | str | text@@(age_entry.get())
        result_label.config(text="Next year you will be " + str(age @@+ | - | *@@ 1))

    .. cloze::
        :instructions: Clear the box and put new words in.

        name_entry.@@delete | clear | remove@@(0, tk.@@END | LAST | STOP@@)
        name_entry.@@insert | add | put@@(0, "Type here")

    .. cloze::
        :instructions: Run a function when Enter is pressed.

        def submit(@@event | self | root@@):
            print(name_entry.get())

        name_entry.@@bind | command | config@@("@@<Return> | <Enter> | <Click>@@", submit)

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
