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
