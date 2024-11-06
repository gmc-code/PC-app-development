====================================================
tk Label
====================================================

| See: https://www.geeksforgeeks.org/python-tkinter-label/

----

Usage
---------------

| The `tkinter.Label` widget provides a text label.
| To create a label widget the general syntax is:

.. py:function:: label_widget  = tk.Label(parent, option=value)

    | `parent` is the window or frame object.
    | Options can be passed as parameters separated by commas.

----

Text
--------------

.. py:function:: label_widget  = tk.Label(parent, text=text_string)

    | `text_string` is text to display in the label widget.
    | e.g. label = tk.Label(window, text="label text")

Text example
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk

    # Create the main window
    window = tk.Tk()
    window.geometry("300x200")  # Set window size
    window.title("Label text")  # Set window title

    # Create the label widget
    label = tk.Label(window, text="label text")

    # Pack the label into the window
    label.pack()

    # Run the main event loop
    window.mainloop()

.. image:: images/label_text.png
    :scale: 100%

----

Font
----------

.. py:function:: label_widget  = tk.Label(parent, font=(font_type, font_size, font_style))

   - font_type is a font name. e.g "Arial"
   - font_size is the size of the font.  eg. 12
   - font_style can be bold, italic, underline or a space separated combination
   - Default Value: System-dependent (usually a default font)
   - Description: Specifies the font family, size, and style for the label text.
   - Example: To use a 12-point Arial font, use `font=("Arial", 12)`.
   - Example: To use a bold 12-point Arial font, use `font=("Arial", 12, "bold")`.
   - Example: To use a bold underlines 12-point Arial font, use `font=("Arial", 12, "bold underline")`.


font example
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk

    # Create the main window
    window = tk.Tk()
    window.geometry("300x200")  # Set window size
    window.title("Label font")  # Set window title

    # Create the label widget with options
    label = tk.Label(window, text="label text", font=("Arial", 24))

    # Pack the label into the window
    label.pack()

    # Run the main event loop
    window.mainloop()


.. image:: images/label_font.png
    :scale: 100%

----

Text color
---------------

.. py:function:: label_widget  = tk.Label(parent, fg=color)

   - color can be a color name, e.g blue, or a hex colour, e.g. #0000FF.
   - Default Value: System-dependent (usually black)
   - Description: Sets the foreground (text) color of the label.
   - Example: To set the text color to blue, use `fg="blue"` or `fg="#0000FF"`.


fg example
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk

    # Create the main window
    window = tk.Tk()
    window.geometry("300x200")  # Set window size
    window.title("Label fg")  # Set window title

    # Create the label widget with options
    label = tk.Label(window, text="label text", font=("Arial", 24), fg="blue")

    # Pack the label into the window
    label.pack()

    # Run the main event loop
    window.mainloop()

.. image:: images/label_fg.png
    :scale: 100%

----

Background color
--------------------------

.. py:function:: label_widget  = tk.Label(parent, bg=color)

   - color can be a color name or a hex colour.
   - Default Value: System-dependent (usually white)
   - Description: Sets the background color of the label.
   - Example: To set the background color to light yellow, use `bg="lightyellow"`.


bg example
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk

    # Create the main window
    window = tk.Tk()
    window.geometry("300x200")  # Set window size
    window.title("Label bg")  # Set window title

    # Create the label widget with options
    label = tk.Label(window, text="label text", font=("Arial", 24), fg="blue", bg="lightyellow")

    # Pack the label into the window
    label.pack()

    # Run the main event loop
    window.mainloop()

.. image:: images/label_bg.png
    :scale: 100%

----

Padding
-------------------

.. py:function:: label_widget  = tk.Label(parent, padx=x_integer, pady=y_integer)

   - x_integer and y_integer are integers
   - Default Value: 0
   - Description: Adds extra space (in pixels) around the label text.
   - Example: To add 12 pixels of padding on the left and right sides, use `padx=12`.
   - Example: To add 5 pixels of padding on the top and bottom, use `pady=5`.


padding example
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk

    # Create the main window
    window = tk.Tk()
    window.geometry("300x200")  # Set window size
    window.title("Label padding]")  # Set window title

    # Create the label widget with options
    label = tk.Label(text="label text", font=("Arial", 24), fg="blue", bg="lightyellow",
                    padx=60, pady=20)

    # Pack the label into the window
    label.pack()

    # Run the main event loop
    window.mainloop()

.. image:: images/label_padding.png
    :scale: 100%

----

Border
---------------

.. py:function:: label_widget  = tk.Label(parent, borderwidth=width)

   - width is an integer
   - Default Value: 0
   - Description: Specifies the border width for the label.
   - Example: To create a width of 2 pixels, use `borderwidth=2`.

.. py:function:: label_widget  = tk.Label(parent, relief=border_style)

   - border_style is one of "flat", "raised", "sunken", "solid", "ridge", "groove"
   - Default Value: "flat" (no border)
   - Description: Specifies the border style and width for the label.
   - Example: To create a solid border with a width of 1 pixels, use `relief="solid"` and `borderwidth=1`.


border example
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import tkinter as tk

    # Create the main window
    window = tk.Tk()
    window.geometry("300x200")  # Set window size
    window.title("Label border")  # Set window title

    # Create the label widget with options
    label = tk.Label(text="label text", font=("Arial", 24), fg="blue", bg="lightyellow",
                    padx=60, pady=20,
                    relief="solid", borderwidth=1)

    # Pack the label into the window
    label.pack()

    # Run the main event loop
    window.mainloop()

.. image:: images/label_border.png
    :scale: 67%

----

Options
--------------

.. py:function:: label_widget = tk.Label(parent, option=value)

    | parent is the window or frame object.
    | Options can be passed as parameters separated by commas.

    **Parameters:**

    .. py:attribute:: anchor

        | Syntax: ``label_widget = tk.Label(parent, anchor="position")``
        | Description: Sets the position of the text within the label widget. Common values are "n", "s", "e", "w", "ne", "nw", "se", "sw", and "center".
        | Default: ``"center"``
        | Example: ``label_widget = tk.Label(window, anchor="center")``

    .. py:attribute:: background
    .. py:attribute:: bg

        | Syntax: ``label_widget = tk.Label(parent, bg="color")``
        | Description: Sets the background color of the label.
        | Default: SystemButtonFace RGB: (240, 240, 240)
        | Example: ``label_widget = tk.Label(window, bg="blue")``

    .. py:attribute:: bitmap

        | Syntax: ``label_widget = tk.Label(parent, bitmap="bitmap_name")``
        | Description: Displays a bitmap on the label.
        | Default: ``None``
        | Example: ``label_widget = tk.Label(window, bitmap="error")``

    .. py:attribute:: borderwidth
    .. py:attribute:: bd

        | Syntax: ``label_widget = tk.Label(parent, bd=width)``
        | Description: Sets the width of the label's border in pixels.
        | Default: ``2``
        | Example: ``label_widget = tk.Label(window, bd=2)``

    .. py:attribute:: compound

        | Syntax: ``label_widget = tk.Label(parent, compound="position")``
        | Description: Specifies the position of text relative to the image on the label. Common values are "top", "bottom", "left", "right", "center".
        | Default: ``None``
        | Example: ``label_widget = tk.Label(window, compound="left")``

    .. py:attribute:: cursor

        | Syntax: ``label_widget = tk.Label(parent, cursor="cursor_type")``
        | Description: Changes the cursor appearance when hovering over the label.
        | Default: ``None``
        | Example: ``label_widget = tk.Label(window, cursor="hand2")``

        | Possible values include:
            - **"arrow"**: Standard arrow cursor.
            - **"circle"**: Small circle cursor.
            - **"clock"**: Clock or watch cursor.
            - **"cross"**: Crosshair cursor.
            - **"dotbox"**: Dotted box cursor.
            - **"exchange"**: Two arrows pointing in opposite directions.
            - **"fleur"**: Four-way arrow for moving.
            - **"hand2"**: Hand cursor, commonly used for clickable items.
            - **"heart"**: Heart-shaped cursor.
            - **"man"**: Small icon of a person.
            - **"mouse"**: Cursor shaped like a mouse.
            - **"pirate"**: Skull-and-crossbones cursor.
            - **"plus"**: Plus sign cursor.
            - **"shuttle"**: Shuttle or spaceship cursor.
            - **"sizing"**: Cursor for resizing.
            - **"spider"**: Spider cursor.
            - **"spraycan"**: Spray can cursor.
            - **"star"**: Star-shaped cursor.
            - **"target"**: Target or bullseye cursor.
            - **"tcross"**: T-shaped crosshair cursor.
            - **"umbrella"**: Umbrella cursor.
            - **"wait"**: Hourglass or watch cursor, typically used to indicate loading.
            - **"xterm"**: I-beam cursor, commonly used for text selection.

    .. py:attribute:: font

        | Syntax: ``label_widget = tk.Label(parent, font=("font_name", size))``
        | Description: Sets the font type and size of the label text.
        | Default: ``None``; Default Font Family: Segoe UI; Default Font Size: 9
        | Example: ``label_widget = tk.Label(window, font=("Arial", 12))``

    .. py:attribute:: foreground
    .. py:attribute:: fg

        | Syntax: ``label_widget = tk.Label(parent, fg="color")``
        | Description: Sets the foreground (text) color of the label.
        | Default: SystemButtonText RGB: (0, 0, 0)
        | Example: ``label_widget = tk.Label(window, fg="white")``

    .. py:attribute:: height

        | Syntax: ``label_widget = tk.Label(parent, height=height_in_lines)``
        | Description: Sets the height of the label in lines of text.
        | Default: ``None``
        | Example: ``label_widget = tk.Label(window, height=2)``

    .. py:attribute:: image

        | Syntax: ``label_widget = tk.Label(parent, image=image_object)``
        | Description: Displays an image on the label.
        | Default: ``None``
        | Example: ``label_widget = tk.Label(window, image=my_image)``

    .. py:attribute:: justify

        | Syntax: ``label_widget = tk.Label(parent, justify="alignment")``
        | Description: Specifies the alignment for multiple lines of text. Common values are "left", "center", and "right".
        | Default: ``"center"``
        | Example: ``label_widget = tk.Label(window, justify="left")``

    .. py:attribute:: padx

        | Syntax: ``label_widget = tk.Label(parent, padx=padding)``
        | Description: Sets horizontal padding inside the label.
        | Default: ``1``
        | Example: ``label_widget = tk.Label(window, padx=10)``

    .. py:attribute:: pady

        | Syntax: ``label_widget = tk.Label(parent, pady=padding)``
        | Description: Sets vertical padding inside the label.
        | Default: ``1``
        | Example: ``label_widget = tk.Label(window, pady=5)``

    .. py:attribute:: relief

        | Syntax: ``label_widget = tk.Label(parent, relief="relief_type")``
        | Description: Sets the border style of the label. Common values are "flat", "raised", "sunken", "ridge", "solid", and "groove".
        | Default: ``"flat"``
        | Example: ``label_widget = tk.Label(window, relief="solid")``

    .. py:attribute:: takefocus

        | Syntax: ``label_widget = tk.Label(parent, takefocus=boolean)``
        | Description: Determines if the label can receive focus via the Tab key.
        | Default: ``None``
        | Example: ``label_widget = tk.Label(window, takefocus=True)``

    .. py:attribute:: text

        | Syntax: ``label_widget = tk.Label(parent, text="text")``
        | Description: Sets the text displayed on the label.
        | Default: ``""``
        | Example: ``label_widget = tk.Label(window, text="Hello, World!")``

    .. py:attribute:: textvariable

        | Syntax: ``label_widget = tk.Label(parent, textvariable=stringvar)``
        | Description: Binds a StringVar variable to the label's text, enabling dynamic updates.
        | Default: ``None``
        | Example: ``label_widget = tk.Label(window, textvariable=my_var)``

    .. py:attribute:: underline

        | Syntax: ``label_widget = tk.Label(parent, underline=index)``
        | Description: Specifies the index of the character in the text to underline.
        | Default: ``-1`` (No underline)
        | Example: ``label_widget = tk.Label(window, text="Save", underline=1)``

    .. py:attribute:: width

        | Syntax: ``label_widget = tk.Label(parent, width=width_in_chars)``
        | Description: Sets the width of the label in characters.
        | Default: ``None``
        | Example: ``label_widget = tk.Label(window, width=10)``

    .. py:attribute:: wraplength

        | Syntax: ``label_widget = tk.Label(parent, wraplength=width_in_pixels)``
        | Description: Specifies the width in pixels at which the text should wrap to the next line.
        | Default: ``0`` (No wrapping)
        | Example: ``label_widget = tk.Label(window, wraplength=100)``


