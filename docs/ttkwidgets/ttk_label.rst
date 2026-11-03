====================================================
ttk Label
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk Label?
-----------------------

| A **ttk Label** shows words or a picture in a window, just like a tk Label.
| Unlike most ttk widgets, a ttk Label **does** have ``font``, ``foreground`` and ``background`` options, so it can be styled directly **or** with a style.
| ttk uses the full words ``foreground`` and ``background``, not ``fg`` and ``bg``.

----

Making a ttk Label
---------------------

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk Label")

    hello_label = ttk.Label(root, text="Hello, world!")    # 1. Create the label
    hello_label.pack(pady=20)                             # 2. Place it

    root.mainloop()                 # Keep the window open

----

ttk Label options
--------------------

text
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the words on the label. Use ``\n`` for a new line.
| **How to write it:** ``text="your words"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("text")

    ttk.Label(root, text="Line one\nLine two").pack(pady=20)

    root.mainloop()

font
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the style and size of the letters.
| **How to write it:** ``font=("font name", size)`` or ``font=("font name", size, "style")``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("font")

    ttk.Label(root, text="Arial 24", font=("Arial", 24)).pack(pady=5)
    ttk.Label(root, text="Bold and italic", font=("Arial", 18, "bold italic")).pack(pady=5)

    root.mainloop()

foreground and background
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``foreground`` sets the colour of the words. ``background`` sets the colour behind them.
| **How to write them:** ``foreground="blue"``, ``background="yellow"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("foreground and background")

    ttk.Label(root, text="Blue on yellow", font=("Arial", 18),
              foreground="blue", background="yellow").pack(pady=40)

    root.mainloop()

width
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the width of the label in **characters**.
| **How to write it:** ``width=20``
| A ttk Label has no ``height`` option. Use ``padding`` to make it taller.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width")

    ttk.Label(root, text="Wide label", width=25, background="lightblue").pack(pady=40)

    root.mainloop()

padding
~~~~~~~~~~~~~~~~~~

| **What it does:** adds space around the words, inside the label.
| **How to write it:** ``padding=10`` (all sides), ``padding=(40, 10)`` (left-right, top-bottom), or ``padding=(left, top, right, bottom)``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("padding")

    ttk.Label(root, text="Padded", font=("Arial", 18), background="lightgreen",
              padding=(40, 20)).pack(pady=40)

    root.mainloop()

anchor
~~~~~~~~~~~~~~~~~~

| **What it does:** moves the words to a side or corner of the label.
| **How to write it:** ``anchor="w"``
| **Positions:** ``"n"``, ``"s"``, ``"e"``, ``"w"``, ``"ne"``, ``"nw"``, ``"se"``, ``"sw"``, ``"center"``.
| The label must be wider than its words for anchor to move them.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("anchor")

    for position in ["w", "center", "e"]:
        ttk.Label(root, text=position, width=30, anchor=position,
                  background="lightyellow").pack(pady=5)

    root.mainloop()

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** draw a border around the label.
| **How to write them:** ``relief="solid", borderwidth=2``
| **Styles:** ``"flat"`` (the default), ``"solid"``, ``"raised"``, ``"sunken"``, ``"groove"``, ``"ridge"``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("relief")

    ttk.Label(root, text="Border", font=("Arial", 16), relief="solid", borderwidth=2,
              padding=10).pack(pady=40)

    root.mainloop()

wraplength and justify
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``wraplength`` wraps long text onto new lines (in pixels). ``justify`` lines the wrapped lines up ``"left"``, ``"center"`` or ``"right"``.
| **How to write them:** ``wraplength=200, justify="center"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("wraplength")

    ttk.Label(root, text="This sentence is too long for one line, so it wraps onto the next.",
              font=("Arial", 13), wraplength=200, justify="center").pack(pady=30)

    root.mainloop()

image and compound
~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``image`` shows a picture. ``compound`` shows the picture **and** the words, e.g. ``"top"`` puts the picture above.
| **How to write them:** ``image=picture, compound="top"``
| The picture must be a .png or .gif in the same folder as your Python file.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("image")

    picture = tk.PhotoImage(file="logo.png")

    ttk.Label(root, image=picture, text="Our logo", compound="top").pack(pady=20)

    root.mainloop()

textvariable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the label to a ``StringVar``. When the variable changes with ``.set()``, the label changes by itself.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def win():
        message.set("You win!")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("textvariable")

    message = tk.StringVar(value="Click Play")

    ttk.Label(root, textvariable=message, font=("Arial", 18)).pack(pady=20)
    ttk.Button(root, text="Play", command=win).pack()

    root.mainloop()

----

ttk Label methods
--------------------

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options after the label has been made, e.g. to show an answer.
| **How to write it:** ``label.config(option=value)``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def change():
        result_label.config(text="Changed!", foreground="white", background="green")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    result_label = ttk.Label(root, text="Not changed yet", font=("Arial", 16), padding=5)
    result_label.pack(pady=20)

    ttk.Button(root, text="Change", command=change).pack()

    root.mainloop()

cget
~~~~~~~~~~~~~~~~~~

| **What it does:** reads an option, e.g. the label's text. The text is a **string**, so use ``int()`` before doing maths.
| **How to write it:** ``words = label.cget("text")``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def add_five():
        number = int(score_label.cget("text"))
        score_label.config(text=number + 5)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("cget")

    score_label = ttk.Label(root, text="0", font=("Arial", 40))
    score_label.pack(pady=10)

    ttk.Button(root, text="Add 5", command=add_five).pack()

    root.mainloop()

----

Styling a ttk Label
----------------------

| The style for every ttk Label is ``"TLabel"``.
| Using a style is better than setting ``font`` and colours on every label: change the style once and every label matches.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x220")
    root.title("Label styles")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12))                                  # Every label
    style.configure("Title.TLabel", font=("Arial", 22, "bold"), foreground="navy")
    style.configure("Warning.TLabel", foreground="white", background="red", padding=5)

    ttk.Label(root, text="My App", style="Title.TLabel").pack(pady=10)
    ttk.Label(root, text="A normal label").pack(pady=5)
    ttk.Label(root, text="Save your work!", style="Warning.TLabel").pack(pady=5)

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
      - Words on the label
      - ``text="Hello"``
    * - ``font``
      - Font name, size and style
      - ``font=("Arial", 16)``
    * - ``foreground``
      - Colour of the words
      - ``foreground="blue"``
    * - ``background``
      - Colour behind the words
      - ``background="yellow"``
    * - ``width``
      - Width in characters
      - ``width=20``
    * - ``padding``
      - Space around the words
      - ``padding=(20, 10)``
    * - ``anchor``
      - Where the words sit
      - ``anchor="w"``
    * - ``relief``, ``borderwidth``
      - Border style and thickness
      - ``relief="solid", borderwidth=2``
    * - ``wraplength``, ``justify``
      - Wrap long text and line it up
      - ``wraplength=200``
    * - ``image``, ``compound``
      - Show a picture
      - ``image=pic, compound="top"``
    * - ``textvariable``
      - Link to a StringVar
      - ``textvariable=message``
    * - ``config()``, ``cget()``
      - Change or read an option
      - ``label.config(text="Hi")``
    * - ``"TLabel"``
      - Style name for every ttk Label
      - ``style.configure("TLabel", font=("Arial", 12))``

----

All Label options
---------------------------

| Here is every option a ttk Label can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``anchor``
      - Where the words sit inside it (``"w"`` = left, ``"center"`` = middle)
      - ``anchor="w"``
    * - ``background``
      - Background colour (write ``background``, not ``bg``)
      - ``background="lavender"``
    * - ``borderwidth``
      - How thick the border is (write ``borderwidth``, not ``bd``)
      - ``borderwidth=3``
    * - ``class_``
      - A group name used to style many widgets at once (advanced). Written ``class_`` in Python
      - ``class_="Sidebar"``
    * - ``compound``
      - Where the picture goes compared to the words
      - ``compound="left"``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``font``
      - Style and size of the words
      - ``font=("Arial", 14)``
    * - ``foreground``
      - Word colour (write ``foreground``, not ``fg``)
      - ``foreground="purple"``
    * - ``image``
      - Shows a picture instead of (or with) the words
      - ``image=dog_picture``
    * - ``justify``
      - Lines up many lines of words: ``"left"``, ``"center"`` or ``"right"``
      - ``justify="left"``
    * - ``padding``
      - Extra space inside it, around the words (one number, or left, top, right, bottom)
      - ``padding=10``
    * - ``relief``
      - Border style: ``"raised"``, ``"sunken"``, ``"flat"``, ``"ridge"``, ``"groove"`` or ``"solid"``
      - ``relief="sunken"``
    * - ``state``
      - ``"normal"`` or ``"disabled"`` (greyed out)
      - ``state="disabled"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TLabel"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``text``
      - Words shown on the label
      - ``text="Hello"``
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

| The ``image`` option needs a picture made first, e.g. ``dog_picture = tk.PhotoImage(file="dog.png")``.

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

        How is a ttk Label made?

        [x] ttk.Label(root, text="Hello") | Correct. It works like a tk Label.
        [ ] tk.Label(root, ttk=True) | Incorrect. Not an option.
        [ ] ttk.label(root) | Incorrect. Needs a capital L.
        [ ] ttk.Text(root) | Incorrect. Not a ttk widget.

    .. multichoice::

        Which option sets the words?

        [ ] label | Incorrect. Not an option.
        [x] text | Correct. text sets the words.
        [ ] words | Incorrect. Not an option.
        [ ] value | Incorrect. Not an option.

    .. multichoice::

        Which option colours the words of a ttk Label?

        [ ] fg | Incorrect. ttk uses the full word foreground.
        [x] foreground | Correct. foreground is the word colour.
        [ ] colour | Incorrect. Not an option.
        [ ] textcolour | Incorrect. Not an option.

    .. multichoice::

        Which option colours the background of a ttk Label?

        [x] background | Correct. ttk Labels have background.
        [ ] bg | Incorrect. Use the full word.
        [ ] fill | Incorrect. Not an option.
        [ ] back | Incorrect. Not an option.

    .. multichoice::

        What does font=("Arial", 18, "bold") do?

        [ ] Colours the text | Incorrect. foreground does that.
        [x] Makes the words bold Arial, size 18 | Correct. Name, size, style.
        [ ] Makes it 18 wide | Incorrect. width does that.
        [ ] Makes it italic | Incorrect. "italic" would.

    .. multichoice::

        What does width=20 mean?

        [ ] 20 pixels | Incorrect. It counts characters.
        [x] About 20 characters wide | Correct. Text labels count characters.
        [ ] 20 lines | Incorrect. Not lines.
        [ ] 20 labels | Incorrect. One label.

    .. multichoice::

        What does padding=10 do?

        [x] Adds space inside the label around the words | Correct. padding makes it bigger.
        [ ] Moves the label | Incorrect. pack moves it.
        [ ] Changes the font | Incorrect. font does that.
        [ ] Adds a border | Incorrect. relief does that.

    .. multichoice::

        What does anchor="e" do in a wide label?

        [ ] Puts the words on the left | Incorrect. That is "w".
        [x] Puts the words on the right | Correct. e is east, the right.
        [ ] Puts the words at the top | Incorrect. That is "n".
        [ ] Hides the words | Incorrect. It moves them.

    .. multichoice::

        What does relief="solid" with borderwidth=1 do?

        [x] Draws a thin plain line around the label | Correct. solid makes a simple border.
        [ ] Makes the words solid | Incorrect. It is the border.
        [ ] Hides the border | Incorrect. flat would.
        [ ] Makes it 1 character wide | Incorrect. width does that.

    .. multichoice::

        What does wraplength=200 do?

        [ ] Makes it 200 characters wide | Incorrect. width does that.
        [x] Starts a new line when the words reach 200 pixels | Correct. It wraps long text.
        [ ] Shows 200 letters | Incorrect. All letters show.
        [ ] Sets the font size | Incorrect. font does that.

    .. multichoice::

        What does justify="center" do?

        [x] Centres each line of wrapped text | Correct. justify lines up lines.
        [ ] Centres the label in the window | Incorrect. pack does that.
        [ ] Wraps the text | Incorrect. wraplength does that.
        [ ] Makes it bold | Incorrect. font does that.

    .. multichoice::

        What does compound="top" do with an image?

        [ ] Puts the label at the top | Incorrect. It places the picture.
        [x] Shows the picture above the words | Correct. compound places the image.
        [ ] Hides the words | Incorrect. Both show.
        [ ] Hides the picture | Incorrect. Both show.

    .. multichoice::

        What must be made before showing a picture?

        [ ] A Canvas | Incorrect. Not needed.
        [x] A PhotoImage, e.g. tk.PhotoImage(file="cat.png") | Correct. Then use image=picture.
        [ ] A Frame | Incorrect. Not needed.
        [ ] A Button | Incorrect. Not needed.

    .. multichoice::

        What does textvariable=message do?

        [x] Links the label to a StringVar, so message.set() changes the words | Correct. It updates by itself.
        [ ] Sets the font | Incorrect. font does that.
        [ ] Names the label | Incorrect. It links a variable.
        [ ] Hides the label | Incorrect. It does not hide it.

    .. multichoice::

        Which line changes the text later?

        [ ] result_label.text = "Done" | Incorrect. Use config.
        [x] result_label.config(text="Done") | Correct. config changes options.
        [ ] result_label.set("Done") | Incorrect. Labels have no set.
        [ ] result_label.cget(text="Done") | Incorrect. cget reads.

    .. multichoice::

        What does result_label.cget("foreground") give?

        [x] The current word colour | Correct. cget reads an option.
        [ ] It changes the colour | Incorrect. config changes it.
        [ ] The text | Incorrect. It reads foreground.
        [ ] An error | Incorrect. It works.

    .. multichoice::

        Which style name changes every ttk Label?

        [ ] "Label" | Incorrect. Use TLabel.
        [x] "TLabel" | Correct. T then the widget name.
        [ ] "TText" | Incorrect. Not the name.
        [ ] "ttk.Label" | Incorrect. Not a style name.

    .. multichoice::

        How do you make every label size 14 Arial?

        [x] style.configure("TLabel", font=("Arial", 14)) | Correct. TLabel changes them all.
        [ ] root.config(font=14) | Incorrect. Not how it works.
        [ ] label.font(14) | Incorrect. Not a method.
        [ ] style.font("TLabel", 14) | Incorrect. Not a method.

    .. multichoice::

        Can the user type into a ttk Label?

        [ ] Yes | Incorrect. Labels only show text.
        [x] No | Correct. Use an Entry to type.
        [ ] Only with textvariable | Incorrect. Still no.
        [ ] Only with padding | Incorrect. Still no.

    .. multichoice::

        Which anchor value puts the words in the middle?

        [ ] "middle" | Incorrect. Not a value.
        [x] "center" | Correct. center is the middle.
        [ ] "c" | Incorrect. Use "center".
        [ ] "m" | Incorrect. Not a value.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a ttk Label with coloured words.

        title_label = ttk.@@Label | Entry | Button@@(root, text="Quiz", font=("Arial", 24), @@foreground | fg | colour@@="blue")
        title_label.pack()

    .. cloze::
        :instructions: Add a background, space and a border.

        info = ttk.Label(root, text="Info", @@background | bg | fill@@="lightyellow", @@padding | padx | space@@=10, relief="solid", borderwidth=1)

    .. cloze::
        :instructions: Wrap long text.

        long_label = ttk.Label(root, text=long_text, @@wraplength | width | wrap@@=200, justify="@@left | west | w@@")

    .. cloze::
        :instructions: Show a picture with words under it.

        cat_picture = tk.@@PhotoImage | Image | Picture@@(file="cat.png")
        cat_label = ttk.Label(root, text="Cat", image=cat_picture, @@compound | anchor | side@@="top")

    .. cloze::
        :instructions: Change and read the label.

        result_label.@@config | cget | set@@(text="Correct!")
        colour = result_label.@@cget | config | get@@("foreground")

----

.. admonition:: Tasks

    #. Make a window titled "About me" that is 300x200. Add a ttk Label showing your name in Arial size 24 with white words on a purple background.
    #. Add a second ttk Label with a solid border, a borderwidth of 2 and padding of 10 showing your favourite food.
    #. Make a ``"Heading.TLabel"`` style with Arial size 20 bold, dark green words. Use it on a label "Science" and add a normal label below it.
    #. Make a label showing "1" and a ttk Button "Double". When clicked, use ``cget`` and ``config`` to double the number.

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
                    root.title("About me")

                    ttk.Label(root, text="Sam", font=("Arial", 24), foreground="white",
                              background="purple").pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("About me")

                    ttk.Label(root, text="Sam", font=("Arial", 24), foreground="white",
                              background="purple").pack(pady=10)
                    ttk.Label(root, text="Pizza", relief="solid", borderwidth=2,
                              padding=10).pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Heading")

                    style = ttk.Style()
                    style.configure("Heading.TLabel", font=("Arial", 20, "bold"), foreground="darkgreen")

                    ttk.Label(root, text="Science", style="Heading.TLabel").pack(pady=10)
                    ttk.Label(root, text="Chapter 1: Cells").pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def double():
                        number = int(number_label.cget("text"))
                        number_label.config(text=number * 2)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Double")

                    number_label = ttk.Label(root, text="1", font=("Arial", 36))
                    number_label.pack(pady=10)

                    ttk.Button(root, text="Double", command=double).pack()

                    root.mainloop()
