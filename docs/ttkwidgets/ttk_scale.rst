====================================================
ttk Scale
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk Scale?
-----------------------

| A **ttk Scale** is a slider the user drags to choose a number, like a tk Scale.
| It looks more modern but is **simpler**:

- It does **not** show the number. Use a Label to show it.
- It has no ``label``, ``resolution``, ``tickinterval`` or ``showvalue`` options.
- Its value is a **decimal** (e.g. ``42.7``), so use ``int()`` or ``round()`` to get a whole number.

----

Making a ttk Scale
---------------------

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk Scale")

    volume_scale = ttk.Scale(root, from_=0, to=100, length=250)    # 1. Create it
    volume_scale.pack(pady=40)                                     # 2. Place it

    root.mainloop()                 # Keep the window open

| ``from_`` has an underscore at the end, because ``from`` is a special Python word.

----

ttk Scale options
--------------------

from\_ and to
~~~~~~~~~~~~~~~~~~

| **What they do:** set the number at each end of the slider.
| **How to write them:** ``from_=1, to=10``

orient and length
~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``orient`` chooses ``"horizontal"`` (side to side, the default) or ``"vertical"``. ``length`` sets how long it is in pixels.
| **How to write them:** ``orient="vertical", length=150``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("orient and length")

    ttk.Scale(root, from_=0, to=100, orient="horizontal", length=200).pack(pady=10)
    ttk.Scale(root, from_=100, to=0, orient="vertical", length=120).pack()

    root.mainloop()

| On a vertical scale, ``from_`` is at the top. ``from_=100, to=0`` puts 100 at the top.

value
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the starting position of the slider.
| **How to write it:** ``value=50``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("value")

    ttk.Scale(root, from_=0, to=100, length=250, value=50).pack(pady=40)

    root.mainloop()

command
~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function every time the slider moves.
| The scale sends its value to the function as a **string** such as ``"42.7"``, so the function needs a parameter. Use ``float()`` then ``int()`` (or ``round()``).
| **How to write it:** ``command=function_name``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def show_value(value):
        number = int(float(value))          # "42.7" -> 42.7 -> 42
        value_label.config(text=f"Volume: {number}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("command")

    ttk.Scale(root, from_=0, to=100, length=250, command=show_value).pack(pady=20)

    value_label = ttk.Label(root, text="Volume: 0", font=("Arial", 16))
    value_label.pack()

    root.mainloop()

variable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the scale to a Tkinter variable. Moving the slider changes the variable, and changing the variable with ``.set()`` moves the slider.
| A ttk Scale stores **decimals**, so use a ``tk.DoubleVar()`` and ``round()`` the value when you show it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def show(value):
        number_label.config(text=round(rating.get()))


    root = tk.Tk()
    root.geometry("300x200")
    root.title("variable")

    rating = tk.DoubleVar(value=5)

    ttk.Scale(root, from_=1, to=10, length=250, variable=rating, command=show).pack(pady=20)

    number_label = ttk.Label(root, text="5", font=("Arial", 30))
    number_label.pack()

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** turns the scale off or on.
| **How to write it:** ``scale.state(["disabled"])`` and ``scale.state(["!disabled"])``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def lock():
        speed_scale.state(["disabled"])


    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    speed_scale = ttk.Scale(root, from_=0, to=100, length=250)
    speed_scale.pack(pady=20)

    ttk.Button(root, text="Lock", command=lock).pack()

    root.mainloop()

----

ttk Scale methods
--------------------

get
~~~~~~~~~~~~~~~~~~

| **What it does:** reads the slider's value, as a decimal number.
| **How to write it:** ``number = round(scale.get())``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def convert():
        celsius = round(temp_scale.get())
        fahrenheit = celsius * 9 / 5 + 32
        result_label.config(text=f"{celsius} °C = {fahrenheit} °F")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("get")

    temp_scale = ttk.Scale(root, from_=0, to=100, length=250)
    temp_scale.pack(pady=20)

    ttk.Button(root, text="Convert", command=convert).pack()

    result_label = ttk.Label(root, text="", font=("Arial", 14))
    result_label.pack(pady=10)

    root.mainloop()

set
~~~~~~~~~~~~~~~~~~

| **What it does:** moves the slider to a number from code.
| **How to write it:** ``scale.set(50)``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("set")

    volume_scale = ttk.Scale(root, from_=0, to=100, length=250)
    volume_scale.pack(pady=20)

    for amount in [0, 50, 100]:
        ttk.Button(root, text=f"Set to {amount}",
                   command=lambda amount=amount: volume_scale.set(amount)).pack(pady=2)

    root.mainloop()

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options after the scale has been made.
| **How to write it:** ``scale.config(to=20)``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def hard_mode():
        level_scale.config(to=20)
        info_label.config(text="Levels 1 to 20")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    level_scale = ttk.Scale(root, from_=1, to=10, length=250)
    level_scale.pack(pady=20)

    info_label = ttk.Label(root, text="Levels 1 to 10")
    info_label.pack()

    ttk.Button(root, text="Hard mode", command=hard_mode).pack(pady=10)

    root.mainloop()

Colour mixer example
~~~~~~~~~~~~~~~~~~~~~~~

| Three scales control the red, green and blue of a colour. ``f"#{red:02x}{green:02x}{blue:02x}"`` makes a hex colour code.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def mix(value):
        red = int(red_scale.get())
        green = int(green_scale.get())
        blue = int(blue_scale.get())
        colour = f"#{red:02x}{green:02x}{blue:02x}"
        colour_label.config(background=colour, text=colour)


    root = tk.Tk()
    root.geometry("300x260")
    root.title("Colour mixer")

    ttk.Label(root, text="Red").pack()
    red_scale = ttk.Scale(root, from_=0, to=255, length=250, command=mix)
    red_scale.pack()

    ttk.Label(root, text="Green").pack()
    green_scale = ttk.Scale(root, from_=0, to=255, length=250, command=mix)
    green_scale.pack()

    ttk.Label(root, text="Blue").pack()
    blue_scale = ttk.Scale(root, from_=0, to=255, length=250, command=mix)
    blue_scale.pack()

    colour_label = ttk.Label(root, text="#000000", background="#000000", foreground="white",
                             width=20, anchor="center", padding=10)
    colour_label.pack(pady=10)

    root.mainloop()

----

Styling a ttk Scale
----------------------

| The style is ``"Horizontal.TScale"`` (or ``"Vertical.TScale"``). With the ``"clam"`` theme:

- ``troughcolor`` - colour of the track
- ``background`` - colour of the handle
- ``sliderlength`` - length of the handle in pixels

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Scale style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Horizontal.TScale", troughcolor="lightyellow", background="orange",
                    sliderlength=40)
    style.configure("Blue.Horizontal.TScale", troughcolor="lightblue", background="navy")

    ttk.Scale(root, from_=0, to=100, length=250).pack(pady=20)
    ttk.Scale(root, from_=0, to=100, length=250, style="Blue.Horizontal.TScale").pack()

    root.mainloop()

| For your own style, put a name in front: ``"Blue.Horizontal.TScale"``.

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
      - Side to side or up and down
      - ``orient="vertical"``
    * - ``length``
      - Length in pixels
      - ``length=250``
    * - ``value``
      - Starting value
      - ``value=50``
    * - ``command``
      - Function to run when it moves
      - ``command=update``
    * - ``variable``
      - Link to a DoubleVar
      - ``variable=rating``
    * - ``state()``
      - Turn on or off
      - ``scale.state(["disabled"])``
    * - ``get()``
      - Read the value (a decimal)
      - ``round(scale.get())``
    * - ``set()``
      - Move the slider
      - ``scale.set(50)``
    * - ``config()``
      - Change options later
      - ``scale.config(to=20)``
    * - ``"Horizontal.TScale"``
      - Style name
      - ``style.configure("Horizontal.TScale", troughcolor="pink")``

----

All Scale options
---------------------------

| Here is every option a ttk Scale can have, for reference. You will only need a few of them most of the time.

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
      - Function to run when the slider moves (it is given the new value)
      - ``command=update``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``from_``
      - Lowest number. Written ``from_`` in Python
      - ``from_=0``
    * - ``length``
      - How long the slider is (in pixels)
      - ``length=200``
    * - ``orient``
      - Which way it goes: ``"horizontal"`` or ``"vertical"``
      - ``orient="horizontal"``
    * - ``state``
      - ``"normal"`` or ``"disabled"`` (greyed out)
      - ``state="disabled"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.TScale"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``to``
      - Highest number
      - ``to=100``
    * - ``value``
      - Where the slider is right now
      - ``value=50``
    * - ``variable``
      - A variable that holds the slider's number
      - ``variable=volume``

| ttk Scale has no ``bg``, ``fg`` or ``font`` options. Change its colours and fonts with a style, e.g. ``style.configure("Horizontal.TScale", background="lightblue")``.

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

        What is a ttk Scale?

        [x] A themed slider for picking a number | Correct. Drag it to choose a value.
        [ ] A box for typing numbers | Incorrect. That is an Entry or Spinbox.
        [ ] A progress bar | Incorrect. That shows progress.
        [ ] A list | Incorrect. That is a Listbox.

    .. multichoice::

        How is the lowest number written?

        [ ] from=0 | Incorrect. from is a Python keyword.
        [x] from_=0 | Correct. The underscore is needed.
        [ ] min=0 | Incorrect. Not an option.
        [ ] start=0 | Incorrect. Not an option.

    .. multichoice::

        What does to=100 set?

        [x] The highest number | Correct. to is the top of the range.
        [ ] The lowest number | Incorrect. from\_ does that.
        [ ] The length | Incorrect. length does that.
        [ ] The step | Incorrect. ttk Scale has no step option.

    .. multichoice::

        What is the default orient for ttk.Scale?

        [ ] "vertical" | Incorrect. ttk Scales are horizontal by default.
        [x] "horizontal" | Correct. They go left to right.
        [ ] "both" | Incorrect. Not a value.
        [ ] "none" | Incorrect. Not a value.

    .. multichoice::

        What does length=300 do?

        [x] Makes the slider 300 pixels long | Correct. length sets its size.
        [ ] Sets the highest number | Incorrect. to does that.
        [ ] Sets 300 steps | Incorrect. Not steps.
        [ ] Makes it 300 thick | Incorrect. Not thickness.

    .. multichoice::

        What does value=50 do?

        [ ] Sets the highest number to 50 | Incorrect. to does that.
        [x] Starts the slider at 50 | Correct. value is where the slider is.
        [ ] Moves it by 50 | Incorrect. It sets the position.
        [ ] Shows 50 ticks | Incorrect. ttk Scale has no ticks.

    .. multichoice::

        What does the command function receive?

        [x] The new value as a string, so it needs a parameter | Correct. Use float() to make it a number.
        [ ] Nothing | Incorrect. It gets the value.
        [ ] The Scale | Incorrect. It gets the value.
        [ ] An event | Incorrect. It gets the value.

    .. multichoice::

        Why does a ttk Scale often give values like 42.3786?

        [ ] It is broken | Incorrect. It is normal.
        [x] It moves smoothly with decimals, so round() or int() is often used | Correct. ttk Scale has no resolution option.
        [ ] Because of length | Incorrect. Not related.
        [ ] Because of the style | Incorrect. Not related.

    .. multichoice::

        What does variable=volume do?

        [ ] Sets the colour | Incorrect. A style does that.
        [x] Links the slider to a variable, so volume.get() reads it | Correct. The variable updates as it moves.
        [ ] Names the slider | Incorrect. It links a variable.
        [ ] Sets the length | Incorrect. length does that.

    .. multichoice::

        Which line greys out a ttk Scale?

        [x] scale.state(["disabled"]) | Correct. ttk uses the state method.
        [ ] scale.config(bg="grey") | Incorrect. ttk has no bg.
        [ ] scale.disable() | Incorrect. Not a method.
        [ ] scale.stop() | Incorrect. Not a method.

    .. multichoice::

        Which method reads the slider's value?

        [ ] scale.read() | Incorrect. Not a method.
        [x] scale.get() | Correct. get gives the value.
        [ ] scale.value | Incorrect. Not an attribute.
        [ ] scale.number() | Incorrect. Not a method.

    .. multichoice::

        Which line moves the slider to 25?

        [ ] scale.get(25) | Incorrect. get reads.
        [x] scale.set(25) | Correct. set moves the slider.
        [ ] scale.move(25) | Incorrect. Not a method.
        [ ] scale.to(25) | Incorrect. to is an option.

    .. multichoice::

        Which line changes the highest number later?

        [x] scale.config(to=20) | Correct. config changes options.
        [ ] scale.to(20) | Incorrect. Not a method.
        [ ] scale.set(to=20) | Incorrect. set moves the slider.
        [ ] scale.max = 20 | Incorrect. Use config.

    .. multichoice::

        Which tk Scale options are missing from ttk.Scale?

        [ ] from\_ and to | Incorrect. ttk has these.
        [x] label, tickinterval and resolution | Correct. Use a Label to show the value.
        [ ] length | Incorrect. ttk has length.
        [ ] orient | Incorrect. ttk has orient.

    .. multichoice::

        How can the number be shown next to a ttk Scale?

        [ ] showvalue=True | Incorrect. ttk Scale has no showvalue.
        [x] Use a Label and update it in the command function | Correct. The Label shows the number.
        [ ] label="Value" | Incorrect. ttk Scale has no label option.
        [ ] It shows by itself | Incorrect. It does not.

    .. multichoice::

        In a colour mixer, what range does each colour Scale use?

        [x] 0 to 255 | Correct. Each part of a colour goes from 0 to 255.
        [ ] 0 to 100 | Incorrect. Colours use 0 to 255.
        [ ] 1 to 10 | Incorrect. Too small.
        [ ] 0 to 1000 | Incorrect. Too big.

    .. multichoice::

        Which style name is used for a horizontal ttk Scale?

        [ ] "TScale" | Incorrect. It needs the direction.
        [x] "Horizontal.TScale" | Correct. The direction is part of the name.
        [ ] "Slider" | Incorrect. Not the name.
        [ ] "Scale" | Incorrect. Not the name.

    .. multichoice::

        How can a decimal like 42.7 be made a whole number?

        [ ] str(42.7) | Incorrect. That makes text.
        [x] int(42.7) or round(42.7) | Correct. int cuts to 42, round gives 43.
        [ ] float(42.7) | Incorrect. It is already a float.
        [ ] 42.7.whole | Incorrect. Not valid.

    .. multichoice::

        Which orient makes the slider go up and down?

        [x] "vertical" | Correct. vertical goes up and down.
        [ ] "horizontal" | Incorrect. That goes across.
        [ ] "up" | Incorrect. Not a value.
        [ ] "y" | Incorrect. Not a value.

    .. multichoice::

        Can the user type a number into a ttk Scale?

        [ ] Yes | Incorrect. It is dragged, not typed.
        [x] No, use a Spinbox or Entry for typing | Correct. Scales are dragged.
        [ ] Only with a style | Incorrect. Still no.
        [ ] Only when vertical | Incorrect. Still no.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a ttk Scale from 0 to 100.

        volume = ttk.@@Scale | Progressbar | Spinbox@@(root, @@from_ | from | start@@=0, @@to | end | max@@=100, length=300)
        volume.pack()

    .. cloze::
        :instructions: Start the slider in the middle.

        volume = ttk.Scale(root, from_=0, to=100, @@value | start | level@@=50, orient="@@horizontal | across | x@@")

    .. cloze::
        :instructions: Show the value in a label.

        def update(@@value | self | event@@):
            value_label.config(text=str(@@round | float | str@@(float(value))))

        volume = ttk.Scale(root, from_=0, to=100, @@command | click | run@@=update)

    .. cloze::
        :instructions: Read, set and turn off the slider.

        level = volume.@@get | read | value@@()
        volume.@@set | get | move@@(25)
        volume.@@state | config | set@@(["disabled"])

    .. cloze::
        :instructions: Change the range later.

        volume.@@config | set | range@@(@@to | max | end@@=20)

----

.. admonition:: Tasks

    #. Make a window titled "Rating" that is 300x200 with a ttk Scale from 1 to 10 that is 250 pixels long, starting on 5.
    #. Link the scale to a ``DoubleVar`` and use ``command`` to show the rounded number in a label.
    #. Make a ttk Scale from 0 to 100 with a ``command`` that shows "Battery:" and the whole number followed by "%".
    #. Make a ttk Scale from 1 to 12 and a "Times table" button. When clicked, a label shows the number from the scale times 9.

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
                    root.title("Rating")

                    ttk.Scale(root, from_=1, to=10, length=250, value=5).pack(pady=30)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def show(value):
                        number_label.config(text=round(rating.get()))


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Rating")

                    rating = tk.DoubleVar(value=5)

                    ttk.Scale(root, from_=1, to=10, length=250, variable=rating,
                              command=show).pack(pady=20)

                    number_label = ttk.Label(root, text="5", font=("Arial", 24))
                    number_label.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def show_battery(value):
                        battery_label.config(text=f"Battery: {int(float(value))}%")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Battery")

                    ttk.Scale(root, from_=0, to=100, length=250, command=show_battery).pack(pady=20)

                    battery_label = ttk.Label(root, text="Battery: 0%", font=("Arial", 16))
                    battery_label.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def times_table():
                        number = round(number_scale.get())
                        answer_label.config(text=f"{number} x 9 = {number * 9}")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Times table")

                    number_scale = ttk.Scale(root, from_=1, to=12, length=250)
                    number_scale.pack(pady=20)

                    ttk.Button(root, text="Times table", command=times_table).pack()

                    answer_label = ttk.Label(root, text="", font=("Arial", 16))
                    answer_label.pack(pady=10)

                    root.mainloop()
