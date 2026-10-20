====================================================
ttk LabelFrame
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets>`_

----

What is a ttk LabelFrame?
----------------------------

| A **ttk LabelFrame** is a frame with a border and a title, just like a tk LabelFrame.
| Use it to show which widgets belong together, e.g. "Your details" or "Choose a size".
| The title's font and colour are set with the ``"TLabelframe.Label"`` style.

----

Making a ttk LabelFrame
--------------------------

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first ttk LabelFrame")

    details = ttk.LabelFrame(root, text="Your details", padding=10)   # 1. Create it
    details.pack(pady=20)                                             # 2. Place it

    ttk.Label(details, text="Name:").pack()          # 3. Widgets go in "details"
    ttk.Entry(details).pack()

    root.mainloop()                 # Keep the window open

----

ttk LabelFrame options
-------------------------

text
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the title shown in the border.
| **How to write it:** ``text="your title"``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("text")

    settings = ttk.LabelFrame(root, text="Settings", padding=10)
    settings.pack(pady=20)

    sound = tk.IntVar()
    ttk.Checkbutton(settings, text="Sound on", variable=sound).pack()

    root.mainloop()

padding
~~~~~~~~~~~~~~~~~~

| **What it does:** adds space between the border and the widgets inside.
| **How to write it:** ``padding=15`` or ``padding=(30, 10)`` (left-right, top-bottom)

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("padding")

    squashed = ttk.LabelFrame(root, text="No padding")
    squashed.pack(pady=10)
    ttk.Button(squashed, text="Squashed").pack()

    roomy = ttk.LabelFrame(root, text="Padding", padding=(30, 15))
    roomy.pack(pady=10)
    ttk.Button(roomy, text="Roomy").pack()

    root.mainloop()

labelanchor
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses where the title sits on the border.
| **How to write it:** ``labelanchor="n"``
| **Values:** ``"nw"`` (top left, the default), ``"n"`` (top middle), ``"ne"``, ``"sw"``, ``"s"``, ``"se"``, and ``"w"``, ``"e"`` and others for the sides.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("labelanchor")

    centred = ttk.LabelFrame(root, text="Centred title", labelanchor="n", padding=15)
    centred.pack(pady=30)
    ttk.Label(centred, text="The title is in the middle").pack()

    root.mainloop()

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** change the style and thickness of the border.
| **How to write them:** ``relief="solid", borderwidth=2``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("relief")

    warning = ttk.LabelFrame(root, text="Warning", relief="solid", borderwidth=2, padding=10)
    warning.pack(pady=30)
    ttk.Label(warning, text="Save your work!").pack()

    root.mainloop()

width and height
~~~~~~~~~~~~~~~~~~

| **What they do:** set the size of an **empty** LabelFrame in pixels.
| **How to write them:** ``width=200, height=100``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and height")

    ttk.LabelFrame(root, text="Coming soon", width=200, height=100).pack(pady=30)

    root.mainloop()

----

Using ttk LabelFrames
------------------------

Grouping radiobuttons
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("Order")

    size_box = ttk.LabelFrame(root, text="Size", padding=10)
    size_box.pack(fill="x", padx=10, pady=5)

    size = tk.StringVar(value="Small")
    for choice in ["Small", "Medium", "Large"]:
        ttk.Radiobutton(size_box, text=choice, variable=size, value=choice).pack(anchor="w")

    drink_box = ttk.LabelFrame(root, text="Drink", padding=10)
    drink_box.pack(fill="x", padx=10, pady=5)

    drink = tk.StringVar(value="Water")
    for choice in ["Water", "Juice"]:
        ttk.Radiobutton(drink_box, text=choice, variable=drink, value=choice).pack(anchor="w")

    root.mainloop()

Side-by-side LabelFrames
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("350x200")
    root.title("Scoreboard")

    for team in ["Home", "Away"]:
        box = ttk.LabelFrame(root, text=team, padding=(30, 10))
        box.pack(side="left", padx=15, pady=30)
        ttk.Label(box, text="0", font=("Arial", 30)).pack()

    root.mainloop()

A form with grid
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Form")

    form = ttk.LabelFrame(root, text="Sign up", padding=10)
    form.pack(pady=20)

    ttk.Label(form, text="Name:").grid(row=0, column=0, sticky="e", pady=2)
    ttk.Entry(form).grid(row=0, column=1, pady=2)
    ttk.Label(form, text="Email:").grid(row=1, column=0, sticky="e", pady=2)
    ttk.Entry(form).grid(row=1, column=1, pady=2)

    root.mainloop()

----

ttk LabelFrame methods
-------------------------

config and cget
~~~~~~~~~~~~~~~~~~

| ``labelframe.config(text="New title")`` changes the title. ``labelframe.cget("text")`` reads it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def next_round():
        number = int(game_box.cget("text").replace("Round ", ""))
        game_box.config(text=f"Round {number + 1}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config and cget")

    game_box = ttk.LabelFrame(root, text="Round 1", padding=20)
    game_box.pack(pady=30)
    ttk.Button(game_box, text="Next round", command=next_round).pack()

    root.mainloop()

| ttk LabelFrames also have ``pack_forget()``, ``winfo_children()`` and ``destroy()``, the same as a **ttk Frame**.

----

Styling a ttk LabelFrame
---------------------------

| A ttk LabelFrame uses **two** styles:

- ``"TLabelframe"`` - the box: ``background``, ``bordercolor`` (with ``"clam"``), ``relief``, ``borderwidth``.
- ``"TLabelframe.Label"`` - the title: ``font``, ``foreground``, ``background``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x220")
    root.title("LabelFrame style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabelframe", background="lightyellow", bordercolor="orange")
    style.configure("TLabelframe.Label", font=("Arial", 14, "bold"), foreground="darkorange",
                    background="lightyellow")
    style.configure("TLabel", background="lightyellow")

    notes = ttk.LabelFrame(root, text="Notes", padding=15)
    notes.pack(pady=30)
    ttk.Label(notes, text="Bring a hat tomorrow").pack()

    root.mainloop()

Your own LabelFrame style
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| For a custom style, name **both** parts the same way: ``"Red.TLabelframe"`` and ``"Red.TLabelframe.Label"``, then use ``style="Red.TLabelframe"``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("350x200")
    root.title("Custom LabelFrame style")

    style = ttk.Style()
    style.configure("Red.TLabelframe.Label", foreground="red", font=("Arial", 13, "bold"))
    style.configure("Blue.TLabelframe.Label", foreground="blue", font=("Arial", 13, "bold"))

    red_team = ttk.LabelFrame(root, text="Red team", style="Red.TLabelframe", padding=15)
    red_team.pack(side="left", padx=20, pady=30)
    ttk.Label(red_team, text="Score: 0").pack()

    blue_team = ttk.LabelFrame(root, text="Blue team", style="Blue.TLabelframe", padding=15)
    blue_team.pack(side="left", padx=20, pady=30)
    ttk.Label(blue_team, text="Score: 0").pack()

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
      - Title in the border
      - ``text="Settings"``
    * - ``padding``
      - Space inside the border
      - ``padding=10``
    * - ``labelanchor``
      - Where the title sits
      - ``labelanchor="n"``
    * - ``relief``, ``borderwidth``
      - Border style and thickness
      - ``relief="solid", borderwidth=2``
    * - ``width``, ``height``
      - Size of an empty box
      - ``width=200, height=100``
    * - ``style``
      - Use a custom style
      - ``style="Red.TLabelframe"``
    * - ``config()``, ``cget()``
      - Change or read an option
      - ``box.config(text="New title")``
    * - ``"TLabelframe"``
      - Style name of the box
      - ``style.configure("TLabelframe", background="white")``
    * - ``"TLabelframe.Label"``
      - Style name of the title
      - ``style.configure("TLabelframe.Label", font=("Arial", 14))``

----

.. admonition:: Tasks

    #. Make a window titled "Profile" that is 300x200 with a ttk LabelFrame "About you" and padding of 10. Put a ttk Label "Name:" and a ttk Entry inside it.
    #. Move the title to the middle of the top border.
    #. Make a ttk LabelFrame "Favourite season" holding four ttk Radiobuttons: "Summer", "Autumn", "Winter" and "Spring".
    #. Style every LabelFrame title in Arial size 14 bold, coloured purple.

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
                    root.title("Profile")

                    about = ttk.LabelFrame(root, text="About you", padding=10)
                    about.pack(pady=20)
                    ttk.Label(about, text="Name:").pack()
                    ttk.Entry(about).pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Profile")

                    about = ttk.LabelFrame(root, text="About you", padding=10, labelanchor="n")
                    about.pack(pady=20)
                    ttk.Label(about, text="Name:").pack()
                    ttk.Entry(about).pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x220")
                    root.title("Seasons")

                    season_box = ttk.LabelFrame(root, text="Favourite season", padding=10)
                    season_box.pack(pady=10)

                    season = tk.StringVar(value="Summer")
                    for choice in ["Summer", "Autumn", "Winter", "Spring"]:
                        ttk.Radiobutton(season_box, text=choice, variable=season,
                                        value=choice).pack(anchor="w")

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x220")
                    root.title("Seasons")

                    style = ttk.Style()
                    style.configure("TLabelframe.Label", font=("Arial", 14, "bold"), foreground="purple")

                    season_box = ttk.LabelFrame(root, text="Favourite season", padding=10)
                    season_box.pack(pady=10)

                    season = tk.StringVar(value="Summer")
                    for choice in ["Summer", "Autumn", "Winter", "Spring"]:
                        ttk.Radiobutton(season_box, text=choice, variable=season,
                                        value=choice).pack(anchor="w")

                    root.mainloop()
