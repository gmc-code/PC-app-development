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

All Button options
---------------------------

| Here is every option a Button can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``activebackground``
      - Background colour when the mouse is over it
      - ``activebackground="lightblue"``
    * - ``activeforeground``
      - Word colour when the mouse is over it
      - ``activeforeground="red"``
    * - ``anchor``
      - Where the words sit inside it (``"w"`` = left, ``"center"`` = middle)
      - ``anchor="w"``
    * - ``bg`` or ``background``
      - Background colour
      - ``bg="lavender"``
    * - ``bitmap``
      - Shows a small built-in picture
      - ``bitmap="question"``
    * - ``bd`` or ``borderwidth``
      - How thick the border is
      - ``bd=3``
    * - ``command``
      - Function to run when it is clicked
      - ``command=show``
    * - ``compound``
      - Where the picture goes compared to the words
      - ``compound="left"``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``default``
      - Marks it as the default button: ``"normal"``, ``"active"`` or ``"disabled"``
      - ``default="active"``
    * - ``disabledforeground``
      - Word colour when it is turned off
      - ``disabledforeground="grey"``
    * - ``font``
      - Style and size of the words
      - ``font=("Arial", 14)``
    * - ``fg`` or ``foreground``
      - Word colour
      - ``fg="purple"``
    * - ``height``
      - How tall it is (in lines of text)
      - ``height=2``
    * - ``highlightbackground``
      - Colour of the focus outline when it is not selected by the keyboard
      - ``highlightbackground="white"``
    * - ``highlightcolor``
      - Colour of the focus outline when it is selected by the keyboard
      - ``highlightcolor="blue"``
    * - ``highlightthickness``
      - How thick the focus outline is
      - ``highlightthickness=2``
    * - ``image``
      - Shows a picture instead of (or with) the words
      - ``image=dog_picture``
    * - ``justify``
      - Lines up many lines of words: ``"left"``, ``"center"`` or ``"right"``
      - ``justify="left"``
    * - ``overrelief``
      - Border style when the mouse is over it
      - ``overrelief="raised"``
    * - ``padx``
      - Extra space on the left and right of the words
      - ``padx=10``
    * - ``pady``
      - Extra space above and below the words
      - ``pady=5``
    * - ``relief``
      - Border style: ``"raised"``, ``"sunken"``, ``"flat"``, ``"ridge"``, ``"groove"`` or ``"solid"``
      - ``relief="sunken"``
    * - ``repeatdelay``
      - How long to hold the button before ``command`` starts repeating (milliseconds)
      - ``repeatdelay=500``
    * - ``repeatinterval``
      - How often ``command`` repeats while the button is held (milliseconds)
      - ``repeatinterval=100``
    * - ``state``
      - ``"normal"`` (can click), ``"active"`` or ``"disabled"`` (greyed out)
      - ``state="disabled"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``text``
      - Words shown on the button
      - ``text="Click me"``
    * - ``textvariable``
      - A variable that holds the words, so they can change
      - ``textvariable=label_words``
    * - ``underline``
      - Number of the letter to underline (``0`` = first letter)
      - ``underline=0``
    * - ``width``
      - How wide it is (in characters)
      - ``width=15``
    * - ``wraplength``
      - Starts a new line when the words get this long (in pixels)
      - ``wraplength=100``

| The picture option (``image``) needs a picture made first, e.g. ``dog_picture = tk.PhotoImage(file="dog.png")``.

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

        What does a Button do?

        [x] Runs a function when it is clicked | Correct. A button is clicked to make something happen.
        [ ] Shows a list of choices | Incorrect. A Listbox shows a list of choices.
        [ ] Lets the user type words | Incorrect. An Entry lets the user type.
        [ ] Draws shapes | Incorrect. A Canvas draws shapes.

    .. multichoice::

        Which option sets the words on a button?

        [ ] label | Incorrect. label is not a Button option.
        [ ] words | Incorrect. words is not an option.
        [x] text | Correct. text sets the words on the button.
        [ ] name | Incorrect. name is not used for the words.

    .. multichoice::

        How should command be written to run a function called say_hello?

        [ ] command=say_hello() | Incorrect. The brackets run the function straight away, before the click.
        [x] command=say_hello | Correct. Leave the brackets off so it runs when clicked.
        [ ] command="say_hello" | Incorrect. A string is not a function.
        [ ] command=[say_hello] | Incorrect. A list is not a function.

    .. multichoice::

        What does fg="white" change?

        [x] The colour of the words | Correct. fg is the foreground (word) colour.
        [ ] The background colour | Incorrect. bg sets the background colour.
        [ ] The border colour | Incorrect. fg does not change the border.
        [ ] The font | Incorrect. font sets the font.

    .. multichoice::

        What does bg="green" change?

        [ ] The word colour | Incorrect. fg sets the word colour.
        [x] The background colour | Correct. bg is the background colour.
        [ ] The colour when clicked | Incorrect. activebackground sets that.
        [ ] The window colour | Incorrect. It only changes the button.

    .. multichoice::

        What does font=("Arial", 16) set?

        [ ] Colour and size | Incorrect. Colour is set with fg.
        [ ] Width and height | Incorrect. width and height set the size of the button.
        [x] Font name and size | Correct. The first part is the name, the second is the size.
        [ ] Text and colour | Incorrect. text sets the words.

    .. multichoice::

        What does activebackground change?

        [x] The background colour while the mouse button is pressed on it | Correct. It is the colour when the button is active.
        [ ] The background when the button is disabled | Incorrect. That is not what it does.
        [ ] The window background | Incorrect. It only changes the button.
        [ ] The word colour | Incorrect. activeforeground sets the word colour.

    .. multichoice::

        For a button with text, what does width=10 mean?

        [ ] 10 pixels wide | Incorrect. With text, width is measured in characters.
        [x] About 10 characters wide | Correct. Text buttons measure width in characters.
        [ ] 10 centimetres wide | Incorrect. Tkinter does not use centimetres here.
        [ ] 10 buttons in a row | Incorrect. width sets the size of one button.

    .. multichoice::

        What do padx and pady add?

        [ ] Space outside the button | Incorrect. That is done in pack(padx=...).
        [x] Extra space inside the button around the words | Correct. They make the button bigger around its text.
        [ ] Extra buttons | Incorrect. They add space, not buttons.
        [ ] A border | Incorrect. relief and borderwidth make a border.

    .. multichoice::

        Which relief value makes a button look pushed in?

        [ ] "raised" | Incorrect. raised sticks out.
        [ ] "flat" | Incorrect. flat has no 3D look.
        [x] "sunken" | Correct. sunken looks pressed in.
        [ ] "ridge" | Incorrect. ridge looks like a raised edge.

    .. multichoice::

        What does overrelief do?

        [x] Changes the border style when the mouse is over the button | Correct. It is the relief used on hover.
        [ ] Changes the colour on hover | Incorrect. activebackground is used for colour.
        [ ] Hides the border | Incorrect. relief="flat" hides it.
        [ ] Makes the button larger | Incorrect. It only changes the border style.

    .. multichoice::

        What does cursor="hand2" do?

        [ ] Makes the button clickable twice | Incorrect. It changes the mouse pointer only.
        [x] Shows a pointing hand when the mouse is over the button | Correct. hand2 is a pointing hand pointer.
        [ ] Shows a hand picture on the button | Incorrect. image puts a picture on the button.
        [ ] Changes the font | Incorrect. font changes the words.

    .. multichoice::

        What does state="disabled" do?

        [ ] Deletes the button | Incorrect. destroy() removes a widget.
        [ ] Hides the button | Incorrect. pack_forget() hides it.
        [x] Greys out the button so it cannot be clicked | Correct. A disabled button does nothing when clicked.
        [ ] Runs the command | Incorrect. invoke() runs the command.

    .. multichoice::

        Which line changes the text of an existing button called go_button?

        [x] go_button.config(text="Stop") | Correct. config changes options after the button is made.
        [ ] go_button.text = "Stop" | Incorrect. Options are not changed like this.
        [ ] go_button.set("Stop") | Incorrect. Buttons do not have set.
        [ ] go_button.cget(text="Stop") | Incorrect. cget reads an option.

    .. multichoice::

        What does go_button.cget("text") give?

        [ ] It changes the text | Incorrect. config changes it.
        [x] The words currently on the button | Correct. cget reads the value of an option.
        [ ] The button's command | Incorrect. It gives the text, because "text" was asked for.
        [ ] An error | Incorrect. cget is a real method.

    .. multichoice::

        What does go_button.invoke() do?

        [ ] Deletes the button | Incorrect. destroy() does that.
        [ ] Disables the button | Incorrect. config(state="disabled") does that.
        [x] Runs the button's command, as if it was clicked | Correct. invoke acts like a click from your code.
        [ ] Changes the button colour | Incorrect. config changes colours.

    .. multichoice::

        Which command makes a Quit button close the window?

        [x] command=root.destroy | Correct. destroy closes the window.
        [ ] command=root.mainloop | Incorrect. mainloop keeps the window open.
        [ ] command=root.quit() | Incorrect. The brackets would run it straight away.
        [ ] command=close | Incorrect. close is not defined.

    .. multichoice::

        Why is lambda used in command=lambda: add(5)?

        [ ] To make the button faster | Incorrect. lambda does not change speed.
        [ ] To change the button colour | Incorrect. lambda is about the function call.
        [ ] To delete the button | Incorrect. lambda does not delete anything.
        [x] To send a value to the function when the button is clicked | Correct. lambda waits for the click, then calls add(5).

    .. multichoice::

        Which method places a button in the window?

        [ ] button.show() | Incorrect. Buttons do not have show.
        [x] button.pack() | Correct. pack places the widget.
        [ ] button.place_it() | Incorrect. This method does not exist.
        [ ] button.add() | Incorrect. add is not used for placing.

    .. multichoice::

        What is wrong with tk.Button(root, text="Go", command=go())?

        [ ] Nothing | Incorrect. go() runs at the start, not when clicked.
        [ ] text must be in capitals | Incorrect. Option names are lowercase.
        [x] go() runs straight away, not when the button is clicked | Correct. Leave the brackets off: command=go.
        [ ] Buttons cannot have text | Incorrect. Buttons can have text.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a button that runs say_hello when clicked.

        hello_button = tk.@@Button | Label | Entry@@(root, text="Hello", @@command | click | run@@=say_hello)
        hello_button.@@pack | show | draw@@()

    .. cloze::
        :instructions: Make a red button with white words.

        red_button = tk.Button(root, text="Stop", @@bg | fg | font@@="red", @@fg | bg | colour@@="white")
        red_button.pack()

    .. cloze::
        :instructions: Make a large button with extra space inside.

        big_button = tk.Button(root, text="Start", font=("Arial", @@20 | "20" | Arial@@), @@padx | width | size@@=20, pady=10)
        big_button.pack()

    .. cloze::
        :instructions: Turn a button off, then change its words.

        go_button.@@config | cget | invoke@@(state="@@disabled | off | hidden@@")
        go_button.config(@@text | words | label@@="Finished")

    .. cloze::
        :instructions: Make a Quit button and a button that sends a value.

        quit_button = tk.Button(root, text="Quit", command=root.@@destroy | mainloop | pack@@)
        add_button = tk.Button(root, text="+5", command=@@lambda | def | return@@: add(5))

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
