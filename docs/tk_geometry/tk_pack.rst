==================================
Python Tkinter Pack Geometry Manager
==================================

| In Python's **Tkinter** library, the ``pack()`` geometry manager organizes widgets in blocks before placing them in the parent container.
| Rather than specifying exact pixel coordinates, ``pack()`` places widgets relative to one another along the sides of a container (top, bottom, left, right).
| It is ideal for simple layouts like vertical stacked forms, horizontal button rows, and basic application layouts.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.title("Pack Manager Example")

    # Stack three buttons vertically using default pack()
    btn1 = tk.Button(root, text="Button 1")
    btn1.pack()

    btn2 = tk.Button(root, text="Button 2")
    btn2.pack()

    btn3 = tk.Button(root, text="Button 3")
    btn3.pack()

    root.mainloop()

----

Basic Packing and Alignment (side & fill)
=========================================

The ``.pack()`` method arranges widgets along container boundaries using fundamental positioning arguments:

- **The side Parameter**: Controls which edge of the parent container the widget attaches to: ``tk.TOP`` (default), ``tk.BOTTOM``, ``tk.LEFT``, or ``tk.RIGHT``.
- **The fill Parameter**: Stretches the widget to fill allocated space along an axis: ``tk.X`` (horizontal), ``tk.Y`` (vertical), or ``tk.BOTH`` (both directions).
- **Default Behavior**: Calling ``.pack()`` without arguments stacks widgets vertically from top to bottom (``side=tk.TOP``).
- **Combining side and fill**: Enables liquid, responsive layouts that automatically adjust when windows resize.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()

    # Fill horizontally along top edge
    header = tk.Label(root, text="Header", bg="blue", fg="white")
    header.pack(side=tk.TOP, fill=tk.X)

    # Arrange buttons horizontally along left edge
    btn_left = tk.Button(root, text="Left")
    btn_left.pack(side=tk.LEFT)

    btn_right = tk.Button(root, text="Right")
    btn_right.pack(side=tk.LEFT)

    root.mainloop()

Quiz: Basic Packing and Alignment
---------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. By default, calling `.pack()` stacks widgets along the @@TOP@@ side of the window.
    2. To attach a widget to the left side of a container, set `side=tk.@@LEFT@@`.
    3. The @@fill@@ parameter determines whether a widget expands to take up extra assigned space.
    4. To make a widget stretch horizontally across the window, set `fill=tk.@@X@@`.
    5. In Tkinter, the four valid options for the `side` parameter are TOP, BOTTOM, LEFT, and @@RIGHT@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Pack two buttons side by side horizontally.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    b1 = tk.Button(root, text="Yes").pack(side=tk.LEFT)
    b2 = tk.Button(root, text="No").pack(side=tk.LEFT)

----

**Example 2:** Pack a full-width header banner across top of window.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    header = tk.Label(root, text="Welcome", bg="gray")
    header.pack(side=tk.TOP, fill=tk.X)

----

**Example 3:** Create a bottom status bar filling horizontally.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    status = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN)
    status.pack(side=tk.BOTTOM, fill=tk.X)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What is the default placement direction when calling ``.pack()`` without arguments?

        [x] tk.TOP | Correct! By default, .pack() attaches widgets to the TOP side.
        [ ] tk.LEFT | Incorrect. Horizontal packing requires setting side=tk.LEFT.
        [ ] tk.BOTTOM | Incorrect. Attaching to bottom requires side=tk.BOTTOM.
        [ ] tk.RIGHT | Incorrect. Attaching to right requires side=tk.RIGHT.


    .. multichoice::

        Which option causes a widget to stretch across the full width of its parent container?

        [x] fill=tk.X | Correct! fill=tk.X expands widgets horizontally across the container width.
        [ ] fill=tk.Y | Incorrect. fill=tk.Y expands widgets vertically.
        [ ] side=tk.X | Incorrect. X is a fill option, not a side option.
        [ ] expand=tk.WIDTH | Incorrect. The parameter name is fill=tk.X.


    .. multichoice::

        How do you place two buttons side-by-side horizontally in a window?

        [x] Pack both buttons with side=tk.LEFT | Correct! Packing consecutively with side=tk.LEFT aligns them horizontally.
        [ ] Pack both buttons with fill=tk.X | Correct fill stretches widgets, but side=tk.LEFT sets horizontal flow.
        [ ] Pack both buttons with side=tk.TOP | Incorrect. side=tk.TOP stacks them vertically.
        [ ] Call .pack(horizontal=True) on both | Incorrect. No horizontal parameter exists in .pack().


    .. multichoice::

        What happens if you combine ``fill=tk.BOTH`` with ``expand=True``?

        [x] The widget fills all remaining horizontal and vertical space when window resizes | Correct! Combining expand and fill=tk.BOTH claims and fills available window space dynamically.
        [ ] Python raises a GeometryError | Incorrect. Combining fill and expand is standard Tkinter layout practice.
        [ ] The widget shrinks to 0 pixels | Incorrect. Widget expands to occupy available container space.
        [ ] The widget gets locked into fixed pixel size | Incorrect. It creates dynamic, fluid layouts.


    .. multichoice::

        Which constant is NOT a valid value for the ``side`` argument in ``.pack()``?

        [x] tk.CENTER | Correct! CENTER is used for anchor parameter, not side (valid sides are TOP, BOTTOM, LEFT, RIGHT).
        [ ] tk.TOP | Incorrect. tk.TOP is a valid side argument.
        [ ] tk.LEFT | Incorrect. tk.LEFT is a valid side argument.
        [ ] tk.RIGHT | Incorrect. tk.RIGHT is a valid side argument.


    .. multichoice::

        What is the effect of setting ``fill=tk.Y`` on a packed widget?

        [x] The widget stretches vertically to fill allocated space | Correct! fill=tk.Y expands space vertically along the Y axis.
        [ ] The widget stretches horizontally | Incorrect. Horizontal expansion requires fill=tk.X.
        [ ] The widget shifts 10 pixels to the right | Incorrect. Padding parameters handle shifting.
        [ ] The widget hides from display | Incorrect. fill controls scaling along axis.


    .. multichoice::

        In what order does ``.pack()`` arrange widgets in a container?

        [x] In the exact order the .pack() calls are executed in code | Correct! .pack() allocates edge space chronologically based on execution order.
        [ ] Alphabetically by variable name | Incorrect. Layout order relies on execution call sequence.
        [ ] Ordered by widget pixel width | Incorrect. Size does not dictate sequence order.
        [ ] Random order | Incorrect. Execution order strictly dictates layout structure.


    .. multichoice::

        Given ``lbl.pack(side=tk.BOTTOM)``, where will ``lbl`` attach inside the parent window?

        [x] Along the bottom inner boundary | Correct! side=tk.BOTTOM anchors widgets along the bottom edge.
        [ ] In the exact center of screen | Incorrect. Requires expand and anchor parameters.
        [ ] Along the top boundary | Incorrect. TOP anchors to top edge.
        [ ] Along the left edge | Incorrect. LEFT anchors to left edge.


    .. multichoice::

        Can you mix ``.pack()`` and ``.grid()`` geometry managers inside the SAME parent window?

        [x] No, mixing pack() and grid() in the same parent container causes application freezes/crashes | Correct! Tkinter geometry managers conflict if mixed in a single container.
        [ ] Yes, Tkinter allows mixing geometry managers freely | Incorrect. Mixing causes infinite layout loops and crashes.
        [ ] Yes, but only for labels and buttons | Incorrect. Never mix pack() and grid() within same container.
        [ ] Yes, but only on macOS | Incorrect. Incompatibility applies across all operating systems.


    .. multichoice::

        What is the output of ``lbl.pack(fill=tk.BOTH)`` without setting ``expand=True``?

        [x] The widget fills its assigned bounding box, but box won't grow to claim unused window space | Correct! fill fills allocated area, expand requests unused window space.
        [ ] The widget fills the entire screen | Incorrect. Requires expand=True to claim extra space.
        [ ] Python raises a SyntaxError | Incorrect. Syntax is valid.
        [ ] The widget disappears | Incorrect. Renders within default space.

----

Advanced Sizing and Spacing (expand, padx, pady, anchor)
========================================================

Fine-tuning widget spacing, positioning, and resize behavior is controlled using optional packing arguments:

- **The expand Parameter**: Accepts Boolean values (``True`` or ``False``). When set to ``True``, the widget claims extra unallocated space when the window expands.
- **External Padding (padx, pady)**: Adds empty pixel margins *outside* the widget border (horizontal ``padx``, vertical ``pady``).
- **Internal Padding (ipadx, ipady)**: Adds internal pixel space *inside* widget boundaries, increasing widget dimensions.
- **The anchor Parameter**: Aligns the widget within its allocated space using compass points: ``tk.N``, ``tk.S``, ``tk.E``, ``tk.W``, ``tk.CENTER``, ``tk.NW``, etc.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")

    # Centered expanding button with external padding
    btn = tk.Button(root, text="Centered Action")
    btn.pack(
        expand=True,         # Claim extra window space
        anchor=tk.CENTER,    # Anchor to middle
        padx=20, pady=10     # External margins
    )

    root.mainloop()

Quiz: Advanced Sizing and Spacing
---------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Setting `expand=@@True@@` allows a widget to claim extra space when the window is resized.
    2. External space added outside widget borders is controlled by `padx` and @@pady@@.
    3. To add internal padding inside a widget's borders, use `ipadx` or @@ipady@@.
    4. Compass directions like `tk.N`, `tk.S`, and `tk.NW` are passed to the @@anchor@@ parameter.
    5. To align a widget to the North-West (top-left) corner of its allocated block, use `anchor=tk.@@NW@@`.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Pack a button with external padding on all sides.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    btn = tk.Button(root, text="Spaced Button")
    btn.pack(padx=15, pady=20)

----

**Example 2:** Create an expanding canvas that fills window during window resizing.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

----

**Example 3:** Anchor a label to the top-right (North-East) corner.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    info = tk.Label(root, text="Info")
    info.pack(side=tk.TOP, anchor=tk.NE)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What distinction exists between ``padx`` and ``ipadx``?

        [x] padx adds external margins outside widget, ipadx adds internal space inside widget | Correct! padx is external padding, ipadx is internal padding.
        [ ] padx works vertically, ipadx works horizontally | Incorrect. Both operate along horizontal X-axis.
        [ ] ipadx works only on iPads | Incorrect. 'i' stands for internal.
        [ ] padx requires integers, ipadx requires floats | Incorrect. Both expect integer pixel values.


    .. multichoice::

        Which parameter allows a packed widget to grow and shrink dynamically when a user resizes the window?

        [x] expand=True | Correct! expand=True distributes unused window space dynamically.
        [ ] resize=True | Incorrect. Tkinter uses expand=True parameter.
        [ ] stretch=True | Incorrect. stretch is not a valid pack parameter.
        [ ] fill=True | Incorrect. fill expects axis constants like tk.X or tk.BOTH.


    .. multichoice::

        How do you align a widget to the South-East (bottom-right) within its assigned space?

        [x] anchor=tk.SE | Correct! Compass direction tk.SE represents South-East (bottom-right).
        [ ] side=tk.SOUTHEAST | Incorrect. Alignment within allocated space uses anchor parameter.
        [ ] align=tk.SE | Incorrect. Tkinter uses anchor parameter.
        [ ] position="bottom-right" | Incorrect. Compass constants are required.


    .. multichoice::

        What happens if you set ``ipady=20`` on a Tkinter ``Button`` widget?

        [x] The button grows taller because 20 pixels of internal space are added above and below the text | Correct! Internal vertical padding increases widget height.
        [ ] The button shifts down 20 pixels relative to window | Incorrect. External shift uses pady.
        [ ] The font size increases by 20 points | Incorrect. Font sizes are set in font parameter.
        [ ] The button border turns transparent | Incorrect. Controls internal dimensions.


    .. multichoice::

        Given ``btn.pack(side=tk.LEFT, anchor=tk.N)``, where is ``btn`` positioned within its allocated column?

        [x] Aligned to top (North) of left column | Correct! side=tk.LEFT attaches to left edge, anchor=tk.N aligns to North top.
        [ ] In center of window | Incorrect. Attached to left side, anchored North.
        [ ] Bottom-left corner | Incorrect. tk.N aligns North (top).
        [ ] Top-right corner | Incorrect. Attached to left, not right.


    .. multichoice::

        What unit of measurement is used when specifying ``padx=10`` in Tkinter?

        [x] Pixels | Correct! Padding arguments represent distances measured in screen pixels.
        [ ] Inches | Incorrect. Tkinter uses pixel measurements by default.
        [ ] Percentages | Incorrect. Integer values represent exact pixel counts.
        [ ] Centimeters | Incorrect. Measured in pixels.


    .. multichoice::

        Which parameter value anchors a widget to the exact middle of its packing area?

        [x] anchor=tk.CENTER | Correct! tk.CENTER centers widget within allocated space.
        [ ] anchor=tk.MIDDLE | Incorrect. Valid constant is tk.CENTER.
        [ ] anchor=tk.C | Incorrect. Standard constant name is tk.CENTER.
        [ ] align="center" | Incorrect. Tkinter uses anchor=tk.CENTER.


    .. multichoice::

        What is the effect of ``btn.pack(pady=(10, 30))`` when passing a tuple?

        [x] Adds 10 pixels padding ABOVE and 30 pixels padding BELOW the widget | Correct! Tuple padding syntax specifies (top, bottom) or (left, right) asymmetrical margins.
        [ ] Adds 10 pixels to left and 30 pixels to right | Incorrect. pady operates vertically (top, bottom).
        [ ] Sets button height to 10 and width to 30 | Incorrect. pady sets external vertical padding.
        [ ] Raises a TypeError | Incorrect. Tuple padding syntax is valid in modern Tkinter.


    .. multichoice::

        How do you make a widget fill the entire application window completely?

        [x] pack(fill=tk.BOTH, expand=True) | Correct! Combining expand=True and fill=tk.BOTH fills window dimensions completely.
        [ ] pack(fill=True) | Incorrect. Must specify fill=tk.BOTH with expand=True.
        [ ] pack(side=tk.CENTER) | Incorrect. Does not force widget to expand to window borders.
        [ ] pack(fullscreen=True) | Incorrect. Invalid pack parameter.


    .. multichoice::

        Which option would you use to place 5 pixels of external space to the LEFT and 15 pixels to the RIGHT of a widget?

        [x] padx=(5, 15) | Correct! Tuple format (left, right) specifies asymmetrical horizontal margins.
        [ ] padx=5, 15 | Incorrect. Must pass values wrapped inside parentheses as a tuple (5, 15).
        [ ] ipadx=(5, 15) | Incorrect. ipadx controls internal padding, not external margins.
        [ ] side=(5, 15) | Incorrect. side accepts edge constants.


