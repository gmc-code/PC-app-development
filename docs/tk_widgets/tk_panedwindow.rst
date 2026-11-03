====================================================
tk PanedWindow
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.PanedWindow>`_

----

What is a PanedWindow?
-------------------------

| A **PanedWindow** splits part of a window into two or more sections called **panes**.
| Between the panes is a line called a **sash**. The user drags the sash to make one pane bigger and the other smaller.
| You have seen this in apps like File Explorer, where you can drag the line between the folder list and the files.

----

Making a PanedWindow
-------------------------

| A PanedWindow is made differently from most widgets. Widgets go **into** it with ``.add()``, not ``.pack()``.

#. **Create** the PanedWindow and **place** it with ``.pack()``.
#. **Create** a widget for each pane, using the PanedWindow as the parent.
#. **Add** each widget to the PanedWindow with ``.add(widget)``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first PanedWindow")

    panes = tk.PanedWindow(root)                    # 1. Create the PanedWindow
    panes.pack(fill="both", expand=True)            #    and fill the window

    left_label = tk.Label(panes, text="Left", bg="lightblue")      # 2. Create the widgets
    right_label = tk.Label(panes, text="Right", bg="lightgreen")

    panes.add(left_label)                           # 3. Add them as panes
    panes.add(right_label)

    root.mainloop()                 # Keep the window open

| Move the mouse over the line between the two colours, then drag it left and right.

----

PanedWindow options
----------------------

| Options are written as ``option=value`` inside ``tk.PanedWindow( )``, separated by commas.

orient
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses whether the panes sit side by side or one above the other.
| **How to write it:** ``orient="vertical"``
| **Values:** ``"horizontal"`` (side by side, the default) and ``"vertical"`` (top and bottom).

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("orient")

    panes = tk.PanedWindow(root, orient="vertical")
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Top", bg="pink"))
    panes.add(tk.Label(panes, text="Bottom", bg="lightyellow"))

    root.mainloop()

| ``panes.add(tk.Label(panes, ...))`` creates a label and adds it in one line.

sashwidth and sashrelief
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``sashwidth`` sets how thick the dragging line is, in pixels. ``sashrelief`` sets its border style.
| **How to write them:** ``sashwidth=8, sashrelief="raised"``
| A thicker sash is easier to find and drag.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("sashwidth")

    panes = tk.PanedWindow(root, sashwidth=10, sashrelief="raised")
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Drag the", bg="lightblue"))
    panes.add(tk.Label(panes, text="thick sash", bg="lightgreen"))

    root.mainloop()

bg
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the colour of the PanedWindow. This is the colour of the **sash**, because the panes cover the rest.
| **How to write it:** ``bg="colour"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("bg")

    panes = tk.PanedWindow(root, bg="red", sashwidth=6)
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Left", bg="white"))
    panes.add(tk.Label(panes, text="Right", bg="white"))

    root.mainloop()

showhandle
~~~~~~~~~~~~~~~~~~

| **What it does:** ``showhandle=True`` draws a small square handle on the sash, showing the user where to grab it.
| **How to write it:** ``showhandle=True``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("showhandle")

    panes = tk.PanedWindow(root, showhandle=True, sashwidth=6)
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Left", bg="lightblue"))
    panes.add(tk.Label(panes, text="Right", bg="lightgreen"))

    root.mainloop()

relief and borderwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** draw a border around the whole PanedWindow.
| **How to write them:** ``relief="solid", borderwidth=2``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("relief")

    panes = tk.PanedWindow(root, relief="solid", borderwidth=2)
    panes.pack(fill="both", expand=True, padx=10, pady=10)

    panes.add(tk.Label(panes, text="Left", bg="lightblue"))
    panes.add(tk.Label(panes, text="Right", bg="lightgreen"))

    root.mainloop()

----

PanedWindow methods
----------------------

| A **method** is an action that a widget can do. Methods are written after a dot, e.g. ``panes.add(...)``.

add
~~~~~~~~~~~~~~~~~~

| **What it does:** puts a widget into the PanedWindow as a new pane.
| **How to write it:** ``panes.add(widget)``
| Panes appear in the order they are added. Any widget can be a pane, including a **Frame** full of other widgets.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("400x200")
    root.title("add")

    panes = tk.PanedWindow(root, sashwidth=5)
    panes.pack(fill="both", expand=True)

    # Pane 1: a list of topics
    topic_list = tk.Listbox(panes)
    for topic in ["Planets", "Stars", "Moons"]:
        topic_list.insert(tk.END, topic)
    panes.add(topic_list)

    # Pane 2: a box for notes
    notes_box = tk.Text(panes, wrap="word")
    notes_box.insert("1.0", "Type your notes here")
    panes.add(notes_box)

    root.mainloop()

add with minsize and width
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``add()`` can also have options for that pane:

- ``width=150`` sets the starting width of the pane in pixels (use ``height`` for vertical panes).
- ``minsize=80`` stops the user dragging the pane smaller than 80 pixels.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("400x200")
    root.title("minsize")

    panes = tk.PanedWindow(root, sashwidth=5)
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="Menu", bg="lightblue"), width=100, minsize=80)
    panes.add(tk.Label(panes, text="Main area", bg="white"), minsize=150)

    root.mainloop()

forget
~~~~~~~~~~~~~~~~~~

| **What it does:** removes a pane from the PanedWindow.
| **How to write it:** ``panes.forget(widget)``
| Use ``panes.add(widget)`` to put it back.

.. code-block:: python

    import tkinter as tk


    def hide_help():
        panes.forget(help_label)


    def show_help():
        panes.add(help_label)


    root = tk.Tk()
    root.geometry("400x250")
    root.title("forget")

    panes = tk.PanedWindow(root, sashwidth=5)
    panes.pack(fill="both", expand=True)

    game_label = tk.Label(panes, text="Game area", bg="white")
    help_label = tk.Label(panes, text="Help:\nUse the arrow keys", bg="lightyellow")
    panes.add(game_label)
    panes.add(help_label)

    tk.Button(root, text="Hide help", command=hide_help).pack(side="left", padx=10, pady=5)
    tk.Button(root, text="Show help", command=show_help).pack(side="left", padx=10, pady=5)

    root.mainloop()

panes
~~~~~~~~~~~~~~~~~~

| **What it does:** gives back a list of the panes, so you can count them.
| **How to write it:** ``count = len(panes.panes())``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("panes")

    panes = tk.PanedWindow(root)
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="A", bg="pink"))
    panes.add(tk.Label(panes, text="B", bg="lightblue"))
    panes.add(tk.Label(panes, text="C", bg="lightgreen"))

    count_label = tk.Label(root, text=f"Number of panes: {len(panes.panes())}")
    count_label.pack()

    root.mainloop()

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options **after** the PanedWindow has been made.
| **How to write it:** ``panes.config(option=value)``

.. code-block:: python

    import tkinter as tk


    def flip():
        if panes.cget("orient") == "horizontal":
            panes.config(orient="vertical")
        else:
            panes.config(orient="horizontal")


    root = tk.Tk()
    root.geometry("300x250")
    root.title("config")

    panes = tk.PanedWindow(root, sashwidth=5)
    panes.pack(fill="both", expand=True)

    panes.add(tk.Label(panes, text="One", bg="lightblue"))
    panes.add(tk.Label(panes, text="Two", bg="lightgreen"))

    tk.Button(root, text="Flip", command=flip).pack(pady=5)

    root.mainloop()

----

Panes inside panes
---------------------

| A PanedWindow can be added to another PanedWindow. This makes layouts like a code editor: a list on the left, and on the right a top pane and a bottom pane.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("400x250")
    root.title("Panes inside panes")

    outer = tk.PanedWindow(root, orient="horizontal", sashwidth=5)
    outer.pack(fill="both", expand=True)

    outer.add(tk.Label(outer, text="Files", bg="lightblue"), width=100)

    inner = tk.PanedWindow(outer, orient="vertical", sashwidth=5)     # Inside "outer"
    outer.add(inner)

    inner.add(tk.Label(inner, text="Code", bg="white"), height=150)
    inner.add(tk.Label(inner, text="Output", bg="black", fg="white"))

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
    * - ``orient``
      - Side by side or top and bottom
      - ``orient="vertical"``
    * - ``sashwidth``
      - Thickness of the dragging line
      - ``sashwidth=8``
    * - ``sashrelief``
      - Border style of the dragging line
      - ``sashrelief="raised"``
    * - ``bg``
      - Colour of the sash
      - ``bg="gray"``
    * - ``showhandle``
      - Show a handle on the sash
      - ``showhandle=True``
    * - ``relief``, ``borderwidth``
      - Border around the whole widget
      - ``relief="solid", borderwidth=2``
    * - ``add()``
      - Put a widget in as a pane
      - ``panes.add(label)``
    * - ``add(..., width=)``
      - Starting size of the pane
      - ``panes.add(label, width=100)``
    * - ``add(..., minsize=)``
      - Smallest size of the pane
      - ``panes.add(label, minsize=80)``
    * - ``forget()``
      - Remove a pane
      - ``panes.forget(label)``
    * - ``panes()``
      - List of the panes
      - ``len(panes.panes())``
    * - ``config()``
      - Change options later
      - ``panes.config(sashwidth=10)``

----

All PanedWindow options
---------------------------

| Here is every option a PanedWindow can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``bg`` or ``background``
      - Background colour
      - ``bg="lavender"``
    * - ``bd`` or ``borderwidth``
      - How thick the border is
      - ``bd=3``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``handlepad``
      - How far the handle is from the end of the sash (in pixels)
      - ``handlepad=20``
    * - ``handlesize``
      - Size of the handle square (in pixels)
      - ``handlesize=10``
    * - ``height``
      - How tall it is (in pixels)
      - ``height=200``
    * - ``opaqueresize``
      - ``True`` resizes the panes while you drag. ``False`` waits until you let go
      - ``opaqueresize=False``
    * - ``orient``
      - Panes side by side (``"horizontal"``) or stacked (``"vertical"``)
      - ``orient="vertical"``
    * - ``proxybackground``
      - Colour of the sash outline while dragging (when ``opaqueresize=False``)
      - ``proxybackground="grey"``
    * - ``proxyborderwidth``
      - Border thickness of that dragging outline
      - ``proxyborderwidth=2``
    * - ``proxyrelief``
      - Border style of that dragging outline
      - ``proxyrelief="raised"``
    * - ``relief``
      - Border style: ``"raised"``, ``"sunken"``, ``"flat"``, ``"ridge"``, ``"groove"`` or ``"solid"``
      - ``relief="sunken"``
    * - ``sashcursor``
      - Mouse pointer shape over the sash
      - ``sashcursor="sb_h_double_arrow"``
    * - ``sashpad``
      - Space around the sash (in pixels)
      - ``sashpad=4``
    * - ``sashrelief``
      - Border style of the sash (the bar you drag)
      - ``sashrelief="raised"``
    * - ``sashwidth``
      - How wide the sash (the bar you drag) is, in pixels
      - ``sashwidth=8``
    * - ``showhandle``
      - ``True`` shows a small square handle on the sash
      - ``showhandle=True``
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

        What is a PanedWindow?

        [x] A container split into panes that the user can resize by dragging | Correct. The bar between panes is the sash.
        [ ] A window with glass | Incorrect. It is a container.
        [ ] A pop-up window | Incorrect. That is a Toplevel.
        [ ] A list | Incorrect. That is a Listbox.

    .. multichoice::

        What is the sash?

        [ ] The title bar | Incorrect. The sash is between panes.
        [x] The bar between panes that is dragged to resize them | Correct. Drag it to change the pane sizes.
        [ ] A scrollbar | Incorrect. It is not a scrollbar.
        [ ] A button | Incorrect. It is a bar.

    .. multichoice::

        What does orient="vertical" do?

        [x] Stacks the panes one above the other | Correct. vertical goes up and down.
        [ ] Puts the panes side by side | Incorrect. That is "horizontal".
        [ ] Hides the panes | Incorrect. It sets the direction.
        [ ] Rotates the text | Incorrect. It sets the direction.

    .. multichoice::

        What is the default orient?

        [ ] "vertical" | Incorrect. The default is horizontal.
        [x] "horizontal", so panes are side by side | Correct. Side by side is the default.
        [ ] "both" | Incorrect. Not a value.
        [ ] "none" | Incorrect. Not a value.

    .. multichoice::

        What does sashwidth=10 do?

        [ ] Makes the panes 10 wide | Incorrect. It sets the sash.
        [x] Makes the sash 10 pixels wide, so it is easier to grab | Correct. A wider sash is easier to drag.
        [ ] Adds 10 panes | Incorrect. It sets the sash width.
        [ ] Moves the sash | Incorrect. Dragging moves it.

    .. multichoice::

        What does sashrelief="raised" do?

        [ ] Raises the window | Incorrect. It styles the sash.
        [x] Makes the sash look raised, so it is easy to see | Correct. It sets the border style.
        [ ] Hides the sash | Incorrect. It shows it.
        [ ] Adds a handle | Incorrect. showhandle does that.

    .. multichoice::

        What does showhandle=True do?

        [x] Shows a small square handle on the sash | Correct. It helps users see what to drag.
        [ ] Shows the window title | Incorrect. Not related.
        [ ] Adds a new pane | Incorrect. add does that.
        [ ] Locks the sash | Incorrect. It shows a handle.

    .. multichoice::

        What does bg change on a PanedWindow?

        [ ] The panes' widgets | Incorrect. They have their own colours.
        [x] The background, which shows in the sash and gaps | Correct. bg is its background.
        [ ] The window title | Incorrect. Not related.
        [ ] Nothing | Incorrect. It changes the background.

    .. multichoice::

        How is a widget put into a pane?

        [ ] widget.pack() | Incorrect. Panes use add, not pack.
        [x] panes.add(widget) | Correct. add puts the widget in a new pane.
        [ ] panes.insert(widget) | Incorrect. Use add.
        [ ] widget.grid() | Incorrect. Use add.

    .. multichoice::

        What should a widget's parent be when it goes in a pane?

        [x] The PanedWindow | Correct. e.g. tk.Label(panes, ...).
        [ ] root | Incorrect. Use the PanedWindow.
        [ ] Another widget | Incorrect. The PanedWindow is the parent.
        [ ] Nothing | Incorrect. It needs a parent.

    .. multichoice::

        What does minsize=100 do in panes.add(left, minsize=100)?

        [ ] Sets the font | Incorrect. Not related.
        [x] Stops the pane being dragged smaller than 100 pixels | Correct. It sets the smallest size.
        [ ] Makes the pane 100 wide at the start | Incorrect. width does that.
        [ ] Adds 100 panes | Incorrect. It sets the minimum.

    .. multichoice::

        What does width=200 do in panes.add(left, width=200)?

        [x] Starts the pane 200 pixels wide | Correct. It sets the starting size.
        [ ] Stops it going below 200 | Incorrect. minsize does that.
        [ ] Makes the window 200 wide | Incorrect. It sets the pane.
        [ ] Nothing | Incorrect. It sets the pane width.

    .. multichoice::

        What does panes.forget(left) do?

        [ ] Deletes the widget forever | Incorrect. It removes it from the PanedWindow.
        [x] Takes the widget out of the PanedWindow | Correct. The widget still exists.
        [ ] Hides the sash | Incorrect. It removes a pane.
        [ ] Forgets the size | Incorrect. It removes the pane.

    .. multichoice::

        What does panes.panes() give?

        [ ] The number of sashes | Incorrect. It gives the panes.
        [x] A list of the widgets in the panes | Correct. Each pane holds a widget.
        [ ] The pane sizes | Incorrect. It lists the widgets.
        [ ] The window | Incorrect. It lists panes.

    .. multichoice::

        Which line changes the sash width later?

        [ ] panes.sashwidth = 10 | Incorrect. Use config.
        [x] panes.config(sashwidth=10) | Correct. config changes options.
        [ ] panes.set(sashwidth=10) | Incorrect. Not a method.
        [ ] panes.add(sashwidth=10) | Incorrect. add adds panes.

    .. multichoice::

        How do you make a PanedWindow fill the whole window?

        [x] panes.pack(fill="both", expand=True) | Correct. It stretches both ways.
        [ ] panes.pack() | Incorrect. It only takes the space it needs.
        [ ] panes.add(fill="both") | Incorrect. add is for panes.
        [ ] panes.config(fill="both") | Incorrect. fill is a pack option.

    .. multichoice::

        Can a PanedWindow go inside another PanedWindow?

        [ ] No | Incorrect. It can.
        [x] Yes, to make both side-by-side and stacked panes | Correct. Nest them for complex layouts.
        [ ] Only vertical ones | Incorrect. Any can.
        [ ] Only with grid | Incorrect. Use add.

    .. multichoice::

        How many widgets go in each pane?

        [ ] As many as you like with pack | Incorrect. Each pane holds one widget.
        [x] One, but it can be a Frame holding many widgets | Correct. Put a Frame in to hold more.
        [ ] Two | Incorrect. One per pane.
        [ ] None | Incorrect. Each holds one.

    .. multichoice::

        Which relief value hides the sash border style?

        [ ] "raised" | Incorrect. raised shows it.
        [ ] "sunken" | Incorrect. sunken shows it.
        [x] "flat" | Correct. flat has no 3D look.
        [ ] "ridge" | Incorrect. ridge shows it.

    .. multichoice::

        What happens when the user drags the sash?

        [x] The panes on each side change size | Correct. That is the point of a PanedWindow.
        [ ] The window moves | Incorrect. The sash resizes panes.
        [ ] A function always runs | Incorrect. Nothing runs by default.
        [ ] The panes swap | Incorrect. They resize.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a PanedWindow with two panes.

        panes = tk.@@PanedWindow | Frame | Canvas@@(root, @@orient | side | direction@@="horizontal")
        panes.pack(fill="both", expand=True)
        left = tk.Label(@@panes | root | left@@, text="Left", bg="lightblue")
        panes.@@add | pack | insert@@(left)

    .. cloze::
        :instructions: Make the sash easy to see and grab.

        panes = tk.PanedWindow(root, @@sashwidth | sashsize | width@@=10, @@sashrelief | relief | border@@="raised", showhandle=True)

    .. cloze::
        :instructions: Stack panes on top of each other.

        panes = tk.PanedWindow(root, orient="@@vertical | horizontal | stacked@@")
        panes.add(top, @@minsize | width | size@@=100)

    .. cloze::
        :instructions: Set a starting width and remove a pane.

        panes.add(left, @@width | minsize | length@@=200)
        panes.@@forget | delete | remove@@(left)

    .. cloze::
        :instructions: List the panes and change an option.

        widgets = panes.@@panes | children | list@@()
        panes.@@config | set | add@@(bg="grey")

----

.. admonition:: Tasks

    #. Make a window titled "Panes" that is 300x200. Add a PanedWindow that fills the window, with two labels side by side: "Left" on a yellow background and "Right" on an orange background.
    #. Change your PanedWindow so the panes are top and bottom, and the sash is 10 pixels thick.
    #. Make a PanedWindow with a Listbox of three animals in the left pane and a Text box in the right pane. The left pane should start 120 pixels wide.
    #. Make a PanedWindow with three panes, "Red", "Green" and "Blue", each with that colour as the background. Use ``minsize`` so no pane can be dragged smaller than 50 pixels.

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
                    root.title("Panes")

                    panes = tk.PanedWindow(root)
                    panes.pack(fill="both", expand=True)

                    left_label = tk.Label(panes, text="Left", bg="yellow")
                    right_label = tk.Label(panes, text="Right", bg="orange")
                    panes.add(left_label)
                    panes.add(right_label)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Panes")

                    panes = tk.PanedWindow(root, orient="vertical", sashwidth=10)
                    panes.pack(fill="both", expand=True)

                    top_label = tk.Label(panes, text="Top", bg="yellow")
                    bottom_label = tk.Label(panes, text="Bottom", bg="orange")
                    panes.add(top_label)
                    panes.add(bottom_label)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("400x200")
                    root.title("Animals")

                    panes = tk.PanedWindow(root, sashwidth=5)
                    panes.pack(fill="both", expand=True)

                    animal_list = tk.Listbox(panes)
                    for animal in ["Koala", "Wombat", "Platypus"]:
                        animal_list.insert(tk.END, animal)
                    panes.add(animal_list, width=120)

                    notes_box = tk.Text(panes)
                    panes.add(notes_box)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("RGB")

                    panes = tk.PanedWindow(root, sashwidth=5)
                    panes.pack(fill="both", expand=True)

                    for colour in ["Red", "Green", "Blue"]:
                        panes.add(tk.Label(panes, text=colour, bg=colour.lower(), fg="white"),
                                  minsize=50)

                    root.mainloop()
