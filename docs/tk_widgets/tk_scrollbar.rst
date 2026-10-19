====================================================
tk Scrollbar
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Scrollbar>`_

----

What is a Scrollbar?
-----------------------

| A **Scrollbar** is the bar down the side (or along the bottom) of a box that lets the user move through content that does not fit.
| A scrollbar is always used **with** another widget, such as a **Listbox**, **Text** or **Canvas**.

----

Making a Scrollbar
---------------------

| A scrollbar must be **linked** to the widget it scrolls. The link goes both ways:

- The **widget** tells the scrollbar when its content moves, so the scrollbar's handle moves too.
- The **scrollbar** tells the widget to move when the user drags the handle.

#. **Create** the scrollbar and **pack** it on the right with ``side="right", fill="y"``.
#. **Create** the widget with ``yscrollcommand=scrollbar.set`` and pack it on the left.
#. **Link** the scrollbar back with ``scrollbar.config(command=widget.yview)``.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("300x200")        # Window size: 300 wide, 200 high
    root.title("My first scrollbar")

    scrollbar = tk.Scrollbar(root)                      # 1. Create the scrollbar
    scrollbar.pack(side="right", fill="y")              #    down the right side

    number_list = tk.Listbox(root, yscrollcommand=scrollbar.set)    # 2. Widget -> scrollbar
    number_list.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=number_list.yview)         # 3. Scrollbar -> widget

    for number in range(1, 101):
        number_list.insert(tk.END, f"Item {number}")

    root.mainloop()                 # Keep the window open

| ``yview`` means "the up-and-down view". ``fill="y"`` stretches the scrollbar the full height.

----

Scrollbar options
--------------------

| Options are written as ``option=value`` inside ``tk.Scrollbar( )``, separated by commas.

orient
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses whether the scrollbar goes up-and-down or side-to-side.
| **How to write it:** ``orient="horizontal"``
| **Values:** ``"vertical"`` (the default) and ``"horizontal"``.
| A horizontal scrollbar uses ``xscrollcommand`` and ``xview`` instead of ``yscrollcommand`` and ``yview``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("orient")

    scrollbar = tk.Scrollbar(root, orient="horizontal")
    scrollbar.pack(side="bottom", fill="x")             # Along the bottom, full width

    long_text = tk.Text(root, wrap="none", xscrollcommand=scrollbar.set)
    long_text.pack(fill="both", expand=True)

    scrollbar.config(command=long_text.xview)

    long_text.insert("1.0", "This line is much too long to fit in the window, "
                            "so you need to scroll sideways to read all of it.")

    root.mainloop()

| ``wrap="none"`` stops the Text widget wrapping lines, so they run off the side and need scrolling.

width
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how thick the scrollbar is, in pixels.
| **How to write it:** ``width=25``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width")

    scrollbar = tk.Scrollbar(root, width=30)
    scrollbar.pack(side="right", fill="y")

    word_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
    word_list.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=word_list.yview)

    for number in range(1, 51):
        word_list.insert(tk.END, f"Word {number}")

    root.mainloop()

Colours
~~~~~~~~~~~~~~~~~~

| ``bg``, ``troughcolor`` and ``activebackground`` change the colours of the scrollbar.
| **Note:** on Windows, the scrollbar uses the normal Windows look and these colours are ignored. They work on Linux and some other computers.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("colours")

    scrollbar = tk.Scrollbar(root, bg="orange", troughcolor="lightyellow",
                             activebackground="red")
    scrollbar.pack(side="right", fill="y")

    item_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
    item_list.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=item_list.yview)

    for number in range(1, 51):
        item_list.insert(tk.END, f"Item {number}")

    root.mainloop()

----

Using scrollbars with other widgets
---------------------------------------

With a Text widget
~~~~~~~~~~~~~~~~~~~~~

| The same three steps work for a **Text** widget.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Text with a scrollbar")

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side="right", fill="y")

    story_box = tk.Text(root, wrap="word", yscrollcommand=scrollbar.set)
    story_box.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=story_box.yview)

    for number in range(1, 31):
        story_box.insert(tk.END, f"This is line {number} of the story.\n")

    root.mainloop()

Inside a Frame
~~~~~~~~~~~~~~~~~

| Put the widget and its scrollbar in a **Frame** to keep them together. Then other widgets can go above or below without getting mixed up.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("In a frame")

    tk.Label(root, text="Countries", font=("Arial", 14)).pack()

    list_frame = tk.Frame(root)
    list_frame.pack(pady=5)

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side="right", fill="y")

    country_list = tk.Listbox(list_frame, height=6, yscrollcommand=scrollbar.set)
    country_list.pack(side="left")
    scrollbar.config(command=country_list.yview)

    for country in ["Australia", "Brazil", "Canada", "Denmark", "Egypt", "France",
                    "Germany", "India", "Japan", "Kenya", "Mexico", "Norway"]:
        country_list.insert(tk.END, country)

    tk.Button(root, text="Choose").pack()

    root.mainloop()

Two scrollbars
~~~~~~~~~~~~~~~~~

| A widget can have both an up-and-down **and** a side-to-side scrollbar. Pack the scrollbars **before** the widget.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Two scrollbars")

    down_bar = tk.Scrollbar(root, orient="vertical")
    down_bar.pack(side="right", fill="y")

    across_bar = tk.Scrollbar(root, orient="horizontal")
    across_bar.pack(side="bottom", fill="x")

    grid_box = tk.Text(root, wrap="none",
                       yscrollcommand=down_bar.set, xscrollcommand=across_bar.set)
    grid_box.pack(side="left", fill="both", expand=True)

    down_bar.config(command=grid_box.yview)
    across_bar.config(command=grid_box.xview)

    for row in range(1, 41):
        grid_box.insert(tk.END, f"Row {row}: " + "x " * 60 + "\n")

    root.mainloop()

With a Canvas
~~~~~~~~~~~~~~~~

| A Canvas needs one extra option: ``scrollregion``. It tells the canvas how big the **whole** drawing is, including the part you cannot see.
| **How to write it:** ``scrollregion=(0, 0, width, height)``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Canvas with a scrollbar")

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side="right", fill="y")

    canvas = tk.Canvas(root, bg="white", scrollregion=(0, 0, 300, 1000),
                       yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=canvas.yview)

    for y in range(0, 1000, 100):
        canvas.create_text(100, y + 50, text=f"{y} pixels down", font=("Arial", 14))

    root.mainloop()

----

Scrollbar methods
--------------------

config
~~~~~~~~~~~~~~~~~~

| **What it does:** changes options **after** the scrollbar has been made. It is mostly used to link the scrollbar to its widget.
| **How to write it:** ``scrollbar.config(command=widget.yview)``

| See the examples above: every one uses ``config`` as step 3.

Scrolling from code
~~~~~~~~~~~~~~~~~~~~~~

| These are methods of the **widget** (not the scrollbar), but they make the scrollbar move:

- ``widget.yview_moveto(0)`` jumps to the **top**. ``widget.yview_moveto(1)`` jumps to the **bottom**.
- ``widget.see(index)`` scrolls so an item can be seen (Listbox and Text).

.. code-block:: python

    import tkinter as tk


    def go_top():
        name_list.yview_moveto(0)


    def go_bottom():
        name_list.yview_moveto(1)


    root = tk.Tk()
    root.geometry("300x250")
    root.title("yview_moveto")

    list_frame = tk.Frame(root)
    list_frame.pack(pady=5)

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side="right", fill="y")

    name_list = tk.Listbox(list_frame, height=8, yscrollcommand=scrollbar.set)
    name_list.pack(side="left")
    scrollbar.config(command=name_list.yview)

    for number in range(1, 101):
        name_list.insert(tk.END, f"Student {number}")

    tk.Button(root, text="Top", command=go_top).pack(side="left", padx=60)
    tk.Button(root, text="Bottom", command=go_bottom).pack(side="left")

    root.mainloop()

get
~~~~~~~~~~~~~~~~~~

| **What it does:** tells you where the handle is, as two decimals between 0 and 1.
| The first number is the top of what you can see, and the second is the bottom. ``(0.0, 0.1)`` means you can see the first tenth of the list.
| **How to write it:** ``top, bottom = scrollbar.get()``

.. code-block:: python

    import tkinter as tk


    def where():
        top, bottom = scrollbar.get()
        result_label.config(text=f"You have scrolled {round(bottom * 100)}% of the way")


    root = tk.Tk()
    root.geometry("300x250")
    root.title("get")

    list_frame = tk.Frame(root)
    list_frame.pack(pady=5)

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side="right", fill="y")

    item_list = tk.Listbox(list_frame, height=8, yscrollcommand=scrollbar.set)
    item_list.pack(side="left")
    scrollbar.config(command=item_list.yview)

    for number in range(1, 51):
        item_list.insert(tk.END, f"Item {number}")

    tk.Button(root, text="How far?", command=where).pack()
    result_label = tk.Label(root, text="")
    result_label.pack()

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
    * - ``pack(side=, fill=)``
      - Put a vertical scrollbar down the right
      - ``pack(side="right", fill="y")``
    * - ``yscrollcommand``
      - Widget tells the scrollbar it moved
      - ``yscrollcommand=scrollbar.set``
    * - ``command``
      - Scrollbar tells the widget to move
      - ``scrollbar.config(command=box.yview)``
    * - ``orient``
      - Up-and-down or side-to-side
      - ``orient="horizontal"``
    * - ``xscrollcommand``, ``xview``
      - Linking a horizontal scrollbar
      - ``xscrollcommand=bar.set``
    * - ``width``
      - Thickness in pixels
      - ``width=25``
    * - ``scrollregion``
      - Size of the whole drawing (Canvas only)
      - ``scrollregion=(0, 0, 300, 1000)``
    * - ``yview_moveto()``
      - Jump to the top (0) or bottom (1)
      - ``box.yview_moveto(1)``
    * - ``get()``
      - Where the handle is (0 to 1)
      - ``scrollbar.get()``

----

.. admonition:: Tasks

    #. Make a window titled "Numbers" that is 300x200. Add a Listbox with the numbers 1 to 200 and a vertical scrollbar linked to it.
    #. Make your scrollbar 25 pixels thick and add a "Bottom" button that jumps to the end of the list.
    #. Make a Text widget with ``wrap="none"`` and a horizontal scrollbar along the bottom. Insert one very long line of text.
    #. Put a Listbox of ten fruits and its scrollbar inside a Frame. Put a label "Fruit" above the frame and a "Choose" button below it.

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
                    root.title("Numbers")

                    scrollbar = tk.Scrollbar(root)
                    scrollbar.pack(side="right", fill="y")

                    number_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
                    number_list.pack(side="left", fill="both", expand=True)
                    scrollbar.config(command=number_list.yview)

                    for number in range(1, 201):
                        number_list.insert(tk.END, number)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk


                    def bottom():
                        number_list.yview_moveto(1)


                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Numbers")

                    tk.Button(root, text="Bottom", command=bottom).pack(side="bottom")

                    scrollbar = tk.Scrollbar(root, width=25)
                    scrollbar.pack(side="right", fill="y")

                    number_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
                    number_list.pack(side="left", fill="both", expand=True)
                    scrollbar.config(command=number_list.yview)

                    for number in range(1, 201):
                        number_list.insert(tk.END, number)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x200")
                    root.title("Long line")

                    scrollbar = tk.Scrollbar(root, orient="horizontal")
                    scrollbar.pack(side="bottom", fill="x")

                    long_text = tk.Text(root, wrap="none", xscrollcommand=scrollbar.set)
                    long_text.pack(fill="both", expand=True)
                    scrollbar.config(command=long_text.xview)

                    long_text.insert("1.0", "This is a very very very long line of text " * 5)

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("300x250")
                    root.title("Fruit")

                    tk.Label(root, text="Fruit", font=("Arial", 14)).pack()

                    list_frame = tk.Frame(root)
                    list_frame.pack(pady=5)

                    scrollbar = tk.Scrollbar(list_frame)
                    scrollbar.pack(side="right", fill="y")

                    fruit_list = tk.Listbox(list_frame, height=5, yscrollcommand=scrollbar.set)
                    fruit_list.pack(side="left")
                    scrollbar.config(command=fruit_list.yview)

                    for fruit in ["Apple", "Banana", "Cherry", "Grape", "Kiwi",
                                  "Lemon", "Mango", "Orange", "Peach", "Pear"]:
                        fruit_list.insert(tk.END, fruit)

                    tk.Button(root, text="Choose").pack()

                    root.mainloop()
