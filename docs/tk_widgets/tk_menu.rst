====================================================
tk Menu
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Menu>`_

----

What is a Menu?
-------------------

| A **Menu** is a list of commands the user can choose from.
| The most common kind is the **menu bar** along the top of a window, with words like **File**, **Edit** and **Help**. Clicking a word opens a drop-down list of commands.
| A menu can also pop up when the user right-clicks.

----

Making a menu bar
--------------------

| A menu bar is built in layers:

#. **Create** the menu bar with ``tk.Menu(root)`` and attach it to the window with ``root.config(menu=menubar)``.
#. **Create** a drop-down menu (e.g. File) with ``tk.Menu(menubar, tearoff=0)``.
#. **Add** commands to the drop-down menu with ``.add_command(...)``.
#. **Add** the drop-down menu to the menu bar with ``menubar.add_cascade(...)``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library


    def say_hello():
        message_label.config(text="Hello!")


    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first menu")     # Words in the title bar

    menubar = tk.Menu(root)                     # 1. Create the menu bar
    root.config(menu=menubar)                   #    and attach it to the window

    file_menu = tk.Menu(menubar, tearoff=0)     # 2. Create the File drop-down menu

    file_menu.add_command(label="Say hello", command=say_hello)    # 3. Add commands
    file_menu.add_command(label="Exit", command=root.destroy)

    menubar.add_cascade(label="File", menu=file_menu)              # 4. Put "File" on the bar

    message_label = tk.Label(root, text="Click File at the top", font=("Arial", 14))
    message_label.pack(pady=40)

    root.mainloop()                 # Keep the window open

----

Menu options
-------------------

| Options are written as ``option=value`` inside ``tk.Menu( )``, separated by commas.

tearoff
~~~~~~~~~~~~~~~~~~

| **What it does:** controls the dashed line at the top of a drop-down menu. Clicking that line "tears off" the menu into its own small window.
| **How to write it:** ``tearoff=0``
| Almost every program uses ``tearoff=0`` to hide the dashed line, because most users find it confusing.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("tearoff")

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    with_line = tk.Menu(menubar, tearoff=1)
    with_line.add_command(label="Open")
    menubar.add_cascade(label="Tearoff on", menu=with_line)

    without_line = tk.Menu(menubar, tearoff=0)
    without_line.add_command(label="Open")
    menubar.add_cascade(label="Tearoff off", menu=without_line)

    root.mainloop()

font, fg and bg
~~~~~~~~~~~~~~~~~~

| **What they do:** ``font`` sets the style and size of the words in a drop-down menu. ``fg`` and ``bg`` set the word and background colours.
| **How to write them:** ``font=("Arial", 14)``, ``fg="white"``, ``bg="navy"``
| **Note:** on Windows, these change the **drop-down** menus but not the menu bar itself.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("font, fg and bg")

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    colour_menu = tk.Menu(menubar, tearoff=0, font=("Arial", 14), fg="white", bg="navy")
    colour_menu.add_command(label="Red")
    colour_menu.add_command(label="Green")
    menubar.add_cascade(label="Colours", menu=colour_menu)

    root.mainloop()

activebackground and activeforeground
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** set the colours of the command the mouse is pointing at.
| **How to write them:** ``activebackground="gold"``, ``activeforeground="black"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("active colours")

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    game_menu = tk.Menu(menubar, tearoff=0, activebackground="gold", activeforeground="black")
    game_menu.add_command(label="New game")
    game_menu.add_command(label="High scores")
    menubar.add_cascade(label="Game", menu=game_menu)

    root.mainloop()

----

Menu methods
-------------------

| A **method** is an action that a widget can do. Methods are written after a dot, e.g. ``file_menu.add_command(...)``.

add_command
~~~~~~~~~~~~~~~~~~

| **What it does:** adds a command to a menu.
| **How to write it:** ``menu.add_command(label="words", command=function_name)``
| ``label`` is the words shown. ``command`` is the function to run (no brackets).
| ``accelerator="Ctrl+N"`` shows a keyboard shortcut next to the words. (It only **shows** the shortcut; see **bind** below to make the keys work.)

.. code-block:: python

    import tkinter as tk


    def new_note():
        notes_box.delete("1.0", tk.END)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("add_command")

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New", command=new_note, accelerator="Ctrl+N")
    file_menu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)

    notes_box = tk.Text(root, height=8)
    notes_box.insert("1.0", "Some notes...")
    notes_box.pack(fill="both", expand=True)

    root.mainloop()

add_cascade
~~~~~~~~~~~~~~~~~~

| **What it does:** adds a drop-down menu to the menu bar, or puts a smaller menu **inside** another menu (a sub-menu).
| **How to write it:** ``menubar.add_cascade(label="words", menu=drop_down_menu)``

.. code-block:: python

    import tkinter as tk


    def set_size(size):
        word_label.config(font=("Arial", size))


    root = tk.Tk()
    root.geometry("300x200")
    root.title("add_cascade")

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    view_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="View", menu=view_menu)       # View on the menu bar

    size_menu = tk.Menu(view_menu, tearoff=0)
    size_menu.add_command(label="Small", command=lambda: set_size(10))
    size_menu.add_command(label="Large", command=lambda: set_size(30))
    view_menu.add_cascade(label="Text size", menu=size_menu)    # Sub-menu inside View

    word_label = tk.Label(root, text="Hello", font=("Arial", 10))
    word_label.pack(pady=40)

    root.mainloop()

| ``lambda:`` lets each command send a different number to the same function. See the **Button** page for more about ``lambda``.

add_separator
~~~~~~~~~~~~~~~~~~

| **What it does:** draws a line across the menu to split the commands into groups.
| **How to write it:** ``menu.add_separator()``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("add_separator")

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")
    file_menu.add_separator()                       # A line between the groups
    file_menu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)

    root.mainloop()

add_checkbutton
~~~~~~~~~~~~~~~~~~

| **What it does:** adds a command that can be ticked on and off, like a **Checkbutton**.
| **How to write it:** ``menu.add_checkbutton(label="words", variable=int_var, command=function_name)``

.. code-block:: python

    import tkinter as tk


    def change_theme():
        if dark.get() == 1:
            root.config(bg="black")
        else:
            root.config(bg="white")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("add_checkbutton")
    root.config(bg="white")

    dark = tk.IntVar()

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    view_menu = tk.Menu(menubar, tearoff=0)
    view_menu.add_checkbutton(label="Dark mode", variable=dark, command=change_theme)
    menubar.add_cascade(label="View", menu=view_menu)

    root.mainloop()

add_radiobutton
~~~~~~~~~~~~~~~~~~

| **What it does:** adds a group of commands where only **one** can be chosen, like **Radiobuttons**.
| **How to write it:** ``menu.add_radiobutton(label="words", variable=string_var, value="value", command=function_name)``

.. code-block:: python

    import tkinter as tk


    def change_level():
        level_label.config(text="Level: " + level.get())


    root = tk.Tk()
    root.geometry("300x200")
    root.title("add_radiobutton")

    level = tk.StringVar(value="Easy")

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    level_menu = tk.Menu(menubar, tearoff=0)
    for choice in ["Easy", "Medium", "Hard"]:
        level_menu.add_radiobutton(label=choice, variable=level, value=choice,
                                   command=change_level)
    menubar.add_cascade(label="Level", menu=level_menu)

    level_label = tk.Label(root, text="Level: Easy", font=("Arial", 16))
    level_label.pack(pady=40)

    root.mainloop()

entryconfig
~~~~~~~~~~~~~~~~~~

| **What it does:** changes one command in a menu, e.g. to turn it off (grey it out) or change its words.
| **How to write it:** ``menu.entryconfig("label", state="disabled")``
| Use ``state="normal"`` to turn it back on.

.. code-block:: python

    import tkinter as tk


    def start():
        game_menu.entryconfig("Start", state="disabled")
        game_menu.entryconfig("Stop", state="normal")
        status_label.config(text="Playing...")


    def stop():
        game_menu.entryconfig("Start", state="normal")
        game_menu.entryconfig("Stop", state="disabled")
        status_label.config(text="Stopped")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("entryconfig")

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    game_menu = tk.Menu(menubar, tearoff=0)
    game_menu.add_command(label="Start", command=start)
    game_menu.add_command(label="Stop", command=stop, state="disabled")
    menubar.add_cascade(label="Game", menu=game_menu)

    status_label = tk.Label(root, text="Stopped", font=("Arial", 16))
    status_label.pack(pady=40)

    root.mainloop()

bind (keyboard shortcuts)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``accelerator`` only **shows** a shortcut. To make the keys work, use ``root.bind``.
| **How to write it:** ``root.bind("<Control-n>", function_name)``
| A function run by ``bind`` is given an ``event``, so use ``event=None`` to let it work from the menu **and** the keys.

.. code-block:: python

    import tkinter as tk


    def clear(event=None):
        notes_box.delete("1.0", tk.END)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Shortcuts")

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    edit_menu = tk.Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Clear", command=clear, accelerator="Ctrl+L")
    menubar.add_cascade(label="Edit", menu=edit_menu)

    root.bind("<Control-l>", clear)         # Make Ctrl+L work

    notes_box = tk.Text(root)
    notes_box.insert("1.0", "Press Ctrl+L to clear me")
    notes_box.pack(fill="both", expand=True)

    root.mainloop()

tk_popup (right-click menu)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What it does:** shows a menu where the mouse is, e.g. when the user right-clicks.
| **How to write it:** ``popup_menu.tk_popup(event.x_root, event.y_root)``
| ``"<Button-3>"`` is a right-click. ``event.x_root`` and ``event.y_root`` are where the mouse is on the screen.

.. code-block:: python

    import tkinter as tk


    def show_popup(event):
        popup_menu.tk_popup(event.x_root, event.y_root)


    def change_colour(colour):
        root.config(bg=colour)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Right-click menu")

    popup_menu = tk.Menu(root, tearoff=0)
    popup_menu.add_command(label="Pink", command=lambda: change_colour("pink"))
    popup_menu.add_command(label="Light blue", command=lambda: change_colour("lightblue"))
    popup_menu.add_command(label="White", command=lambda: change_colour("white"))

    root.bind("<Button-3>", show_popup)     # Right-click anywhere in the window

    tk.Label(root, text="Right-click me!", font=("Arial", 16)).pack(pady=60)

    root.mainloop()

----

A complete menu bar
----------------------

| This example puts several menus together on one menu bar.

.. code-block:: python

    import tkinter as tk


    def new():
        notes_box.delete("1.0", tk.END)


    def about():
        notes_box.insert(tk.END, "\nNote Pad version 1.0")


    def change_wrap():
        if wrap_on.get() == 1:
            notes_box.config(wrap="word")
        else:
            notes_box.config(wrap="none")


    root = tk.Tk()
    root.geometry("350x250")
    root.title("Note Pad")

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New", command=new)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)

    # View menu
    wrap_on = tk.IntVar(value=1)
    view_menu = tk.Menu(menubar, tearoff=0)
    view_menu.add_checkbutton(label="Word wrap", variable=wrap_on, command=change_wrap)
    menubar.add_cascade(label="View", menu=view_menu)

    # Help menu
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="About", command=about)
    menubar.add_cascade(label="Help", menu=help_menu)

    notes_box = tk.Text(root, wrap="word")
    notes_box.pack(fill="both", expand=True)

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
    * - ``root.config(menu=...)``
      - Attach the menu bar to the window
      - ``root.config(menu=menubar)``
    * - ``tearoff``
      - ``0`` hides the dashed tear-off line
      - ``tk.Menu(menubar, tearoff=0)``
    * - ``font``, ``fg``, ``bg``
      - Font and colours of a drop-down menu
      - ``font=("Arial", 14)``
    * - ``activebackground``
      - Colour of the command being pointed at
      - ``activebackground="gold"``
    * - ``add_command()``
      - Add a command
      - ``add_command(label="Save", command=save)``
    * - ``add_cascade()``
      - Add a drop-down or sub-menu
      - ``add_cascade(label="File", menu=file_menu)``
    * - ``add_separator()``
      - Add a dividing line
      - ``file_menu.add_separator()``
    * - ``add_checkbutton()``
      - Add a tick-on/tick-off command
      - ``add_checkbutton(label="Sound", variable=sound)``
    * - ``add_radiobutton()``
      - Add a choose-one command
      - ``add_radiobutton(label="Easy", variable=level, value="Easy")``
    * - ``entryconfig()``
      - Change one command
      - ``entryconfig("Save", state="disabled")``
    * - ``tk_popup()``
      - Show a menu where the mouse is
      - ``menu.tk_popup(event.x_root, event.y_root)``

----

.. admonition:: Tasks

    #. Make a window titled "Menus" that is 300x200. Add a menu bar with a "File" menu containing one command, "Exit", that closes the window.
    #. Add a "Colour" menu with the commands "Red", "Green" and "Blue" that change the window's background colour.
    #. Add a separator to your File menu and a "Clear colour" command above it that sets the background back to white.
    #. Make a right-click menu with the commands "Happy" and "Sad" that change a label to show ":)" or ":(".

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Menus")

                    menubar = tk.Menu(root)
                    root.config(menu=menubar)

                    file_menu = tk.Menu(menubar, tearoff=0)
                    file_menu.add_command(label="Exit", command=root.destroy)
                    menubar.add_cascade(label="File", menu=file_menu)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk


                    def change_colour(colour):
                        root.config(bg=colour)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Menus")

                    menubar = tk.Menu(root)
                    root.config(menu=menubar)

                    file_menu = tk.Menu(menubar, tearoff=0)
                    file_menu.add_command(label="Exit", command=root.destroy)
                    menubar.add_cascade(label="File", menu=file_menu)

                    colour_menu = tk.Menu(menubar, tearoff=0)
                    colour_menu.add_command(label="Red", command=lambda: change_colour("red"))
                    colour_menu.add_command(label="Green", command=lambda: change_colour("green"))
                    colour_menu.add_command(label="Blue", command=lambda: change_colour("blue"))
                    menubar.add_cascade(label="Colour", menu=colour_menu)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk


                    def change_colour(colour):
                        root.config(bg=colour)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Menus")

                    menubar = tk.Menu(root)
                    root.config(menu=menubar)

                    file_menu = tk.Menu(menubar, tearoff=0)
                    file_menu.add_command(label="Clear colour", command=lambda: change_colour("white"))
                    file_menu.add_separator()
                    file_menu.add_command(label="Exit", command=root.destroy)
                    menubar.add_cascade(label="File", menu=file_menu)

                    colour_menu = tk.Menu(menubar, tearoff=0)
                    colour_menu.add_command(label="Red", command=lambda: change_colour("red"))
                    colour_menu.add_command(label="Green", command=lambda: change_colour("green"))
                    colour_menu.add_command(label="Blue", command=lambda: change_colour("blue"))
                    menubar.add_cascade(label="Colour", menu=colour_menu)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def show_popup(event):
                        mood_menu.tk_popup(event.x_root, event.y_root)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Moods")

                    face_label = tk.Label(root, text="Right-click me", font=("Arial", 30))
                    face_label.pack(pady=50)

                    mood_menu = tk.Menu(root, tearoff=0)
                    mood_menu.add_command(label="Happy", command=lambda: face_label.config(text=":)"))
                    mood_menu.add_command(label="Sad", command=lambda: face_label.config(text=":("))

                    root.bind("<Button-3>", show_popup)

                    root.mainloop()
