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

All Toplevel options
---------------------------

| Here is every option a Toplevel can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``bg`` or ``background``
      - Background colour of the window
      - ``bg="lightyellow"``
    * - ``bd`` or ``borderwidth``
      - How thick the border is
      - ``bd=3``
    * - ``class_``
      - A group name used to style many widgets at once (advanced). Written ``class_`` in Python
      - ``class_="Sidebar"``
    * - ``colormap``
      - Which set of colours to use (advanced, rarely needed)
      - ``colormap="new"``
    * - ``container``
      - Lets another program be placed inside it (advanced, rarely needed)
      - ``container=False``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``height``
      - How tall it is (in pixels)
      - ``height=200``
    * - ``highlightbackground``
      - Colour of the focus outline when it is not selected by the keyboard
      - ``highlightbackground="white"``
    * - ``highlightcolor``
      - Colour of the focus outline when it is selected by the keyboard
      - ``highlightcolor="blue"``
    * - ``highlightthickness``
      - How thick the focus outline is
      - ``highlightthickness=2``
    * - ``menu``
      - A menu bar for the window
      - ``menu=menu_bar``
    * - ``padx``
      - Extra space inside it, on the left and right
      - ``padx=10``
    * - ``pady``
      - Extra space inside it, at the top and bottom
      - ``pady=10``
    * - ``relief``
      - Border style: ``"raised"``, ``"sunken"``, ``"flat"``, ``"ridge"``, ``"groove"`` or ``"solid"``
      - ``relief="sunken"``
    * - ``screen``
      - Which screen the window opens on (advanced, rarely needed)
      - ``screen=":0"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``use``
      - Puts the window inside another program's window (advanced)
      - ``use=window_id``
    * - ``visual``
      - Colour mode for the window (advanced, rarely needed)
      - ``visual="truecolor"``
    * - ``width``
      - How wide it is (in pixels)
      - ``width=300``

----

Quiz
--------------------------------

.. mcqgroup::
    :nav_position: top
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 20

    .. multichoice::

        What is a Toplevel?

        [x] A new window that opens on top of the main window | Correct. It is a second window.
        [ ] A frame at the top | Incorrect. It is a whole window.
        [ ] The main window | Incorrect. The main window is tk.Tk().
        [ ] A menu bar | Incorrect. That is a Menu.

    .. multichoice::

        How many tk.Tk() windows should a program have?

        [ ] One for every window | Incorrect. Use Toplevel for extra windows.
        [x] Only one | Correct. Extra windows should be Toplevels.
        [ ] Two | Incorrect. Only one.
        [ ] None | Incorrect. One is needed.

    .. multichoice::

        Which line makes a new window?

        [ ] new_window = tk.Tk() | Incorrect. That makes a second main window.
        [x] new_window = tk.Toplevel(root) | Correct. Toplevel makes an extra window.
        [ ] new_window = tk.Window(root) | Incorrect. Not a widget.
        [ ] new_window = root.new() | Incorrect. Not a method.

    .. multichoice::

        How do you put a Label in the new window?

        [x] tk.Label(new_window, text="Hi").pack() | Correct. The new window is the parent.
        [ ] tk.Label(root, text="Hi").pack() | Incorrect. That goes in the main window.
        [ ] new_window.Label("Hi") | Incorrect. Use tk.Label.
        [ ] tk.Label(text="Hi", window=new_window) | Incorrect. The parent goes first.

    .. multichoice::

        What does new_window.title("Settings") do?

        [ ] Adds a Label | Incorrect. It sets the title bar.
        [x] Sets the words in the window's title bar | Correct. title names the window.
        [ ] Closes the window | Incorrect. destroy does that.
        [ ] Makes it bigger | Incorrect. geometry does that.

    .. multichoice::

        What does new_window.geometry("300x200") do?

        [x] Makes the window 300 wide and 200 high | Correct. geometry sets the size.
        [ ] Moves it to 300, 200 | Incorrect. That needs +x+y.
        [ ] Makes it 300 high | Incorrect. Width comes first.
        [ ] Adds 300 widgets | Incorrect. It sets size.

    .. multichoice::

        What does geometry("300x200+100+50") do?

        [ ] Makes it 100 by 50 | Incorrect. The first part is the size.
        [x] Makes it 300 by 200 and puts it 100 across and 50 down the screen | Correct. +x+y sets the position.
        [ ] Causes an error | Incorrect. It is allowed.
        [ ] Makes 2 windows | Incorrect. One window.

    .. multichoice::

        What does new_window.destroy() do?

        [ ] Closes the whole program | Incorrect. Only this window closes.
        [x] Closes this Toplevel window | Correct. The main window stays open.
        [ ] Hides it for later | Incorrect. withdraw hides it.
        [ ] Empties it | Incorrect. It closes it.

    .. multichoice::

        What does resizable(False, False) do?

        [x] Stops the user changing the window's width and height | Correct. Both directions are locked.
        [ ] Makes it full screen | Incorrect. It locks the size.
        [ ] Hides it | Incorrect. It locks the size.
        [ ] Makes it bigger | Incorrect. It locks it.

    .. multichoice::

        What does bg="lightyellow" do on a Toplevel?

        [ ] Colours the title bar | Incorrect. The title bar is set by the computer.
        [x] Colours the window's background | Correct. bg is the background.
        [ ] Colours the words | Incorrect. Not words.
        [ ] Nothing | Incorrect. It colours the window.

    .. multichoice::

        What do padx and pady do on a Toplevel?

        [ ] Move the window | Incorrect. geometry moves it.
        [x] Add space inside the window's edges | Correct. They pad the inside.
        [ ] Add more windows | Incorrect. They add space.
        [ ] Change the title | Incorrect. title does that.

    .. multichoice::

        What does grab_set() do?

        [x] Makes the user finish with this window before using the main window | Correct. It makes the window modal.
        [ ] Closes the window | Incorrect. destroy does that.
        [ ] Grabs the mouse forever | Incorrect. Only while the window is open.
        [ ] Moves the window | Incorrect. geometry moves it.

    .. multichoice::

        What does transient(root) do?

        [ ] Makes the window see-through | Incorrect. It links the windows.
        [x] Keeps the new window on top of the main window and links them | Correct. It acts like a dialog.
        [ ] Closes root | Incorrect. It does not close.
        [ ] Makes it bigger | Incorrect. It links windows.

    .. multichoice::

        What does withdraw() do?

        [x] Hides the window without closing it | Correct. Use deiconify to show it again.
        [ ] Closes it forever | Incorrect. destroy closes.
        [ ] Shrinks it | Incorrect. It hides it.
        [ ] Deletes its widgets | Incorrect. It hides the window.

    .. multichoice::

        What does deiconify() do?

        [ ] Deletes the icon | Incorrect. It shows the window.
        [x] Shows a hidden window again | Correct. It undoes withdraw.
        [ ] Hides the window | Incorrect. withdraw hides.
        [ ] Minimises it | Incorrect. It shows it.

    .. multichoice::

        Which line changes the window's colour later?

        [x] new_window.config(bg="pink") | Correct. config changes options.
        [ ] new_window.bg("pink") | Incorrect. Not a method.
        [ ] new_window.colour = "pink" | Incorrect. Use config.
        [ ] new_window.title("pink") | Incorrect. title sets the title.

    .. multichoice::

        Which is the best way to open a new window when a button is clicked?

        [ ] Make the Toplevel at the start | Incorrect. It would open straight away.
        [x] Make the Toplevel inside the button's command function | Correct. It opens on click.
        [ ] Use root.mainloop() again | Incorrect. Only one mainloop is needed.
        [ ] Use tk.Tk() in the function | Incorrect. Use Toplevel.

    .. multichoice::

        What happens to Toplevels when the main window is closed?

        [ ] They stay open | Incorrect. They close too.
        [x] They close as well | Correct. They belong to the main window.
        [ ] They become the main window | Incorrect. They close.
        [ ] An error happens | Incorrect. They close.

    .. multichoice::

        Which button command closes only the Toplevel?

        [x] command=new_window.destroy | Correct. destroy closes that window.
        [ ] command=root.destroy | Incorrect. That closes everything.
        [ ] command=new_window.title | Incorrect. title sets the title.
        [ ] command=root.quit() | Incorrect. The brackets run it straight away.

    .. multichoice::

        How do you make a Toplevel window for settings?

        [ ] settings = tk.Frame(root) | Incorrect. A Frame is not a window.
        [x] settings = tk.Toplevel(root) | Correct. It opens a new window.
        [ ] settings = tk.Settings() | Incorrect. Not a widget.
        [ ] settings = tk.Tk(root) | Incorrect. Use Toplevel.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Open a new window when a button is clicked.

        def open_window():
            new_window = tk.@@Toplevel | Tk | Frame@@(root)
            new_window.@@title | name | label@@("Settings")
            new_window.@@geometry | size | config@@("300x200")

    .. cloze::
        :instructions: Put widgets in the new window.

        tk.Label(@@new_window | root | window@@, text="Settings").pack()
        tk.Button(new_window, text="Close", command=new_window.@@destroy | mainloop | close@@).pack()

    .. cloze::
        :instructions: Stop resizing and colour the window.

        new_window.@@resizable | resize | fixed@@(False, False)
        new_window.config(@@bg | fg | colour@@="lightyellow")

    .. cloze::
        :instructions: Make the window act like a dialog.

        new_window.@@transient | grab | modal@@(root)
        new_window.@@grab_set | focus_set | grab@@()

    .. cloze::
        :instructions: Hide and show a window.

        help_window.@@withdraw | destroy | hide@@()
        help_window.@@deiconify | show | open@@()

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
