====================================================
ttk Treeview
====================================================

| See: `<https://docs.python.org/3/library/tkinter.ttk.html#treeview>`_

----

What is a Treeview?
----------------------

| A **Treeview** shows information in **rows and columns**, like a table or a spreadsheet. It can also show a **tree**: items with smaller items inside them that open and close, like folders in File Explorer.
| Use a Treeview for a class list, a scoreboard, a table of results, or a list of folders. tk has no Treeview; it only comes with ttk.

----

Making a table
-----------------

| A table needs three steps:

#. **Create** the Treeview with a name for each column: ``columns=("name", "score")``. Add ``show="headings"`` to hide the tree part and show only the table.
#. **Set the headings** (the words at the top of each column) with ``.heading(...)``.
#. **Add rows** with ``.insert("", tk.END, values=(...))``.

.. code-block:: python

    import tkinter as tk            # Load tkinter
    from tkinter import ttk         # Load the themed widgets

    root = tk.Tk()                  # Make the window
    root.geometry("320x220")
    root.title("My first Treeview")

    table = ttk.Treeview(root, columns=("name", "score"), show="headings")   # 1. Create it

    table.heading("name", text="Name")              # 2. Headings
    table.heading("score", text="Score")

    table.insert("", tk.END, values=("Ava", 95))    # 3. Rows
    table.insert("", tk.END, values=("Ben", 88))
    table.insert("", tk.END, values=("Chloe", 91))

    table.pack(pady=10)

    root.mainloop()                 # Keep the window open

| In ``insert("", tk.END, ...)``, ``""`` means "at the top level" (not inside another row) and ``tk.END`` means "at the end".
| The ``values`` must be in the **same order** as the ``columns``.

----

Treeview options
-------------------

columns
~~~~~~~~~~~~~~~~~~

| **What it does:** names each column. The names are used in your code; the user sees the **headings** instead.
| **How to write it:** ``columns=("name", "year", "house")``

show
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses which parts are shown.
| **Values:**

- ``"headings"`` - only the table (the most common for tables).
- ``"tree"`` - only the tree column, with no headings.
- ``"tree headings"`` - both (the default).

height
~~~~~~~~~~~~~~~~~~

| **What it does:** sets how many rows show before the user needs to scroll.
| **How to write it:** ``height=5``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("320x200")
    root.title("height")

    table = ttk.Treeview(root, columns=("number", "square"), show="headings", height=5)
    table.heading("number", text="Number")
    table.heading("square", text="Square")

    for number in range(1, 21):
        table.insert("", tk.END, values=(number, number * number))

    table.pack(pady=10)

    root.mainloop()

| There are 20 rows but only 5 show. Use the mouse wheel to scroll, or add a Scrollbar (see below).

selectmode
~~~~~~~~~~~~~~~~~~

| **What it does:** chooses how many rows the user can select.
| **Values:** ``"extended"`` (several rows with Ctrl or Shift, the default), ``"browse"`` (one row only), ``"none"`` (no selecting).
| **How to write it:** ``selectmode="browse"``

----

Column methods
-----------------

heading
~~~~~~~~~~~~~~~~~~

| **What it does:** sets the words at the top of a column. ``anchor`` lines the heading up ``"w"`` (left), ``"center"`` or ``"e"`` (right).
| **How to write it:** ``table.heading("score", text="Score", anchor="center")``

column
~~~~~~~~~~~~~~~~~~

| **What it does:** changes a column's size and how its values line up.
| **How to write it:** ``table.column("score", width=80, anchor="center")``
| **Options:** ``width`` (pixels), ``minwidth`` (smallest the user can drag it), ``anchor`` (``"w"``, ``"center"``, ``"e"``), ``stretch`` (``False`` stops it growing).

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("350x200")
    root.title("heading and column")

    table = ttk.Treeview(root, columns=("name", "year", "house"), show="headings", height=4)

    table.heading("name", text="Name", anchor="w")
    table.heading("year", text="Year", anchor="center")
    table.heading("house", text="House", anchor="center")

    table.column("name", width=150, anchor="w")
    table.column("year", width=60, anchor="center")
    table.column("house", width=100, anchor="center")

    students = [("Ava Smith", 7, "Red"), ("Ben Lee", 8, "Blue"), ("Chloe Ng", 7, "Gold")]
    for student in students:
        table.insert("", tk.END, values=student)

    table.pack(pady=10)

    root.mainloop()

----

Row methods
--------------

insert
~~~~~~~~~~~~~~~~~~

| **What it does:** adds a row. It gives back the row's **id**, a name Tkinter uses to find the row later.
| **How to write it:** ``row_id = table.insert("", tk.END, values=("Ava", 95))``

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def add_row():
        table.insert("", tk.END, values=(name_entry.get(), score_entry.get()))
        name_entry.delete(0, tk.END)
        score_entry.delete(0, tk.END)


    root = tk.Tk()
    root.geometry("320x300")
    root.title("insert")

    form = ttk.Frame(root, padding=5)
    form.pack()
    ttk.Label(form, text="Name:").grid(row=0, column=0)
    name_entry = ttk.Entry(form, width=12)
    name_entry.grid(row=0, column=1)
    ttk.Label(form, text="Score:").grid(row=1, column=0)
    score_entry = ttk.Entry(form, width=12)
    score_entry.grid(row=1, column=1)
    ttk.Button(form, text="Add", command=add_row).grid(row=2, column=0, columnspan=2, pady=5)

    table = ttk.Treeview(root, columns=("name", "score"), show="headings", height=6)
    table.heading("name", text="Name")
    table.heading("score", text="Score")
    table.pack()

    root.mainloop()

selection and item
~~~~~~~~~~~~~~~~~~~~~

| ``table.selection()`` gives a tuple of the **ids** of the selected rows.
| ``table.item(row_id, "values")`` gives the values in that row.
| Numbers come back as **strings**, so use ``int()`` before doing maths.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def show_selected():
        selected = table.selection()
        if selected:
            name, score = table.item(selected[0], "values")
            result_label.config(text=f"{name} scored {score}")
        else:
            result_label.config(text="Click a row first")


    root = tk.Tk()
    root.geometry("320x260")
    root.title("selection and item")

    table = ttk.Treeview(root, columns=("name", "score"), show="headings", height=4,
                         selectmode="browse")
    table.heading("name", text="Name")
    table.heading("score", text="Score")
    for row in [("Ava", 95), ("Ben", 88), ("Chloe", 91)]:
        table.insert("", tk.END, values=row)
    table.pack(pady=10)

    ttk.Button(root, text="Show selected", command=show_selected).pack()

    result_label = ttk.Label(root, text="")
    result_label.pack(pady=5)

    root.mainloop()

bind (clicking a row)
~~~~~~~~~~~~~~~~~~~~~~~~

| ``table.bind("<<TreeviewSelect>>", function_name)`` runs a function as soon as a row is selected. The function needs an ``event`` parameter.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def row_clicked(event):
        for row_id in table.selection():
            planet, moons = table.item(row_id, "values")
            result_label.config(text=f"{planet} has {moons} moons")


    root = tk.Tk()
    root.geometry("320x250")
    root.title("TreeviewSelect")

    table = ttk.Treeview(root, columns=("planet", "moons"), show="headings", height=5,
                         selectmode="browse")
    table.heading("planet", text="Planet")
    table.heading("moons", text="Moons")
    for row in [("Mercury", 0), ("Venus", 0), ("Earth", 1), ("Mars", 2), ("Jupiter", 95)]:
        table.insert("", tk.END, values=row)
    table.pack(pady=10)
    table.bind("<<TreeviewSelect>>", row_clicked)

    result_label = ttk.Label(root, text="Click a planet", font=("Arial", 14))
    result_label.pack()

    root.mainloop()

item (changing a row)
~~~~~~~~~~~~~~~~~~~~~~~~

| ``table.item(row_id, values=(...))`` changes the values in a row.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def add_point():
        for row_id in table.selection():
            name, points = table.item(row_id, "values")
            table.item(row_id, values=(name, int(points) + 1))


    root = tk.Tk()
    root.geometry("320x230")
    root.title("Changing a row")

    table = ttk.Treeview(root, columns=("team", "points"), show="headings", height=3)
    table.heading("team", text="Team")
    table.heading("points", text="Points")
    for row in [("Red", 0), ("Blue", 0), ("Gold", 0)]:
        table.insert("", tk.END, values=row)
    table.pack(pady=10)

    ttk.Button(root, text="Add a point to the selected team", command=add_point).pack()

    root.mainloop()

delete and get_children
~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``table.delete(row_id)`` removes a row.
| ``table.get_children()`` gives the ids of **every** row. Use it to loop through all rows, count them, or clear the table.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def delete_selected():
        for row_id in table.selection():
            table.delete(row_id)
        update_count()


    def clear_all():
        for row_id in table.get_children():
            table.delete(row_id)
        update_count()


    def update_count():
        count_label.config(text=f"Rows: {len(table.get_children())}")


    root = tk.Tk()
    root.geometry("320x280")
    root.title("delete")

    table = ttk.Treeview(root, columns=("job",), show="headings", height=5)
    table.heading("job", text="Job")
    for job in ["Feed the dog", "Do homework", "Tidy room", "Practise piano"]:
        table.insert("", tk.END, values=(job,))
    table.pack(pady=5)

    count_label = ttk.Label(root, text="")
    count_label.pack()
    update_count()

    ttk.Button(root, text="Delete selected", command=delete_selected).pack(pady=2)
    ttk.Button(root, text="Clear all", command=clear_all).pack()

    root.mainloop()

| ``columns=("job",)`` has a comma because a tuple with **one** item needs a comma in Python. ``values=(job,)`` is the same.

Adding up a column
~~~~~~~~~~~~~~~~~~~~~

| Loop through ``get_children()`` to work with every row, e.g. to find a total or an average.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk


    def average():
        total = 0
        rows = table.get_children()
        for row_id in rows:
            name, score = table.item(row_id, "values")
            total = total + int(score)
        result_label.config(text=f"Class average: {total / len(rows):.1f}")


    root = tk.Tk()
    root.geometry("320x260")
    root.title("Average")

    table = ttk.Treeview(root, columns=("name", "score"), show="headings", height=5)
    table.heading("name", text="Name")
    table.heading("score", text="Score")
    for row in [("Ava", 95), ("Ben", 88), ("Chloe", 91), ("Dev", 76), ("Eli", 84)]:
        table.insert("", tk.END, values=row)
    table.pack(pady=10)

    ttk.Button(root, text="Average", command=average).pack()
    result_label = ttk.Label(root, text="", font=("Arial", 14))
    result_label.pack(pady=5)

    root.mainloop()

----

Coloured rows with tags
--------------------------

| A **tag** is a named style for rows. Make it with ``tag_configure``, then add ``tags=("name",)`` when inserting a row.
| Tags can set ``background``, ``foreground`` and ``font``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("320x220")
    root.title("tags")

    table = ttk.Treeview(root, columns=("name", "score"), show="headings", height=6)
    table.heading("name", text="Name")
    table.heading("score", text="Score")

    table.tag_configure("pass", foreground="green")
    table.tag_configure("fail", foreground="red", background="mistyrose")

    for name, score in [("Ava", 95), ("Ben", 42), ("Chloe", 71), ("Dev", 38)]:
        if score >= 50:
            table.insert("", tk.END, values=(name, score), tags=("pass",))
        else:
            table.insert("", tk.END, values=(name, score), tags=("fail",))

    table.pack(pady=10)

    root.mainloop()

Striped rows
~~~~~~~~~~~~~~~

| Give every second row a different tag to make a striped table that is easy to read. ``number % 2 == 0`` is ``True`` for even numbers.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("320x240")
    root.title("Striped rows")

    table = ttk.Treeview(root, columns=("day", "temp"), show="headings", height=7)
    table.heading("day", text="Day")
    table.heading("temp", text="Temperature (°C)")
    table.tag_configure("odd", background="aliceblue")
    table.tag_configure("even", background="white")

    days = [("Mon", 22), ("Tue", 25), ("Wed", 19), ("Thu", 21), ("Fri", 28), ("Sat", 30), ("Sun", 26)]
    for number, day in enumerate(days):
        if number % 2 == 0:
            table.insert("", tk.END, values=day, tags=("even",))
        else:
            table.insert("", tk.END, values=day, tags=("odd",))

    table.pack(pady=10)

    root.mainloop()

| ``enumerate(days)`` gives each item **and** its number (0, 1, 2 ...).

----

Making a tree
----------------

| To put a row **inside** another row, give ``insert`` the **id** of the parent row instead of ``""``.
| ``text="..."`` sets the words in the **tree column** (the first column, with the open/close arrow).
| ``open=True`` makes a parent start opened.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("300x250")
    root.title("A tree")

    tree = ttk.Treeview(root, show="tree", height=10)

    science = tree.insert("", tk.END, text="Science", open=True)    # Parent rows
    maths = tree.insert("", tk.END, text="Maths")

    tree.insert(science, tk.END, text="Biology")                    # Rows inside Science
    tree.insert(science, tk.END, text="Chemistry")
    physics = tree.insert(science, tk.END, text="Physics")
    tree.insert(physics, tk.END, text="Forces")                     # Inside Physics

    tree.insert(maths, tk.END, text="Algebra")                      # Rows inside Maths
    tree.insert(maths, tk.END, text="Geometry")

    tree.pack(fill="both", expand=True, padx=10, pady=10)

    root.mainloop()

| Click the small arrows to open and close each section.

A tree with columns
~~~~~~~~~~~~~~~~~~~~~~

| Use ``show="tree headings"`` (the default) to show the tree column **and** other columns. The tree column's name is ``"#0"``.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("350x250")
    root.title("Tree with columns")

    tree = ttk.Treeview(root, columns=("legs",), height=8)
    tree.heading("#0", text="Animal")           # The tree column
    tree.heading("legs", text="Legs")
    tree.column("#0", width=200)
    tree.column("legs", width=80, anchor="center")

    mammals = tree.insert("", tk.END, text="Mammals", open=True)
    tree.insert(mammals, tk.END, text="Kangaroo", values=(2,))
    tree.insert(mammals, tk.END, text="Koala", values=(4,))

    insects = tree.insert("", tk.END, text="Insects", open=True)
    tree.insert(insects, tk.END, text="Ant", values=(6,))
    tree.insert(insects, tk.END, text="Bee", values=(6,))

    tree.pack(fill="both", expand=True, padx=10, pady=10)

    root.mainloop()

----

Adding a scrollbar
---------------------

| A Treeview links to a ttk Scrollbar in the same way as a Listbox.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("320x230")
    root.title("Scrollbar")

    box = ttk.Frame(root, padding=10)
    box.pack(fill="both", expand=True)

    scrollbar = ttk.Scrollbar(box)
    scrollbar.pack(side="right", fill="y")

    table = ttk.Treeview(box, columns=("number", "times7"), show="headings",
                         yscrollcommand=scrollbar.set)
    table.heading("number", text="Number")
    table.heading("times7", text="x 7")
    table.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=table.yview)

    for number in range(1, 101):
        table.insert("", tk.END, values=(number, number * 7))

    root.mainloop()

----

Styling a Treeview
---------------------

| A Treeview uses two styles:

- ``"Treeview"`` - the rows: ``font``, ``rowheight``, ``background``, ``foreground``, ``fieldbackground`` (the empty area below the rows).
- ``"Treeview.Heading"`` - the headings: ``font``, ``foreground``, ``background``.

| If you make the font bigger, make ``rowheight`` bigger too, or the rows overlap.

.. code-block:: python

    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.geometry("340x240")
    root.title("Treeview style")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", font=("Arial", 12), rowheight=28, background="white",
                    fieldbackground="white")
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"), foreground="white",
                    background="teal")
    style.map("Treeview", background=[("selected", "gold")], foreground=[("selected", "black")])

    table = ttk.Treeview(root, columns=("name", "score"), show="headings", height=5)
    table.heading("name", text="Name")
    table.heading("score", text="Score")
    for row in [("Ava", 95), ("Ben", 88), ("Chloe", 91)]:
        table.insert("", tk.END, values=row)
    table.pack(pady=10)

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
    * - ``columns``
      - Names of the columns
      - ``columns=("name", "score")``
    * - ``show``
      - Table only, tree only, or both
      - ``show="headings"``
    * - ``height``
      - Rows shown
      - ``height=5``
    * - ``selectmode``
      - Select one row or many
      - ``selectmode="browse"``
    * - ``heading()``
      - Words at the top of a column
      - ``table.heading("name", text="Name")``
    * - ``column()``
      - Column width and line-up
      - ``table.column("score", width=80, anchor="center")``
    * - ``insert()``
      - Add a row
      - ``table.insert("", tk.END, values=("Ava", 95))``
    * - ``selection()``
      - Ids of the selected rows
      - ``table.selection()``
    * - ``item(id, "values")``
      - Read a row
      - ``table.item(row_id, "values")``
    * - ``item(id, values=...)``
      - Change a row
      - ``table.item(row_id, values=("Ava", 96))``
    * - ``delete()``
      - Remove a row
      - ``table.delete(row_id)``
    * - ``get_children()``
      - Ids of every row
      - ``table.get_children()``
    * - ``bind("<<TreeviewSelect>>")``
      - Run a function when a row is selected
      - ``table.bind("<<TreeviewSelect>>", show)``
    * - ``tag_configure()``
      - Colour rows with a tag
      - ``table.tag_configure("fail", foreground="red")``
    * - ``"Treeview"``, ``"Treeview.Heading"``
      - Style names
      - ``style.configure("Treeview", rowheight=28)``

----

All Treeview options
---------------------------

| Here is every option a ttk Treeview can have, for reference. You will only need a few of them most of the time.

.. list-table::
    :header-rows: 1
    :widths: 25 45 30

    * - Option
      - What it does
      - Example
    * - ``class_``
      - A group name used to style many widgets at once (advanced). Written ``class_`` in Python
      - ``class_="Sidebar"``
    * - ``columns``
      - Names of the extra columns
      - ``columns=("name", "age")``
    * - ``cursor``
      - Mouse pointer shape over it
      - ``cursor="hand2"``
    * - ``displaycolumns``
      - Which columns to show, and in what order (``"#all"`` = all of them)
      - ``displaycolumns=("age", "name")``
    * - ``height``
      - How many rows show at once
      - ``height=8``
    * - ``padding``
      - Extra space inside it, around the rows
      - ``padding=5``
    * - ``selectmode``
      - How many rows can be chosen: ``"extended"`` (many), ``"browse"`` (one) or ``"none"``
      - ``selectmode="browse"``
    * - ``show``
      - What to show: ``"tree"`` (the first column), ``"headings"`` (column titles) or both
      - ``show="headings"``
    * - ``style``
      - Name of the style that sets its look
      - ``style="Big.Treeview"``
    * - ``takefocus``
      - Whether the Tab key can move to it
      - ``takefocus=0``
    * - ``xscrollcommand``
      - Connects it to a side-to-side scrollbar
      - ``xscrollcommand=x_scrollbar.set``
    * - ``yscrollcommand``
      - Connects it to an up-and-down scrollbar
      - ``yscrollcommand=scrollbar.set``

| ttk Treeview has no ``bg``, ``fg`` or ``font`` options. Change its colours and fonts with a style, e.g. ``style.configure("Treeview", font=("Arial", 12))``.

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

        What is a Treeview?

        [x] A widget that shows rows and columns like a table, or items in a tree | Correct. Good for lists of records.
        [ ] A drawing of a tree | Incorrect. It shows data.
        [ ] A menu | Incorrect. It shows rows.
        [ ] A text box | Incorrect. It shows rows and columns.

    .. multichoice::

        What does columns=("name", "age") do?

        [ ] Adds two rows | Incorrect. It sets columns.
        [x] Names two data columns | Correct. These names are used with heading and column.
        [ ] Sets the column titles | Incorrect. heading does that.
        [ ] Sets the width | Incorrect. column does that.

    .. multichoice::

        What does show="headings" do?

        [x] Shows only the data columns and their titles, hiding the first tree column | Correct. Good for tables.
        [ ] Shows only the tree | Incorrect. That is "tree".
        [ ] Hides the titles | Incorrect. It shows them.
        [ ] Shows nothing | Incorrect. It shows the table.

    .. multichoice::

        What does height=8 mean?

        [ ] 8 pixels | Incorrect. It counts rows.
        [x] 8 rows show at once | Correct. More rows scroll.
        [ ] Only 8 rows can be added | Incorrect. More can be added.
        [ ] 8 columns | Incorrect. It counts rows.

    .. multichoice::

        What does selectmode="browse" do?

        [x] Lets only one row be chosen at a time | Correct. browse allows one.
        [ ] Lets many rows be chosen | Incorrect. That is "extended".
        [ ] Stops choosing | Incorrect. That is "none".
        [ ] Opens a web browser | Incorrect. Not related.

    .. multichoice::

        Which line sets a column's title?

        [ ] tree.column("name", text="Name") | Incorrect. column sets width.
        [x] tree.heading("name", text="Name") | Correct. heading sets the title.
        [ ] tree.title("name", "Name") | Incorrect. Not a method.
        [ ] tree.insert("name", "Name") | Incorrect. insert adds rows.

    .. multichoice::

        What does tree.column("age", width=60) do?

        [x] Makes the age column 60 pixels wide | Correct. column sets width and alignment.
        [ ] Sets the title | Incorrect. heading does that.
        [ ] Adds 60 rows | Incorrect. It sets width.
        [ ] Deletes the column | Incorrect. It sets width.

    .. multichoice::

        What does anchor="center" do in tree.column("age", anchor="center")?

        [ ] Centres the window | Incorrect. It centres the values.
        [x] Centres the values in that column | Correct. anchor lines up the cells.
        [ ] Centres the title only | Incorrect. heading has its own anchor.
        [ ] Hides the column | Incorrect. It lines up values.

    .. multichoice::

        Which line adds a row?

        [x] tree.insert("", tk.END, values=("Ana", 12)) | Correct. "" means no parent, tk.END adds to the end.
        [ ] tree.add(("Ana", 12)) | Incorrect. Not a method.
        [ ] tree.insert(values=("Ana", 12)) | Incorrect. It needs a parent and position.
        [ ] tree.append("Ana", 12) | Incorrect. Not a method.

    .. multichoice::

        In tree.insert("", tk.END, values=...), what does "" mean?

        [ ] The row is empty | Incorrect. It means the top level.
        [x] The row has no parent, so it is at the top level | Correct. Use an item id to put rows under it.
        [ ] Delete the row | Incorrect. It sets the parent.
        [ ] Add a heading | Incorrect. It sets the parent.

    .. multichoice::

        What does tree.selection() give?

        [ ] The text of the chosen row | Incorrect. It gives ids.
        [x] The ids of the chosen rows | Correct. Use tree.item(id) to read them.
        [ ] The number of rows | Incorrect. Use get_children.
        [ ] The columns | Incorrect. It gives chosen rows.

    .. multichoice::

        How do you read the values of a chosen row?

        [x] tree.item(row_id)["values"] | Correct. item gives the row's details.
        [ ] tree.get(row_id) | Incorrect. Not how Treeview works.
        [ ] row_id.values | Incorrect. ids are strings.
        [ ] tree.values() | Incorrect. Not a method.

    .. multichoice::

        Which event runs when the user chooses a row?

        [ ] "<Click>" | Incorrect. Not an event.
        [x] "<<TreeviewSelect>>" | Correct. It fires when the choice changes.
        [ ] "<<RowSelect>>" | Incorrect. Not the name.
        [ ] "<Return>" | Incorrect. That is Enter.

    .. multichoice::

        How do you change a row's values?

        [ ] tree.set(row_id, ("Ben", 13)) | Incorrect. set changes one cell.
        [x] tree.item(row_id, values=("Ben", 13)) | Correct. item can change the values.
        [ ] tree.insert(row_id, ...) | Incorrect. insert adds.
        [ ] tree.change(row_id) | Incorrect. Not a method.

    .. multichoice::

        What does tree.get_children() give?

        [x] The ids of all the top-level rows | Correct. Loop through them to work with every row.
        [ ] The columns | Incorrect. It gives rows.
        [ ] The chosen rows | Incorrect. selection does that.
        [ ] The headings | Incorrect. It gives rows.

    .. multichoice::

        Which line deletes every row?

        [ ] tree.delete("all") | Incorrect. "all" is for Canvas.
        [x] tree.delete(\*tree.get_children()) | Correct. Delete every row id.
        [ ] tree.clear() | Incorrect. Not a method.
        [ ] tree.delete() | Incorrect. It needs ids.

    .. multichoice::

        How can a column of numbers be added up?

        [ ] tree.sum("age") | Incorrect. Not a method.
        [x] Loop through get_children() and add each row's value | Correct. Use tree.item(row)["values"].
        [ ] len(tree) | Incorrect. Not a total.
        [ ] tree.column("age", total=True) | Incorrect. Not an option.

    .. multichoice::

        How are striped rows made?

        [x] Give every second row a tag and use tree.tag_configure(tag, background=...) | Correct. Tags colour rows.
        [ ] tree.config(stripes=True) | Incorrect. Not an option.
        [ ] Use a Separator | Incorrect. Not for rows.
        [ ] They are always striped | Incorrect. You must add tags.

    .. multichoice::

        How is a row put under another row in a tree?

        [ ] tree.insert(tk.END, ...) | Incorrect. The parent comes first.
        [x] tree.insert(parent_id, tk.END, text="Child") | Correct. Use the parent's id.
        [ ] tree.child(parent_id) | Incorrect. Not a method.
        [ ] tree.add(parent_id) | Incorrect. Not a method.

    .. multichoice::

        Which style name changes the headings?

        [ ] "Treeview" | Incorrect. That is the rows.
        [x] "Treeview.Heading" | Correct. Headings have their own style part.
        [ ] "THeading" | Incorrect. Not the name.
        [ ] "Heading" | Incorrect. Needs the full name.

----

Fill in the gaps
--------------------------------

.. clozegroup::
    :nav-position: top
    :num-questions: 5
    :show-instant-feedback:


    .. cloze::
        :instructions: Make a Treeview with two columns.

        tree = ttk.@@Treeview | Notebook | Listbox@@(root, @@columns | rows | values@@=("name", "age"), show="@@headings | tree | table@@", height=8)
        tree.pack()

    .. cloze::
        :instructions: Set the column titles and widths.

        tree.@@heading | column | title@@("name", text="Name")
        tree.@@column | heading | width@@("age", width=60, @@anchor | justify | side@@="center")

    .. cloze::
        :instructions: Add rows.

        tree.@@insert | add | append@@("", tk.END, @@values | text | columns@@=("Ana", 12))

    .. cloze::
        :instructions: Read the chosen row.

        def picked(event):
            row_id = tree.@@selection | get_children | focus_get@@()[0]
            name = tree.@@item | get | row@@(row_id)["values"][0]

        tree.bind("@@<<TreeviewSelect>> | <Click> | <<Select>>@@", picked)

    .. cloze::
        :instructions: Colour every second row.

        tree.@@tag_configure | config | tag_add@@("grey", background="lightgrey")
        tree.insert("", tk.END, values=("Ben", 13), @@tags | tag | style@@=("grey",))

----

.. admonition:: Tasks

    #. Make a window titled "Class list" that is 350x250 with a Treeview table with the columns "Name" and "Year". Add four students.
    #. Make the "Year" column 60 pixels wide with the years in the centre.
    #. Add an Entry for a name, an Entry for a year, and an "Add" button that adds a new row.
    #. Use tags so Year 7 students show in blue and Year 8 students show in green.

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
                    root.geometry("350x250")
                    root.title("Class list")

                    table = ttk.Treeview(root, columns=("name", "year"), show="headings")
                    table.heading("name", text="Name")
                    table.heading("year", text="Year")

                    for row in [("Ava", 7), ("Ben", 8), ("Chloe", 7), ("Dev", 8)]:
                        table.insert("", tk.END, values=row)

                    table.pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("350x250")
                    root.title("Class list")

                    table = ttk.Treeview(root, columns=("name", "year"), show="headings")
                    table.heading("name", text="Name")
                    table.heading("year", text="Year")
                    table.column("year", width=60, anchor="center")

                    for row in [("Ava", 7), ("Ben", 8), ("Chloe", 7), ("Dev", 8)]:
                        table.insert("", tk.END, values=row)

                    table.pack(pady=10)

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk


                    def add():
                        table.insert("", tk.END, values=(name_entry.get(), year_entry.get()))


                    root = tk.Tk()
                    root.geometry("350x330")
                    root.title("Class list")

                    table = ttk.Treeview(root, columns=("name", "year"), show="headings", height=6)
                    table.heading("name", text="Name")
                    table.heading("year", text="Year")
                    table.column("year", width=60, anchor="center")

                    for row in [("Ava", 7), ("Ben", 8), ("Chloe", 7), ("Dev", 8)]:
                        table.insert("", tk.END, values=row)

                    table.pack(pady=10)

                    name_entry = ttk.Entry(root)
                    name_entry.pack()
                    year_entry = ttk.Entry(root, width=5)
                    year_entry.pack(pady=2)
                    ttk.Button(root, text="Add", command=add).pack()

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk
                    from tkinter import ttk

                    root = tk.Tk()
                    root.geometry("350x250")
                    root.title("Class list")

                    table = ttk.Treeview(root, columns=("name", "year"), show="headings")
                    table.heading("name", text="Name")
                    table.heading("year", text="Year")
                    table.column("year", width=60, anchor="center")
                    table.tag_configure("year7", foreground="blue")
                    table.tag_configure("year8", foreground="green")

                    for name, year in [("Ava", 7), ("Ben", 8), ("Chloe", 7), ("Dev", 8)]:
                        table.insert("", tk.END, values=(name, year), tags=(f"year{year}",))

                    table.pack(pady=10)

                    root.mainloop()
