====================================================
ttk widgets and styling
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html>`_

----

What is ttk?
-------------------

| **ttk** stands for **themed Tk**. It is a second set of widgets that comes with tkinter.
| ttk widgets look more modern and more like the other apps on your computer.
| Most ttk widgets have the same name as a tk widget (``Button``, ``Label``, ``Entry`` ...). ttk also has some widgets tk does not have, such as ``Combobox``, ``Notebook``, ``Progressbar`` and ``Treeview``.

----

Using ttk widgets
-------------------

| ttk must be imported as well as tkinter:

.. code-block:: python

    import tkinter as tk            # The window, variables and tk widgets
    from tkinter import ttk         # The themed widgets

    root = tk.Tk()                  # The window is still made with tk
    root.geometry("300x200")
    root.title("tk and ttk")

    old_button = tk.Button(root, text="tk Button")      # tk version
    old_button.pack(pady=10)

    new_button = ttk.Button(root, text="ttk Button")    # ttk version
    new_button.pack(pady=10)

    root.mainloop()

| The only change is ``ttk.`` instead of ``tk.`` in front of the widget name.
| ``root``, ``StringVar``, ``IntVar`` and ``tk.END`` still come from ``tk``.

----

The big difference: styles
-----------------------------

| With **tk** widgets, colours and fonts are set on each widget:

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("tk colours")

    tk.Button(root, text="One", fg="white", bg="purple", font=("Arial", 14)).pack(pady=5)
    tk.Button(root, text="Two", fg="white", bg="purple", font=("Arial", 14)).pack(pady=5)

    root.mainloop()

| Most **ttk** widgets do **not** have ``fg``, ``bg`` or ``font`` options. Instead, the look is set **once** in a **style**, and every widget that uses that style gets that look.
| Change the style once, and every button changes.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("ttk style")

    style = ttk.Style()                                     # 1. Make a Style object
    style.theme_use("clam")                                 # 2. Choose a theme (see below)
    style.configure("TButton", foreground="white", background="purple",
                    font=("Arial", 14))                     # 3. Style every ttk Button

    ttk.Button(root, text="One").pack(pady=5)               # No colour options needed
    ttk.Button(root, text="Two").pack(pady=5)

    root.mainloop()

----

Themes
-------------------

| A **theme** is a complete look for every ttk widget: the shape of buttons, the colours, the borders.
| ``style.theme_names()`` lists the themes on your computer. ``style.theme_use("name")`` switches theme.

.. list-table::
    :header-rows: 1
    :widths: 25 75

    * - Theme
      - What it looks like
    * - ``"vista"``
      - The normal Windows look. This is the default on Windows.
    * - ``"winnative"``, ``"xpnative"``
      - Older Windows looks.
    * - ``"clam"``
      - A clean, flat look. **Allows the most colour changes.**
    * - ``"alt"``, ``"default"``, ``"classic"``
      - Simple looks that work on every computer.
    * - ``"aqua"``
      - The normal Mac look (Mac only).

.. important::

    On Windows the ``"vista"`` theme **ignores some colours**, such as the background of a Button.
    If a colour does not change, add ``style.theme_use("clam")`` near the top of your program.
    The examples on these pages that change colours all use ``"clam"`` so that they work.

Theme picker example
~~~~~~~~~~~~~~~~~~~~~~~

| Run this to see every theme on your computer. Click a theme to switch to it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def change_theme(theme_name):
        style.theme_use(theme_name)
        current_label.config(text="Theme: " + theme_name)


    root = tk.Tk()
    root.geometry("350x300")
    root.title("Theme picker")

    style = ttk.Style()

    current_label = ttk.Label(root, text="Theme: " + style.theme_use(), font=("Arial", 14))
    current_label.pack(pady=5)

    for theme_name in style.theme_names():
        ttk.Button(root, text=theme_name,
                   command=lambda name=theme_name: change_theme(name)).pack(pady=2)

    ttk.Checkbutton(root, text="A checkbutton").pack(pady=5)
    ttk.Entry(root).pack()

    root.mainloop()

| ``style.theme_use()`` with nothing in the brackets tells you which theme is being used now.

----

Style names
-------------------

| Every ttk widget uses a style. The style name is usually ``T`` followed by the widget name.

.. list-table::
    :header-rows: 1
    :widths: 40 60

    * - Widget
      - Style name
    * - ``ttk.Button``
      - ``"TButton"``
    * - ``ttk.Label``
      - ``"TLabel"``
    * - ``ttk.Entry``
      - ``"TEntry"``
    * - ``ttk.Checkbutton``
      - ``"TCheckbutton"``
    * - ``ttk.Radiobutton``
      - ``"TRadiobutton"``
    * - ``ttk.Combobox``
      - ``"TCombobox"``
    * - ``ttk.Spinbox``
      - ``"TSpinbox"``
    * - ``ttk.Frame``
      - ``"TFrame"``
    * - ``ttk.LabelFrame``
      - ``"TLabelframe"`` (and ``"TLabelframe.Label"`` for its title)
    * - ``ttk.Menubutton``
      - ``"TMenubutton"``
    * - ``ttk.Notebook``
      - ``"TNotebook"`` (and ``"TNotebook.Tab"`` for its tabs)
    * - ``ttk.PanedWindow``
      - ``"TPanedwindow"``
    * - ``ttk.Progressbar``
      - ``"Horizontal.TProgressbar"`` or ``"Vertical.TProgressbar"``
    * - ``ttk.Scale``
      - ``"Horizontal.TScale"`` or ``"Vertical.TScale"``
    * - ``ttk.Scrollbar``
      - ``"Vertical.TScrollbar"`` or ``"Horizontal.TScrollbar"``
    * - ``ttk.Separator``
      - ``"TSeparator"``
    * - ``ttk.Sizegrip``
      - ``"TSizegrip"``
    * - ``ttk.Treeview``
      - ``"Treeview"`` (and ``"Treeview.Heading"`` for its headings)

| A widget's ``winfo_class()`` method tells you its style name, e.g. ``ttk.Button(root).winfo_class()`` gives ``"TButton"``.

----

Style methods
-------------------

configure
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how every widget with that style looks.
| **How to write it:** ``style.configure("StyleName", option=value, option=value)``
| **Common options:**

- ``font`` - e.g. ``("Arial", 14, "bold")``
- ``foreground`` - colour of the words
- ``background`` - colour behind the words
- ``padding`` - space inside the widget, e.g. ``10`` or ``(20, 5)`` for (left-right, top-bottom)
- ``fieldbackground`` - colour **inside** an Entry, Combobox or Spinbox box

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("configure")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", font=("Arial", 16), foreground="navy")
    style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
    style.configure("TEntry", fieldbackground="lightyellow")

    ttk.Label(root, text="Name:").pack(pady=5)
    ttk.Entry(root).pack()
    ttk.Button(root, text="Submit").pack(pady=10)

    root.mainloop()

Making your own style
~~~~~~~~~~~~~~~~~~~~~~~~

| To make **some** buttons look different, make a **new style** based on the normal one.
| **How to write it:** put your own name and a dot in front of the normal style name, e.g. ``"Danger.TButton"``.
| Then give the widget ``style="Danger.TButton"``.
| The new style copies everything from ``"TButton"`` and only changes what you set.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x220")
    root.title("Custom styles")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font=("Arial", 12), padding=8)          # Every button
    style.configure("Go.TButton", foreground="white", background="green")
    style.configure("Danger.TButton", foreground="white", background="red")

    ttk.Button(root, text="Normal").pack(pady=5)
    ttk.Button(root, text="Start", style="Go.TButton").pack(pady=5)
    ttk.Button(root, text="Delete", style="Danger.TButton").pack(pady=5)

    root.mainloop()

| Notice that "Start" and "Delete" are also size 12 with padding 8: they copied that from ``"TButton"``.

map
~~~~~~~~~~~~~~~~~~

| **What it does:** changes the look when the widget is in a certain **state**, e.g. when the mouse is over it or it is pressed.
| **How to write it:** ``style.map("StyleName", option=[("state", value), ("state", value)])``
| **Common states:**

- ``"active"`` - the mouse is over the widget
- ``"pressed"`` - the widget is being clicked
- ``"disabled"`` - the widget is turned off
- ``"selected"`` - a Checkbutton or Radiobutton is chosen
- ``"focus"`` - the widget is ready for typing
- ``"readonly"`` - an Entry or Combobox cannot be typed in

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("map")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Fancy.TButton", font=("Arial", 14), foreground="white", background="blue")
    style.map("Fancy.TButton",
              background=[("pressed", "navy"), ("active", "deepskyblue")],
              foreground=[("pressed", "yellow")])

    ttk.Button(root, text="Hover, then press", style="Fancy.TButton").pack(pady=60)

    root.mainloop()

| The first state in the list that matches is used. Put ``"pressed"`` before ``"active"``, because a pressed button is also active.

lookup
~~~~~~~~~~~~~~~~~~

| **What it does:** reads a style setting.
| **How to write it:** ``value = style.lookup("StyleName", "option")``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("lookup")

    style = ttk.Style()
    style.configure("Big.TLabel", font=("Arial", 24))

    font_used = style.lookup("Big.TLabel", "font")
    ttk.Label(root, text="Big text", style="Big.TLabel").pack(pady=20)
    ttk.Label(root, text="The font is: " + str(font_used)).pack()

    root.mainloop()

----

Widget states
-------------------

| Most tk widgets use ``state="disabled"`` and ``state="normal"``.
| ttk widgets can have **several** states at once, so they have two extra methods.

state
~~~~~~~~~~~~~~~~~~

| **What it does:** turns states on or off.
| **How to write it:**
| ``widget.state(["disabled"])`` turns the widget off.
| ``widget.state(["!disabled"])`` turns it back on. ``!`` means "not".

instate
~~~~~~~~~~~~~~~~~~

| **What it does:** checks whether a widget is in a state. It gives back ``True`` or ``False``.
| **How to write it:** ``if widget.instate(["disabled"]):``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def lock_or_unlock():
        if submit_button.instate(["disabled"]):
            submit_button.state(["!disabled"])      # Turn on
            lock_button.config(text="Lock")
        else:
            submit_button.state(["disabled"])       # Turn off
            lock_button.config(text="Unlock")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("state and instate")

    submit_button = ttk.Button(root, text="Submit")
    submit_button.pack(pady=20)

    lock_button = ttk.Button(root, text="Lock", command=lock_or_unlock)
    lock_button.pack()

    root.mainloop()

| ``config(state="disabled")`` and ``config(state="normal")`` also work on ttk widgets.

----

Styling a whole app
----------------------

| Put all the style settings together near the top of the program. Every widget below then matches.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("320x260")
    root.title("Sign up")
    root.config(bg="white")

    # ---------- Styles ----------
    style = ttk.Style()
    style.theme_use("clam")
    style.configure(".", font=("Arial", 12), background="white")      # "." means every widget
    style.configure("Title.TLabel", font=("Arial", 20, "bold"), foreground="teal")
    style.configure("TButton", foreground="white", background="teal", padding=8)
    style.map("TButton", background=[("active", "darkcyan")])
    style.configure("TEntry", fieldbackground="azure")

    # ---------- Widgets ----------
    ttk.Label(root, text="Sign up", style="Title.TLabel").pack(pady=10)

    ttk.Label(root, text="Name:").pack()
    ttk.Entry(root).pack(pady=2)

    ttk.Label(root, text="Email:").pack()
    ttk.Entry(root).pack(pady=2)

    ttk.Checkbutton(root, text="Send me the newsletter").pack(pady=5)
    ttk.Button(root, text="Join").pack(pady=5)

    root.mainloop()

| ``style.configure(".", ...)`` sets the starting look for **every** ttk widget. Other styles can then change just what they need.

----

tk or ttk?
-------------------

.. list-table::
    :header-rows: 1
    :widths: 34 33 33

    * -
      - tk
      - ttk
    * - Look
      - Older, the same on every computer
      - Modern, matches the computer
    * - Colours and fonts
      - Options on each widget (``fg``, ``bg``, ``font``)
      - A ``Style`` shared by many widgets
    * - Turning off
      - ``state="disabled"``
      - ``state(["disabled"])`` or ``config(state="disabled")``
    * - Extra widgets
      - Canvas, Text, Listbox, Menu, Message
      - Combobox, Notebook, Progressbar, Separator, Sizegrip, Treeview

| tk and ttk widgets can be used in the same window. Canvas, Text, Listbox and Menu have **no** ttk version, so always use the tk ones.

----

Quick reference
-------------------

.. list-table::
    :header-rows: 1
    :widths: 35 35 30

    * - Code
      - What it does
      - Example
    * - ``from tkinter import ttk``
      - Load the themed widgets
      - ``ttk.Button(root, text="OK")``
    * - ``style = ttk.Style()``
      - Make a Style object
      - ``style = ttk.Style()``
    * - ``style.theme_names()``
      - List the themes
      - ``print(style.theme_names())``
    * - ``style.theme_use()``
      - Choose a theme
      - ``style.theme_use("clam")``
    * - ``style.configure()``
      - Set the look of a style
      - ``style.configure("TLabel", font=("Arial", 14))``
    * - ``"Name.TButton"``
      - Make your own style
      - ``style="Danger.TButton"``
    * - ``style.map()``
      - Change the look in a state
      - ``style.map("TButton", background=[("active", "red")])``
    * - ``style.lookup()``
      - Read a style setting
      - ``style.lookup("TLabel", "font")``
    * - ``widget.state()``
      - Turn a state on or off
      - ``button.state(["disabled"])``
    * - ``widget.instate()``
      - Check a state
      - ``button.instate(["disabled"])``

----

.. admonition:: Tasks

    #. Make a window titled "ttk" that is 300x200 with a ttk Label "Hello" and a ttk Button "OK".
    #. Use ``style.theme_use("clam")`` and ``style.configure`` so every ttk Button has white words on an orange background, in Arial size 14.
    #. Make your own style called ``"Big.TLabel"`` with Arial size 30. Use it on one label, and leave a second label with the normal style.
    #. Use ``style.map`` so your buttons turn red while the mouse is over them.

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
                    root.title("ttk")

                    ttk.Label(root, text="Hello").pack(pady=10)
                    ttk.Button(root, text="OK").pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("ttk")

                    style = ttk.Style()
                    style.theme_use("clam")
                    style.configure("TButton", foreground="white", background="orange",
                                    font=("Arial", 14))

                    ttk.Label(root, text="Hello").pack(pady=10)
                    ttk.Button(root, text="OK").pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("ttk")

                    style = ttk.Style()
                    style.configure("Big.TLabel", font=("Arial", 30))

                    ttk.Label(root, text="Big", style="Big.TLabel").pack(pady=10)
                    ttk.Label(root, text="Normal").pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("ttk")

                    style = ttk.Style()
                    style.theme_use("clam")
                    style.configure("TButton", foreground="white", background="orange",
                                    font=("Arial", 14))
                    style.map("TButton", background=[("active", "red")])

                    ttk.Button(root, text="OK").pack(pady=10)
                    ttk.Button(root, text="Cancel").pack()

                    root.mainloop()
