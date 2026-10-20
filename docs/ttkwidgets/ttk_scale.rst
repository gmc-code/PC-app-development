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
