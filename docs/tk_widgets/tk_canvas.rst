====================================================
tk Canvas
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Canvas>`_

----

What is a Canvas?
-------------------

| A **Canvas** is a blank area you can **draw** on with code.
| You can draw lines, rectangles, circles, shapes and words, then move them or change their colour.
| Canvases are used for drawings, graphs and simple games.

----

Making a Canvas
-------------------

#. **Create** the canvas with ``tk.Canvas(...)`` and give it a size.
#. **Place** the canvas in the window with ``.pack()``.
#. **Draw** on it with the ``create_`` methods.

.. code-block:: python

    import tkinter as tk            # Load the tkinter library

    root = tk.Tk()                  # Make the window
    root.geometry("320x240")        # Window size: 320 wide, 240 high
    root.title("My first canvas")   # Words in the title bar

    canvas = tk.Canvas(root, width=300, height=200, bg="white")    # 1. Create the canvas
    canvas.pack(pady=10)                                            # 2. Place it

    canvas.create_line(20, 20, 280, 180)                            # 3. Draw a line

    root.mainloop()                 # Keep the window open

----

Canvas coordinates
---------------------

| Every point on a canvas has an **x** and a **y** number, measured in pixels.

- **x** is how far **across** from the left edge.
- **y** is how far **down** from the top edge.
- The top-left corner is ``(0, 0)``.

.. important::

    On a canvas, **y gets bigger going down**. This is the opposite of a graph in maths, where y gets bigger going up.

| On a 300 x 200 canvas: the top-right corner is ``(300, 0)``, the bottom-left is ``(0, 200)`` and the middle is ``(150, 100)``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("320x240")
    root.title("Coordinates")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack(pady=10)

    canvas.create_text(30, 15, text="(0, 0)")
    canvas.create_text(265, 15, text="(300, 0)")
    canvas.create_text(30, 185, text="(0, 200)")
    canvas.create_text(150, 100, text="(150, 100)")

    root.mainloop()

----

Canvas options
-------------------

| Options are written as ``option=value`` inside ``tk.Canvas( )``, separated by commas.

width and height
~~~~~~~~~~~~~~~~~~

| **What they do:** set the size of the canvas in **pixels**.
| **How to write them:** ``width=400``, ``height=300``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("width and height")

    small_canvas = tk.Canvas(root, width=150, height=100, bg="lightblue")
    small_canvas.pack(pady=20)

    root.mainloop()

bg (background colour)
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What it does:** sets the colour of the canvas.
| **How to write it:** ``bg="colour"``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("320x240")
    root.title("bg")

    night_sky = tk.Canvas(root, width=300, height=200, bg="midnightblue")
    night_sky.pack(pady=10)

    root.mainloop()

relief, borderwidth and highlightthickness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **What they do:** ``relief`` and ``borderwidth`` draw a border around the canvas.
| ``highlightthickness=0`` removes the thin grey outline that a canvas has by default.
| **How to write them:** ``relief="solid", borderwidth=2``, ``highlightthickness=0``

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("320x240")
    root.title("border")

    canvas = tk.Canvas(root, width=280, height=180, bg="white",
                       relief="solid", borderwidth=3, highlightthickness=0)
    canvas.pack(pady=10)

    root.mainloop()

cursor
~~~~~~~~~~~~~~~~~~

| **What it does:** changes the mouse pointer when it is over the canvas.
| **How to write it:** ``cursor="pencil"``
| **Some values:** ``"pencil"``, ``"cross"``, ``"hand2"``, ``"circle"``, ``"spraycan"``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("320x240")
    root.title("cursor")

    canvas = tk.Canvas(root, width=300, height=200, bg="white", cursor="pencil")
    canvas.pack(pady=10)

    root.mainloop()

----

Drawing methods
-------------------

| Each ``create_`` method draws one **item** on the canvas. Most use these drawing options:

- ``fill`` - the colour inside a shape, or the colour of a line or text.
- ``outline`` - the colour of the edge of a shape.
- ``width`` - how thick the line or edge is, in pixels.

create_line
~~~~~~~~~~~~~~~~~~

| **What it does:** draws a straight line from one point to another.
| **How to write it:** ``canvas.create_line(x1, y1, x2, y2)``
| Add more points to draw a zig-zag. Add ``arrow="last"`` to put an arrowhead on the end.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("320x240")
    root.title("create_line")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack(pady=10)

    canvas.create_line(20, 30, 280, 30)                                     # Thin black line
    canvas.create_line(20, 70, 280, 70, fill="red", width=5)                # Thick red line
    canvas.create_line(20, 110, 280, 110, fill="blue", width=3, arrow="last")   # Arrow
    canvas.create_line(20, 180, 80, 140, 140, 180, 200, 140, 260, 180,
                       fill="green", width=3)                               # Zig-zag

    root.mainloop()

create_rectangle
~~~~~~~~~~~~~~~~~~

| **What it does:** draws a rectangle (or a square).
| **How to write it:** ``canvas.create_rectangle(x1, y1, x2, y2)``
| ``(x1, y1)`` is the **top-left** corner and ``(x2, y2)`` is the **bottom-right** corner.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("320x240")
    root.title("create_rectangle")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack(pady=10)

    canvas.create_rectangle(20, 20, 120, 80)                                    # Outline only
    canvas.create_rectangle(150, 20, 280, 80, fill="yellow")                    # Filled
    canvas.create_rectangle(20, 110, 120, 180, fill="orange", outline="red", width=4)
    canvas.create_rectangle(150, 110, 220, 180, fill="skyblue", outline="")    # No edge

    root.mainloop()

create_oval
~~~~~~~~~~~~~~~~~~

| **What it does:** draws an oval (or a circle).
| **How to write it:** ``canvas.create_oval(x1, y1, x2, y2)``
| Imagine an invisible rectangle from ``(x1, y1)`` to ``(x2, y2)``. The oval fits exactly inside it.
| If the invisible rectangle is a **square**, you get a **circle**.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("320x240")
    root.title("create_oval")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack(pady=10)

    canvas.create_oval(20, 50, 180, 150, fill="lightgreen")      # Oval: 160 wide, 100 high
    canvas.create_oval(200, 50, 280, 130, fill="red")            # Circle: 80 wide, 80 high

    root.mainloop()

create_polygon
~~~~~~~~~~~~~~~~~~

| **What it does:** draws a shape with straight sides by joining up a list of points, e.g. a triangle or a star.
| **How to write it:** ``canvas.create_polygon(x1, y1, x2, y2, x3, y3, ...)``
| The last point joins back to the first one automatically.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("320x240")
    root.title("create_polygon")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack(pady=10)

    canvas.create_polygon(60, 20, 110, 120, 10, 120, fill="purple")                 # Triangle
    canvas.create_polygon(150, 120, 200, 40, 250, 120, 200, 180, fill="gold",
                          outline="black", width=2)                                 # Diamond

    root.mainloop()

create_text
~~~~~~~~~~~~~~~~~~

| **What it does:** writes words on the canvas.
| **How to write it:** ``canvas.create_text(x, y, text="words")``
| ``(x, y)`` is the **middle** of the text. Use ``fill`` for the colour and ``font`` for the style and size.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("320x240")
    root.title("create_text")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack(pady=10)

    canvas.create_text(150, 60, text="Hello!", font=("Arial", 32, "bold"), fill="blue")
    canvas.create_text(150, 140, text="Words on a canvas", font=("Arial", 14))

    root.mainloop()

create_image
~~~~~~~~~~~~~~~~~~

| **What it does:** puts a picture on the canvas.
| **How to write it:** load the picture with ``tk.PhotoImage(file="name.png")``, then ``canvas.create_image(x, y, image=picture)``
| ``(x, y)`` is the **middle** of the picture. The file must be a **.png** or **.gif** in the same folder as your Python file.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("320x240")
    root.title("create_image")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack(pady=10)

    picture = tk.PhotoImage(file="logo.png")
    canvas.create_image(150, 100, image=picture)

    root.mainloop()

Drawing a picture
~~~~~~~~~~~~~~~~~~~~

| Put several shapes together to draw a picture. Shapes drawn **later** go **on top** of earlier ones.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("320x240")
    root.title("House")

    canvas = tk.Canvas(root, width=300, height=200, bg="skyblue")
    canvas.pack(pady=10)

    canvas.create_rectangle(0, 160, 300, 200, fill="green", outline="")         # Grass
    canvas.create_oval(230, 20, 280, 70, fill="yellow", outline="")             # Sun
    canvas.create_rectangle(80, 90, 200, 170, fill="tan")                       # House
    canvas.create_polygon(70, 90, 140, 40, 210, 90, fill="brown")               # Roof
    canvas.create_rectangle(125, 125, 155, 170, fill="maroon")                  # Door

    root.mainloop()

----

Changing items
-----------------

| Every ``create_`` method gives back an **id number** for the item. Save it in a variable to change the item later.

.. code-block:: python

    ball = canvas.create_oval(10, 10, 50, 50, fill="red")    # ball stores the item's id number

move
~~~~~~~~~~~~~~~~~~

| **What it does:** moves an item by an amount.
| **How to write it:** ``canvas.move(item, x_amount, y_amount)``
| Positive x moves right, negative x moves left. Positive y moves **down**, negative y moves **up**.

.. code-block:: python

    import tkinter as tk


    def move_right():
        canvas.move(ball, 20, 0)


    def move_down():
        canvas.move(ball, 0, 20)


    root = tk.Tk()
    root.geometry("320x280")
    root.title("move")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack(pady=5)

    ball = canvas.create_oval(10, 10, 50, 50, fill="red")

    tk.Button(root, text="Right", command=move_right).pack(side="left", padx=40)
    tk.Button(root, text="Down", command=move_down).pack(side="left")

    root.mainloop()

itemconfig
~~~~~~~~~~~~~~~~~~

| **What it does:** changes the options of an item, e.g. its colour or text.
| **How to write it:** ``canvas.itemconfig(item, option=value)``

.. code-block:: python

    import tkinter as tk


    def go():
        canvas.itemconfig(light, fill="green")
        canvas.itemconfig(sign, text="GO")


    def stop():
        canvas.itemconfig(light, fill="red")
        canvas.itemconfig(sign, text="STOP")


    root = tk.Tk()
    root.geometry("320x280")
    root.title("itemconfig")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack(pady=5)

    light = canvas.create_oval(100, 20, 200, 120, fill="red")
    sign = canvas.create_text(150, 160, text="STOP", font=("Arial", 24, "bold"))

    tk.Button(root, text="Go", command=go).pack(side="left", padx=60)
    tk.Button(root, text="Stop", command=stop).pack(side="left")

    root.mainloop()

delete
~~~~~~~~~~~~~~~~~~

| **What it does:** removes items from the canvas.
| **How to write it:** ``canvas.delete(item)`` removes one item. ``canvas.delete("all")`` clears the whole canvas.

.. code-block:: python

    import tkinter as tk
    import random


    def add_star():
        x = random.randint(10, 290)
        y = random.randint(10, 190)
        canvas.create_oval(x, y, x + 6, y + 6, fill="white", outline="")


    def clear():
        canvas.delete("all")


    root = tk.Tk()
    root.geometry("320x280")
    root.title("delete")

    canvas = tk.Canvas(root, width=300, height=200, bg="black")
    canvas.pack(pady=5)

    tk.Button(root, text="Add a star", command=add_star).pack(side="left", padx=50)
    tk.Button(root, text="Clear", command=clear).pack(side="left")

    root.mainloop()

coords
~~~~~~~~~~~~~~~~~~

| **What it does:** reads where an item is, or moves it to an exact place.
| ``canvas.coords(item)`` gives back the item's points, e.g. ``[10.0, 10.0, 50.0, 50.0]``.
| ``canvas.coords(item, x1, y1, x2, y2)`` moves the item to those points.

.. code-block:: python

    import tkinter as tk


    def where():
        x1, y1, x2, y2 = canvas.coords(box)
        result_label.config(text=f"Top-left corner is at ({x1}, {y1})")


    def move():
        canvas.move(box, 15, 10)


    def home():
        canvas.coords(box, 10, 10, 60, 60)      # Back to the start


    root = tk.Tk()
    root.geometry("320x300")
    root.title("coords")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack(pady=5)

    box = canvas.create_rectangle(10, 10, 60, 60, fill="orange")

    button_row = tk.Frame(root)
    button_row.pack()
    tk.Button(button_row, text="Move", command=move).pack(side="left", padx=5)
    tk.Button(button_row, text="Where?", command=where).pack(side="left", padx=5)
    tk.Button(button_row, text="Home", command=home).pack(side="left", padx=5)

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

----

Using the mouse and keyboard
-------------------------------

bind (mouse clicks)
~~~~~~~~~~~~~~~~~~~~~~

| **What it does:** runs a function when the mouse is used on the canvas.
| **How to write it:** ``canvas.bind("<Button-1>", function_name)``
| ``"<Button-1>"`` is a left click. ``"<B1-Motion>"`` is dragging with the left button held down.
| The function gets an ``event``. ``event.x`` and ``event.y`` tell you **where** the mouse is.

.. code-block:: python

    import tkinter as tk


    def draw_dot(event):
        x = event.x
        y = event.y
        canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="blue", outline="")


    root = tk.Tk()
    root.geometry("320x240")
    root.title("Paint")

    canvas = tk.Canvas(root, width=300, height=200, bg="white", cursor="pencil")
    canvas.pack(pady=10)

    canvas.bind("<Button-1>", draw_dot)     # Click to draw a dot
    canvas.bind("<B1-Motion>", draw_dot)    # Drag to draw a line of dots

    root.mainloop()

bind (keys)
~~~~~~~~~~~~~~~~~~

| ``root.bind("<Left>", function_name)`` runs a function when the left arrow key is pressed.
| Other keys: ``"<Right>"``, ``"<Up>"``, ``"<Down>"``, ``"<space>"``, ``"a"``.

.. code-block:: python

    import tkinter as tk


    def left(event):
        canvas.move(player, -10, 0)


    def right(event):
        canvas.move(player, 10, 0)


    def up(event):
        canvas.move(player, 0, -10)


    def down(event):
        canvas.move(player, 0, 10)


    root = tk.Tk()
    root.geometry("320x240")
    root.title("Arrow keys")

    canvas = tk.Canvas(root, width=300, height=200, bg="lightgreen")
    canvas.pack(pady=10)

    player = canvas.create_rectangle(140, 90, 160, 110, fill="blue")

    root.bind("<Left>", left)
    root.bind("<Right>", right)
    root.bind("<Up>", up)
    root.bind("<Down>", down)

    root.mainloop()

Animation with after
~~~~~~~~~~~~~~~~~~~~~~~

| ``root.after(milliseconds, function_name)`` runs a function after a short wait.
| If the function calls ``after`` again at its end, it keeps repeating. This makes things move by themselves.

.. code-block:: python

    import tkinter as tk

    speed = 4


    def animate():
        global speed
        canvas.move(ball, speed, 0)
        x1, y1, x2, y2 = canvas.coords(ball)
        if x2 >= 300 or x1 <= 0:         # Hit an edge?
            speed = -speed              # Bounce: go the other way
        root.after(20, animate)         # Run again in 20 milliseconds


    root = tk.Tk()
    root.geometry("320x240")
    root.title("Bouncing ball")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack(pady=10)

    ball = canvas.create_oval(10, 80, 50, 120, fill="red")

    animate()                           # Start the animation

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
      - Size of the canvas in pixels
      - ``width=300, height=200``
    * - ``bg``
      - Background colour
      - ``bg="white"``
    * - ``create_line()``
      - Draw a line
      - ``create_line(0, 0, 100, 100)``
    * - ``create_rectangle()``
      - Draw a rectangle
      - ``create_rectangle(10, 10, 50, 50)``
    * - ``create_oval()``
      - Draw an oval or circle
      - ``create_oval(10, 10, 50, 50)``
    * - ``create_polygon()``
      - Draw a shape from points
      - ``create_polygon(50, 0, 100, 80, 0, 80)``
    * - ``create_text()``
      - Write words
      - ``create_text(150, 100, text="Hi")``
    * - ``create_image()``
      - Show a picture
      - ``create_image(150, 100, image=pic)``
    * - ``fill``, ``outline``, ``width``
      - Inside colour, edge colour, thickness
      - ``fill="red", outline="black", width=2``
    * - ``move()``
      - Move an item by an amount
      - ``canvas.move(ball, 10, 0)``
    * - ``coords()``
      - Read or set an item's position
      - ``canvas.coords(ball)``
    * - ``itemconfig()``
      - Change an item's options
      - ``canvas.itemconfig(ball, fill="blue")``
    * - ``delete()``
      - Remove items
      - ``canvas.delete("all")``
    * - ``bind()``
      - Run a function on a click or key
      - ``canvas.bind("<Button-1>", click)``

----

.. admonition:: Tasks

    #. Make a window titled "Drawing" with a 300x200 white canvas. Draw a red line from the top-left corner to the bottom-right corner.
    #. On the same canvas, draw a yellow circle with a black edge in the middle of the canvas, 100 pixels wide.
    #. Draw a snowman: three white circles on top of each other on a light blue canvas, with a carrot-coloured triangle for the nose.
    #. Draw a green square and add four buttons, "Up", "Down", "Left" and "Right", that each move the square 10 pixels in that direction.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("320x240")
                    root.title("Drawing")

                    canvas = tk.Canvas(root, width=300, height=200, bg="white")
                    canvas.pack(pady=10)

                    canvas.create_line(0, 0, 300, 200, fill="red")

                    root.mainloop()

            .. tab-item:: Q2

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("320x240")
                    root.title("Drawing")

                    canvas = tk.Canvas(root, width=300, height=200, bg="white")
                    canvas.pack(pady=10)

                    canvas.create_line(0, 0, 300, 200, fill="red")
                    canvas.create_oval(100, 50, 200, 150, fill="yellow", outline="black")

                    root.mainloop()

            .. tab-item:: Q3

                .. code-block:: python

                    import tkinter as tk

                    root = tk.Tk()
                    root.geometry("320x340")
                    root.title("Snowman")

                    canvas = tk.Canvas(root, width=300, height=300, bg="lightblue")
                    canvas.pack(pady=10)

                    canvas.create_oval(90, 170, 210, 290, fill="white")      # Bottom
                    canvas.create_oval(110, 95, 190, 175, fill="white")      # Middle
                    canvas.create_oval(120, 40, 180, 100, fill="white")      # Head
                    canvas.create_polygon(150, 65, 150, 75, 175, 70, fill="orange")  # Nose

                    root.mainloop()

            .. tab-item:: Q4

                .. code-block:: python

                    import tkinter as tk


                    def up():
                        canvas.move(square, 0, -10)


                    def down():
                        canvas.move(square, 0, 10)


                    def left():
                        canvas.move(square, -10, 0)


                    def right():
                        canvas.move(square, 10, 0)


                    root = tk.Tk()
                    root.geometry("320x280")
                    root.title("Move the square")

                    canvas = tk.Canvas(root, width=300, height=200, bg="white")
                    canvas.pack(pady=5)

                    square = canvas.create_rectangle(130, 80, 170, 120, fill="green")

                    tk.Button(root, text="Up", command=up).pack(side="left", padx=10)
                    tk.Button(root, text="Down", command=down).pack(side="left", padx=10)
                    tk.Button(root, text="Left", command=left).pack(side="left", padx=10)
                    tk.Button(root, text="Right", command=right).pack(side="left", padx=10)

                    root.mainloop()
