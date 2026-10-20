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
