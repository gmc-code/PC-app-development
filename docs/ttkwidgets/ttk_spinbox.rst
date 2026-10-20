====================================================
ttk Spinbox
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#spinbox>`_

----

What is a ttk Spinbox?
-------------------------

| A **ttk Spinbox** is a box with up and down arrows for choosing a number or a choice from a list, just like a tk Spinbox.
| It has one handy extra method: ``set()``, which changes the value without needing ``delete`` and ``insert``.

----

Making a ttk Spinbox
-----------------------

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk Spinbox")

    tickets_spinbox = ttk.Spinbox(root, from_=1, to=10)    # 1. Create it
    tickets_spinbox.set(1)                                 #    and choose the starting value
    tickets_spinbox.pack(pady=30)                          # 2. Place it

    root.mainloop()                 # Keep the window open

.. note::

    A ttk Spinbox starts **empty**. Use ``set()`` or a ``textvariable`` to give it a starting value.

----

ttk Spinbox options
----------------------

from\_, to and increment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``from_`` and ``to`` set the lowest and highest number. ``increment`` sets the size of each step.
| **How to write them:** ``from_=0, to=60, increment=5``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("from_, to and increment")

    minutes = ttk.Spinbox(root, from_=0, to=60, increment=5)
    minutes.set(0)
    minutes.pack(pady=30)

    root.mainloop()

values
~~~~~~~~~~~~~~~~~~

| **What it does:** steps through a list of choices instead of numbers.
| **How to write it:** ``values=("Small", "Medium", "Large")``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("values")

    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

    day_spinbox = ttk.Spinbox(root, values=days)
    day_spinbox.set(days[0])
    day_spinbox.pack(pady=30)

    root.mainloop()

wrap
~~~~~~~~~~~~~~~~~~

| **What it does:** ``wrap=True`` goes back to the start after the end, like a clock.
| **How to write it:** ``wrap=True``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("wrap")

    hour_spinbox = ttk.Spinbox(root, from_=1, to=12, wrap=True)
    hour_spinbox.set(12)
    hour_spinbox.pack(pady=30)

    root.mainloop()

width, font, foreground and justify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``width`` sets the width in characters. ``font`` and ``foreground`` set the style and colour of the text. ``justify`` lines it up ``"left"``, ``"center"`` or ``"right"``.
| **How to write them:** ``width=5, font=("Arial", 20), foreground="navy", justify="center"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and font")

    score_spinbox = ttk.Spinbox(root, from_=0, to=99, width=4, font=("Arial", 24),
                                foreground="navy", justify="center")
    score_spinbox.set(0)
    score_spinbox.pack(pady=30)

    root.mainloop()

format
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses how numbers are shown, e.g. always with two decimal places.
| **How to write it:** ``format="%.2f"`` shows ``1.50``. ``format="%02.0f"`` shows ``05`` (two digits, like a clock).

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("format")

    price = ttk.Spinbox(root, from_=0, to=10, increment=0.5, format="%.2f")
    price.set("0.00")
    price.pack(pady=10)

    minutes = ttk.Spinbox(root, from_=0, to=59, format="%02.0f", wrap=True, width=4)
    minutes.set("00")
    minutes.pack(pady=10)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** controls typing.
| **Values:** ``"normal"`` (arrows and typing), ``"readonly"`` (arrows only, so no wrong typing), ``"disabled"`` (off).
| **How to write it:** ``state="readonly"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    size_spinbox = ttk.Spinbox(root, values=("Small", "Medium", "Large"), state="readonly")
    size_spinbox.set("Small")
    size_spinbox.pack(pady=30)

    root.mainloop()

| ``set()`` still works on a readonly spinbox.

command
~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function every time an arrow is clicked.
| **How to write it:** ``command=function_name``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def update_price():
        tickets = int(tickets_spinbox.get())
        price_label.config(text=f"Total: ${tickets * 15}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("command")

    tickets_spinbox = ttk.Spinbox(root, from_=1, to=10, width=5, state="readonly",
                                  command=update_price)
    tickets_spinbox.set(1)
    tickets_spinbox.pack(pady=20)

    price_label = ttk.Label(root, text="Total: $15", font=("Arial", 16))
    price_label.pack()

    root.mainloop()

textvariable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the spinbox to a variable. It is the easiest way to give a starting value.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("textvariable")

    players = tk.IntVar(value=4)

    ttk.Spinbox(root, from_=1, to=8, textvariable=players).pack(pady=20)
    ttk.Label(root, textvariable=players, font=("Arial", 20)).pack()

    root.mainloop()

----

ttk Spinbox methods
----------------------

get and set
~~~~~~~~~~~~~~~~~~

| ``get()`` reads the value as a **string**, so use ``int()`` or ``float()`` for maths. ``set()`` changes the value.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def calculate():
        pizzas = int(pizza_spinbox.get())
        result_label.config(text=f"{pizzas * 8} slices")


    def reset():
        pizza_spinbox.set(1)
        result_label.config(text="")


    root = tk.Tk()
    root.geometry("300x220")
    root.title("get and set")

    ttk.Label(root, text="How many pizzas?").pack(pady=5)

    pizza_spinbox = ttk.Spinbox(root, from_=1, to=20, width=5)
    pizza_spinbox.set(1)
    pizza_spinbox.pack()

    ttk.Button(root, text="How many slices?", command=calculate).pack(pady=5)
    ttk.Button(root, text="Reset", command=reset).pack()

    result_label = ttk.Label(root, text="", font=("Arial", 14))
    result_label.pack(pady=5)

    root.mainloop()

Checking typed numbers
~~~~~~~~~~~~~~~~~~~~~~~~~

| When the state is ``"normal"``, the user could type a word. Use ``try`` and ``except ValueError``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def double():
        try:
            number = int(number_spinbox.get())
            result_label.config(text=f"Double: {number * 2}")
        except ValueError:
            result_label.config(text="That is not a number!")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Checking")

    number_spinbox = ttk.Spinbox(root, from_=1, to=100, width=6)
    number_spinbox.set(1)
    number_spinbox.pack(pady=10)

    ttk.Button(root, text="Double it", command=double).pack()

    result_label = ttk.Label(root, text="", font=("Arial", 14))
    result_label.pack(pady=5)

    root.mainloop()

bind (Increment and Decrement)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``"<<Increment>>"`` happens when the up arrow is clicked and ``"<<Decrement>>"`` when the down arrow is clicked. The function needs an ``event`` parameter.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def going_up(event):
        result_label.config(text="Up!", foreground="green")


    def going_down(event):
        result_label.config(text="Down!", foreground="red")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("bind")

    level_spinbox = ttk.Spinbox(root, from_=1, to=10, width=5)
    level_spinbox.set(5)
    level_spinbox.pack(pady=20)
    level_spinbox.bind("<<Increment>>", going_up)
    level_spinbox.bind("<<Decrement>>", going_down)

    result_label = ttk.Label(root, text="", font=("Arial", 16))
    result_label.pack()

    root.mainloop()

config
~~~~~~~~~~~~~~~~~~

| ``spinbox.config(option=value)`` changes options later, e.g. a new range.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def adults_only():
        age_spinbox.config(from_=18, to=100)
        age_spinbox.set(18)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    age_spinbox = ttk.Spinbox(root, from_=0, to=100, width=5)
    age_spinbox.set(0)
    age_spinbox.pack(pady=20)

    ttk.Button(root, text="Adults only", command=adults_only).pack()

    root.mainloop()

----

Styling a ttk Spinbox
------------------------

| The style is ``"TSpinbox"``. With ``"clam"``: ``fieldbackground`` (box colour), ``foreground``, ``arrowcolor``, ``arrowsize`` and ``padding``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Spinbox style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TSpinbox", fieldbackground="lightyellow", foreground="darkgreen",
                    arrowcolor="darkgreen", arrowsize=16, padding=5)

    level = ttk.Spinbox(root, from_=1, to=10, width=5, font=("Arial", 16))
    level.set(1)
    level.pack(pady=40)

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
      - Lowest and highest number
      - ``from_=1, to=10``
    * - ``increment``
      - Size of each step
      - ``increment=5``
    * - ``values``
      - A list of choices
      - ``values=("S", "M", "L")``
    * - ``wrap``
      - Go back to the start after the end
      - ``wrap=True``
    * - ``width``, ``font``, ``foreground``
      - Size, font and colour
      - ``font=("Arial", 16)``
    * - ``format``
      - How numbers are shown
      - ``format="%.2f"``
    * - ``state``
      - Typing, arrows only, or off
      - ``state="readonly"``
    * - ``command``
      - Function to run when an arrow is clicked
      - ``command=update``
    * - ``textvariable``
      - Link to a variable
      - ``textvariable=players``
    * - ``get()``, ``set()``
      - Read or change the value
      - ``spinbox.set(5)``
    * - ``bind()``
      - ``"<<Increment>>"``, ``"<<Decrement>>"``
      - ``spinbox.bind("<<Increment>>", up)``
    * - ``"TSpinbox"``
      - Style name
      - ``style.configure("TSpinbox", fieldbackground="pink")``

----

.. admonition:: Tasks

    #. Make a window titled "Tickets" that is 300x200 with a ttk Spinbox from 1 to 6 that starts on 2.
    #. Make it readonly with Arial size 20 and a width of 4.
    #. Make a ttk Spinbox that steps through "Red", "Orange", "Yellow" and "Green" and wraps back to the start.
    #. Make a ttk Spinbox from 1 to 10 with a ``command`` that shows the number times 3 in a label.

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
                    root.title("Tickets")

                    tickets_spinbox = ttk.Spinbox(root, from_=1, to=6)
                    tickets_spinbox.set(2)
                    tickets_spinbox.pack(pady=30)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Tickets")

                    tickets_spinbox = ttk.Spinbox(root, from_=1, to=6, state="readonly",
                                                  font=("Arial", 20), width=4)
                    tickets_spinbox.set(2)
                    tickets_spinbox.pack(pady=30)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Colours")

                    colour_spinbox = ttk.Spinbox(root, values=("Red", "Orange", "Yellow", "Green"),
                                                 wrap=True)
                    colour_spinbox.set("Red")
                    colour_spinbox.pack(pady=30)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def times_three():
                        number = int(number_spinbox.get())
                        answer_label.config(text=f"{number} x 3 = {number * 3}")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Times 3")

                    number_spinbox = ttk.Spinbox(root, from_=1, to=10, width=5, command=times_three)
                    number_spinbox.set(1)
                    number_spinbox.pack(pady=20)

                    answer_label = ttk.Label(root, text="1 x 3 = 3", font=("Arial", 16))
                    answer_label.pack()

                    root.mainloop()
