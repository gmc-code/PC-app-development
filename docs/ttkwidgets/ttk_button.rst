====================================================
ttk Button
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk Button?
------------------------

| A **ttk Button** is a button the user clicks to make the program do something, just like a tk Button.
| It looks more modern. Its colours and font are set with a **style** instead of ``fg``, ``bg`` and ``font``.
| See the **ttk widgets and styling** page for how styles work.

----

Making a ttk Button
----------------------

#. **Import** ttk with ``from tkinter import ttk``.
#. **Create** the button with ``ttk.Button(...)``.
#. **Place** it with ``.pack()``.

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets


    def say_hello():
        message_label.config(text="Hello!")


    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk Button")

    hello_button = ttk.Button(root, text="Say hello", command=say_hello)   # 2. Create
    hello_button.pack(pady=20)                                            # 3. Place

    message_label = ttk.Label(root, text="", font=("Arial", 18))
    message_label.pack()

    root.mainloop()                 # Keep the window open

----

ttk Button options
---------------------

text
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the words on the button.
| **How to write it:** ``text="your words"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("text")

    start_button = ttk.Button(root, text="Start the game")
    start_button.pack(pady=20)

    root.mainloop()

command
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses the function that runs when the button is clicked.
| **How to write it:** ``command=function_name``
| Do **not** put brackets after the function name, or it runs straight away instead of when clicked.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def add_one():
        number = int(count_label.cget("text"))
        count_label.config(text=number + 1)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("command")

    count_label = ttk.Label(root, text="0", font=("Arial", 36))
    count_label.pack(pady=10)

    add_button = ttk.Button(root, text="Add 1", command=add_one)
    add_button.pack()

    root.mainloop()

width
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how wide the button is, in **characters**.
| **How to write it:** ``width=15``
| Use the same width on several buttons so they line up.
| A ttk Button has no ``height`` option. Use ``padding`` in a style to make it taller.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width")

    ttk.Button(root, text="Yes", width=15).pack(pady=5)
    ttk.Button(root, text="No", width=15).pack(pady=5)
    ttk.Button(root, text="Maybe", width=15).pack(pady=5)

    root.mainloop()

padding
~~~~~~~~~~~~~~~~~~

| **What it does:** adds space inside the button around the words, making it bigger.
| **How to write it:** ``padding=10`` (all sides) or ``padding=(30, 10)`` (left-right, top-bottom)

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("padding")

    big_button = ttk.Button(root, text="Big button", padding=(30, 15))
    big_button.pack(pady=40)

    root.mainloop()

image and compound
~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``image`` shows a picture on the button. ``compound`` puts the picture beside the words.
| **How to write them:** ``image=picture, compound="left"``
| **compound values:** ``"left"``, ``"right"``, ``"top"``, ``"bottom"``, ``"center"``. The picture must be a .png or .gif in the same folder as your Python file.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("image")

    picture = tk.PhotoImage(file="logo.png")

    logo_button = ttk.Button(root, text="Home", image=picture, compound="left")
    logo_button.pack(pady=40)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** turns the button on or off.
| **How to write it:** ``state="disabled"`` when making it, or ``button.state(["disabled"])`` later.
| Use ``button.state(["!disabled"])`` to turn it back on.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    ttk.Button(root, text="I work").pack(pady=10)
    ttk.Button(root, text="I am turned off", state="disabled").pack(pady=10)

    root.mainloop()

cursor
~~~~~~~~~~~~~~~~~~

| **What it does:** changes the mouse pointer when it is over the button.
| **How to write it:** ``cursor="hand2"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("cursor")

    ttk.Button(root, text="Point at me", cursor="hand2").pack(pady=40)

    root.mainloop()

style
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses which style the button uses.
| **How to write it:** ``style="Name.TButton"``
| See **Styling a ttk Button** below.

----

ttk Button methods
---------------------

config and cget
~~~~~~~~~~~~~~~~~~

| **What they do:** ``config()`` changes options after the button has been made. ``cget()`` reads an option.
| **How to write them:** ``button.config(text="Done")``, ``words = button.cget("text")``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def switch():
        if light_button.cget("text") == "Turn ON":
            light_button.config(text="Turn OFF")
            light_label.config(text="Light is ON")
        else:
            light_button.config(text="Turn ON")
            light_label.config(text="Light is OFF")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config and cget")

    light_button = ttk.Button(root, text="Turn ON", width=12, command=switch)
    light_button.pack(pady=20)

    light_label = ttk.Label(root, text="Light is OFF", font=("Arial", 16))
    light_label.pack()

    root.mainloop()

state and instate
~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``state(["disabled"])`` turns the button off. ``state(["!disabled"])`` turns it on. ``instate(["disabled"])`` checks if it is off.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def vote():
        vote_button.state(["disabled"])         # Can only vote once
        result_label.config(text="Thanks for voting!")


    def reset():
        vote_button.state(["!disabled"])        # Turn back on
        result_label.config(text="")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    vote_button = ttk.Button(root, text="Vote", command=vote)
    vote_button.pack(pady=10)

    ttk.Button(root, text="Reset", command=reset).pack()

    result_label = ttk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()

invoke
~~~~~~~~~~~~~~~~~~

| **What it does:** "clicks" the button from your code, so its command runs.
| **How to write it:** ``button.invoke()``
| Below, pressing **Enter** invokes the button.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def greet():
        result_label.config(text="Hello!")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("invoke")

    greet_button = ttk.Button(root, text="Greet", command=greet)
    greet_button.pack(pady=20)

    result_label = ttk.Label(root, text="Press Enter or click")
    result_label.pack()

    root.bind("<Return>", lambda event: greet_button.invoke())

    root.mainloop()

Sending a value with lambda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``lambda:`` lets several buttons use **one** function, each sending a different value.
| **How to write it:** ``command=lambda: function_name(value)``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def change_colour(colour):
        root.config(bg=colour)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("lambda")

    ttk.Button(root, text="Red", command=lambda: change_colour("red")).pack(pady=5)
    ttk.Button(root, text="Green", command=lambda: change_colour("green")).pack(pady=5)
    ttk.Button(root, text="Blue", command=lambda: change_colour("blue")).pack(pady=5)

    root.mainloop()

----

Styling a ttk Button
-----------------------

| The style for every ttk Button is ``"TButton"``.

Changing every button
~~~~~~~~~~~~~~~~~~~~~~~~

| ``style.configure("TButton", ...)`` changes **all** ttk Buttons.
| ``"clam"`` is used so the background colour works on Windows.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Every button")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font=("Arial", 14), foreground="white",
                    background="purple", padding=10)

    ttk.Button(root, text="One").pack(pady=5)
    ttk.Button(root, text="Two").pack(pady=5)

    root.mainloop()

Changing some buttons
~~~~~~~~~~~~~~~~~~~~~~~~

| Make your own style, e.g. ``"Go.TButton"``, and use ``style="Go.TButton"`` on the buttons that need it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Some buttons")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Go.TButton", foreground="white", background="green", font=("Arial", 14))
    style.configure("Stop.TButton", foreground="white", background="red", font=("Arial", 14))

    ttk.Button(root, text="GO", style="Go.TButton").pack(pady=5)
    ttk.Button(root, text="STOP", style="Stop.TButton").pack(pady=5)
    ttk.Button(root, text="Normal button").pack(pady=5)

    root.mainloop()

Colours for hover and press
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``style.map`` changes the colour when the mouse is over the button (``"active"``) or it is being clicked (``"pressed"``).

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("map")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font=("Arial", 14), foreground="white", background="teal")
    style.map("TButton",
              background=[("pressed", "darkslategray"), ("active", "mediumturquoise")],
              foreground=[("disabled", "gray")])

    ttk.Button(root, text="Hover and press me").pack(pady=20)
    ttk.Button(root, text="Turned off", state="disabled").pack()

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
      - Function to run when clicked
      - ``command=start``
    * - ``width``
      - Width in characters
      - ``width=15``
    * - ``padding``
      - Space inside around the words
      - ``padding=(30, 10)``
    * - ``image``, ``compound``
      - Picture, and where it goes
      - ``image=pic, compound="left"``
    * - ``state``
      - Turn on or off
      - ``state="disabled"``
    * - ``cursor``
      - Mouse pointer
      - ``cursor="hand2"``
    * - ``style``
      - Which style to use
      - ``style="Go.TButton"``
    * - ``config()``, ``cget()``
      - Change or read an option
      - ``button.config(text="Done")``
    * - ``state([...])``
      - Turn a state on or off
      - ``button.state(["disabled"])``
    * - ``instate([...])``
      - Check a state
      - ``button.instate(["disabled"])``
    * - ``invoke()``
      - Click from code
      - ``button.invoke()``
    * - ``"TButton"``
      - Style name for every ttk Button
      - ``style.configure("TButton", font=("Arial", 12))``

----

All Button options
---------------------------

| Here is every option a ttk Button can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``class_``
      - A group name used to style many widgets at once (advanced). Written ``class_`` in Python
      - ``class_="Sidebar"``
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
    * - ``image``
      - Shows a picture instead of (or with) the words
      - ``image=dog_picture``
    * - ``padding``
      - Extra space inside it, around the words (one number, or left, top, right, bottom)
      - ``padding=10``
    * - ``state``
      - ``"normal"`` or ``"disabled"`` (greyed out)
      - ``state="disabled"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TButton"``
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

| The ``image`` option needs a picture made first, e.g. ``dog_picture = tk.PhotoImage(file="dog.png")``.
| ttk Button has no ``bg``, ``fg`` or ``font`` options. Change its colours and fonts with a style, e.g. ``style.configure("TButton", foreground="purple")``.

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

        How is a ttk Button made?

        [x] ttk.Button(root, text="Go") | Correct. Import ttk from tkinter first.
        [ ] tk.Button(root, style="ttk") | Incorrect. That makes a tk Button.
        [ ] ttk.button(root, text="Go") | Incorrect. The name needs a capital B.
        [ ] tk.ttk(root, text="Go") | Incorrect. ttk is a module, not a widget.

    .. multichoice::

        Which import is needed for ttk widgets?

        [ ] import ttk | Incorrect. ttk is inside tkinter.
        [x] from tkinter import ttk | Correct. ttk comes from tkinter.
        [ ] import tkinter.ttk as tk | Incorrect. Keep tk for tkinter.
        [ ] from ttk import Button | Incorrect. Not where it lives.

    .. multichoice::

        What is the main difference between ttk and tk buttons?

        [x] ttk buttons match the computer's theme and are styled with ttk.Style | Correct. They look more modern.
        [ ] ttk buttons cannot be clicked | Incorrect. They can.
        [ ] ttk buttons have no text | Incorrect. They have text.
        [ ] There is no difference | Incorrect. The look and styling differ.

    .. multichoice::

        Why does ttk.Button(root, bg="red") cause an error?

        [ ] bg must be in capitals | Incorrect. ttk has no bg option at all.
        [x] ttk widgets do not have a bg option; colours are set with a style | Correct. Use style.configure.
        [ ] Red is not a colour | Incorrect. Red is fine.
        [ ] Buttons cannot be red | Incorrect. They can, with a style.

    .. multichoice::

        What does padding=10 do?

        [ ] Adds space outside the button | Incorrect. That is done in pack.
        [x] Adds 10 pixels of space inside the button around the words | Correct. padding makes it bigger.
        [ ] Makes 10 buttons | Incorrect. It adds space.
        [ ] Moves the button | Incorrect. pack or grid move it.

    .. multichoice::

        What does width=15 mean on a ttk Button?

        [x] About 15 characters wide | Correct. Text buttons count characters.
        [ ] 15 pixels | Incorrect. It counts characters.
        [ ] 15 lines | Incorrect. Not lines.
        [ ] 15 buttons | Incorrect. One button.

    .. multichoice::

        What does compound="left" do?

        [ ] Puts the button on the left | Incorrect. It places the picture.
        [x] Shows the picture on the left of the words | Correct. compound places the image next to the text.
        [ ] Hides the words | Incorrect. It shows both.
        [ ] Joins two buttons | Incorrect. It places the image.

    .. multichoice::

        Which line greys out a ttk Button?

        [ ] button.config(bg="grey") | Incorrect. ttk has no bg.
        [x] button.state(["disabled"]) | Correct. The state method takes a list.
        [ ] button.disable() | Incorrect. Not a method.
        [ ] button.grey() | Incorrect. Not a method.

    .. multichoice::

        Which line turns the button back on?

        [x] button.state(["!disabled"]) | Correct. The ! means "not disabled".
        [ ] button.state(["enabled"]) | Incorrect. Not a ttk state.
        [ ] button.state("on") | Incorrect. Not right.
        [ ] button.config(on=True) | Incorrect. Not an option.

    .. multichoice::

        What does button.instate(["disabled"]) give?

        [ ] It disables the button | Incorrect. state does that.
        [x] True if the button is disabled, otherwise False | Correct. instate checks a state.
        [ ] The button text | Incorrect. It checks state.
        [ ] An error | Incorrect. It is a real method.

    .. multichoice::

        What does cursor="hand2" do?

        [x] Shows a pointing hand when the mouse is over the button | Correct. It changes the pointer.
        [ ] Adds a picture of a hand | Incorrect. image does that.
        [ ] Makes the button bigger | Incorrect. It changes the pointer.
        [ ] Clicks twice | Incorrect. It changes the pointer.

    .. multichoice::

        What does style="Big.TButton" do?

        [ ] Makes a new widget | Incorrect. It uses a style.
        [x] Uses the style called Big.TButton for this button only | Correct. Custom styles end with the class name.
        [ ] Changes every button | Incorrect. "TButton" would change every button.
        [ ] Causes an error | Incorrect. It works once the style is set.

    .. multichoice::

        Which style name changes every ttk Button?

        [x] "TButton" | Correct. TButton is the style for all buttons.
        [ ] "Button" | Incorrect. The style name is TButton.
        [ ] "ttk.Button" | Incorrect. Not a style name.
        [ ] "AllButtons" | Incorrect. Not a style name.

    .. multichoice::

        Which line makes the style object?

        [ ] style = ttk.style() | Incorrect. Style needs a capital S.
        [x] style = ttk.Style() | Correct. Then use style.configure.
        [ ] style = tk.Style() | Incorrect. Style is in ttk.
        [ ] style = root.style() | Incorrect. Not a method.

    .. multichoice::

        What does style.configure("TButton", font=("Arial", 14)) do?

        [ ] Changes one button | Incorrect. It changes every ttk Button.
        [x] Changes the font of every ttk Button | Correct. TButton is the style for all of them.
        [ ] Changes every widget | Incorrect. Only buttons.
        [ ] Nothing | Incorrect. It changes the font.

    .. multichoice::

        What does style.map("TButton", background=[("active", "yellow")]) do?

        [x] Makes buttons turn yellow when the mouse is over them | Correct. map sets colours for states.
        [ ] Makes all buttons yellow all the time | Incorrect. Only when active.
        [ ] Draws a map | Incorrect. It maps states to colours.
        [ ] Deletes yellow | Incorrect. It sets a colour.

    .. multichoice::

        What does button.cget("text") give?

        [ ] It changes the text | Incorrect. config changes it.
        [x] The current words on the button | Correct. cget reads an option.
        [ ] The style | Incorrect. It reads text.
        [ ] An error | Incorrect. It is a real method.

    .. multichoice::

        What does button.invoke() do?

        [ ] Deletes it | Incorrect. destroy does that.
        [x] Runs the button's command, as if clicked | Correct. invoke acts like a click.
        [ ] Disables it | Incorrect. state does that.
        [ ] Changes its style | Incorrect. config does that.

    .. multichoice::

        Why is lambda used in command=lambda: add(5)?

        [ ] To make it faster | Incorrect. Not about speed.
        [x] To send a value to the function when the button is clicked | Correct. lambda waits for the click.
        [ ] To change the style | Incorrect. Not about style.
        [ ] It is not needed | Incorrect. Without it add(5) runs at the start.

    .. multichoice::

        Some themes on Windows ignore background colours on buttons. What can be used instead?

        [x] style.theme_use("clam") | Correct. The clam theme allows colour changes.
        [ ] tk.Button with ttk | Incorrect. Not the fix.
        [ ] bg="red" | Incorrect. ttk has no bg.
        [ ] A Label | Incorrect. A Label is not a button.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: both
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a ttk Button.

        from tkinter import @@ttk | tk | Style@@
        go_button = ttk.@@Button | button | Label@@(root, text="Go", @@command | click | run@@=go)
        go_button.pack()

    .. cloze::
        :instructions: Give it padding and a width.

        go_button = ttk.Button(root, text="Start", @@padding | padx | space@@=10, @@width | size | length@@=15)

    .. cloze::
        :instructions: Style every button.

        style = ttk.@@Style | style | Theme@@()
        style.@@configure | config | set@@("@@TButton | Button | ttkButton@@", font=("Arial", 14))

    .. cloze::
        :instructions: Make one special button.

        style.configure("Big.TButton", font=("Arial", 20))
        big_button = ttk.Button(root, text="Big", @@style | theme | font@@="Big.TButton")

    .. cloze::
        :instructions: Turn a button off and on.

        go_button.@@state | config | set@@(["disabled"])
        go_button.state(["@@!disabled | enabled | on@@"])

----

.. admonition:: Tasks

    #. Make a window titled "ttk Buttons" that is 300x200. Add a ttk Button "Click me" with a width of 15 and padding of 10.
    #. Add a label below the button. When the button is clicked, the label shows "Clicked!".
    #. Use a style so every ttk Button uses Arial size 16 with white words on a dark blue background.
    #. Make a "Danger.TButton" style with a red background that turns dark red while pressed. Use it on a "Delete" button, and keep a normal "Cancel" button.

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
                    root.title("ttk Buttons")

                    click_button = ttk.Button(root, text="Click me", width=15, padding=10)
                    click_button.pack(pady=20)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def clicked():
                        result_label.config(text="Clicked!")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("ttk Buttons")

                    click_button = ttk.Button(root, text="Click me", width=15, padding=10,
                                              command=clicked)
                    click_button.pack(pady=20)

                    result_label = ttk.Label(root, text="")
                    result_label.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def clicked():
                        result_label.config(text="Clicked!")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("ttk Buttons")

                    style = ttk.Style()
                    style.theme_use("clam")
                    style.configure("TButton", font=("Arial", 16), foreground="white",
                                    background="darkblue")

                    click_button = ttk.Button(root, text="Click me", width=15, padding=10,
                                              command=clicked)
                    click_button.pack(pady=20)

                    result_label = ttk.Label(root, text="")
                    result_label.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Delete")

                    style = ttk.Style()
                    style.theme_use("clam")
                    style.configure("Danger.TButton", foreground="white", background="red")
                    style.map("Danger.TButton", background=[("pressed", "darkred")])

                    ttk.Button(root, text="Delete", style="Danger.TButton").pack(pady=10)
                    ttk.Button(root, text="Cancel").pack()

                    root.mainloop()
