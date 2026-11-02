====================================================
tk Message
====================================================

| See: `<https://www.tcl-lang.org/man/tcl8.6/TkCmd/message.htm>`_

----

What is a Message?
-------------------

| A **Message** shows text, like a **Label**, but it is made for **longer** text.
| A Message wraps the words onto new lines **by itself**, so the text forms a neat block.
| Use a Message for instructions, a story or a paragraph of information.

----

Making a Message
-------------------

#. **Create** the message with ``tk.Message(...)``.
#. **Place** it in the window with ``.pack()``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first message")  # Words in the title bar

    rules = tk.Message(root, text="Answer each question by clicking a button. "
                                  "You get one point for each correct answer. "
                                  "Good luck!")          # 1. Create the message
    rules.pack(pady=10)                                  # 2. Place it in the window

    root.mainloop()                 # Keep the window open

| Long text can be split over several lines of code inside brackets. Python joins strings that sit next to each other, so remember the space at the end of each part.

----

Message options
-------------------

| Options are written as ``option=value`` inside ``tk.Message( )``, separated by commas.

text
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the words shown in the message.
| **How to write it:** ``text="your words"``
| Use ``\n`` to start a new paragraph.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("text")

    note = tk.Message(root, text="Dear class,\nPlease bring your laptop on Friday.\nThanks!")
    note.pack(pady=10)

    root.mainloop()

width
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how wide the block of text can be, in **pixels**. The text wraps when it reaches this width.
| **How to write it:** ``width=250``
| Note: for a Message, width is in **pixels**, but for a Label it is in characters.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("350x250")
    root.title("width")

    text = "Koalas sleep for up to 20 hours a day and eat only gum leaves."

    narrow = tk.Message(root, text=text, width=100, bg="lightblue")
    narrow.pack(pady=5)

    wide = tk.Message(root, text=text, width=300, bg="lightgreen")
    wide.pack(pady=5)

    root.mainloop()

aspect
~~~~~~~~~~~~~~~~~~

| **What it does:** if ``width`` is not set, ``aspect`` chooses the shape of the text block.
| It is the width compared with the height, times 100.

- ``aspect=150`` (the default) makes a block a bit wider than it is tall.
- ``aspect=400`` makes a wide, short block.
- ``aspect=50`` makes a narrow, tall block.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("350x300")
    root.title("aspect")

    text = "The water cycle moves water from the ocean to the sky and back again."

    tk.Message(root, text=text, aspect=400, bg="lightblue").pack(pady=5)
    tk.Message(root, text=text, aspect=50, bg="lightgreen").pack(pady=5)

    root.mainloop()

| ``tk.Message(...).pack()`` creates and places a widget in one line. Only do this when you never need to use the widget's name again.

font
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the style and size of the letters.
| **How to write it:** ``font=("font name", size)`` or ``font=("font name", size, "style")``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("font")

    quote = tk.Message(root, text="Science is a way of thinking.", width=250,
                       font=("Georgia", 16, "italic"))
    quote.pack(pady=20)

    root.mainloop()

fg and bg (colours)
~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``fg`` sets the colour of the words. ``bg`` sets the colour behind them.
| **How to write them:** ``fg="colour"``, ``bg="colour"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("fg and bg")

    warning = tk.Message(root, text="Warning: the oven is hot. Use oven mitts.", width=250,
                         fg="white", bg="red", font=("Arial", 14))
    warning.pack(pady=20)

    root.mainloop()

justify
~~~~~~~~~~~~~~~~~~

| **What it does:** lines up the wrapped lines on the left, in the centre or on the right.
| **How to write it:** ``justify="center"``
| **Values:** ``"left"`` (the default), ``"center"``, ``"right"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("justify")

    poem = tk.Message(root, text="Roses are red,\nviolets are blue,\nPython is fun\nand Tkinter is too!",
                      width=250, justify="center", font=("Arial", 14))
    poem.pack(pady=10)

    root.mainloop()

padx and pady
~~~~~~~~~~~~~~~~~~

| **What they do:** add empty space around the text, **inside** the message.
| **How to write them:** ``padx=20``, ``pady=10`` (pixels)

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("padx and pady")

    tip = tk.Message(root, text="Tip: save your work often!", width=250,
                     bg="lightyellow", padx=20, pady=20)
    tip.pack(pady=20)

    root.mainloop()

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** draw a border around the message.
| **How to write them:** ``relief="solid", borderwidth=2``
| **Styles:** ``"flat"`` (the default), ``"solid"``, ``"raised"``, ``"sunken"``, ``"groove"``, ``"ridge"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("relief")

    box = tk.Message(root, text="This message has a solid border around it.", width=200,
                     relief="solid", borderwidth=2, padx=10, pady=10)
    box.pack(pady=20)

    root.mainloop()

textvariable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the message to a **StringVar**. When the variable changes, the message changes by itself.
| **How to write it:** ``story = tk.StringVar(value="start text")`` then ``textvariable=story``

.. code-block:: python

    import tkinter as tk


    def next_page():
        story.set("The dragon flew over the mountains, looking for somewhere to land.")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("textvariable")

    story = tk.StringVar(value="Once upon a time, there was a small green dragon.")

    page = tk.Message(root, textvariable=story, width=250, font=("Arial", 12))
    page.pack(pady=10)

    tk.Button(root, text="Next page", command=next_page).pack()

    root.mainloop()

----

Message methods
-------------------

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options **after** the message has been made, e.g. to show new text.
| **How to write it:** ``message.config(option=value)``

.. code-block:: python

    import tkinter as tk

    facts = [
        "The Sun is a star.",
        "Light from the Sun takes about 8 minutes to reach Earth.",
        "Jupiter is the largest planet in our solar system.",
    ]
    fact_number = 0


    def next_fact():
        global fact_number              # Allow the function to change fact_number
        fact_number = (fact_number + 1) % len(facts)     # Go back to 0 after the last fact
        fact_message.config(text=facts[fact_number])


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    fact_message = tk.Message(root, text=facts[0], width=250, font=("Arial", 14))
    fact_message.pack(pady=10)

    tk.Button(root, text="Next fact", command=next_fact).pack()

    root.mainloop()

cget
~~~~~~~~~~~~~~~~~~

| **What it does:** reads the current value of an option, e.g. the text.
| **How to write it:** ``words = message.cget("text")``

.. code-block:: python

    import tkinter as tk


    def count_words():
        words = info.cget("text").split()
        count_label.config(text=f"That message has {len(words)} words")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("cget")

    info = tk.Message(root, text="Plants make their own food using sunlight, water and air.",
                      width=250)
    info.pack(pady=10)

    tk.Button(root, text="Count words", command=count_words).pack()

    count_label = tk.Label(root, text="")
    count_label.pack(pady=5)

    root.mainloop()

----

Message or Label?
--------------------

| A **Label** with ``wraplength`` can also wrap text. Both work. Use whichever is easier:

.. list-table::
    :header-rows: 1
    :widths: 30 35 35

    * -
      - Message
      - Label
    * - Wraps text
      - By itself
      - Only if ``wraplength`` is set
    * - ``width`` measured in
      - Pixels
      - Characters
    * - Can show a picture
      - No
      - Yes

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
      - Words shown
      - ``text="Hello"``
    * - ``width``
      - Width of the text block in pixels
      - ``width=250``
    * - ``aspect``
      - Shape of the block if no width is set
      - ``aspect=300``
    * - ``font``
      - Font name, size and style
      - ``font=("Arial", 14)``
    * - ``fg``, ``bg``
      - Word colour, background colour
      - ``fg="white", bg="red"``
    * - ``justify``
      - Line up the lines
      - ``justify="center"``
    * - ``padx``, ``pady``
      - Space around the text
      - ``padx=10, pady=10``
    * - ``relief``, ``borderwidth``
      - Border style and thickness
      - ``relief="solid", borderwidth=2``
    * - ``textvariable``
      - Link to a StringVar
      - ``textvariable=story``
    * - ``config()``
      - Change options later
      - ``message.config(text="New")``
    * - ``cget()``
      - Read an option
      - ``message.cget("text")``

----

All Message options
---------------------------

| Here is every option a Message can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``anchor``
      - Where the words sit inside it (``"w"`` = left, ``"center"`` = middle)
      - ``anchor="w"``
    * - ``aspect``
      - Shape of the text: width compared to height as a percentage (200 = twice as wide as tall)
      - ``aspect=200``
    * - ``bg`` or ``background``
      - Background colour
      - ``bg="lavender"``
    * - ``bd`` or ``borderwidth``
      - How thick the border is
      - ``bd=3``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
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
    * - ``justify``
      - Lines up many lines of words: ``"left"``, ``"center"`` or ``"right"``
      - ``justify="left"``
    * - ``padx``
      - Extra space on the left and right of the words
      - ``padx=10``
    * - ``pady``
      - Extra space above and below the words
      - ``pady=5``
    * - ``relief``
      - Border style: ``"raised"``, ``"sunken"``, ``"flat"``, ``"ridge"``, ``"groove"`` or ``"solid"``
      - ``relief="sunken"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``text``
      - Words to show (they wrap onto new lines by themselves)
      - ``text="Welcome to the quiz"``
    * - ``textvariable``
      - A variable that holds the words, so they can change
      - ``textvariable=label_words``
    * - ``width``
      - How wide the text is (in pixels). ``0`` uses ``aspect`` instead
      - ``width=200``

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

        What is a Message widget?

        [x] A label that wraps long text onto many lines by itself | Correct. It is good for paragraphs.
        [ ] A pop-up box | Incorrect. That is messagebox.
        [ ] A box to type in | Incorrect. That is Entry or Text.
        [ ] A button | Incorrect. It only shows text.

    .. multichoice::

        How is Message different from Label?

        [ ] Message cannot show text | Incorrect. It shows text.
        [x] Message wraps text automatically to a shape | Correct. Labels need wraplength.
        [ ] Message can be typed in | Incorrect. It cannot.
        [ ] There is no difference | Incorrect. Wrapping differs.

    .. multichoice::

        Which option sets the words?

        [ ] message | Incorrect. Not an option.
        [x] text | Correct. text sets the words.
        [ ] words | Incorrect. Not an option.
        [ ] value | Incorrect. Not an option.

    .. multichoice::

        For a Message, width=200 means:

        [ ] 200 characters | Incorrect. Message width is in pixels.
        [x] 200 pixels wide before wrapping | Correct. Message width is in pixels.
        [ ] 200 lines | Incorrect. Not lines.
        [ ] 200 words | Incorrect. Not words.

    .. multichoice::

        What does aspect=200 do?

        [x] Makes the text box about twice as wide as it is tall | Correct. aspect is width compared to height as a percentage.
        [ ] Sets the font size | Incorrect. font does that.
        [ ] Makes it 200 pixels wide | Incorrect. width does that.
        [ ] Shows 200 letters | Incorrect. All letters show.

    .. multichoice::

        If both width and aspect are given, which is used?

        [ ] aspect | Incorrect. width wins when it is not 0.
        [x] width | Correct. aspect is only used when width is 0.
        [ ] Neither | Incorrect. One is used.
        [ ] Both | Incorrect. Only one.

    .. multichoice::

        Which option sets the font?

        [ ] size | Incorrect. Not an option.
        [x] font=("Arial", 14) | Correct. font sets name and size.
        [ ] style | Incorrect. Not an option.
        [ ] text | Incorrect. text sets words.

    .. multichoice::

        What does fg="navy" do?

        [ ] Colours the background | Incorrect. bg does that.
        [x] Colours the words navy | Correct. fg is the word colour.
        [ ] Colours the border | Incorrect. It colours the words.
        [ ] Nothing | Incorrect. It changes word colour.

    .. multichoice::

        What does justify="center" do?

        [x] Centres each line of the text | Correct. justify lines up the lines.
        [ ] Centres the window | Incorrect. It only affects the text.
        [ ] Makes the text bigger | Incorrect. font does that.
        [ ] Removes wrapping | Incorrect. It lines up lines.

    .. multichoice::

        Which justify value lines up the lines on the right?

        [ ] "left" | Incorrect. That is left.
        [ ] "e" | Incorrect. justify uses words, not letters.
        [x] "right" | Correct. right lines up on the right.
        [ ] "end" | Incorrect. Not a value.

    .. multichoice::

        What do padx and pady do?

        [ ] Move the widget | Incorrect. pack or grid move it.
        [x] Add space inside the Message around the text | Correct. They pad the inside.
        [ ] Add more text | Incorrect. They add space.
        [ ] Change the font | Incorrect. font does that.

    .. multichoice::

        Which pair adds a visible border?

        [x] relief and borderwidth | Correct. relief is the style, borderwidth the thickness.
        [ ] fg and bg | Incorrect. These are colours.
        [ ] padx and pady | Incorrect. These add space.
        [ ] width and aspect | Incorrect. These set shape.

    .. multichoice::

        What does textvariable=story do?

        [ ] Sets the font | Incorrect. font does that.
        [x] Links the text to a StringVar, so story.set() changes it | Correct. The Message updates by itself.
        [ ] Hides the text | Incorrect. It links a variable.
        [ ] Names the widget | Incorrect. It links a variable.

    .. multichoice::

        Which line changes the text later?

        [ ] msg.text("Hi") | Incorrect. Not a method.
        [x] msg.config(text="Hi") | Correct. config changes options.
        [ ] msg.set("Hi") | Incorrect. Not for the widget.
        [ ] msg.cget(text="Hi") | Incorrect. cget reads.

    .. multichoice::

        What does msg.cget("width") give?

        [x] The current width of the Message | Correct. cget reads an option.
        [ ] It changes the width | Incorrect. config does that.
        [ ] The text | Incorrect. It reads width.
        [ ] An error | Incorrect. cget works.

    .. multichoice::

        Can the user type into a Message?

        [ ] Yes | Incorrect. It only shows text.
        [x] No | Correct. Use Entry or Text for typing.
        [ ] Only with textvariable | Incorrect. Still no.
        [ ] Only when state="normal" | Incorrect. Still no.

    .. multichoice::

        Which is the best widget for a few sentences of instructions?

        [x] Message | Correct. It wraps paragraphs well.
        [ ] Entry | Incorrect. Entry is for typing.
        [ ] Button | Incorrect. Buttons are for clicks.
        [ ] Scale | Incorrect. Scale picks a number.

    .. multichoice::

        What does bg="lightyellow" change?

        [ ] The words | Incorrect. fg changes words.
        [x] The background of the Message | Correct. bg is the background.
        [ ] The window | Incorrect. Only the Message.
        [ ] The border | Incorrect. It changes the background.

    .. multichoice::

        What happens to a very long word in a narrow Message?

        [ ] It is deleted | Incorrect. Text is not deleted.
        [x] It stays on one line because Message wraps between words | Correct. Wrapping happens at spaces.
        [ ] It turns red | Incorrect. No colour change.
        [ ] An error happens | Incorrect. No error.

    .. multichoice::

        Which line makes and places a Message?

        [x] tk.Message(root, text="Hello", width=200).pack() | Correct. Make it, then pack it.
        [ ] tk.Message.pack(text="Hello") | Incorrect. Make it first.
        [ ] root.Message(text="Hello") | Incorrect. Use tk.Message.
        [ ] tk.Message(text="Hello").show() | Incorrect. show is not a method.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a Message that wraps at 200 pixels.

        info = tk.@@Message | Label | Entry@@(root, text=long_text, @@width | length | wrap@@=200)
        info.pack()

    .. cloze::
        :instructions: Use aspect instead of width.

        info = tk.Message(root, text=long_text, @@aspect | shape | ratio@@=300)
        info.@@pack | show | place_it@@()

    .. cloze::
        :instructions: Style the Message.

        info = tk.Message(root, text="Welcome", font=("Arial", @@14 | Arial | big@@), @@fg | bg | font@@="navy", bg="lightyellow")

    .. cloze::
        :instructions: Centre the lines and add space.

        info = tk.Message(root, text=long_text, @@justify | anchor | side@@="center", @@padx | width | fill@@=10, pady=10)

    .. cloze::
        :instructions: Change and read the text.

        story = tk.@@StringVar | IntVar | Message@@(value="Once upon a time")
        info = tk.Message(root, @@textvariable | text | variable@@=story)
        story.@@set | get | config@@("The end")

----

.. admonition:: Tasks

    #. Make a window titled "Instructions" that is 300x200. Add a Message 250 pixels wide that explains how to play a game of your choice, in Arial size 12.
    #. Give your Message a light yellow background, a solid border with a borderwidth of 1, and 10 pixels of padding.
    #. Make a Message showing a four-line poem with each line centred. Use ``\n`` to start each new line.
    #. Make a Message and a "Change" button. When clicked, use ``config`` to change the message text to a fun fact and its background to light green.

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
                    root.title("Instructions")

                    how_to = tk.Message(root, text="Roll the dice and move your piece. "
                                                   "If you land on a ladder, climb up. "
                                                   "If you land on a snake, slide down.",
                                        width=250, font=("Arial", 12))
                    how_to.pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Instructions")

                    how_to = tk.Message(root, text="Roll the dice and move your piece. "
                                                   "If you land on a ladder, climb up. "
                                                   "If you land on a snake, slide down.",
                                        width=250, font=("Arial", 12), bg="lightyellow",
                                        relief="solid", borderwidth=1, padx=10, pady=10)
                    how_to.pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Poem")

                    poem = tk.Message(root, text="Twinkle, twinkle, little star,\n"
                                                 "How I wonder what you are!\n"
                                                 "Up above the world so high,\n"
                                                 "Like a diamond in the sky.",
                                      width=250, justify="center")
                    poem.pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def change():
                        fact.config(text="An octopus has three hearts!", bg="lightgreen")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Fun fact")

                    fact = tk.Message(root, text="Click the button for a fun fact.", width=250)
                    fact.pack(pady=10)

                    tk.Button(root, text="Change", command=change).pack()

                    root.mainloop()
