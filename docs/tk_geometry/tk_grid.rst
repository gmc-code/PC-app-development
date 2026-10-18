==================================
Python Tkinter Grid Geometry Manager
==================================

| In Python's **Tkinter** library, the ``grid()`` geometry manager organizes widgets into a two-dimensional table of **rows** and **columns**.
| Rather than placing widgets relative to edges or at fixed pixel coordinates, ``grid()`` aligns elements in neat rows (horizontal) and columns (vertical).
| It is the most popular choice for building structured user interfaces such as forms, calculators, and control panels.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.title("Grid Manager Example")

    # Creating a simple 2x2 grid layout
    lbl1 = tk.Label(root, text="Row 0, Col 0")
    lbl1.grid(row=0, column=0)

    lbl2 = tk.Label(root, text="Row 0, Col 1")
    lbl2.grid(row=0, column=1)

    lbl3 = tk.Label(root, text="Row 1, Col 0")
    lbl3.grid(row=1, column=0)

    lbl4 = tk.Label(root, text="Row 1, Col 1")
    lbl4.grid(row=1, column=1)

    root.mainloop()

----

Rows, Columns, and Spanning (row, column, rowspan, columnspan)
==============================================================

The ``.grid()`` manager uses zero-indexed table coordinates and spanning options to control widget placement:

- **The row and column Parameters**: Define the exact grid cell location (starting at ``row=0, column=0`` in the top-left).
- **The columnspan Parameter**: Allows a widget to stretch across multiple columns horizontally.
- **The rowspan Parameter**: Allows a widget to stretch across multiple rows vertically.
- **Automatic Column/Row Sizing**: Grid cells automatically fit the size of the largest widget inside them.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()

    # Form Labels and Entries using row and column
    tk.Label(root, text="Username:").grid(row=0, column=0)
    tk.Entry(root).grid(row=0, column=1)

    tk.Label(root, text="Password:").grid(row=1, column=0)
    tk.Entry(root, show="*").grid(row=1, column=1)

    # Submit button spanning across two columns
    submit = tk.Button(root, text="Login")
    submit.grid(row=2, column=0, columnspan=2)

    root.mainloop()

Quiz: Rows, Columns, and Spanning
---------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. In Tkinter's `grid()` manager, row and column numbering starts at @@0@@.
    2. To place a widget in the second horizontal row down, set `row=@@1@@`.
    3. To make a widget stretch across three columns horizontally, use `columnspan=@@3@@`.
    4. To make a widget stretch across two rows vertically, use `rowspan=@@2@@`.
    5. Grid cell locations are defined using the @@row@@ and `column` parameters.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a 2-row login form with label and entry fields.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    tk.Label(root, text="Name").grid(row=0, column=0)
    tk.Entry(root).grid(row=0, column=1)

----

**Example 2:** Place a wide submit button spanning across two columns.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    btn = tk.Button(root, text="Submit")
    btn.grid(row=2, column=0, columnspan=2)

----

**Example 3:** Position a tall image box spanning two vertical rows.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    img_lbl = tk.Label(root, text="Image")
    img_lbl.grid(row=0, column=0, rowspan=2)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What cell coordinate corresponds to the top-left corner in a Tkinter grid layout?

        [x] row=0, column=0 | Correct! Grid row and column indexing begins at zero (0, 0).
        [ ] row=1, column=1 | Incorrect. Grid layout indexing is zero-based, not one-based.
        [ ] row=top, column=left | Incorrect. Integer index values are required.
        [ ] x=0, y=0 | Incorrect. x and y are parameters for place(), not grid().


    .. multichoice::

        Which parameter causes a widget to expand across multiple horizontal columns?

        [x] columnspan | Correct! columnspan specifies how many columns a cell spans horizontally.
        [ ] rowspan | Incorrect. rowspan stretches widgets vertically across rows.
        [ ] col_width | Incorrect. Parameter name is columnspan.
        [ ] fill_x | Incorrect. Alignment uses sticky or fill in pack.


    .. multichoice::

        If a widget is placed at ``row=0, column=2``, which column is it occupying?

        [x] The third column | Correct! Column indexing starts at 0, so column 2 is the 3rd column.
        [ ] The second column | Incorrect. Column index 1 is the second column.
        [ ] The first column | Incorrect. Column index 0 is the first column.
        [ ] The zero column | Incorrect. Column index 2 represents the 3rd column.


    .. multichoice::

        What happens if you leave empty numbers in grid sequence (e.g., placing widgets at ``row=0`` and ``row=5`` with no rows between)?

        [x] Tkinter collapses empty rows, placing row 5 directly below row 0 unless weight/minsize is set | Correct! Default empty rows and columns have zero height/width.
        [ ] Python raises a GridIndexError | Incorrect. Non-consecutive indices are allowed.
        [ ] 4 blank giant rows are rendered | Incorrect. Empty grid tracks collapse by default.
        [ ] Program crashes on launch | Incorrect. Valid syntax, empty tracks collapse.


    .. multichoice::

        Which parameter stretches a widget across multiple vertical rows?

        [x] rowspan | Correct! rowspan dictates vertical grid cell spanning.
        [ ] columnspan | Incorrect. columnspan operates horizontally across columns.
        [ ] row_height | Incorrect. Parameter name is rowspan.
        [ ] fill_y | Incorrect. rowspan is used for cell spanning.


    .. multichoice::

        How do you place an Entry box in the second row, first column?

        [x] entry.grid(row=1, column=0) | Correct! Row 1 is the 2nd row, Column 0 is the 1st column.
        [ ] entry.grid(row=2, column=1) | Incorrect. Indexing starts at 0, so this would be row 3, column 2.
        [ ] entry.grid(row=0, column=1) | Incorrect. Row 0 is 1st row, Column 1 is 2nd column.
        [ ] entry.grid(row=1, column=2) | Incorrect. Column 2 is 3rd column.


    .. multichoice::

        What is the default value of ``columnspan`` if not explicitly provided?

        [x] 1 | Correct! By default, a widget occupies exactly 1 grid column.
        [ ] 0 | Incorrect. 0 would mean occupying no space.
        [ ] 2 | Incorrect. Default span is 1 column.
        [ ] None | Incorrect. Default integer value is 1.


    .. multichoice::

        Can you use ``.grid()`` and ``.pack()`` inside the SAME parent frame or window?

        [x] No, mixing pack() and grid() in the same parent container causes application freezes | Correct! Geometry managers conflict if used within same container.
        [ ] Yes, they work together automatically | Incorrect. Mixing causes infinite geometry calculations.
        [ ] Yes, but only for labels | Incorrect. Mixing geometry managers in same parent is never allowed.
        [ ] Yes, on Windows OS only | Incorrect. Applies to all platforms.


    .. multichoice::

        Given ``btn.grid(row=3, column=1, columnspan=3)``, how many total columns does ``btn`` span?

        [x] 3 columns | Correct! columnspan=3 occupies 3 column cells starting at column index 1.
        [ ] 1 column | Incorrect. columnspan=3 explicitly expands across 3 columns.
        [ ] 4 columns | Incorrect. It spans 3 columns (columns 1, 2, and 3).
        [ ] 0 columns | Incorrect. Value is 3.


    .. multichoice::

        What dictates the default width of a grid column in Tkinter?

        [x] The width of the widest widget inside that specific column | Correct! Grid columns automatically fit around the widest element contained inside.
        [ ] The width of the window screen in pixels | Incorrect. Column width fits widget contents.
        [ ] Fixed default size of 100 pixels | Incorrect. Columns adjust dynamically to content width.
        [ ] Total number of rows | Incorrect. Column width depends on element content width.

----

Alignment and Spacing (sticky, padding, columnconfigure)
========================================================

Fine-tuning alignment inside grid cells and making columns responsive requires extra options:

- **The sticky Parameter**: Aligns or stretches widgets inside their grid cell using compass directions: ``tk.N``, ``tk.S``, ``tk.E``, ``tk.W``, or combinations like ``tk.N + tk.S + tk.E + tk.W`` (or ``"nsew"``) to stretch completely.
- **Cell Padding (padx, pady)**: Adds space outside the widget within the grid cell.
- **Internal Padding (ipadx, ipady)**: Adds space inside widget borders.
- **The rowconfigure / columnconfigure Methods**: Sets row or column weights (e.g., ``root.columnconfigure(0, weight=1)``) so cells expand dynamically when the window is resized.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")

    # Allow column 0 and row 0 to grow when window resizes
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Expanding button filling entire grid cell using sticky="nsew"
    btn = tk.Button(root, text="Expanding Button")
    btn.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    root.mainloop()

Quiz: Alignment and Spacing
---------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. In `grid()`, the @@sticky@@ parameter controls alignment and stretching inside a grid cell using compass directions.
    2. To stretch a widget horizontally to fill both left and right cell edges, set `sticky="@@ew@@"`.
    3. To stretch a widget to fill all four sides of a grid cell, set `sticky="@@nsew@@"`.
    4. To configure a column to expand when window resizes, set its @@weight@@ option using `columnconfigure()`.
    5. External cell spacing surrounding a widget is configured using `padx` and @@pady@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Align a label to the left (West) edge of its grid cell.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    lbl = tk.Label(root, text="Left Aligned")
    lbl.grid(row=0, column=0, sticky="w")

----

**Example 2:** Configure a grid column to expand with window resizing.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    btn = tk.Button(root, text="Expand")
    btn.grid(row=0, column=0, sticky="nsew")

----

**Example 3:** Apply cell padding around a grid widget.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    box = tk.Label(root, text="Padded")
    box.grid(row=0, column=0, padx=15, pady=20)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which parameter in ``.grid()`` replaces ``fill`` and ``anchor`` used in ``.pack()``?

        [x] sticky | Correct! sticky handles alignment and stretching along compass directions inside grid cells.
        [ ] align | Incorrect. Parameter name is sticky.
        [ ] position | Incorrect. Parameter name is sticky.
        [ ] side | Incorrect. side is used in pack().


    .. multichoice::

        How do you make a widget stretch horizontally to fill the full width of its grid cell?

        [x] sticky="ew" | Correct! East-West ("ew") alignment stretches widget horizontally across cell.
        [ ] sticky="ns" | Incorrect. "ns" (North-South) stretches vertically.
        [ ] fill=True | Incorrect. grid() uses sticky parameter for filling.
        [ ] expand=True | Incorrect. columnconfigure weight handles expansion; sticky handles cell stretching.


    .. multichoice::

        What is required for a grid column to expand when the application window is resized?

        [x] Calling root.columnconfigure(col_index, weight=1) | Correct! Setting column weight > 0 allows dynamic resizing.
        [ ] Setting sticky="center" | Incorrect. sticky aligns within cell, weight allows cell to grow.
        [ ] Setting rowspan=100 | Incorrect. rowspan spans cells, does not handle resize weight.
        [ ] Setting padx=100 | Incorrect. Padding adds static pixel margins.


    .. multichoice::

        What compass point combination makes a widget fill its grid cell completely in all directions?

        [x] "nsew" | Correct! North-South-East-West ("nsew") stretches element along all 4 cell boundaries.
        [ ] "center" | Incorrect. center anchors middle without stretching.
        [ ] "top-bottom" | Incorrect. Compass direction strings like "nsew" are required.
        [ ] "all" | Incorrect. Compass directions "nsew" are used.


    .. multichoice::

        What is the default alignment of a widget inside its grid cell if ``sticky`` is NOT set?

        [x] Centered in the middle of the cell | Correct! Widgets default to centered position inside cell area.
        [ ] Top-left corner | Incorrect. Default alignment is centered.
        [ ] Stretched to fill full cell | Incorrect. Requires sticky parameter.
        [ ] Bottom-right corner | Incorrect. Default is centered.


    .. multichoice::

        What unit of measurement is used for ``padx`` and ``pady`` in grid layout?

        [x] Pixels | Correct! Padding arguments specify exact pixel spacing.
        [ ] Inches | Incorrect. Measured in screen pixels.
        [ ] Percentages | Incorrect. Integer values represent pixels.
        [ ] Grid cells | Incorrect. Padding distance uses pixels.


    .. multichoice::

        Given ``root.columnconfigure(0, weight=1)`` and ``root.columnconfigure(1, weight=2)``, how will extra horizontal window space be divided when resized?

        [x] Column 1 receives twice as much extra space as Column 0 | Correct! Weight ratios dictate expansion proportion (weight 2 grows twice as fast as weight 1).
        [ ] Column 0 receives twice as much space as Column 1 | Incorrect. Higher weight receives greater proportion.
        [ ] Both columns expand equally | Incorrect. Weights 1 and 2 define a 1:2 ratio.
        [ ] Column 1 remains fixed size | Incorrect. Weight 2 enables expansion.


    .. multichoice::

        Which option adds 10 pixels of space inside widget boundaries vertically?

        [x] ipady=10 | Correct! ipady sets internal vertical padding.
        [ ] pady=10 | Incorrect. pady sets external vertical margin.
        [ ] ipadx=10 | Incorrect. ipadx operates horizontally.
        [ ] sticky="ns" | Incorrect. sticky controls alignment/stretch.


    .. multichoice::

        How do you align a label to the East (right) side of its grid cell without stretching it?

        [x] sticky="e" | Correct! "e" (East) anchors element to right edge.
        [ ] sticky="w" | Incorrect. "w" anchors to West (left) edge.
        [ ] sticky="ew" | Incorrect. "ew" stretches element across both edges.
        [ ] align="right" | Incorrect. Tkinter uses sticky="e".


    .. multichoice::

        What code snippet expands row 0 vertically when the window is resized?

        [x] root.rowconfigure(0, weight=1) | Correct! rowconfigure with weight enables vertical row resizing.
        [ ] root.columnconfigure(0, weight=1) | Incorrect. columnconfigure operates horizontally on columns.
        [ ] root.grid_row(0, expand=True) | Incorrect. Correct method name is rowconfigure.
        [ ] root.resize_row(0) | Incorrect. Method name is rowconfigure.


