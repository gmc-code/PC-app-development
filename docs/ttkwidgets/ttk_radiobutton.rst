====================================================
ttk Radiobutton
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk Radiobutton?
-----------------------------

| A **ttk Radiobutton** is a round button in a **group**. The user can choose **only one** button in the group, just like tk Radiobuttons.
| Colours and fonts are set with the ``"TRadiobutton"`` style.
| The special ``"Toolbutton"`` style makes radiobuttons look like normal buttons.

----

Making a group of ttk Radiobuttons
-------------------------------------

| All the radiobuttons in a group share **one variable**. Each one has its own **value**.

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk Radiobuttons")

    drink = tk.StringVar(value="Water")     # 1. One shared variable; "Water" is chosen at the start

    ttk.Radiobutton(root, text="Water", variable=drink, value="Water").pack()   # 2. Create
    ttk.Radiobutton(root, text="Juice", variable=drink, value="Juice").pack()   #    and place
    ttk.Radiobutton(root, text="Milk", variable=drink, value="Milk").pack()

    root.mainloop()                 # Keep the window open

----

ttk Radiobutton options
--------------------------

text, variable and value
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``text`` is the words shown. ``variable`` is the shared variable for the group. ``value`` is what is stored when **this** button is chosen.
| **How to write them:** ``text="Year 7", variable=year, value="Year 7"``
| Read the chosen value with ``variable.get()``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def show():
        result_label.config(text="You chose " + year.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("text, variable and value")

    year = tk.StringVar(value="Year 7")

    for choice in ["Year 7", "Year 8", "Year 9"]:
        ttk.Radiobutton(root, text=choice, variable=year, value=choice).pack()

    ttk.Button(root, text="Show", command=show).pack(pady=5)

    result_label = ttk.Label(root, text="")
    result_label.pack()

    root.mainloop()

command
~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function as soon as a radiobutton is clicked. Give every button in the group the same command.
| **How to write it:** ``command=function_name``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def change_colour():
        root.config(bg=colour.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("command")

    colour = tk.StringVar(value="white")

    for name in ["white", "pink", "lightblue", "lightgreen"]:
        ttk.Radiobutton(root, text=name, variable=colour, value=name,
                        command=change_colour).pack(pady=2)

    root.mainloop()

width and padding
~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``width`` sets the width in characters. ``padding`` adds space around the button.
| Use the same ``width`` on each button and ``pack(anchor="w")`` to line them up neatly.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and padding")

    sport = tk.StringVar(value="Soccer")

    for choice in ["Soccer", "Netball", "Basketball"]:
        ttk.Radiobutton(root, text=choice, variable=sport, value=choice,
                        width=15, padding=5).pack(anchor="w", padx=80)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** turns a radiobutton off (greyed out) or on.
| **How to write it:** ``state="disabled"``, or later ``radio.state(["disabled"])`` and ``radio.state(["!disabled"])``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    seat = tk.StringVar(value="Window")

    ttk.Radiobutton(root, text="Window seat", variable=seat, value="Window").pack()
    ttk.Radiobutton(root, text="Aisle seat (full)", variable=seat, value="Aisle",
                    state="disabled").pack()

    root.mainloop()

style="Toolbutton"
~~~~~~~~~~~~~~~~~~~~~

| **What it does:** makes each radiobutton look like a normal button. The chosen one stays pressed in.
| **How to write it:** ``style="Toolbutton"``
| This does the same job as ``indicatoron=0`` on a tk Radiobutton.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Toolbutton")

    level = tk.StringVar(value="Easy")

    row = ttk.Frame(root)
    row.pack(pady=40)
    for choice in ["Easy", "Medium", "Hard"]:
        ttk.Radiobutton(row, text=choice, variable=level, value=choice,
                        style="Toolbutton", width=8).pack(side="left", padx=2)

    root.mainloop()

----

ttk Radiobutton methods
--------------------------

get and set (the variable)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``variable.get()`` reads the chosen value. ``variable.set(value)`` chooses a button from code.
| Setting a value that matches **no** button, e.g. ``"none"``, means nothing is chosen.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def reset():
        drink.set("none")           # Matches no button, so nothing is chosen


    root = tk.Tk()
    root.geometry("300x200")
    root.title("get and set")

    drink = tk.StringVar(value="Juice")

    for choice in ["Water", "Juice", "Milk"]:
        ttk.Radiobutton(root, text=choice, variable=drink, value=choice).pack()

    ttk.Button(root, text="Reset", command=reset).pack(pady=10)

    root.mainloop()

Checking a quiz answer
~~~~~~~~~~~~~~~~~~~~~~~~~

| Compare ``variable.get()`` with the right answer.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def check():
        if answer.get() == "Mars":
            result_label.config(text="Correct!", foreground="green")
        else:
            result_label.config(text="Try again", foreground="red")


    root = tk.Tk()
    root.geometry("300x220")
    root.title("Quiz")

    ttk.Label(root, text="Which planet is red?", font=("Arial", 14)).pack(pady=5)

    answer = tk.StringVar(value="none")

    for planet in ["Venus", "Mars", "Jupiter"]:
        ttk.Radiobutton(root, text=planet, variable=answer, value=planet).pack()

    ttk.Button(root, text="Check", command=check).pack(pady=5)

    result_label = ttk.Label(root, text="", font=("Arial", 14))
    result_label.pack()

    root.mainloop()

invoke and instate
~~~~~~~~~~~~~~~~~~~~~

| ``radio.invoke()`` chooses the radiobutton and runs its command, like a click.
| ``radio.instate(["selected"])`` gives ``True`` if this radiobutton is the chosen one.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def show():
        if large_radio.instate(["selected"]):
            result_label.config(text="Large chosen: $5")
        else:
            result_label.config(text="Small chosen: $3")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("invoke and instate")

    size = tk.StringVar(value="none")

    small_radio = ttk.Radiobutton(root, text="Small", variable=size, value="Small", command=show)
    small_radio.pack()
    large_radio = ttk.Radiobutton(root, text="Large", variable=size, value="Large", command=show)
    large_radio.pack()

    result_label = ttk.Label(root, text="")
    result_label.pack(pady=10)

    small_radio.invoke()            # Choose Small and run show() at the start

    root.mainloop()

----

Styling ttk Radiobuttons
---------------------------

| The style for every ttk Radiobutton is ``"TRadiobutton"``.
| ``indicatorbackground`` (with ``"clam"``) sets the colour inside the round button. ``style.map`` with ``"selected"`` changes the chosen one.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Radiobutton style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TRadiobutton", font=("Arial", 14), background="lavender")
    style.map("TRadiobutton", foreground=[("selected", "purple")],
              indicatorbackground=[("selected", "violet")])

    pet = tk.StringVar(value="Dog")
    for choice in ["Dog", "Cat", "Rabbit"]:
        ttk.Radiobutton(root, text=choice, variable=pet, value=choice).pack(pady=3)

    root.mainloop()

Styling Toolbuttons
~~~~~~~~~~~~~~~~~~~~~~

| Make your own style based on ``"Toolbutton"``, e.g. ``"Level.Toolbutton"``, to colour the chosen button.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Toolbutton style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Level.Toolbutton", font=("Arial", 12), padding=8)
    style.map("Level.Toolbutton", background=[("selected", "gold")])

    level = tk.StringVar(value="Medium")

    row = ttk.Frame(root)
    row.pack(pady=40)
    for choice in ["Easy", "Medium", "Hard"]:
        ttk.Radiobutton(row, text=choice, variable=level, value=choice,
                        style="Level.Toolbutton").pack(side="left", padx=2)

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
      - Words next to the button
      - ``text="Year 7"``
    * - ``variable``
      - Shared variable for the group
      - ``variable=year``
    * - ``value``
      - Stored when this button is chosen
      - ``value="Year 7"``
    * - ``command``
      - Function to run when clicked
      - ``command=show``
    * - ``width``, ``padding``
      - Width and space around it
      - ``width=15, padding=5``
    * - ``state``
      - Turn on or off
      - ``state="disabled"``
    * - ``style="Toolbutton"``
      - Look like normal buttons
      - ``style="Toolbutton"``
    * - ``variable.get()``, ``.set()``
      - Read or choose a value
      - ``year.set("Year 8")``
    * - ``invoke()``
      - Choose and run the command
      - ``radio.invoke()``
    * - ``instate(["selected"])``
      - Is this one chosen?
      - ``radio.instate(["selected"])``
    * - ``"TRadiobutton"``
      - Style name
      - ``style.configure("TRadiobutton", font=("Arial", 14))``

----

.. admonition:: Tasks

    #. Make a window titled "Transport" that is 300x200 with three ttk Radiobuttons, "Bus", "Car" and "Walk", sharing one ``StringVar``. Start on "Walk".
    #. Add a "Show" button and a label that shows "You travel by" and the choice.
    #. Make a question "What is 4 x 5?" with the choices 15, 20 and 25. Use ``command`` to check the answer as soon as one is clicked.
    #. Make three Toolbutton-style radiobuttons side by side, "Small", "Medium" and "Large", where the chosen one turns light green.

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
                    root.title("Transport")

                    transport = tk.StringVar(value="Walk")

                    for choice in ["Bus", "Car", "Walk"]:
                        ttk.Radiobutton(root, text=choice, variable=transport, value=choice).pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def show():
                        result_label.config(text="You travel by " + transport.get())


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Transport")

                    transport = tk.StringVar(value="Walk")

                    for choice in ["Bus", "Car", "Walk"]:
                        ttk.Radiobutton(root, text=choice, variable=transport, value=choice).pack()

                    ttk.Button(root, text="Show", command=show).pack(pady=5)
                    result_label = ttk.Label(root, text="")
                    result_label.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def check():
                        if answer.get() == 20:
                            result_label.config(text="Correct!", foreground="green")
                        else:
                            result_label.config(text="Try again", foreground="red")


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Quiz")

                    ttk.Label(root, text="What is 4 x 5?", font=("Arial", 14)).pack()

                    answer = tk.IntVar(value=0)
                    for number in [15, 20, 25]:
                        ttk.Radiobutton(root, text=number, variable=answer, value=number,
                                        command=check).pack()

                    result_label = ttk.Label(root, text="", font=("Arial", 14))
                    result_label.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Sizes")

                    style = ttk.Style()
                    style.theme_use("clam")
                    style.map("Size.Toolbutton", background=[("selected", "lightgreen")])

                    size = tk.StringVar(value="Medium")

                    row = ttk.Frame(root)
                    row.pack(pady=40)
                    for choice in ["Small", "Medium", "Large"]:
                        ttk.Radiobutton(row, text=choice, variable=size, value=choice,
                                        style="Size.Toolbutton").pack(side="left", padx=2)

                    root.mainloop()
