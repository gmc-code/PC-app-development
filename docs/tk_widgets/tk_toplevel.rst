====================================================
tk Toplevel
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Toplevel>`_

----

What is a Toplevel?
----------------------

| A **Toplevel** is an **extra window**.
| Every program has one main window (``root``). A Toplevel opens another window on top of it, e.g. a Settings window, a Help window or a pop-up message.
| You can put any widgets in a Toplevel, just like in ``root``.

----

Making a Toplevel
--------------------

| A Toplevel is usually opened when the user clicks a button, so it is made **inside a function**.

#. **Create** the window with ``tk.Toplevel(root)``.
#. **Set** its title and size, just like ``root``.
#. **Put widgets in it.** Use the Toplevel's name, not ``root``, as the first thing in the brackets.

| A Toplevel does **not** need ``.pack()`` or its own ``mainloop()``. It appears by itself.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library


    def open_window():
        new_window = tk.Toplevel(root)              # 1. Create the extra window
        new_window.title("Second window")           # 2. Title and size
        new_window.geometry("250x150")

        hello_label = tk.Label(new_window, text="Hello from the new window!")   # 3. "new_window"
        hello_label.pack(pady=40)


    root = tk.Tk()                  # Make the main window
    root.geometry("300x200")
    root.title("Main window")

    open_button = tk.Button(root, text="Open a new window", command=open_window)
    open_button.pack(pady=60)

    root.mainloop()                 # Keep the main window open

| Click the button several times: each click opens another window.
| Closing a Toplevel only closes that window. Closing ``root`` closes **every** window and ends the program.

----

Toplevel options
-------------------

| Options are written as ``option=value`` inside ``tk.Toplevel( )``, separated by commas.

bg (background colour)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What it does:** sets the background colour of the new window.
| **How to write it:** ``bg="colour"``

.. code-block:: python

    import tkinter as tk


    def open_window():
        yellow_window = tk.Toplevel(root, bg="lightyellow")
        yellow_window.title("Yellow window")
        yellow_window.geometry("250x150")
        tk.Label(yellow_window, text="I am yellow", bg="lightyellow").pack(pady=40)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("bg")

    tk.Button(root, text="Open", command=open_window).pack(pady=60)

    root.mainloop()

| ``tk.Label(...).pack()`` creates and places a widget in one line. Only do this when you never need to use the widget's name again.

padx and pady
~~~~~~~~~~~~~~~~~~

| **What they do:** add empty space around the inside edge of the window.
| **How to write them:** ``padx=20``, ``pady=20`` (pixels)

.. code-block:: python

    import tkinter as tk


    def open_window():
        padded_window = tk.Toplevel(root, padx=30, pady=30, bg="white")
        padded_window.title("Padded")
        tk.Label(padded_window, text="There is space all around me", bg="lightblue").pack()


    root = tk.Tk()
    root.geometry("300x200")
    root.title("padx and pady")

    tk.Button(root, text="Open", command=open_window).pack(pady=60)

    root.mainloop()

| This window has no ``geometry``, so it is just big enough to fit its widgets and padding.

----

Toplevel methods
-------------------

| A **method** is an action that a widget can do. Methods are written after a dot. Most of these also work on ``root``.

title
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the words in the window's title bar.
| **How to write it:** ``window.title("words")``

geometry
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the size of the window, and where it appears on the screen.
| **How to write it:** ``window.geometry("width x height")`` e.g. ``"300x200"``
| Add ``+x+y`` to choose where it appears: ``"300x200+100+50"`` puts the top-left corner 100 pixels from the left of the screen and 50 pixels from the top.

.. code-block:: python

    import tkinter as tk


    def open_window():
        help_window = tk.Toplevel(root)
        help_window.title("Help")                       # title
        help_window.geometry("250x120+100+100")         # size and position
        tk.Label(help_window, text="Click Start to play.").pack(pady=40)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("title and geometry")

    tk.Button(root, text="Help", command=open_window).pack(pady=60)

    root.mainloop()

destroy
~~~~~~~~~~~~~~~~~~

| **What it does:** closes the window.
| **How to write it:** ``window.destroy()``
| Use ``command=window.destroy`` (no brackets) for a Close button inside the window.

.. code-block:: python

    import tkinter as tk


    def open_window():
        pop_up = tk.Toplevel(root)
        pop_up.title("Message")
        pop_up.geometry("250x120")
        tk.Label(pop_up, text="Your work has been saved.").pack(pady=20)
        tk.Button(pop_up, text="Close", command=pop_up.destroy).pack()


    root = tk.Tk()
    root.geometry("300x200")
    root.title("destroy")

    tk.Button(root, text="Save", command=open_window).pack(pady=60)

    root.mainloop()

resizable
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses whether the user can drag the edges to resize the window.
| **How to write it:** ``window.resizable(False, False)``
| The first value is for the width, the second is for the height.

.. code-block:: python

    import tkinter as tk


    def open_window():
        fixed = tk.Toplevel(root)
        fixed.title("Fixed size")
        fixed.geometry("250x120")
        fixed.resizable(False, False)       # Cannot be resized
        tk.Label(fixed, text="Try to resize me!").pack(pady=40)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("resizable")

    tk.Button(root, text="Open", command=open_window).pack(pady=60)

    root.mainloop()

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options **after** the window has been made.
| **How to write it:** ``window.config(option=value)``

.. code-block:: python

    import tkinter as tk


    def open_window():
        party = tk.Toplevel(root)
        party.title("Party")
        party.geometry("250x150")
        tk.Button(party, text="Pink", command=lambda: party.config(bg="pink")).pack(pady=10)
        tk.Button(party, text="Gold", command=lambda: party.config(bg="gold")).pack()


    root = tk.Tk()
    root.geometry("300x200")
    root.title("config")

    tk.Button(root, text="Open", command=open_window).pack(pady=60)

    root.mainloop()

grab_set
~~~~~~~~~~~~~~~~~~

| **What it does:** makes the user deal with this window **first**. The main window ignores clicks until the Toplevel is closed.
| **How to write it:** ``window.grab_set()``
| This is useful for questions that **must** be answered, like "Are you sure?".

.. code-block:: python

    import tkinter as tk


    def ask():
        question = tk.Toplevel(root)
        question.title("Are you sure?")
        question.geometry("250x120")
        question.grab_set()                 # The main window cannot be clicked
        tk.Label(question, text="Delete everything?").pack(pady=10)
        tk.Button(question, text="Yes", width=8, command=lambda: yes(question)).pack(side="left", padx=25)
        tk.Button(question, text="No", width=8, command=question.destroy).pack(side="left")


    def yes(window):
        status_label.config(text="Everything deleted!")
        window.destroy()


    root = tk.Tk()
    root.geometry("300x200")
    root.title("grab_set")

    tk.Button(root, text="Delete", command=ask).pack(pady=30)
    status_label = tk.Label(root, text="")
    status_label.pack()

    root.mainloop()

transient
~~~~~~~~~~~~~~~~~~

| **What it does:** keeps the Toplevel on top of the main window, and hides it if the main window is minimised.
| **How to write it:** ``window.transient(root)``

.. code-block:: python

    import tkinter as tk


    def open_tools():
        tools = tk.Toplevel(root)
        tools.title("Tools")
        tools.geometry("150x150")
        tools.transient(root)               # Always stays in front of root
        tk.Button(tools, text="Pencil").pack(pady=5)
        tk.Button(tools, text="Eraser").pack(pady=5)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("transient")

    tk.Button(root, text="Show tools", command=open_tools).pack(pady=60)

    root.mainloop()

withdraw and deiconify
~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``withdraw()`` hides a window without closing it. ``deiconify()`` shows it again.
| Unlike ``destroy()``, the window and everything in it is kept, so it comes back exactly as it was.

.. code-block:: python

    import tkinter as tk


    def hide():
        notes_window.withdraw()


    def show():
        notes_window.deiconify()


    root = tk.Tk()
    root.geometry("300x200")
    root.title("withdraw")

    notes_window = tk.Toplevel(root)
    notes_window.title("Notes")
    notes_window.geometry("200x150")
    tk.Text(notes_window).pack()

    tk.Button(root, text="Hide notes", command=hide).pack(pady=20)
    tk.Button(root, text="Show notes", command=show).pack()

    root.mainloop()

| Type something in the Notes window, hide it, then show it again: your typing is still there.

----

Sending information between windows
---------------------------------------

| Widgets in the Toplevel can change widgets in the main window, and the other way round.
| This "Change name" window updates a label in the main window.

.. code-block:: python

    import tkinter as tk


    def open_settings():
        settings = tk.Toplevel(root)
        settings.title("Settings")
        settings.geometry("250x130")
        settings.grab_set()

        tk.Label(settings, text="New name:").pack(pady=5)
        name_entry = tk.Entry(settings)
        name_entry.pack()

        def save():
            name_label.config(text="Player: " + name_entry.get())     # Change the main window
            settings.destroy()

        tk.Button(settings, text="Save", command=save).pack(pady=10)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Game")

    name_label = tk.Label(root, text="Player: ???", font=("Arial", 16))
    name_label.pack(pady=30)

    tk.Button(root, text="Change name", command=open_settings).pack()

    root.mainloop()

| The ``save`` function is written **inside** ``open_settings``, so it can use ``name_entry`` and ``settings``.

----

Quick reference
-------------------

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option or method
      - What it does
      - Example
    * - ``tk.Toplevel(root)``
      - Make an extra window
      - ``win = tk.Toplevel(root)``
    * - ``bg``
      - Background colour
      - ``tk.Toplevel(root, bg="pink")``
    * - ``padx``, ``pady``
      - Space inside the window edge
      - ``padx=20, pady=20``
    * - ``title()``
      - Words in the title bar
      - ``win.title("Help")``
    * - ``geometry()``
      - Size (and position)
      - ``win.geometry("300x200+50+50")``
    * - ``destroy()``
      - Close the window
      - ``command=win.destroy``
    * - ``resizable()``
      - Allow or stop resizing
      - ``win.resizable(False, False)``
    * - ``config()``
      - Change options later
      - ``win.config(bg="gold")``
    * - ``grab_set()``
      - Must close this window first
      - ``win.grab_set()``
    * - ``transient()``
      - Keep in front of the main window
      - ``win.transient(root)``
    * - ``withdraw()``, ``deiconify()``
      - Hide and show again
      - ``win.withdraw()``

----

.. admonition:: Tasks

    #. Make a main window titled "Main" with a button "About". When clicked, a new window titled "About" opens, 250x100 in size, with the label "Made by" and your name.
    #. Add a "Close" button to the About window that closes it.
    #. Make the About window light blue and stop it from being resized.
    #. Make a main window with a label "Score: 0" and a button "Bonus". The button opens a Toplevel with an "Add 10 points" button that adds 10 to the score in the main window.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    import tkinter as tk


                    def open_about():
                        about = tk.Toplevel(root)
                        about.title("About")
                        about.geometry("250x100")
                        tk.Label(about, text="Made by Sam").pack(pady=20)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Main")

                    tk.Button(root, text="About", command=open_about).pack(pady=60)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk


                    def open_about():
                        about = tk.Toplevel(root)
                        about.title("About")
                        about.geometry("250x100")
                        tk.Label(about, text="Made by Sam").pack(pady=10)
                        tk.Button(about, text="Close", command=about.destroy).pack()


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Main")

                    tk.Button(root, text="About", command=open_about).pack(pady=60)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk


                    def open_about():
                        about = tk.Toplevel(root, bg="lightblue")
                        about.title("About")
                        about.geometry("250x100")
                        about.resizable(False, False)
                        tk.Label(about, text="Made by Sam", bg="lightblue").pack(pady=10)
                        tk.Button(about, text="Close", command=about.destroy).pack()


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Main")

                    tk.Button(root, text="About", command=open_about).pack(pady=60)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def add_ten():
                        score = int(score_label.cget("text").replace("Score: ", ""))
                        score_label.config(text=f"Score: {score + 10}")


                    def open_bonus():
                        bonus = tk.Toplevel(root)
                        bonus.title("Bonus")
                        bonus.geometry("200x100")
                        tk.Button(bonus, text="Add 10 points", command=add_ten).pack(pady=30)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Game")

                    score_label = tk.Label(root, text="Score: 0", font=("Arial", 18))
                    score_label.pack(pady=30)

                    tk.Button(root, text="Bonus", command=open_bonus).pack()

                    root.mainloop()
