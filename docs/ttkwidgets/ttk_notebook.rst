====================================================
ttk Notebook
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#notebook>`_

----

What is a Notebook?
----------------------

| A **Notebook** shows **tabs** along the top, like the tabs in a web browser.
| Each tab has its own page. Clicking a tab shows that page and hides the others.
| Use a Notebook to split an app into sections, e.g. "Home", "Settings" and "Help". tk has no Notebook; it only comes with ttk.

----

Making a Notebook
--------------------

| Each tab's page is usually a **Frame** holding the widgets for that page.

#. **Create** the Notebook and **place** it.
#. **Create** a Frame for each page, with the Notebook as its parent.
#. **Add** each Frame as a tab with ``notebook.add(frame, text="Tab name")``.
#. **Put widgets** in each Frame.

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")
    root.title("My first Notebook")

    notebook = ttk.Notebook(root)                   # 1. Create the Notebook
    notebook.pack(fill="both", expand=True)

    home_page = ttk.Frame(notebook, padding=10)     # 2. A Frame for each page
    help_page = ttk.Frame(notebook, padding=10)

    notebook.add(home_page, text="Home")            # 3. Add them as tabs
    notebook.add(help_page, text="Help")

    ttk.Label(home_page, text="Welcome to the app!").pack()             # 4. Widgets on each page
    ttk.Label(help_page, text="Click the tabs to change page.").pack()

    root.mainloop()                 # Keep the window open

----

Notebook options
-------------------

width and height
~~~~~~~~~~~~~~~~~~

| **What they do:** set the size of the page area in pixels, when the Notebook is not stretched with ``fill``.
| **How to write them:** ``width=250, height=120``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x220")
    root.title("width and height")

    notebook = ttk.Notebook(root, width=250, height=120)
    notebook.pack(pady=20)

    for name in ["One", "Two", "Three"]:
        page = ttk.Frame(notebook)
        notebook.add(page, text=name)
        ttk.Label(page, text=f"This is page {name}").pack(pady=20)

    root.mainloop()

padding
~~~~~~~~~~~~~~~~~~

| **What it does:** adds space around the outside of the pages.
| **How to write it:** ``padding=10``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("padding")

    notebook = ttk.Notebook(root, padding=10)
    notebook.pack(fill="both", expand=True)

    page = ttk.Frame(notebook)
    notebook.add(page, text="Padded")
    ttk.Label(page, text="There is space around this page").pack(pady=20)

    root.mainloop()

----

Tab options
-------------------

| These options go in ``notebook.add(frame, ...)`` to change one tab.

text
~~~~~~~~~~~~~~~~~~

| **What it does:** the words on the tab.
| **How to write it:** ``notebook.add(page, text="Settings")``

image and compound
~~~~~~~~~~~~~~~~~~~~~

| **What they do:** show a picture on the tab. ``compound="left"`` puts the picture beside the words.
| **How to write them:** ``notebook.add(page, text="Home", image=picture, compound="left")``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("image")

    picture = tk.PhotoImage(file="logo.png")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    home_page = ttk.Frame(notebook)
    notebook.add(home_page, text="Home", image=picture, compound="left")
    ttk.Label(home_page, text="A tab with a picture").pack(pady=20)

    root.mainloop()

state
~~~~~~~~~~~~~~~~~~

| **What it does:** turns a tab on or off.
| **Values:** ``"normal"``, ``"disabled"`` (greyed out, cannot be clicked), ``"hidden"`` (not shown).
| **How to write it:** ``notebook.add(page, text="Secret", state="disabled")``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("tab state")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    level_1 = ttk.Frame(notebook)
    level_2 = ttk.Frame(notebook)
    notebook.add(level_1, text="Level 1")
    notebook.add(level_2, text="Level 2 (locked)", state="disabled")

    ttk.Label(level_1, text="Finish level 1 to unlock level 2").pack(pady=20)

    root.mainloop()

padding (tab page)
~~~~~~~~~~~~~~~~~~~~~

| **What it does:** adds space inside one page.
| **How to write it:** ``notebook.add(page, text="Notes", padding=20)``

----

Notebook methods
-------------------

| A **method** is an action the Notebook can do. Methods are written after a dot, e.g. ``notebook.select(...)``.

add
~~~~~~~~~~~~~~~~~~

| **What it does:** adds a page as a new tab at the end.
| **How to write it:** ``notebook.add(frame, text="Name")``
| Below, a button adds new tabs while the program runs.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def new_tab():
        number = len(notebook.tabs()) + 1
        page = ttk.Frame(notebook, padding=10)
        notebook.add(page, text=f"Note {number}")
        tk.Text(page, height=4, width=25).pack()
        notebook.select(page)                       # Show the new tab


    root = tk.Tk()
    root.geometry("320x220")
    root.title("add")

    ttk.Button(root, text="New tab", command=new_tab).pack(pady=5)

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    new_tab()                                       # Start with one tab

    root.mainloop()

select
~~~~~~~~~~~~~~~~~~

| **What it does:** switches to a tab from code. Give it the page's frame or the tab's number (0 is the first).
| **How to write it:** ``notebook.select(settings_page)`` or ``notebook.select(1)``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("select")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    start_page = ttk.Frame(notebook, padding=10)
    game_page = ttk.Frame(notebook, padding=10)
    notebook.add(start_page, text="Start")
    notebook.add(game_page, text="Game")

    ttk.Label(start_page, text="Ready to play?").pack()
    ttk.Button(start_page, text="Play", command=lambda: notebook.select(game_page)).pack(pady=10)

    ttk.Label(game_page, text="Game started!", font=("Arial", 18)).pack()
    ttk.Button(game_page, text="Back", command=lambda: notebook.select(0)).pack(pady=10)

    root.mainloop()

index("current")
~~~~~~~~~~~~~~~~~~~

| **What it does:** tells you the number of the tab being shown (0 is the first).
| **How to write it:** ``number = notebook.index("current")``
| ``notebook.index("end")`` tells you how many tabs there are.

tab
~~~~~~~~~~~~~~~~~~

| **What it does:** reads or changes one tab's options.
| ``notebook.tab(0, "text")`` reads the words on tab 0.
| ``notebook.tab(1, state="normal")`` changes tab 1, e.g. to unlock it.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def unlock():
        notebook.tab(1, state="normal", text="Level 2")
        notebook.select(1)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("tab")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    level_1 = ttk.Frame(notebook, padding=10)
    level_2 = ttk.Frame(notebook, padding=10)
    notebook.add(level_1, text="Level 1")
    notebook.add(level_2, text="Level 2 (locked)", state="disabled")

    ttk.Button(level_1, text="Finish level 1", command=unlock).pack(pady=20)
    ttk.Label(level_2, text="Welcome to level 2!", font=("Arial", 16)).pack(pady=20)

    root.mainloop()

bind (when the tab changes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function every time the user switches tab.
| **How to write it:** ``notebook.bind("<<NotebookTabChanged>>", function_name)``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def tab_changed(event):
        number = notebook.index("current")
        name = notebook.tab(number, "text")
        status_label.config(text=f"You are on the {name} tab (tab number {number})")


    root = tk.Tk()
    root.geometry("320x200")
    root.title("NotebookTabChanged")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    for name in ["Red", "Green", "Blue"]:
        page = ttk.Frame(notebook, padding=10)
        notebook.add(page, text=name)
        ttk.Label(page, text=f"The {name} page").pack()

    notebook.bind("<<NotebookTabChanged>>", tab_changed)

    status_label = ttk.Label(root, text="")
    status_label.pack(pady=5)

    root.mainloop()

hide and forget
~~~~~~~~~~~~~~~~~~

| ``notebook.hide(page)`` hides a tab. ``notebook.add(page)`` shows it again, in the same place.
| ``notebook.forget(page)`` removes a tab completely.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def hide_help():
        notebook.hide(help_page)


    def show_help():
        notebook.add(help_page)


    root = tk.Tk()
    root.geometry("300x220")
    root.title("hide")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    home_page = ttk.Frame(notebook, padding=10)
    help_page = ttk.Frame(notebook, padding=10)
    notebook.add(home_page, text="Home")
    notebook.add(help_page, text="Help")

    ttk.Button(home_page, text="Hide Help tab", command=hide_help).pack(pady=5)
    ttk.Button(home_page, text="Show Help tab", command=show_help).pack(pady=5)
    ttk.Label(help_page, text="Here is some help.").pack()

    root.mainloop()

tabs
~~~~~~~~~~~~~~~~~~

| ``notebook.tabs()`` gives a list of all the tabs. ``len(notebook.tabs())`` counts them.

----

A complete Notebook app
--------------------------

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def convert():
        try:
            celsius = float(celsius_entry.get())
            result_label.config(text=f"{celsius * 9 / 5 + 32:.1f} °F")
        except ValueError:
            result_label.config(text="Please type a number")


    def save_name():
        about_label.config(text="Made by " + name_entry.get())
        notebook.select(about_page)


    root = tk.Tk()
    root.geometry("320x220")
    root.title("Science tools")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    # Tab 1: converter
    convert_page = ttk.Frame(notebook, padding=15)
    notebook.add(convert_page, text="Converter")
    ttk.Label(convert_page, text="Temperature in °C:").pack()
    celsius_entry = ttk.Entry(convert_page, width=10)
    celsius_entry.pack(pady=5)
    ttk.Button(convert_page, text="Convert", command=convert).pack()
    result_label = ttk.Label(convert_page, text="", font=("Arial", 16))
    result_label.pack(pady=5)

    # Tab 2: settings
    settings_page = ttk.Frame(notebook, padding=15)
    notebook.add(settings_page, text="Settings")
    ttk.Label(settings_page, text="Your name:").pack()
    name_entry = ttk.Entry(settings_page)
    name_entry.pack(pady=5)
    ttk.Button(settings_page, text="Save", command=save_name).pack()

    # Tab 3: about
    about_page = ttk.Frame(notebook, padding=15)
    notebook.add(about_page, text="About")
    about_label = ttk.Label(about_page, text="Made by ???", font=("Arial", 14))
    about_label.pack(pady=20)

    root.mainloop()

----

Styling a Notebook
---------------------

| A Notebook uses two styles:

- ``"TNotebook"`` - the area behind the tabs: ``background``, ``tabmargins``.
- ``"TNotebook.Tab"`` - each tab: ``font``, ``padding``, ``foreground``, ``background``.

| Use ``style.map`` with ``"selected"`` to colour the tab being shown.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("320x200")
    root.title("Notebook style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TNotebook", background="lightgray")
    style.configure("TNotebook.Tab", font=("Arial", 12), padding=(15, 5), background="silver")
    style.map("TNotebook.Tab", background=[("selected", "gold")],
              foreground=[("selected", "black")])

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    for name in ["Maths", "Science", "English"]:
        page = ttk.Frame(notebook, padding=10)
        notebook.add(page, text=name)
        ttk.Label(page, text=f"{name} homework").pack()

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
    * - ``width``, ``height``
      - Size of the page area
      - ``width=250, height=120``
    * - ``padding``
      - Space around the pages
      - ``padding=10``
    * - ``add()``
      - Add a page as a tab
      - ``notebook.add(page, text="Home")``
    * - ``add(..., state=)``
      - Tab on, off or hidden
      - ``state="disabled"``
    * - ``select()``
      - Show a tab
      - ``notebook.select(1)``
    * - ``index("current")``
      - Number of the tab being shown
      - ``notebook.index("current")``
    * - ``tab()``
      - Read or change a tab
      - ``notebook.tab(1, state="normal")``
    * - ``bind("<<NotebookTabChanged>>")``
      - Run a function when the tab changes
      - ``notebook.bind("<<NotebookTabChanged>>", go)``
    * - ``hide()``, ``forget()``
      - Hide or remove a tab
      - ``notebook.hide(page)``
    * - ``tabs()``
      - List the tabs
      - ``len(notebook.tabs())``
    * - ``"TNotebook.Tab"``
      - Style name of the tabs
      - ``style.configure("TNotebook.Tab", padding=10)``

----

.. admonition:: Tasks

    #. Make a window titled "My app" that is 300x200 with a Notebook that fills the window and has three tabs: "Home", "Games" and "Help". Put a label on each page.
    #. Add a "Go to Games" button on the Home page that switches to the Games tab.
    #. Make a fourth tab "Bonus" that starts disabled. Add a button on the Games page that unlocks it.
    #. Style the tabs so they use Arial size 12 and the chosen tab is light green.

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
                    root.title("My app")

                    notebook = ttk.Notebook(root)
                    notebook.pack(fill="both", expand=True)

                    home_page = ttk.Frame(notebook, padding=10)
                    games_page = ttk.Frame(notebook, padding=10)
                    help_page = ttk.Frame(notebook, padding=10)
                    notebook.add(home_page, text="Home")
                    notebook.add(games_page, text="Games")
                    notebook.add(help_page, text="Help")

                    ttk.Label(home_page, text="Welcome!").pack()
                    ttk.Label(games_page, text="Pick a game").pack()
                    ttk.Label(help_page, text="Ask your teacher").pack()

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("My app")

                    notebook = ttk.Notebook(root)
                    notebook.pack(fill="both", expand=True)

                    home_page = ttk.Frame(notebook, padding=10)
                    games_page = ttk.Frame(notebook, padding=10)
                    help_page = ttk.Frame(notebook, padding=10)
                    notebook.add(home_page, text="Home")
                    notebook.add(games_page, text="Games")
                    notebook.add(help_page, text="Help")

                    ttk.Label(home_page, text="Welcome!").pack()
                    ttk.Button(home_page, text="Go to Games",
                               command=lambda: notebook.select(games_page)).pack(pady=10)
                    ttk.Label(games_page, text="Pick a game").pack()
                    ttk.Label(help_page, text="Ask your teacher").pack()

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def unlock():
                        notebook.tab(bonus_page, state="normal")
                        notebook.select(bonus_page)


                    root = tk.Tk()
                    root.geometry("320x200")
                    root.title("My app")

                    notebook = ttk.Notebook(root)
                    notebook.pack(fill="both", expand=True)

                    home_page = ttk.Frame(notebook, padding=10)
                    games_page = ttk.Frame(notebook, padding=10)
                    help_page = ttk.Frame(notebook, padding=10)
                    bonus_page = ttk.Frame(notebook, padding=10)
                    notebook.add(home_page, text="Home")
                    notebook.add(games_page, text="Games")
                    notebook.add(help_page, text="Help")
                    notebook.add(bonus_page, text="Bonus", state="disabled")

                    ttk.Label(home_page, text="Welcome!").pack()
                    ttk.Label(games_page, text="Pick a game").pack()
                    ttk.Button(games_page, text="Unlock bonus", command=unlock).pack(pady=10)
                    ttk.Label(help_page, text="Ask your teacher").pack()
                    ttk.Label(bonus_page, text="You found the bonus!").pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("My app")

                    style = ttk.Style()
                    style.theme_use("clam")
                    style.configure("TNotebook.Tab", font=("Arial", 12))
                    style.map("TNotebook.Tab", background=[("selected", "lightgreen")])

                    notebook = ttk.Notebook(root)
                    notebook.pack(fill="both", expand=True)

                    for name in ["Home", "Games", "Help"]:
                        page = ttk.Frame(notebook, padding=10)
                        notebook.add(page, text=name)
                        ttk.Label(page, text=f"The {name} page").pack()

                    root.mainloop()
