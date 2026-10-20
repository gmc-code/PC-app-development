====================================================
ttk Entry
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk Entry?
-----------------------

| A **ttk Entry** is a box the user types **one line** into, just like a tk Entry.
| It has the same methods as a tk Entry: ``get``, ``insert``, ``delete``, ``focus_set``, ``select_range`` and ``bind``.
| The colour of the box is set with a **style** (``fieldbackground``).

----

Making a ttk Entry
---------------------

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk Entry")

    ttk.Label(root, text="Type your name:").pack(pady=5)

    name_entry = ttk.Entry(root)    # 1. Create the entry
    name_entry.pack()               # 2. Place it

    root.mainloop()                 # Keep the window open

----

ttk Entry options
--------------------

width
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how wide the box is, in **characters**. The default is 20.
| **How to write it:** ``width=10``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width")

    ttk.Entry(root, width=5).pack(pady=10)
    ttk.Entry(root, width=40).pack(pady=10)

    root.mainloop()

font
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the style and size of the typed letters. A bigger font makes the box taller.
| **How to write it:** ``font=("Arial", 18)``
| The font **cannot** be set in the ``"TEntry"`` style. Set it on each Entry.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("font")

    ttk.Entry(root, font=("Arial", 18)).pack(pady=40)

    root.mainloop()

foreground
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the colour of the typed letters.
| **How to write it:** ``foreground="blue"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("foreground")

    ttk.Entry(root, font=("Arial", 16), foreground="blue").pack(pady=40)

    root.mainloop()

justify
~~~~~~~~~~~~~~~~~~

| **What it does:** lines the typed text up on the ``"left"`` (default), ``"center"`` or ``"right"``.
| **How to write it:** ``justify="center"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("justify")

    for side in ["left", "center", "right"]:
        entry = ttk.Entry(root, justify=side, font=("Arial", 14))
        entry.insert(0, side)
        entry.pack(pady=5)

    root.mainloop()

show
~~~~~~~~~~~~~~~~~~

| **What it does:** hides the typing by showing another character instead. Used for **passwords**.
| **How to write it:** ``show="*"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("show")

    ttk.Label(root, text="Password:").pack(pady=5)
    ttk.Entry(root, show="*", font=("Arial", 14)).pack()

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** controls whether the user can type in the box.
| **Values:** ``"normal"`` (can type), ``"readonly"`` (can see and copy, not change), ``"disabled"`` (greyed out).
| **How to write it:** ``state="readonly"``, or ``entry.state(["readonly"])`` later.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("state")

    for setting in ["normal", "readonly", "disabled"]:
        entry = ttk.Entry(root)
        entry.insert(0, setting)            # Insert before locking the box
        entry.config(state=setting)
        entry.pack(pady=5)

    root.mainloop()

textvariable
~~~~~~~~~~~~~~~~~~

| **What it does:** links the box to a ``StringVar``. ``.get()`` on the variable reads the box and ``.set()`` changes it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def shout():
        word.set(word.get().upper())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("textvariable")

    word = tk.StringVar(value="hello")

    ttk.Entry(root, textvariable=word, font=("Arial", 16)).pack(pady=20)
    ttk.Button(root, text="SHOUT", command=shout).pack()

    root.mainloop()

----

ttk Entry methods
--------------------

get
~~~~~~~~~~~~~~~~~~

| **What it does:** reads what the user has typed. It is always a **string**.
| **How to write it:** ``text = entry.get()``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def say_hello():
        answer_label.config(text="Hello " + name_entry.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("get")

    name_entry = ttk.Entry(root, font=("Arial", 14))
    name_entry.pack(pady=10)

    ttk.Button(root, text="Say hello", command=say_hello).pack()

    answer_label = ttk.Label(root, text="", font=("Arial", 14))
    answer_label.pack(pady=10)

    root.mainloop()

Getting a number
~~~~~~~~~~~~~~~~~~~

| Use ``int()`` or ``float()`` to turn the text into a number. ``try`` and ``except ValueError`` stop a crash if a word is typed.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def convert():
        try:
            cm = float(cm_entry.get())
            answer_label.config(text=f"{cm} cm = {cm / 100} m")
        except ValueError:
            answer_label.config(text="Please type a number")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("cm to m")

    cm_entry = ttk.Entry(root, width=10, font=("Arial", 14))
    cm_entry.pack(pady=10)

    ttk.Button(root, text="Convert", command=convert).pack()

    answer_label = ttk.Label(root, text="", font=("Arial", 14))
    answer_label.pack(pady=10)

    root.mainloop()

delete and insert
~~~~~~~~~~~~~~~~~~~~

| ``entry.delete(0, tk.END)`` clears the box. ``entry.insert(0, "text")`` puts text in it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def clear():
        word_entry.delete(0, tk.END)


    def reset():
        word_entry.delete(0, tk.END)
        word_entry.insert(0, "Type here")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("delete and insert")

    word_entry = ttk.Entry(root, font=("Arial", 14))
    word_entry.insert(0, "Type here")
    word_entry.pack(pady=10)

    ttk.Button(root, text="Clear", command=clear).pack(pady=2)
    ttk.Button(root, text="Reset", command=reset).pack(pady=2)

    root.mainloop()

focus_set and select_range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``focus_set()`` puts the typing cursor in the box. ``select_range(0, tk.END)`` highlights all the text so the next typing replaces it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def check():
        if answer_entry.get() == "9":
            result_label.config(text="Correct!", foreground="green")
        else:
            result_label.config(text="Try again", foreground="red")
            answer_entry.focus_set()
            answer_entry.select_range(0, tk.END)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("focus_set")

    ttk.Label(root, text="What is 3 x 3?", font=("Arial", 14)).pack(pady=5)

    answer_entry = ttk.Entry(root, width=5, font=("Arial", 14))
    answer_entry.pack()
    answer_entry.focus_set()

    ttk.Button(root, text="Check", command=check).pack(pady=5)

    result_label = ttk.Label(root, text="", font=("Arial", 14))
    result_label.pack()

    root.mainloop()

bind (pressing Enter)
~~~~~~~~~~~~~~~~~~~~~~~~

| ``entry.bind("<Return>", function_name)`` runs a function when Enter is pressed. Use ``event=None`` so the function also works from a button.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def add_item(event=None):
        items_label.config(text=items_label.cget("text") + "\n" + item_entry.get())
        item_entry.delete(0, tk.END)


    root = tk.Tk()
    root.geometry("300x250")
    root.title("bind")

    item_entry = ttk.Entry(root, font=("Arial", 14))
    item_entry.pack(pady=5)
    item_entry.bind("<Return>", add_item)

    ttk.Button(root, text="Add", command=add_item).pack()

    items_label = ttk.Label(root, text="Shopping list:")
    items_label.pack(pady=5)

    root.mainloop()

----

Styling a ttk Entry
----------------------

| The style for every ttk Entry is ``"TEntry"``.
| ``fieldbackground`` is the colour **inside** the box. ``padding`` adds space inside the box around the text.
| ``"clam"`` is used so ``fieldbackground`` works on Windows.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Entry style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TEntry", fieldbackground="lightyellow", foreground="navy", padding=5)
    style.configure("Wrong.TEntry", fieldbackground="mistyrose")

    ttk.Entry(root, font=("Arial", 14)).pack(pady=10)
    ttk.Entry(root, font=("Arial", 14), style="Wrong.TEntry").pack(pady=10)

    root.mainloop()

Changing colour for a wrong answer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Swap an Entry's style with ``config(style=...)`` to show if an answer is right or wrong.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def check():
        if answer_entry.get().lower() == "canberra":
            answer_entry.config(style="Right.TEntry")
        else:
            answer_entry.config(style="Wrong.TEntry")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Right or wrong")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Right.TEntry", fieldbackground="lightgreen")
    style.configure("Wrong.TEntry", fieldbackground="pink")

    ttk.Label(root, text="Capital of Australia?").pack(pady=5)

    answer_entry = ttk.Entry(root, font=("Arial", 14))
    answer_entry.pack()

    ttk.Button(root, text="Check", command=check).pack(pady=10)

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
    * - ``width``
      - Width in characters
      - ``width=10``
    * - ``font``
      - Font of the typing
      - ``font=("Arial", 14)``
    * - ``foreground``
      - Colour of the typing
      - ``foreground="blue"``
    * - ``justify``
      - Line up the text
      - ``justify="center"``
    * - ``show``
      - Hide typing (passwords)
      - ``show="*"``
    * - ``state``
      - Allow or stop typing
      - ``state="readonly"``
    * - ``textvariable``
      - Link to a StringVar
      - ``textvariable=word``
    * - ``get()``
      - Read the text
      - ``entry.get()``
    * - ``delete()``, ``insert()``
      - Clear the box, put text in
      - ``entry.delete(0, tk.END)``
    * - ``focus_set()``
      - Put the cursor in the box
      - ``entry.focus_set()``
    * - ``select_range()``
      - Highlight the text
      - ``entry.select_range(0, tk.END)``
    * - ``bind()``
      - Run a function on a key press
      - ``entry.bind("<Return>", go)``
    * - ``"TEntry"``
      - Style name; use ``fieldbackground`` for the box colour
      - ``style.configure("TEntry", fieldbackground="pink")``

----

.. admonition:: Tasks

    #. Make a window titled "Login" that is 300x200 with a ttk Label "Username:" and a ttk Entry using Arial size 14.
    #. Add a ttk Label "Password:" and a ttk Entry that shows ``"*"``.
    #. Use a style so both entries have a light blue box colour.
    #. Add a "Log in" button. When clicked, a label shows "Welcome" and the username.

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
                    root.title("Login")

                    ttk.Label(root, text="Username:").pack()
                    user_entry = ttk.Entry(root, font=("Arial", 14))
                    user_entry.pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Login")

                    ttk.Label(root, text="Username:").pack()
                    user_entry = ttk.Entry(root, font=("Arial", 14))
                    user_entry.pack()

                    ttk.Label(root, text="Password:").pack()
                    password_entry = ttk.Entry(root, font=("Arial", 14), show="*")
                    password_entry.pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Login")

                    style = ttk.Style()
                    style.theme_use("clam")
                    style.configure("TEntry", fieldbackground="lightblue")

                    ttk.Label(root, text="Username:").pack()
                    user_entry = ttk.Entry(root, font=("Arial", 14))
                    user_entry.pack()

                    ttk.Label(root, text="Password:").pack()
                    password_entry = ttk.Entry(root, font=("Arial", 14), show="*")
                    password_entry.pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def log_in():
                        welcome_label.config(text="Welcome " + user_entry.get())


                    root = tk.Tk()
                    root.geometry("300x250")
                    root.title("Login")

                    style = ttk.Style()
                    style.theme_use("clam")
                    style.configure("TEntry", fieldbackground="lightblue")

                    ttk.Label(root, text="Username:").pack()
                    user_entry = ttk.Entry(root, font=("Arial", 14))
                    user_entry.pack()

                    ttk.Label(root, text="Password:").pack()
                    password_entry = ttk.Entry(root, font=("Arial", 14), show="*")
                    password_entry.pack()

                    ttk.Button(root, text="Log in", command=log_in).pack(pady=10)

                    welcome_label = ttk.Label(root, text="")
                    welcome_label.pack()

                    root.mainloop()
