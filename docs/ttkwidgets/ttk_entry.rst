====================================================
ttk Entry
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk Entry?
-----------------------

| A **ttk Entry** is a box the user types **one line** into, just like a tk Entry.
| It has the same methods as a tk Entry: ``get``, ``insert``, ``delete``, ``focus_set``, ``select_range`` and ``bind``.
| The colour of the box is set with a **style** (``fieldbackground``).

----

Making a ttk Entry
---------------------

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk Entry")

    ttk.Label(root, text="Type your name:").pack(pady=5)

    name_entry = ttk.Entry(root)    # 1. Create the entry
    name_entry.pack()               # 2. Place it

    root.mainloop()                 # Keep the window open

----

ttk Entry options
--------------------

width
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how wide the box is, in **characters**. The default is 20.
| **How to write it:** ``width=10``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width")

    ttk.Entry(root, width=5).pack(pady=10)
    ttk.Entry(root, width=40).pack(pady=10)

    root.mainloop()

font
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the style and size of the typed letters. A bigger font makes the box taller.
| **How to write it:** ``font=("Arial", 18)``
| The font **cannot** be set in the ``"TEntry"`` style. Set it on each Entry.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("font")

    ttk.Entry(root, font=("Arial", 18)).pack(pady=40)

    root.mainloop()

foreground
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the colour of the typed letters.
| **How to write it:** ``foreground="blue"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("foreground")

    ttk.Entry(root, font=("Arial", 16), foreground="blue").pack(pady=40)

    root.mainloop()

justify
~~~~~~~~~~~~~~~~~~

| **What it does:** lines the typed text up on the ``"left"`` (default), ``"center"`` or ``"right"``.
| **How to write it:** ``justify="center"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("justify")

    for side in ["left", "center", "right"]:
        entry = ttk.Entry(root, justify=side, font=("Arial", 14))
        entry.insert(0, side)
        entry.pack(pady=5)

    root.mainloop()

show
~~~~~~~~~~~~~~~~~~

| **What it does:** hides the typing by showing another character instead. Used for **passwords**.
| **How to write it:** ``show="*"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("show")

    ttk.Label(root, text="Password:").pack(pady=5)
    ttk.Entry(root, show="*", font=("Arial", 14)).pack()

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** controls whether the user can type in the box.
| **Values:** ``"normal"`` (can type), ``"readonly"`` (can see and copy, not change), ``"disabled"`` (greyed out).
| **How to write it:** ``state="readonly"``, or ``entry.state(["readonly"])`` later.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    for setting in ["normal", "readonly", "disabled"]:
        entry = ttk.Entry(root)
        entry.insert(0, setting)            # Insert before locking the box
        entry.config(state=setting)
        entry.pack(pady=5)

    root.mainloop()

textvariable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the box to a ``StringVar``. ``.get()`` on the variable reads the box and ``.set()`` changes it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def shout():
        word.set(word.get().upper())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("textvariable")

    word = tk.StringVar(value="hello")

    ttk.Entry(root, textvariable=word, font=("Arial", 16)).pack(pady=20)
    ttk.Button(root, text="SHOUT", command=shout).pack()

    root.mainloop()

----

ttk Entry methods
--------------------

get
~~~~~~~~~~~~~~~~~~

| **What it does:** reads what the user has typed. It is always a **string**.
| **How to write it:** ``text = entry.get()``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def say_hello():
        answer_label.config(text="Hello " + name_entry.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("get")

    name_entry = ttk.Entry(root, font=("Arial", 14))
    name_entry.pack(pady=10)

    ttk.Button(root, text="Say hello", command=say_hello).pack()

    answer_label = ttk.Label(root, text="", font=("Arial", 14))
    answer_label.pack(pady=10)

    root.mainloop()

Getting a number
~~~~~~~~~~~~~~~~~~~

| Use ``int()`` or ``float()`` to turn the text into a number. ``try`` and ``except ValueError`` stop a crash if a word is typed.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def convert():
        try:
            cm = float(cm_entry.get())
            answer_label.config(text=f"{cm} cm = {cm / 100} m")
        except ValueError:
            answer_label.config(text="Please type a number")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("cm to m")

    cm_entry = ttk.Entry(root, width=10, font=("Arial", 14))
    cm_entry.pack(pady=10)

    ttk.Button(root, text="Convert", command=convert).pack()

    answer_label = ttk.Label(root, text="", font=("Arial", 14))
    answer_label.pack(pady=10)

    root.mainloop()

delete and insert
~~~~~~~~~~~~~~~~~~~~

| ``entry.delete(0, tk.END)`` clears the box. ``entry.insert(0, "text")`` puts text in it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def clear():
        word_entry.delete(0, tk.END)


    def reset():
        word_entry.delete(0, tk.END)
        word_entry.insert(0, "Type here")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("delete and insert")

    word_entry = ttk.Entry(root, font=("Arial", 14))
    word_entry.insert(0, "Type here")
    word_entry.pack(pady=10)

    ttk.Button(root, text="Clear", command=clear).pack(pady=2)
    ttk.Button(root, text="Reset", command=reset).pack(pady=2)

    root.mainloop()

focus_set and select_range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``focus_set()`` puts the typing cursor in the box. ``select_range(0, tk.END)`` highlights all the text so the next typing replaces it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def check():
        if answer_entry.get() == "9":
            result_label.config(text="Correct!", foreground="green")
        else:
            result_label.config(text="Try again", foreground="red")
            answer_entry.focus_set()
            answer_entry.select_range(0, tk.END)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("focus_set")

    ttk.Label(root, text="What is 3 x 3?", font=("Arial", 14)).pack(pady=5)

    answer_entry = ttk.Entry(root, width=5, font=("Arial", 14))
    answer_entry.pack()
    answer_entry.focus_set()

    ttk.Button(root, text="Check", command=check).pack(pady=5)

    result_label = ttk.Label(root, text="", font=("Arial", 14))
    result_label.pack()

    root.mainloop()

bind (pressing Enter)
~~~~~~~~~~~~~~~~~~~~~~~~

| ``entry.bind("<Return>", function_name)`` runs a function when Enter is pressed. Use ``event=None`` so the function also works from a button.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def add_item(event=None):
        items_label.config(text=items_label.cget("text") + "\n" + item_entry.get())
        item_entry.delete(0, tk.END)


    root = tk.Tk()
    root.geometry("300x250")
    root.title("bind")

    item_entry = ttk.Entry(root, font=("Arial", 14))
    item_entry.pack(pady=5)
    item_entry.bind("<Return>", add_item)

    ttk.Button(root, text="Add", command=add_item).pack()

    items_label = ttk.Label(root, text="Shopping list:")
    items_label.pack(pady=5)

    root.mainloop()

----

Styling a ttk Entry
----------------------

| The style for every ttk Entry is ``"TEntry"``.
| ``fieldbackground`` is the colour **inside** the box. ``padding`` adds space inside the box around the text.
| ``"clam"`` is used so ``fieldbackground`` works on Windows.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Entry style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TEntry", fieldbackground="lightyellow", foreground="navy", padding=5)
    style.configure("Wrong.TEntry", fieldbackground="mistyrose")

    ttk.Entry(root, font=("Arial", 14)).pack(pady=10)
    ttk.Entry(root, font=("Arial", 14), style="Wrong.TEntry").pack(pady=10)

    root.mainloop()

Changing colour for a wrong answer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Swap an Entry's style with ``config(style=...)`` to show if an answer is right or wrong.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def check():
        if answer_entry.get().lower() == "canberra":
            answer_entry.config(style="Right.TEntry")
        else:
            answer_entry.config(style="Wrong.TEntry")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Right or wrong")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Right.TEntry", fieldbackground="lightgreen")
    style.configure("Wrong.TEntry", fieldbackground="pink")

    ttk.Label(root, text="Capital of Australia?").pack(pady=5)

    answer_entry = ttk.Entry(root, font=("Arial", 14))
    answer_entry.pack()

    ttk.Button(root, text="Check", command=check).pack(pady=10)

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
    * - ``width``
      - Width in characters
      - ``width=10``
    * - ``font``
      - Font of the typing
      - ``font=("Arial", 14)``
    * - ``foreground``
      - Colour of the typing
      - ``foreground="blue"``
    * - ``justify``
      - Line up the text
      - ``justify="center"``
    * - ``show``
      - Hide typing (passwords)
      - ``show="*"``
    * - ``state``
      - Allow or stop typing
      - ``state="readonly"``
    * - ``textvariable``
      - Link to a StringVar
      - ``textvariable=word``
    * - ``get()``
      - Read the text
      - ``entry.get()``
    * - ``delete()``, ``insert()``
      - Clear the box, put text in
      - ``entry.delete(0, tk.END)``
    * - ``focus_set()``
      - Put the cursor in the box
      - ``entry.focus_set()``
    * - ``select_range()``
      - Highlight the text
      - ``entry.select_range(0, tk.END)``
    * - ``bind()``
      - Run a function on a key press
      - ``entry.bind("<Return>", go)``
    * - ``"TEntry"``
      - Style name; use ``fieldbackground`` for the box colour
      - ``style.configure("TEntry", fieldbackground="pink")``

----

All Entry options
---------------------------

| Here is every option an ttk Entry can have, for reference. You will only need a few of them most of the time.

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
      - ``style="Big.TEntry"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``textvariable``
      - A variable that holds what is typed in the box
      - ``textvariable=name``
    * - ``validate``
      - When to check what is typed: ``"none"``, ``"key"``, ``"focus"``, ``"focusin"``, ``"focusout"`` or ``"all"``
      - ``validate="key"``
    * - ``validatecommand``
      - Function that checks what is typed (returns ``True`` or ``False``)
      - ``validatecommand=(root.register(check), "%P")``
    * - ``width``
      - How wide it is (in characters)
      - ``width=15``
    * - ``xscrollcommand``
      - Connects it to a side-to-side scrollbar
      - ``xscrollcommand=x_scrollbar.set``

| Many themes ignore ``background`` for the typing box. Use a style instead, e.g. ``style.configure("TEntry", fieldbackground="lightyellow")``.

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

        How is a ttk Entry made?

        [x] ttk.Entry(root, width=20) | Correct. It works like the tk Entry.
        [ ] tk.Entry(root, ttk=True) | Incorrect. Not an option.
        [ ] ttk.entry(root) | Incorrect. Needs a capital E.
        [ ] ttk.Text(root) | Incorrect. Text is not a ttk widget.

    .. multichoice::

        What does width=20 mean?

        [ ] 20 pixels | Incorrect. It counts characters.
        [x] About 20 characters wide | Correct. Entry width counts characters.
        [ ] 20 lines | Incorrect. One line.
        [ ] 20 words | Incorrect. Characters.

    .. multichoice::

        Which option makes the typed words blue?

        [ ] fg="blue" | Incorrect. ttk Entry uses foreground.
        [x] foreground="blue" | Correct. Write the full word.
        [ ] colour="blue" | Incorrect. Not an option.
        [ ] text="blue" | Incorrect. Not an option.

    .. multichoice::

        What does justify="right" do?

        [x] Puts the typed words on the right of the box | Correct. Good for numbers.
        [ ] Moves the box right | Incorrect. pack moves it.
        [ ] Makes the box wider | Incorrect. width does that.
        [ ] Clears the box | Incorrect. delete clears.

    .. multichoice::

        What does show="\*" do?

        [ ] Shows the words normally | Incorrect. It hides them.
        [x] Shows a star for each letter, good for passwords | Correct. The real letters are still stored.
        [ ] Adds a star | Incorrect. Each letter becomes a star.
        [ ] Stops typing | Incorrect. state does that.

    .. multichoice::

        Which line stops the user typing but still shows the words?

        [x] entry.state(["readonly"]) | Correct. readonly allows reading but not typing.
        [ ] entry.state(["hidden"]) | Incorrect. Not a state.
        [ ] entry.config(bg="grey") | Incorrect. ttk has no bg.
        [ ] entry.delete(0, tk.END) | Incorrect. That clears it.

    .. multichoice::

        Which method reads what was typed?

        [ ] entry.read() | Incorrect. Not a method.
        [x] entry.get() | Correct. get gives the text.
        [ ] entry.text | Incorrect. Not an attribute.
        [ ] entry.value() | Incorrect. Not a method.

    .. multichoice::

        What type does entry.get() give?

        [x] A string | Correct. Use int() or float() for numbers.
        [ ] A number | Incorrect. It is text.
        [ ] A list | Incorrect. It is one string.
        [ ] True or False | Incorrect. It is text.

    .. multichoice::

        How do you get a decimal number from the box?

        [ ] int(entry.get()) | Incorrect. int is for whole numbers.
        [x] float(entry.get()) | Correct. float makes a decimal number.
        [ ] str(entry.get()) | Incorrect. str makes text.
        [ ] entry.get().float | Incorrect. Not an attribute.

    .. multichoice::

        Why use try and except when changing the text to a number?

        [ ] To make it faster | Incorrect. Not about speed.
        [x] The user might type letters, which causes a ValueError | Correct. except catches the error.
        [ ] Entries cannot hold numbers | Incorrect. They can.
        [ ] It is always needed for text | Incorrect. Only for numbers.

    .. multichoice::

        Which line clears the box?

        [ ] entry.clear() | Incorrect. Not a method.
        [x] entry.delete(0, tk.END) | Correct. From the first character to the end.
        [ ] entry.delete() | Incorrect. It needs a start.
        [ ] entry.set("") | Incorrect. ttk Entry has no set.

    .. multichoice::

        What does entry.insert(0, "Name") do?

        [x] Puts Name at the start of the box | Correct. 0 is the first position.
        [ ] Adds Name at the end | Incorrect. Use tk.END for the end.
        [ ] Deletes Name | Incorrect. insert adds.
        [ ] Reads Name | Incorrect. get reads.

    .. multichoice::

        What does entry.focus_set() do?

        [ ] Highlights all text | Incorrect. select_range does that.
        [x] Puts the typing cursor in the box | Correct. The user can type straight away.
        [ ] Clears the box | Incorrect. delete does that.
        [ ] Disables the box | Incorrect. state does that.

    .. multichoice::

        What does entry.select_range(0, tk.END) do?

        [x] Highlights all the text | Correct. It selects text.
        [ ] Deletes all the text | Incorrect. delete does that.
        [ ] Reads the text | Incorrect. get does that.
        [ ] Moves the cursor to the start | Incorrect. It selects text.

    .. multichoice::

        Which event runs a function when Enter is pressed?

        [ ] "<Enter>" | Incorrect. That is the mouse entering the widget.
        [x] "<Return>" | Correct. Return is the Enter key.
        [ ] "<Key-Enter>" | Incorrect. Not the name.
        [ ] "<Button-1>" | Incorrect. That is a mouse click.

    .. multichoice::

        What does textvariable=name do?

        [ ] Sets the font | Incorrect. font does that.
        [x] Links the box to a StringVar, so name.get() reads it | Correct. It updates as the user types.
        [ ] Names the widget | Incorrect. It links a variable.
        [ ] Hides the text | Incorrect. show hides text.

    .. multichoice::

        How can a ttk Entry turn red for a wrong answer?

        [x] Use a style like "Wrong.TEntry" with a red fieldbackground and set style="Wrong.TEntry" | Correct. ttk colours come from styles.
        [ ] entry.config(bg="red") | Incorrect. ttk has no bg.
        [ ] entry.red() | Incorrect. Not a method.
        [ ] entry.state(["red"]) | Incorrect. Not a state.

    .. multichoice::

        Which style option colours the typing area of a ttk Entry?

        [ ] background | Incorrect. Many themes ignore it.
        [x] fieldbackground | Correct. fieldbackground is the typing area colour.
        [ ] bg | Incorrect. Not a ttk option.
        [ ] fill | Incorrect. Not an option.

    .. multichoice::

        Which style name changes every ttk Entry?

        [ ] "Entry" | Incorrect. Use TEntry.
        [x] "TEntry" | Correct. T then the widget name.
        [ ] "TBox" | Incorrect. Not the name.
        [ ] "ttk.Entry" | Incorrect. Not a style name.

    .. multichoice::

        Which line puts the typing cursor in the box when the program starts?

        [x] name_entry.focus_set() | Correct. focus_set puts the cursor there.
        [ ] name_entry.cursor() | Incorrect. Not a method.
        [ ] name_entry.start() | Incorrect. Not a method.
        [ ] name_entry.select() | Incorrect. Not a method.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a ttk Entry and read it.

        name_entry = ttk.@@Entry | Label | Combobox@@(root, width=20, @@font | size | style@@=("Arial", 14))
        name_entry.pack()
        name = name_entry.@@get | read | text@@()

    .. cloze::
        :instructions: Make a password box with centred text.

        password_entry = ttk.Entry(root, @@show | hide | mask@@="*", @@justify | anchor | side@@="center")

    .. cloze::
        :instructions: Get a decimal number safely.

        try:
            height = @@float | int | str@@(height_entry.get())
        @@except | else | finally@@ ValueError:
            result_label.config(text="Please type a number")

    .. cloze::
        :instructions: Clear the box and get it ready for typing.

        name_entry.@@delete | clear | remove@@(0, tk.END)
        name_entry.@@focus_set | select_range | insert@@()

    .. cloze::
        :instructions: Turn the box red for a wrong answer.

        style.configure("Wrong.TEntry", @@fieldbackground | background | bg@@="pink")
        answer_entry.config(@@style | theme | colour@@="Wrong.TEntry")

----

.. admonition:: Tasks

    #. Make a window titled "Login" that is 300x200 with a ttk Label "Username:" and a ttk Entry using Arial size 14.
    #. Add a ttk Label "Password:" and a ttk Entry that shows ``"*"``.
    #. Use a style so both entries have a light blue box colour.
    #. Add a "Log in" button. When clicked, a label shows "Welcome" and the username.

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
                    root.title("Login")

                    ttk.Label(root, text="Username:").pack()
                    user_entry = ttk.Entry(root, font=("Arial", 14))
                    user_entry.pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Login")

                    ttk.Label(root, text="Username:").pack()
                    user_entry = ttk.Entry(root, font=("Arial", 14))
                    user_entry.pack()

                    ttk.Label(root, text="Password:").pack()
                    password_entry = ttk.Entry(root, font=("Arial", 14), show="*")
                    password_entry.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Login")

                    style = ttk.Style()
                    style.theme_use("clam")
                    style.configure("TEntry", fieldbackground="lightblue")

                    ttk.Label(root, text="Username:").pack()
                    user_entry = ttk.Entry(root, font=("Arial", 14))
                    user_entry.pack()

                    ttk.Label(root, text="Password:").pack()
                    password_entry = ttk.Entry(root, font=("Arial", 14), show="*")
                    password_entry.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def log_in():
                        welcome_label.config(text="Welcome " + user_entry.get())


                    root = tk.Tk()
                    root.geometry("300x250")
                    root.title("Login")

                    style = ttk.Style()
                    style.theme_use("clam")
                    style.configure("TEntry", fieldbackground="lightblue")

                    ttk.Label(root, text="Username:").pack()
                    user_entry = ttk.Entry(root, font=("Arial", 14))
                    user_entry.pack()

                    ttk.Label(root, text="Password:").pack()
                    password_entry = ttk.Entry(root, font=("Arial", 14), show="*")
                    password_entry.pack()

                    ttk.Button(root, text="Log in", command=log_in).pack(pady=10)

                    welcome_label = ttk.Label(root, text="")
                    welcome_label.pack()

                    root.mainloop()
