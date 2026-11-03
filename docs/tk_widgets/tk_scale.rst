====================================================
tk Scale
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Scale>`_

----

What is a Scale?
-------------------

| A **Scale** is a slider. The user drags it to choose a number.
| Use a scale when the user picks a number in a range, e.g. a volume from 0 to 100 or a rating from 1 to 10.

----

Making a Scale
-------------------

| Every Scale is made in two steps:

#. **Create** the scale with ``tk.Scale(...)``. Give it the lowest number (``from_``) and the highest number (``to``).
#. **Place** the scale in the window with ``.pack()``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first scale")    # Words in the title bar

    volume_scale = tk.Scale(root, from_=0, to=100)  # 1. Create the scale
    volume_scale.pack()                             # 2. Place it in the window

    root.mainloop()                 # Keep the window open

| ``from_`` has an underscore at the end. ``from`` on its own is a special Python word, so Tkinter uses ``from_`` instead.

----

Scale options
-------------------

| Options are written as ``option=value`` inside ``tk.Scale( )``, separated by commas.

from\_ and to
~~~~~~~~~~~~~~~~~~

| **What they do:** set the number at each end of the slider.
| **How to write them:** ``from_=1, to=10``
| On an up-and-down slider, ``from_`` is at the top. Make ``from_`` bigger than ``to`` to put the big number at the top.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("from_ and to")

    rating_scale = tk.Scale(root, from_=10, to=1)    # 10 at the top, 1 at the bottom
    rating_scale.pack()

    root.mainloop()

orient
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses whether the slider goes up-and-down or side-to-side.
| **How to write it:** ``orient="horizontal"``
| **Values:** ``"vertical"`` (the default) and ``"horizontal"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("orient")

    speed_scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
    speed_scale.pack(pady=20)

    root.mainloop()

length
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how long the slider is, in pixels.
| **How to write it:** ``length=250``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("length")

    long_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=250)
    long_scale.pack(pady=20)

    root.mainloop()

label
~~~~~~~~~~~~~~~~~~

| **What it does:** puts a title on the scale.
| **How to write it:** ``label="your words"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("label")

    volume_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200,
                            label="Volume")
    volume_scale.pack(pady=20)

    root.mainloop()

resolution
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how much the number goes up by each step.
| **How to write it:** ``resolution=5`` (counts 0, 5, 10, 15 ...) or ``resolution=0.1`` (counts 0.0, 0.1, 0.2 ...)
| The default is ``1``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("resolution")

    fives_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200,
                           resolution=5, label="Steps of 5")
    fives_scale.pack(pady=5)

    tenths_scale = tk.Scale(root, from_=0, to=1, orient="horizontal", length=200,
                            resolution=0.1, label="Steps of 0.1")
    tenths_scale.pack(pady=5)

    root.mainloop()

tickinterval
~~~~~~~~~~~~~~~~~~

| **What it does:** shows numbers along the slider, like the markings on a ruler.
| **How to write it:** ``tickinterval=10`` shows 0, 10, 20 ...

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("tickinterval")

    temp_scale = tk.Scale(root, from_=0, to=40, orient="horizontal", length=250,
                          tickinterval=10, label="Temperature")
    temp_scale.pack(pady=20)

    root.mainloop()

command
~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function **every time** the slider moves.
| **How to write it:** ``command=function_name`` (no brackets)
| The scale sends its new value to the function, so the function needs a **parameter** to receive it.
| The value arrives as a **string**, so use ``int()`` or ``float()`` to turn it into a number.

.. code-block:: python

    import tkinter as tk


    def show_size(value):
        size = int(value)                           # Text -> number
        word_label.config(font=("Arial", size))


    root = tk.Tk()
    root.geometry("300x250")
    root.title("command")

    size_scale = tk.Scale(root, from_=8, to=40, orient="horizontal", length=200,
                          label="Text size", command=show_size)
    size_scale.pack()

    word_label = tk.Label(root, text="Hello", font=("Arial", 8))
    word_label.pack(pady=10)

    root.mainloop()

variable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the scale to a Tkinter variable. Moving the slider changes the variable, and changing the variable moves the slider.
| **How to write it:** ``score = tk.IntVar()`` then ``variable=score``
| Use ``tk.DoubleVar()`` instead if the scale uses decimals.

.. code-block:: python

    import tkinter as tk


    def show():
        result_label.config(text=f"You chose {score.get()}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("variable")

    score = tk.IntVar(value=5)

    score_scale = tk.Scale(root, from_=1, to=10, orient="horizontal", variable=score)
    score_scale.pack()

    show_button = tk.Button(root, text="Show", command=show)
    show_button.pack(pady=5)

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

Colours and size options
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:**
| ``bg`` sets the colour of the slider handle and background. ``fg`` sets the colour of the numbers.
| ``troughcolor`` sets the colour of the track the slider moves along.
| ``width`` sets how thick the track is, and ``sliderlength`` sets how long the handle is (both in pixels).
| ``showvalue=0`` hides the number above the handle.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("colours")

    fancy_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=250,
                           bg="orange", fg="navy", troughcolor="lightyellow",
                           width=25, sliderlength=40)
    fancy_scale.pack(pady=10)

    hidden_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=250,
                            showvalue=0)
    hidden_scale.pack(pady=10)

    root.mainloop()

----

Scale methods
-------------------

| A **method** is an action that a widget can do. Methods are written after a dot, e.g. ``scale.get()``.

get
~~~~~~~~~~~~~~~~~~

| **What it does:** reads the number the slider is on.
| **How to write it:** ``number = scale.get()``
| ``get()`` gives back a number (not text), so it can be used in maths straight away.

.. code-block:: python

    import tkinter as tk


    def convert():
        celsius = temp_scale.get()
        fahrenheit = celsius * 9 / 5 + 32
        result_label.config(text=f"{celsius} °C = {fahrenheit} °F")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("get")

    temp_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200, label="°C")
    temp_scale.pack()

    convert_button = tk.Button(root, text="Convert", command=convert)
    convert_button.pack(pady=5)

    result_label = tk.Label(root, text="", font=("Arial", 14))
    result_label.pack()

    root.mainloop()

set
~~~~~~~~~~~~~~~~~~

| **What it does:** moves the slider to a number from your code.
| **How to write it:** ``scale.set(50)``

.. code-block:: python

    import tkinter as tk


    def reset():
        volume_scale.set(50)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("set")

    volume_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200)
    volume_scale.set(50)        # Start in the middle
    volume_scale.pack()

    reset_button = tk.Button(root, text="Reset to 50", command=reset)
    reset_button.pack(pady=10)

    root.mainloop()

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options **after** the scale has been made.
| **How to write it:** ``scale.config(option=value)``

.. code-block:: python

    import tkinter as tk


    def hard_mode():
        level_scale.config(to=20, troughcolor="red")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    level_scale = tk.Scale(root, from_=1, to=10, orient="horizontal", length=200, label="Level")
    level_scale.pack()

    hard_button = tk.Button(root, text="Hard mode", command=hard_mode)
    hard_button.pack(pady=10)

    root.mainloop()

Colour mixer example
~~~~~~~~~~~~~~~~~~~~~~~~

| Three scales control the red, green and blue in a colour.
| ``f"#{red:02x}{green:02x}{blue:02x}"`` turns the three numbers into a hex colour code like ``"#ff8000"``.

.. code-block:: python

    import tkinter as tk


    def mix(value):
        red = red_scale.get()
        green = green_scale.get()
        blue = blue_scale.get()
        colour = f"#{red:02x}{green:02x}{blue:02x}"
        colour_label.config(bg=colour, text=colour)


    root = tk.Tk()
    root.geometry("300x300")
    root.title("Colour mixer")

    red_scale = tk.Scale(root, from_=0, to=255, orient="horizontal", length=250,
                         label="Red", troughcolor="red", command=mix)
    red_scale.pack()
    green_scale = tk.Scale(root, from_=0, to=255, orient="horizontal", length=250,
                           label="Green", troughcolor="green", command=mix)
    green_scale.pack()
    blue_scale = tk.Scale(root, from_=0, to=255, orient="horizontal", length=250,
                          label="Blue", troughcolor="blue", command=mix)
    blue_scale.pack()

    colour_label = tk.Label(root, text="#000000", bg="#000000", fg="white", width=20, height=2)
    colour_label.pack(pady=10)

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
      - Numbers at each end
      - ``from_=0, to=100``
    * - ``orient``
      - Up-and-down or side-to-side
      - ``orient="horizontal"``
    * - ``length``
      - Length in pixels
      - ``length=250``
    * - ``label``
      - Title on the scale
      - ``label="Volume"``
    * - ``resolution``
      - Size of each step
      - ``resolution=5``
    * - ``tickinterval``
      - Numbers along the slider
      - ``tickinterval=10``
    * - ``command``
      - Function to run when it moves
      - ``command=update``
    * - ``variable``
      - Link to an IntVar or DoubleVar
      - ``variable=score``
    * - ``bg``, ``fg``, ``troughcolor``
      - Colours
      - ``troughcolor="lightyellow"``
    * - ``width``, ``sliderlength``
      - Track thickness, handle length
      - ``width=25, sliderlength=40``
    * - ``showvalue``
      - ``0`` hides the number
      - ``showvalue=0``
    * - ``get()``
      - Read the number
      - ``scale.get()``
    * - ``set()``
      - Move the slider
      - ``scale.set(50)``
    * - ``config()``
      - Change options later
      - ``scale.config(to=20)``

----

All Scale options
---------------------------

| Here is every option a Scale can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``activebackground``
      - Colour of the slider when the mouse is over it
      - ``activebackground="lightblue"``
    * - ``bg`` or ``background``
      - Background colour
      - ``bg="lavender"``
    * - ``bigincrement``
      - How far the slider jumps when you press Ctrl and an arrow key
      - ``bigincrement=10``
    * - ``bd`` or ``borderwidth``
      - How thick the border is
      - ``bd=3``
    * - ``command``
      - Function to run when the slider moves (it is given the new value)
      - ``command=update``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``digits``
      - How many digits to show in the value
      - ``digits=3``
    * - ``font``
      - Style and size of the numbers and label
      - ``font=("Arial", 12)``
    * - ``fg`` or ``foreground``
      - Colour of the numbers and label
      - ``fg="purple"``
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
    * - ``label``
      - Words shown above the slider
      - ``label="Volume"``
    * - ``length``
      - How long the slider is (in pixels)
      - ``length=200``
    * - ``orient``
      - Which way it goes: ``"horizontal"`` or ``"vertical"``
      - ``orient="horizontal"``
    * - ``relief``
      - Border style: ``"raised"``, ``"sunken"``, ``"flat"``, ``"ridge"``, ``"groove"`` or ``"solid"``
      - ``relief="sunken"``
    * - ``repeatdelay``
      - How long to hold the mouse in the track before the slider starts moving (milliseconds)
      - ``repeatdelay=500``
    * - ``repeatinterval``
      - How often the slider moves while the mouse is held in the track (milliseconds)
      - ``repeatinterval=100``
    * - ``resolution``
      - Size of each step (``0.5`` = halves)
      - ``resolution=0.5``
    * - ``showvalue``
      - ``False`` hides the number above the slider
      - ``showvalue=False``
    * - ``sliderlength``
      - How long the slider block is (in pixels)
      - ``sliderlength=40``
    * - ``sliderrelief``
      - Border style of the slider block
      - ``sliderrelief="flat"``
    * - ``state``
      - ``"normal"`` (can click), ``"active"`` or ``"disabled"`` (greyed out)
      - ``state="disabled"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``tickinterval``
      - Puts numbered marks along the slider this far apart
      - ``tickinterval=10``
    * - ``to``
      - Highest number
      - ``to=100``
    * - ``troughcolor``
      - Colour of the track the slider moves along
      - ``troughcolor="lightgrey"``
    * - ``variable``
      - A variable that holds the slider's number
      - ``variable=volume``
    * - ``width``
      - How thick the slider track is (in pixels)
      - ``width=20``

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

        What is a Scale?

        [x] A slider for picking a number | Correct. Drag it to choose a value.
        [ ] A box for typing numbers | Incorrect. That is an Entry or Spinbox.
        [ ] A weighing machine | Incorrect. Here it is a slider.
        [ ] A list | Incorrect. That is a Listbox.

    .. multichoice::

        How is the lowest number written?

        [ ] from=0 | Incorrect. from is a Python keyword.
        [x] from_=0 | Correct. The underscore is needed.
        [ ] start=0 | Incorrect. Not an option.
        [ ] low=0 | Incorrect. Not an option.

    .. multichoice::

        What does to=100 set?

        [x] The highest number | Correct. to is the top of the range.
        [ ] The lowest number | Incorrect. from\_ does that.
        [ ] The step size | Incorrect. resolution does that.
        [ ] The length | Incorrect. length does that.

    .. multichoice::

        What is the default orient for a tk Scale?

        [ ] "horizontal" | Incorrect. The default is vertical.
        [x] "vertical" | Correct. tk Scales stand up by default.
        [ ] "both" | Incorrect. Not a value.
        [ ] "none" | Incorrect. Not a value.

    .. multichoice::

        What does length=300 do?

        [ ] Sets the highest number | Incorrect. to does that.
        [x] Makes the slider 300 pixels long | Correct. length sets its size.
        [ ] Sets 300 steps | Incorrect. resolution sets steps.
        [ ] Makes it 300 thick | Incorrect. width sets thickness.

    .. multichoice::

        What does label="Volume" do?

        [x] Shows Volume above the slider | Correct. label adds a title.
        [ ] Sets the value | Incorrect. It adds words.
        [ ] Makes a Label widget | Incorrect. It is part of the Scale.
        [ ] Changes the font | Incorrect. font does that.

    .. multichoice::

        What does resolution=0.5 do?

        [ ] Moves in steps of 5 | Incorrect. It moves in steps of 0.5.
        [x] Lets the slider move in steps of 0.5 | Correct. resolution is the step size.
        [ ] Makes it half the size | Incorrect. It is the step.
        [ ] Shows half the numbers | Incorrect. It sets the step.

    .. multichoice::

        What does tickinterval=10 do?

        [ ] Moves 10 at a time | Incorrect. resolution does that.
        [x] Shows numbers along the slider every 10 | Correct. Tick marks label the scale.
        [ ] Makes it 10 long | Incorrect. length does that.
        [ ] Sets the highest number to 10 | Incorrect. to does that.

    .. multichoice::

        What does the command function receive?

        [x] The new value, so it needs a parameter | Correct. e.g. def update(value):
        [ ] Nothing | Incorrect. It gets the value.
        [ ] The Scale | Incorrect. It gets the value.
        [ ] An event | Incorrect. It gets the value.

    .. multichoice::

        What type is the value sent to the command function?

        [ ] Always an int | Incorrect. It arrives as text.
        [x] A string, so use int() or float() | Correct. Change it to a number first.
        [ ] A list | Incorrect. It is one value.
        [ ] A Scale | Incorrect. It is the value.

    .. multichoice::

        What does variable=volume do?

        [ ] Sets the colour | Incorrect. Not related.
        [x] Links the slider to a variable, so volume.get() reads it | Correct. The variable updates as it moves.
        [ ] Names the slider | Incorrect. It links a variable.
        [ ] Sets the length | Incorrect. length does that.

    .. multichoice::

        What does troughcolor change?

        [x] The colour of the track the slider moves along | Correct. The trough is the track.
        [ ] The slider colour | Incorrect. bg colours the slider.
        [ ] The numbers | Incorrect. fg colours numbers.
        [ ] The window | Incorrect. Only the Scale.

    .. multichoice::

        What does showvalue=False do?

        [ ] Hides the slider | Incorrect. It hides the number.
        [x] Hides the number shown next to the slider | Correct. The slider still works.
        [ ] Sets the value to 0 | Incorrect. It hides the number.
        [ ] Stops it moving | Incorrect. state does that.

    .. multichoice::

        Which method reads where the slider is?

        [ ] scale.read() | Incorrect. Not a method.
        [x] scale.get() | Correct. get gives the value.
        [ ] scale.value | Incorrect. Not an attribute.
        [ ] scale.cget("value") | Incorrect. Not an option for tk Scale.

    .. multichoice::

        Which line moves the slider to 50 from code?

        [x] scale.set(50) | Correct. set moves the slider.
        [ ] scale.get(50) | Incorrect. get reads.
        [ ] scale.config(value=50) | Incorrect. tk Scale has no value option.
        [ ] scale.move(50) | Incorrect. Not a method.

    .. multichoice::

        Which line changes the highest number later?

        [ ] scale.to(20) | Incorrect. Not a method.
        [x] scale.config(to=20) | Correct. config changes options.
        [ ] scale.set(to=20) | Incorrect. set moves the slider.
        [ ] scale.max = 20 | Incorrect. Use config.

    .. multichoice::

        In a colour mixer with three Scales, what are their from\_ and to?

        [x] 0 and 255 | Correct. Each colour part goes from 0 to 255.
        [ ] 0 and 100 | Incorrect. Colours use 0 to 255.
        [ ] 1 and 10 | Incorrect. Too small.
        [ ] 0 and 1000 | Incorrect. Too big.

    .. multichoice::

        What does sliderlength=40 do?

        [ ] Makes the whole Scale 40 long | Incorrect. length does that.
        [x] Makes the slider block 40 pixels long | Correct. It sizes the block you drag.
        [ ] Moves it 40 | Incorrect. set moves it.
        [ ] Shows 40 ticks | Incorrect. tickinterval does that.

    .. multichoice::

        Which orient makes the slider go left to right?

        [ ] "vertical" | Incorrect. That goes up and down.
        [x] "horizontal" | Correct. horizontal goes left to right.
        [ ] "across" | Incorrect. Not a value.
        [ ] "x" | Incorrect. Not a value.

    .. multichoice::

        What does digits=3 do?

        [ ] Allows 3 sliders | Incorrect. It sets how numbers show.
        [x] Shows the value with 3 digits | Correct. It controls the number display.
        [ ] Sets the highest number to 3 | Incorrect. to does that.
        [ ] Moves in steps of 3 | Incorrect. resolution does that.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a horizontal slider from 0 to 100.

        volume_scale = tk.@@Scale | Spinbox | Entry@@(root, @@from_ | from | start@@=0, @@to | end | max@@=100, orient="horizontal")
        volume_scale.pack()

    .. cloze::
        :instructions: Add a title, length and number marks.

        volume_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", @@label | title | text@@="Volume", @@length | width | size@@=300, tickinterval=25)

    .. cloze::
        :instructions: Move in halves.

        size_scale = tk.Scale(root, from_=0, to=10, @@resolution | step | increment@@=0.5)

    .. cloze::
        :instructions: Run a function as the slider moves.

        def update(@@value | self | event@@):
            result_label.config(text="Volume: " + value)

        volume_scale = tk.Scale(root, from_=0, to=100, @@command | click | run@@=update)

    .. cloze::
        :instructions: Read and set the slider.

        level = volume_scale.@@get | set | read@@()
        volume_scale.@@set | get | move@@(50)

----

.. admonition:: Tasks

    #. Make a window titled "Rating" that is 300x200. Add a horizontal scale from 1 to 10 that is 250 pixels long with the label "Rate this movie".
    #. Make the scale start on 5 and show the numbers 1 to 10 along it using ``tickinterval``.
    #. Make a horizontal scale from 0 to 100 and a label. Use ``command`` so the label shows "Volume:" and the number every time the slider moves.
    #. Make a scale from 1 to 12 and a button "Times table". When clicked, a label shows the number from the scale multiplied by 7.

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
                    root.title("Rating")

                    rating_scale = tk.Scale(root, from_=1, to=10, orient="horizontal",
                                            length=250, label="Rate this movie")
                    rating_scale.pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Rating")

                    rating_scale = tk.Scale(root, from_=1, to=10, orient="horizontal",
                                            length=250, label="Rate this movie", tickinterval=1)
                    rating_scale.set(5)
                    rating_scale.pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk


                    def show_volume(value):
                        volume_label.config(text="Volume: " + value)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Volume")

                    volume_scale = tk.Scale(root, from_=0, to=100, orient="horizontal",
                                            length=250, command=show_volume)
                    volume_scale.pack()

                    volume_label = tk.Label(root, text="Volume: 0", font=("Arial", 14))
                    volume_label.pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def times_table():
                        number = number_scale.get()
                        answer_label.config(text=f"{number} x 7 = {number * 7}")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Times table")

                    number_scale = tk.Scale(root, from_=1, to=12, orient="horizontal", length=250)
                    number_scale.pack()

                    table_button = tk.Button(root, text="Times table", command=times_table)
                    table_button.pack(pady=5)

                    answer_label = tk.Label(root, text="", font=("Arial", 14))
                    answer_label.pack()

                    root.mainloop()
