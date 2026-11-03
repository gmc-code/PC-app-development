====================================================
tk Text
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Text>`_

----

What is a Text widget?
-------------------------

| A **Text** widget is a big box that holds **many lines** of text.
| The user can type in it, like a small word processor, and the program can write in it too.
| Use it for longer writing such as a story or comments, or for showing a list of results.
| For a short, one-line answer, use an **Entry** instead.

----

Making a Text widget
-------------------------

| Every Text widget is made in two steps:

#. **Create** the box with ``tk.Text(...)``.
#. **Place** the box in the window with ``.pack()``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first Text")     # Words in the title bar

    text_box = tk.Text(root, width=30, height=6)    # 1. Create the box
    text_box.pack(pady=10)                          # 2. Place it in the window

    root.mainloop()                 # Keep the window open

| Click in the box and type. Press Enter to start a new line.

----

Positions in a Text widget
-----------------------------

| Many Text methods need to know **where** in the box to work. A position is written as a string: ``"line.character"``

- **Lines** are counted from **1**.
- **Characters** on each line are counted from **0**.

.. list-table::
    :header-rows: 1
    :widths: 30 70

    * - Position
      - Meaning
    * - ``"1.0"``
      - Line 1, character 0: the very start of the box
    * - ``"2.0"``
      - The start of line 2
    * - ``"1.5"``
      - Line 1, after the first 5 characters
    * - ``tk.END``
      - The very end of all the text
    * - ``"end-1c"``
      - The end, minus 1 character (see ``get`` below)

----

Text options
-------------------

| Options are written as ``option=value`` inside ``tk.Text( )``, separated by commas.

width and height
~~~~~~~~~~~~~~~~~~

| **What they do:** set the size of the box.
| ``width`` is measured in **characters** (letters), and ``height`` in **lines**.
| **How to write them:** ``width=30``, ``height=6``
| If you leave them out, the box is 80 characters wide and 24 lines high, which is very big.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and height")

    small_box = tk.Text(root, width=20, height=3)
    small_box.pack(pady=10)

    root.mainloop()

font
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the style and size of all the letters in the box.
| **How to write it:** ``font=("font name", size)`` or ``font=("font name", size, "style")``
| A bigger font makes the box bigger too, because width and height are counted in letters and lines.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("350x200")
    root.title("font")

    text_box = tk.Text(root, width=25, height=4, font=("Comic Sans MS", 14))
    text_box.pack(pady=10)

    root.mainloop()

fg and bg (colours)
~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``fg`` sets the colour of the letters. ``bg`` sets the colour of the box.
| **How to write them:** ``fg="colour"``, ``bg="colour"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("fg and bg")

    text_box = tk.Text(root, width=30, height=6, fg="white", bg="black")
    text_box.pack(pady=10)

    root.mainloop()

insertbackground and selectbackground
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:**
| ``insertbackground`` sets the colour of the flashing typing cursor.
| ``selectbackground`` sets the colour of the highlight when text is selected with the mouse.
| **How to write them:** ``insertbackground="colour"``, ``selectbackground="colour"``
| These are useful with a dark ``bg``, where the normal black cursor is hard to see.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("cursor colours")

    text_box = tk.Text(root, width=30, height=6, fg="white", bg="black",
                       insertbackground="white", selectbackground="purple")
    text_box.pack(pady=10)

    root.mainloop()

wrap
~~~~~~~~~~~~~~~~~~

| **What it does:** decides what happens when a line is too long for the box.
| **How to write it:** ``wrap="word"``
| **Values:**

- ``"char"`` - wraps in the middle of a word (the default).
- ``"word"`` - wraps between words, like a word processor. This is usually the best choice.
- ``"none"`` - does not wrap; the line keeps going off the side.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("wrap")

    text_box = tk.Text(root, width=25, height=5, wrap="word")
    text_box.insert("1.0", "This sentence is too long for one line, so it wraps between words.")
    text_box.pack(pady=10)

    root.mainloop()

padx and pady
~~~~~~~~~~~~~~~~~~

| **What they do:** add empty space between the edge of the box and the text, so it is not squashed against the border.
| **How to write them:** ``padx=10``, ``pady=10`` (measured in pixels)

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("padx and pady")

    text_box = tk.Text(root, width=25, height=4, padx=15, pady=15)
    text_box.insert("1.0", "There is space\naround this text.")
    text_box.pack(pady=10)

    root.mainloop()

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** change the border around the box.
| ``relief`` is the border style. ``borderwidth`` is how thick it is in pixels.
| **How to write them:** ``relief="solid", borderwidth=2``
| **Styles:** ``"sunken"`` (the default), ``"solid"``, ``"flat"``, ``"raised"``, ``"groove"``, ``"ridge"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("relief")

    text_box = tk.Text(root, width=30, height=6, relief="solid", borderwidth=2)
    text_box.pack(pady=10)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** controls whether the user can type in the box.
| **How to write it:** ``state="disabled"``
| **Values:** ``"normal"`` (can type, the default) and ``"disabled"`` (cannot type; good for showing results).
| While a box is ``"disabled"``, your code cannot change it either. See the **config** method below for how to get around this.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    text_box = tk.Text(root, width=30, height=6)
    text_box.insert("1.0", "You can read this,\nbut you cannot change it.")
    text_box.config(state="disabled")       # Lock the box after putting text in
    text_box.pack(pady=10)

    root.mainloop()

undo
~~~~~~~~~~~~~~~~~~

| **What it does:** turns on undo, so **Ctrl+Z** undoes typing and **Ctrl+Y** redoes it.
| **How to write it:** ``undo=True``
| Undo is off unless you turn it on.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("undo")

    text_box = tk.Text(root, width=30, height=6, undo=True)
    text_box.pack(pady=10)

    root.mainloop()

----

Text methods
-------------------

| A **method** is an action that a widget can do. Methods are written after a dot, e.g. ``text_box.insert(...)``.

insert
~~~~~~~~~~~~~~~~~~

| **What it does:** puts text into the box from your code.
| **How to write it:** ``text_box.insert(position, "text")``
| ``text_box.insert("1.0", "Hi")`` puts text at the **start**.
| ``text_box.insert(tk.END, "Hi")`` adds text to the **end**. This is the one you will use most.
| Add ``"\n"`` at the end of the text so the next insert starts on a new line.

.. code-block:: python

    import tkinter as tk


    def add_line():
        text_box.insert(tk.END, "Another line\n")


    root = tk.Tk()
    root.geometry("300x250")
    root.title("insert")

    text_box = tk.Text(root, width=30, height=6)
    text_box.insert("1.0", "First line\n")       # Starting text
    text_box.pack(pady=10)

    add_button = tk.Button(root, text="Add a line", command=add_line)
    add_button.pack()

    root.mainloop()

get
~~~~~~~~~~~~~~~~~~

| **What it does:** reads text from the box.
| **How to write it:** ``writing = text_box.get("1.0", "end-1c")``
| This reads from the start (``"1.0"``) to the end. The Text widget always adds a hidden new line at the end,
  so ``"end-1c"`` ("end minus 1 character") leaves it out.

.. code-block:: python

    import tkinter as tk


    def count_words():
        writing = text_box.get("1.0", "end-1c")     # Read everything that was typed
        words = len(writing.split())                # Split into words and count them
        count_label.config(text=f"Words: {words}")


    root = tk.Tk()
    root.geometry("300x250")
    root.title("get")

    text_box = tk.Text(root, width=30, height=6, wrap="word")
    text_box.pack(pady=10)

    count_button = tk.Button(root, text="Count words", command=count_words)
    count_button.pack()

    count_label = tk.Label(root, text="Words: 0", font=("Arial", 14))
    count_label.pack(pady=5)

    root.mainloop()

delete
~~~~~~~~~~~~~~~~~~

| **What it does:** removes text from the box.
| **How to write it:** ``text_box.delete("1.0", tk.END)`` clears **everything**.
| ``text_box.delete("1.0", "2.0")`` deletes only the first line (from the start of line 1 to the start of line 2).

.. code-block:: python

    import tkinter as tk


    def clear():
        text_box.delete("1.0", tk.END)


    root = tk.Tk()
    root.geometry("300x250")
    root.title("delete")

    text_box = tk.Text(root, width=30, height=6)
    text_box.insert("1.0", "Line 1\nLine 2\nLine 3")
    text_box.pack(pady=10)

    clear_button = tk.Button(root, text="Clear", command=clear)
    clear_button.pack()

    root.mainloop()

see
~~~~~~~~~~~~~~~~~~

| **What it does:** scrolls the box so a position can be seen.
| **How to write it:** ``text_box.see(tk.END)`` scrolls to the bottom.
| Use it after ``insert`` so the newest line is always visible, even when the box is full.

.. code-block:: python

    import tkinter as tk


    def add_line():
        text_box.insert(tk.END, "New line\n")
        text_box.see(tk.END)        # Scroll down to show the new line


    root = tk.Tk()
    root.geometry("300x200")
    root.title("see")

    text_box = tk.Text(root, width=30, height=4)
    text_box.pack(pady=10)

    add_button = tk.Button(root, text="Add a line (click lots!)", command=add_line)
    add_button.pack()

    root.mainloop()

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes one or more options **after** the box has been made.
| **How to write it:** ``text_box.config(option=value)``
| A common use is a **read-only results box**. Your code cannot insert while the box is ``"disabled"``, so:

#. ``config(state="normal")`` to unlock it,
#. ``insert`` the text,
#. ``config(state="disabled")`` to lock it again.

.. code-block:: python

    import tkinter as tk


    def show_table():
        results_box.config(state="normal")          # 1. Unlock
        results_box.delete("1.0", tk.END)
        for number in range(1, 11):
            results_box.insert(tk.END, f"{number} x 5 = {number * 5}\n")    # 2. Insert
        results_box.config(state="disabled")        # 3. Lock again


    root = tk.Tk()
    root.geometry("300x300")
    root.title("config")

    table_button = tk.Button(root, text="Show the 5 times table", command=show_table)
    table_button.pack(pady=10)

    results_box = tk.Text(root, width=20, height=10, state="disabled")
    results_box.pack()

    root.mainloop()

tag_configure (coloured text)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What it does:** makes a named style, called a **tag**, so some text can look different from the rest.
| **How to write it:** ``text_box.tag_configure("name", option=value)``
| Then add the tag name at the end of ``insert``: ``text_box.insert(tk.END, "text", "name")``
| Tags can use ``foreground`` (letter colour), ``background`` and ``font``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("tags")

    text_box = tk.Text(root, width=30, height=6, font=("Arial", 12))
    text_box.pack(pady=10)

    # Make the styles
    text_box.tag_configure("title", font=("Arial", 14, "bold"))
    text_box.tag_configure("right", foreground="green")
    text_box.tag_configure("wrong", foreground="red")

    # Use the styles
    text_box.insert(tk.END, "Quiz results\n", "title")
    text_box.insert(tk.END, "Question 1: correct\n", "right")
    text_box.insert(tk.END, "Question 2: wrong\n", "wrong")

    root.mainloop()

Adding a scrollbar
~~~~~~~~~~~~~~~~~~~~~~

| A Text widget can scroll with the mouse wheel, but a **Scrollbar** shows the user there is more text.
| The scrollbar and the box must be linked both ways:

- ``yscrollcommand=scrollbar.set`` tells the scrollbar when the text moves.
- ``scrollbar.config(command=text_box.yview)`` tells the text to move when the scrollbar is dragged.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("scrollbar")

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side="right", fill="y")      # Scrollbar down the right side

    text_box = tk.Text(root, width=30, height=8, yscrollcommand=scrollbar.set)
    text_box.pack(side="left", padx=10, pady=10)

    scrollbar.config(command=text_box.yview)

    for number in range(1, 51):
        text_box.insert(tk.END, f"Line {number}\n")

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
    * - ``width``, ``height``
      - Size in characters and lines
      - ``width=30, height=6``
    * - ``font``
      - Font name, size and style
      - ``font=("Arial", 12)``
    * - ``fg``, ``bg``
      - Letter colour and box colour
      - ``fg="white", bg="black"``
    * - ``insertbackground``
      - Colour of the typing cursor
      - ``insertbackground="white"``
    * - ``selectbackground``
      - Colour of the highlight
      - ``selectbackground="purple"``
    * - ``wrap``
      - How long lines wrap
      - ``wrap="word"``
    * - ``padx``, ``pady``
      - Space between the edge and the text
      - ``padx=10, pady=10``
    * - ``relief``, ``borderwidth``
      - Border style and thickness
      - ``relief="solid", borderwidth=2``
    * - ``state``
      - Allow or stop typing
      - ``state="disabled"``
    * - ``undo``
      - Turn on Ctrl+Z
      - ``undo=True``
    * - ``insert()``
      - Put text in the box
      - ``text_box.insert(tk.END, "Hi\n")``
    * - ``get()``
      - Read the text
      - ``text_box.get("1.0", "end-1c")``
    * - ``delete()``
      - Remove text
      - ``text_box.delete("1.0", tk.END)``
    * - ``see()``
      - Scroll to a position
      - ``text_box.see(tk.END)``
    * - ``config()``
      - Change options later
      - ``text_box.config(state="normal")``
    * - ``tag_configure()``
      - Make a style for some text
      - ``text_box.tag_configure("red", foreground="red")``

----

All Text options
---------------------------

| Here is every option a Text can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``autoseparators``
      - Adds undo stopping points automatically (needs ``undo=True``)
      - ``autoseparators=True``
    * - ``bg`` or ``background``
      - Background colour
      - ``bg="lavender"``
    * - ``blockcursor``
      - Makes the typing cursor a block instead of a thin line
      - ``blockcursor=True``
    * - ``bd`` or ``borderwidth``
      - How thick the border is
      - ``bd=3``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``endline``
      - Last line of the text to show (advanced)
      - ``endline=10``
    * - ``exportselection``
      - Lets selected text be copied to other programs (``True`` or ``False``)
      - ``exportselection=False``
    * - ``font``
      - Style and size of the words
      - ``font=("Arial", 14)``
    * - ``fg`` or ``foreground``
      - Word colour
      - ``fg="purple"``
    * - ``height``
      - How tall the box is (in lines of text)
      - ``height=10``
    * - ``highlightbackground``
      - Colour of the focus outline when it is not selected by the keyboard
      - ``highlightbackground="white"``
    * - ``highlightcolor``
      - Colour of the focus outline when it is selected by the keyboard
      - ``highlightcolor="blue"``
    * - ``highlightthickness``
      - How thick the focus outline is
      - ``highlightthickness=2``
    * - ``inactiveselectbackground``
      - Colour of selected text when you are using a different widget
      - ``inactiveselectbackground="lightgrey"``
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
    * - ``insertunfocussed``
      - How the cursor looks when you are using a different widget: ``"none"``, ``"hollow"`` or ``"solid"``
      - ``insertunfocussed="hollow"``
    * - ``insertwidth``
      - How wide the typing cursor is (in pixels)
      - ``insertwidth=4``
    * - ``maxundo``
      - Most undos allowed (``0`` = no limit)
      - ``maxundo=20``
    * - ``padx``
      - Extra space inside the box, on the left and right
      - ``padx=10``
    * - ``pady``
      - Extra space inside the box, at the top and bottom
      - ``pady=10``
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
    * - ``setgrid``
      - Makes the window resize in whole lines (advanced)
      - ``setgrid=True``
    * - ``spacing1``
      - Extra space above each line (in pixels)
      - ``spacing1=5``
    * - ``spacing2``
      - Extra space between lines that wrap (in pixels)
      - ``spacing2=2``
    * - ``spacing3``
      - Extra space below each line (in pixels)
      - ``spacing3=5``
    * - ``startline``
      - First line of the text to show (advanced)
      - ``startline=1``
    * - ``state``
      - ``"normal"`` or ``"disabled"`` (cannot be changed)
      - ``state="disabled"``
    * - ``tabs``
      - Where the Tab key stops are (``"2c"`` = 2 cm)
      - ``tabs=("2c", "4c")``
    * - ``tabstyle``
      - How tabs line up: ``"tabular"`` or ``"wordprocessor"``
      - ``tabstyle="wordprocessor"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``undo``
      - ``True`` lets Ctrl+Z undo typing
      - ``undo=True``
    * - ``width``
      - How wide the box is (in characters)
      - ``width=40``
    * - ``wrap``
      - How long lines wrap: ``"char"``, ``"word"`` or ``"none"``
      - ``wrap="word"``
    * - ``xscrollcommand``
      - Connects it to a side-to-side scrollbar
      - ``xscrollcommand=x_scrollbar.set``
    * - ``yscrollcommand``
      - Connects it to an up-and-down scrollbar
      - ``yscrollcommand=scrollbar.set``

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

        What is a Text widget?

        [x] A box for typing or showing many lines of text | Correct. It is like a small word processor.
        [ ] A one-line typing box | Incorrect. That is an Entry.
        [ ] A label | Incorrect. Labels only show text.
        [ ] A message pop-up | Incorrect. That is messagebox.

    .. multichoice::

        For a Text widget, what does height=10 mean?

        [ ] 10 pixels | Incorrect. It counts lines.
        [x] 10 lines tall | Correct. Text height counts lines.
        [ ] 10 words | Incorrect. It counts lines.
        [ ] 10 characters | Incorrect. width counts characters.

    .. multichoice::

        What does width=40 mean?

        [x] About 40 characters wide | Correct. Text width counts characters.
        [ ] 40 pixels | Incorrect. It counts characters.
        [ ] 40 lines | Incorrect. height counts lines.
        [ ] 40 words | Incorrect. It counts characters.

    .. multichoice::

        What does insertbackground="red" change?

        [ ] The background | Incorrect. bg does that.
        [x] The colour of the typing cursor | Correct. The insert cursor is the blinking line.
        [ ] The selected text | Incorrect. selectbackground does that.
        [ ] The words | Incorrect. fg does that.

    .. multichoice::

        What does selectbackground="yellow" change?

        [ ] All the text | Incorrect. It colours selected text.
        [x] The highlight colour of selected text | Correct. It shows when text is selected.
        [ ] The cursor | Incorrect. insertbackground does that.
        [ ] The border | Incorrect. Not the border.

    .. multichoice::

        What does wrap="word" do?

        [x] Wraps long lines between whole words | Correct. Words are not split.
        [ ] Wraps in the middle of words | Incorrect. That is "char".
        [ ] Stops wrapping | Incorrect. That is "none".
        [ ] Makes words bold | Incorrect. font does that.

    .. multichoice::

        What does padx=10 do on a Text widget?

        [ ] Moves it 10 pixels | Incorrect. pack or grid move it.
        [x] Adds 10 pixels of space inside on the left and right | Correct. The text does not touch the edge.
        [ ] Adds 10 lines | Incorrect. It adds space.
        [ ] Makes it 10 wide | Incorrect. width does that.

    .. multichoice::

        What does state="disabled" do?

        [ ] Hides it | Incorrect. It is still shown.
        [x] Stops the user and the code from changing the text | Correct. Set it to "normal" before inserting.
        [ ] Deletes the text | Incorrect. Nothing is deleted.
        [ ] Makes it red | Incorrect. No colour change.

    .. multichoice::

        What does undo=True do?

        [x] Lets Ctrl+Z undo typing | Correct. It turns on the undo feature.
        [ ] Undoes everything at the start | Incorrect. It just allows undo.
        [ ] Deletes the text | Incorrect. It allows undo.
        [ ] Locks the text | Incorrect. state does that.

    .. multichoice::

        In text.insert("1.0", "Hello"), what does "1.0" mean?

        [ ] Line 0, character 1 | Incorrect. It is line first, then character.
        [x] Line 1, character 0, the very start | Correct. Lines start at 1 and characters at 0.
        [ ] One point zero seconds | Incorrect. It is a position.
        [ ] The end | Incorrect. tk.END is the end.

    .. multichoice::

        Which line adds text to the end?

        [ ] text.add("Hi") | Incorrect. Not a method.
        [x] text.insert(tk.END, "Hi") | Correct. insert at END adds to the end.
        [ ] text.append("Hi") | Incorrect. Not a method.
        [ ] text.insert("Hi") | Incorrect. insert needs a position.

    .. multichoice::

        Which line gets all the text?

        [x] text.get("1.0", tk.END) | Correct. From the start to the end.
        [ ] text.get() | Incorrect. get needs a start position.
        [ ] text.get(0, tk.END) | Incorrect. Text positions use "1.0".
        [ ] text.read() | Incorrect. Not a method.

    .. multichoice::

        Why does text.get("1.0", tk.END) often end with a new line?

        [ ] It is a bug in your code | Incorrect. It is normal.
        [x] The Text widget always keeps a new line at the end | Correct. Use "end-1c" to leave it off.
        [ ] Because of wrap | Incorrect. Not related.
        [ ] Because of font | Incorrect. Not related.

    .. multichoice::

        Which line deletes all the text?

        [ ] text.delete(0, tk.END) | Incorrect. Text positions use "1.0".
        [x] text.delete("1.0", tk.END) | Correct. From the start to the end.
        [ ] text.clear() | Incorrect. Not a method.
        [ ] text.delete() | Incorrect. It needs a start.

    .. multichoice::

        What does text.see(tk.END) do?

        [x] Scrolls so the end of the text can be seen | Correct. Useful for logs and chats.
        [ ] Selects all the text | Incorrect. It scrolls.
        [ ] Reads the text | Incorrect. get reads.
        [ ] Deletes the text | Incorrect. It scrolls.

    .. multichoice::

        What does tag_configure("warning", foreground="red") do?

        [ ] Makes all text red | Incorrect. It sets up a tag.
        [x] Sets up a tag called warning that makes text red | Correct. Then insert text with that tag.
        [ ] Deletes red text | Incorrect. It sets up a style.
        [ ] Adds the word warning | Incorrect. It sets up a tag.

    .. multichoice::

        How do you insert red text using the warning tag?

        [ ] text.insert(tk.END, "Careful", fg="red") | Incorrect. insert does not take fg.
        [x] text.insert(tk.END, "Careful", "warning") | Correct. The tag name goes after the text.
        [ ] text.tag("Careful", "warning") | Incorrect. Not how tags are used.
        [ ] text.config(tag="warning") | Incorrect. Not an option.

    .. multichoice::

        Two steps add a Scrollbar to a Text box. One is command=text.yview. What is the other?

        [x] text.config(yscrollcommand=scrollbar.set) | Correct. The Text tells the Scrollbar where it is.
        [ ] text.config(scrollbar=True) | Incorrect. Not an option.
        [ ] text.pack(scrollbar) | Incorrect. Not how it works.
        [ ] text.add(scrollbar) | Incorrect. Not a method.

    .. multichoice::

        Which line changes the font later?

        [ ] text.font = ("Arial", 14) | Incorrect. Use config.
        [x] text.config(font=("Arial", 14)) | Correct. config changes options.
        [ ] text.set(font=...) | Incorrect. Not a method.
        [ ] text.insert(font=...) | Incorrect. insert adds text.

    .. multichoice::

        To add text to a disabled Text widget from code, what must you do first?

        [x] Set state="normal", insert, then set state="disabled" again | Correct. Disabled text cannot be changed, even by code.
        [ ] Nothing | Incorrect. Inserting into a disabled widget does nothing.
        [ ] Delete the widget | Incorrect. Not needed.
        [ ] Use a Label | Incorrect. Not needed.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a Text box that wraps words.

        notes = tk.@@Text | Entry | Label@@(root, width=40, @@height | lines | length@@=10, wrap="@@word | char | none@@")
        notes.pack()

    .. cloze::
        :instructions: Add text at the start and the end.

        notes.@@insert | add | append@@("1.0", "First line\n")
        notes.insert(tk.@@END | LAST | STOP@@, "Last line\n")

    .. cloze::
        :instructions: Read and clear the text.

        words = notes.@@get | read | text@@("1.0", tk.END)
        notes.@@delete | clear | remove@@("@@1.0 | 0 | start@@", tk.END)

    .. cloze::
        :instructions: Make red warning text.

        notes.@@tag_configure | config | tag_add@@("warning", foreground="red")
        notes.insert(tk.END, "Careful!", "@@warning | red | tag@@")

    .. cloze::
        :instructions: Lock the text after adding to it.

        notes.config(@@state | lock | mode@@="normal")
        notes.insert(tk.END, "New message\n")
        notes.config(state="@@disabled | locked | readonly@@")
        notes.@@see | show | scroll@@(tk.END)

----

.. admonition:: Tasks

    #. Make a window titled "Diary" that is 400x300. Add a Text widget 40 characters wide and 10 lines high that wraps between words, with a light yellow background and Arial size 12.
    #. Add a "Clear" button below your diary that deletes all the text.
    #. Add a "Count letters" button and a label. When clicked, the label shows how many characters have been typed. (Hint: ``len()`` counts the characters in a string.)
    #. Make a read-only Text box and a button labelled "Countdown". When clicked, the box shows the numbers 10 down to 1, each on its own line, then "Blast off!" in red.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("400x300")
                    root.title("Diary")

                    diary_box = tk.Text(root, width=40, height=10, wrap="word",
                                        bg="lightyellow", font=("Arial", 12))
                    diary_box.pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk


                    def clear():
                        diary_box.delete("1.0", tk.END)


                    root = tk.Tk()
                    root.geometry("400x300")
                    root.title("Diary")

                    diary_box = tk.Text(root, width=40, height=10, wrap="word",
                                        bg="lightyellow", font=("Arial", 12))
                    diary_box.pack(pady=10)

                    clear_button = tk.Button(root, text="Clear", command=clear)
                    clear_button.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk


                    def count_letters():
                        writing = diary_box.get("1.0", "end-1c")
                        count_label.config(text=f"Characters: {len(writing)}")


                    root = tk.Tk()
                    root.geometry("400x300")
                    root.title("Diary")

                    diary_box = tk.Text(root, width=40, height=10, wrap="word",
                                        bg="lightyellow", font=("Arial", 12))
                    diary_box.pack(pady=10)

                    count_button = tk.Button(root, text="Count letters", command=count_letters)
                    count_button.pack()

                    count_label = tk.Label(root, text="Characters: 0")
                    count_label.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def countdown():
                        output_box.config(state="normal")
                        output_box.delete("1.0", tk.END)
                        for number in range(10, 0, -1):
                            output_box.insert(tk.END, f"{number}\n")
                        output_box.insert(tk.END, "Blast off!", "red")
                        output_box.config(state="disabled")


                    root = tk.Tk()
                    root.geometry("300x300")
                    root.title("Countdown")

                    countdown_button = tk.Button(root, text="Countdown", command=countdown)
                    countdown_button.pack(pady=10)

                    output_box = tk.Text(root, width=15, height=11, state="disabled")
                    output_box.tag_configure("red", foreground="red")
                    output_box.pack()

                    root.mainloop()
