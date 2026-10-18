===================================
Python Tkinter Place Geometry Manager
===================================

| In Python's **Tkinter** library, the ``place()`` geometry manager allows you to position widgets using exact coordinates or relative positioning.
| Unlike ``pack()`` or ``grid()``, which arrange widgets automatically in blocks or rows/columns, ``place()`` gives you total control over precise pixel locations.
| It is ideal for custom pixel-perfect designs, overlapping elements, or positioning widgets at exact percentages of the window size.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Place Manager Example")

    # Place a button at exact pixel coordinates (x=50, y=80)
    btn = tk.Button(root, text="Click Me")
    btn.place(x=50, y=80)

    root.mainloop()

----

Absolute Positioning (x, y, width, height)
===========================================

Absolute positioning places widgets at fixed pixel coordinates relative to the top-left corner of the parent window:

- **The x and y Parameters**: Specify horizontal (``x``) and vertical (``y``) pixel coordinates. The origin ``(x=0, y=0)`` is the top-left corner.
- **The width and height Parameters**: Explicitly define the widget's width and height in pixels.
- **Fixed Layouts**: Widgets placed with absolute positioning maintain fixed sizes and positions regardless of window resizing.
- **Overlapping Widgets**: Multiple widgets assigned identical or overlapping coordinates will stack on top of each other.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("400x300")

    # Placing a card-like box with explicit dimensions
    box = tk.Label(root, text="Card Element", bg="lightblue")
    box.place(x=20, y=20, width=150, height=100)

    # Placing a button nearby using fixed coordinates
    btn = tk.Button(root, text="Action")
    btn.place(x=180, y=50, width=80, height=40)

    root.mainloop()

Quiz: Absolute Positioning
--------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. In Tkinter's `place()` manager, coordinates `(x=0, y=0)` represent the @@top-left@@ corner of the window.
    2. The @@x@@ parameter specifies the horizontal distance in pixels from the left edge.
    3. The @@y@@ parameter specifies the vertical distance in pixels from the top edge.
    4. To set a widget's exact pixel width inside `place()`, use the @@width@@ parameter.
    5. Placing two widgets at the exact same x and y coordinates causes them to @@overlap@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Place a button at pixel coordinates (100, 50).

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    btn = tk.Button(root, text="Start")
    btn.place(x=100, y=50)

----

**Example 2:** Place a label with explicit pixel width and height.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    lbl = tk.Label(root, text="Box", bg="yellow")
    lbl.place(x=30, y=30, width=120, height=60)

----

**Example 3:** Create two overlapping labels using fixed coordinates.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    bg_lbl = tk.Label(root, bg="red").place(x=10, y=10, width=100, height=100)
    fg_lbl = tk.Label(root, bg="blue").place(x=30, y=30, width=60, height=60)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Where is the origin point ``(x=0, y=0)`` located in a Tkinter window?

        [x] Top-left corner | Correct! x=0, y=0 represents the upper-left origin of the container.
        [ ] Bottom-left corner | Incorrect. Bottom-left would be x=0, y=height.
        [ ] Center of the window | Incorrect. Center requires relative values (relx=0.5, rely=0.5).
        [ ] Top-right corner | Incorrect. Top-right is x=width, y=0.


    .. multichoice::

        Which parameter in ``.place()`` sets the vertical pixel coordinate?

        [x] y | Correct! y controls vertical positioning from the top edge.
        [ ] x | Incorrect. x controls horizontal distance.
        [ ] top | Incorrect. Tkinter uses y for vertical positioning.
        [ ] row | Incorrect. row is used in grid(), not place().


    .. multichoice::

        What happens to widgets placed with absolute coordinates ``(x, y)`` when the user resizes the window?

        [x] They remain fixed at their exact pixel coordinates | Correct! Absolute coordinates do not move or scale during window resizing.
        [ ] They automatically scale to remain centered | Incorrect. Scaling requires relative positioning (relx, rely).
        [ ] They snap into a grid layout | Incorrect. place() operates independently of grid logic.
        [ ] They disappear from screen | Incorrect. They stay at their fixed pixel coordinates.


    .. multichoice::

        How do you set a widget's height to 50 pixels using ``.place()``?

        [x] place(height=50) | Correct! height=50 sets explicit pixel height.
        [ ] place(ipady=50) | Incorrect. ipady is used in pack() or grid() for padding.
        [ ] place(size_y=50) | Incorrect. Parameter name is height.
        [ ] place(y_len=50) | Incorrect. Parameter name is height.


    .. multichoice::

        What is a major advantage of ``.place()`` compared to ``.pack()`` and ``.grid()``?

        [x] It allows exact pixel positioning and widget overlapping | Correct! place() allows free-form pixel coordinates and overlapping.
        [ ] It makes forms resize automatically without code | Incorrect. Relative placement requires specific parameters.
        [ ] It automatically handles responsive grid columns | Incorrect. That is the strength of grid().
        [ ] It requires fewer lines of Python code | Incorrect. Code length is similar across geometry managers.


    .. multichoice::

        What unit of measurement is used for ``x`` and ``y`` parameters in ``.place()``?

        [x] Pixels | Correct! Absolute positions are measured in screen pixels.
        [ ] Inches | Incorrect. Tkinter uses pixels.
        [ ] Percentages | Incorrect. Percentages use relx and rely.
        [ ] Grid cells | Incorrect. Grid cells are used in grid().


    .. multichoice::

        Given ``btn.place(x=50, y=100)``, moving the button 20 pixels further DOWN requires changing ``y`` to:

        [x] y=120 | Correct! Increasing y moves elements downward.
        [ ] y=80 | Incorrect. Decreasing y moves elements upward.
        [ ] x=70 | Incorrect. Changing x moves elements horizontally right.
        [ ] y=20 | Incorrect. y=20 moves the button near the top.


    .. multichoice::

        If two widgets are placed at ``x=10, y=10``, which widget will appear on TOP?

        [x] The widget whose .place() method was called second | Correct! Tkinter renders widgets in order of execution; later calls overlay earlier ones.
        [ ] The widget with a larger variable name | Incorrect. Variable names do not affect z-index.
        [ ] The first widget created | Incorrect. Later created/placed widgets draw on top.
        [ ] Python raises a PlacementError | Incorrect. Overlapping is fully supported in place().


    .. multichoice::

        Can you use ``width`` and ``height`` alongside ``x`` and ``y`` in a single ``.place()`` call?

        [x] Yes, you can specify position and dimensions simultaneously | Correct! x, y, width, and height work together seamlessly.
        [ ] No, width and height can only be set in .config() | Incorrect. They are valid parameters in place().
        [ ] Yes, but only for Label widgets | Incorrect. Valid for all Tkinter widgets.
        [ ] No, setting dimensions causes a crash | Incorrect. Valid geometry parameter usage.


    .. multichoice::

        Which code snippet correctly places a button at coordinate (200, 150) with width 100?

        [x] btn.place(x=200, y=150, width=100) | Correct! Proper syntax for placing with explicit location and width.
        [ ] btn.place(pos=(200, 150), w=100) | Incorrect. Invalid parameter names.
        [ ] btn.place(x=150, y=200, size=100) | Incorrect. Swapped x and y coordinates, invalid size parameter.
        [ ] btn.place(left=200, top=150, width=100) | Incorrect. Parameter names are x and y.

----

Relative Positioning and Anchoring (relx, rely, relwidth, relheight, anchor)
==============================================================================

Relative positioning places widgets as a proportion (percentage) of the parent window's size:

- **The relx and rely Parameters**: Values float between ``0.0`` (0%) and ``1.0`` (100%) of parent width and height (e.g., ``relx=0.5`` is horizontal middle).
- **The relwidth and relheight Parameters**: Scale widget dimensions relative to container size (e.g., ``relwidth=0.5`` makes widget half window width).
- **Responsive Scaling**: Widgets using relative parameters adjust position and size dynamically when windows resize.
- **The anchor Parameter**: Defines which point of the widget aligns with the position: ``tk.CENTER``, ``tk.NW``, ``tk.SE``, etc.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("400x300")

    # Perfectly centered button that stays centered when window resizes
    center_btn = tk.Button(root, text="Centered Button")
    center_btn.place(
        relx=0.5, rely=0.5,    # 50% across, 50% down
        anchor=tk.CENTER       # Align center of button to coordinate
    )

    # Banner across top half width
    banner = tk.Label(root, text="Top Banner", bg="lightgreen")
    banner.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.2)

    root.mainloop()

Quiz: Relative Positioning and Anchoring
----------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To position a widget halfway across the window horizontally, set `relx=@@0.5@@`.
    2. Relative position values range from `0.0` (0%) to `@@1.0@@` (100%).
    3. To make a widget automatically stretch to half the window's total height, set `relheight=@@0.5@@`.
    4. By default, a widget's @@top-left@@ corner aligns with the specified `relx` and `rely` coordinates unless `anchor` is changed.
    5. To center a widget precisely at a relative point, set `anchor=tk.@@CENTER@@`.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Center a button perfectly in the middle of a window.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    btn = tk.Button(root, text="Middle")
    btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

----

**Example 2:** Create a sidebar taking up the left 25% of the window width.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    sidebar = tk.Frame(root, bg="gray")
    sidebar.place(relx=0.0, rely=0.0, relwidth=0.25, relheight=1.0)

----

**Example 3:** Place a notification box in the bottom-right corner.

.. ordering::

    import tkinter as tk
    root = tk.Tk()
    note = tk.Label(root, text="Done")
    note.place(relx=1.0, rely=1.0, anchor=tk.SE)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What value of ``relx`` positions a widget at the horizontal right edge of the window?

        [x] 1.0 | Correct! relx=1.0 represents 100% (rightmost boundary).
        [ ] 0.0 | Incorrect. 0.0 represents the left edge.
        [ ] 0.5 | Incorrect. 0.5 represents horizontal center.
        [ ] 100 | Incorrect. Relative values use floats from 0.0 to 1.0.


    .. multichoice::

        What is the effect of ``relwidth=0.8`` on a widget?

        [x] The widget's width becomes 80% of its parent window's width | Correct! relwidth=0.8 sets width to 80% relative to container width.
        [ ] The widget's width is set to 8 pixels | Incorrect. Absolute width uses pixels; relwidth uses fractions.
        [ ] The widget shrinks by 80% | Incorrect. It sets exact proportion to 80%.
        [ ] The widget moves 80 pixels to the right | Incorrect. relx handles horizontal movement.


    .. multichoice::

        Why is ``anchor=tk.CENTER`` important when centering a widget using ``relx=0.5, rely=0.5``?

        [x] Without anchor=tk.CENTER, the top-left corner of the widget sits at the center point rather than its middle | Correct! By default the top-left corner aligns to coordinates; anchoring center aligns widget midpoint.
        [ ] Without anchor, the widget becomes invisible | Incorrect. Widget remains visible but off-center.
        [ ] It prevents the user from clicking the button | Incorrect. Anchor controls geometric alignment.
        [ ] It locks window resizing completely | Incorrect. Anchor affects widget alignment only.


    .. multichoice::

        Which combination creates a top header banner taking up full width and 10% height?

        [x] relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1 | Correct! 0% origin, 100% width, 10% height.
        [ ] relx=1.0, rely=1.0, relwidth=0.1, relheight=1.0 | Incorrect. Places at bottom-right.
        [ ] x=0, y=0, width=1.0, height=0.1 | Incorrect. width and height expect integer pixel values.
        [ ] relx=0.5, rely=0.5, relwidth=1.0, relheight=0.1 | Incorrect. relx/rely origin off-center.


    .. multichoice::

        Can you mix relative parameters (``relx``) and absolute offset parameters (``x``) in a single ``.place()`` call?

        [x] Yes, x acts as a pixel offset added to the calculated relative relx position | Correct! Absolute offsets can fine-tune relative positioning.
        [ ] No, Python raises a SyntaxError | Incorrect. Combining relative and absolute parameters is valid syntax.
        [ ] Yes, but relative parameters are ignored | Incorrect. Both relative base and absolute offset are applied.
        [ ] No, place() crashes if float and int are used together | Incorrect. Combining relative and absolute is fully supported.


    .. multichoice::

        What float range is used for ``relx``, ``rely``, ``relwidth``, and ``relheight``?

        [x] 0.0 to 1.0 | Correct! Represents fractional percentages (0% to 100%).
        [ ] 0 to 100 | Incorrect. Percentages are passed as decimals between 0.0 and 1.0.
        [ ] -1.0 to 1.0 | Incorrect. Standard container coordinates range from 0.0 to 1.0.
        [ ] 1 to 10 | Incorrect. Decimals between 0.0 and 1.0 are used.


    .. multichoice::

        How do you anchor a widget by its top-right corner to coordinate ``relx=1.0, rely=0.0``?

        [x] anchor=tk.NE | Correct! North-East (top-right) anchors corner to top-right edge.
        [ ] anchor=tk.SW | Incorrect. SW is South-West (bottom-left).
        [ ] anchor=tk.CENTER | Incorrect. CENTER anchors middle of widget.
        [ ] anchor=tk.NW | Incorrect. NW is North-West (top-left).


    .. multichoice::

        Given ``lbl.place(relx=0.5, rely=0.2, anchor=tk.N)``, where is ``lbl`` located?

        [x] Horizontally centered, 20% down from the top edge | Correct! relx=0.5 centers horizontally, rely=0.2 places 20% down, anchor=tk.N anchors top edge.
        [ ] In exact center of window | Incorrect. rely=0.2 is near top, not middle (rely=0.5).
        [ ] Bottom-left corner | Incorrect. rely=0.2 is near top.
        [ ] Right edge, 50% down | Incorrect. relx=0.5 is horizontal middle.


    .. multichoice::

        What happens when you use ``relwidth=1.0, relheight=1.0`` on a background image label?

        [x] The background image label stretches/scales to cover the entire window area | Correct! 1.0 width and 1.0 height match full window dimensions.
        [ ] The window shrinks down to 1 pixel | Incorrect. Widget expands to container size.
        [ ] The label gets hidden behind parent frame | Incorrect. Fills front container area.
        [ ] Python raises a GeometryError | Incorrect. Standard background layout technique.


    .. multichoice::

        Which statement best describes the primary difference between ``x=100`` and ``relx=0.5``?

        [x] x=100 sets a fixed 100-pixel offset; relx=0.5 sets a relative position at 50% of parent width | Correct! x uses fixed pixels, relx uses dynamic window proportions.
        [ ] x=100 works vertically; relx=0.5 works horizontally | Incorrect. Both x and relx operate along horizontal axis.
        [ ] x=100 scales on resize; relx=0.5 stays static | Incorrect. Opposite is true; relx scales dynamically.
        [ ] relx=0.5 requires grid() manager | Incorrect. relx is a parameter of place().

