====================================================
tk Button
====================================================

| See: `<https://docs.python.org/3/library/tkinter.html#tkinter.Button>`_
| See: `<https://www.geeksforgeeks.org/python-creating-a-button-in-tkinter/>`_

----

Usage
---------------

| The `tkinter.Button` widget provides a button.
| To create a button widget the general syntax is (assuming import via "import tkinter as tk"):

.. py:function:: button_widget = tk.Button(parent, option=value)

    | parent is the window or frame object.
    | Options can be passed as parameters separated by commas.


----

Sample button
---------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::

      initial
      ^^^
      .. image:: images/button_simple.png
        :scale: 100

   .. grid-item-card::

      pressed
      ^^^
      .. image:: images/button_simple_pressed.png
        :scale: 100

| The code below creates a button with customised colours. The button changes appearance while it is being pressed.
| The button will not appear until it is placed in the window using a geometry manager such as ``pack()``, ``grid()`` or ``place()``.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.title("Button Widget Example")
    root.geometry("350x100")

    # Creating a button with specified options
    button = tk.Button(
        root,
        text="Button",
        fg="black",  # Text color
        bg="lightblue",  # Background color
        activebackground="blue",  # Background color when clicked
        activeforeground="white",  # Text color when clicked
        font=("Arial", 12),
        padx=10,
        pady=5,
        width=15,
    )

    button.pack(padx=20, pady=20)

    root.mainloop()

----

.. admonition:: Tasks

    #. Modify the code above to change the window title to "Button question," set the window size to 350x100, set the button text to "Click Me", a light gray background, black text color, a black background when clicked, white text when clicked, Arial font size 14, centered text alignment, a border width of 3, a height of 2, a hand-shaped cursor on hover, a raised border style, a sunken border style on hovering over the button, horizontal inside padding of 10, vertical inside padding of 5, a width of 15, and text wrapping after 50 pixels, and adjust the pack method to add padding of 20 pixels on all sides.

    .. image:: images/button_question.png
        :scale: 67

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code above to change the window title to "Button question," set the window size to 350x100, set the button text to "Click Me", a light gray background, black text color, a black background when clicked, white text when clicked, Arial font size 14, centered text alignment, a border width of 3, a height of 2, a hand-shaped cursor on hover, a raised border style, a sunken border style on hovering over the button, horizontal inside padding of 10, vertical inside padding of 5, a width of 15, and text wrapping after 50 pixels, and adjust the pack method to add padding of 20 pixels on all sides.

                .. code-block:: python

                    import tkinter as tk

                    # Create a new window
                    root = tk.Tk()
                    # Set the title of the window
                    root.title("Button question")
                    # Set the size of the window
                    root.geometry("350x100")

                    button = tk.Button(
                        root,
                        # Set the text displayed on the button
                        text="Click Me",
                        # Set the background color of the button
                        bg="lightgray",
                        # Set the text color of the button
                        fg="black",
                        # Set the background color when the button is active (clicked)
                        activebackground="black",
                        # Set the text color when the button is active (clicked)
                        activeforeground="white",
                        # Set the font of the button text
                        font=("Arial", 14),
                        # Set the alignment of the text within the button
                        anchor="center",
                        # Set the border width of the button
                        bd=3,
                        # Set the height of the button
                        height=2,
                        # Set the cursor that appears when hovering over the button
                        cursor="hand2",
                        # Set the relief style of the button
                        relief="raised",
                        # Set the relief style of the button when hovering over the button
                        overrelief="sunken",
                        # Set the padding around the text inside the button (horizontal)
                        padx=10,
                        # Set the padding around the text inside the button (vertical)
                        pady=5,
                        # Set the width of the button
                        width=15,
                        # Set the maximum line length for the text before wrapping
                        wraplength=50,
                    )


                    button.pack(padx=20, pady=20)

                    root.mainloop()

----

Methods
----------------

.. py:function:: button_widget.invoke()

    | Calls the button's ``command`` callback as though the button had been clicked.

.. py:function:: button_widget.flash()

    | Briefly flashes the button between its active and normal colours.

.. py:function:: button_widget.config(option=value)

    | Changes one or more button options after the button has been created.

----

Button examples
----------------------

command example
~~~~~~~~~~~~~~~~~~

| ``command`` is the name of the function to run when the button is clicked.
| Write the function name **without** brackets: ``command=add_one``, not ``command=add_one()``.
| With brackets the function runs once when the button is created instead of when it is clicked.

.. code-block:: python

    import tkinter as tk

    clicks = 0


    def add_one():
        global clicks  # Allow the function to change the clicks variable
        clicks = clicks + 1
        count_label.config(text=f"Clicks: {clicks}")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Button command")

    count_label = tk.Label(root, text="Clicks: 0", font=("Arial", 20))
    count_label.pack(pady=20)

    button = tk.Button(root, text="Click me", font=("Arial", 14), command=add_one)
    button.pack()

    root.mainloop()

Changing the button with config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``config()`` changes a button after it has been created, e.g. its text or colour.
| ``cget("text")`` reads the current button text.

.. code-block:: python

    import tkinter as tk


    def toggle():
        if light_button.cget("text") == "Turn ON":
            light_button.config(text="Turn OFF", bg="yellow")
        else:
            light_button.config(text="Turn ON", bg="lightgray")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Button config")

    light_button = tk.Button(root, text="Turn ON", bg="lightgray", font=("Arial", 16),
                             width=10, command=toggle)
    light_button.pack(pady=40)

    root.mainloop()

state example
~~~~~~~~~~~~~~~~~~

| ``state="disabled"`` greys out a button so it cannot be clicked.
| ``state="normal"`` makes it clickable again.

.. code-block:: python

    import tkinter as tk


    def submit():
        submit_button.config(state="disabled")  # Can only submit once
        result_label.config(text="Submitted!")


    def reset():
        submit_button.config(state="normal")  # Clickable again
        result_label.config(text="")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Button state")

    submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=submit)
    submit_button.pack(pady=10)

    reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset)
    reset_button.pack()

    result_label = tk.Label(root, text="", font=("Arial", 16))
    result_label.pack(pady=10)

    root.mainloop()

Passing a value with lambda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``command`` cannot have brackets, so it cannot pass a value to the function directly.
| Wrap the call in ``lambda:`` so the function and its value only run when the button is clicked.
| This lets several buttons share one function.

.. code-block:: python

    import tkinter as tk


    def change_colour(colour):
        root.config(bg=colour)


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Button lambda")

    red_button = tk.Button(root, text="Red", width=8, command=lambda: change_colour("red"))
    red_button.pack(pady=5)

    green_button = tk.Button(root, text="Green", width=8, command=lambda: change_colour("green"))
    green_button.pack(pady=5)

    blue_button = tk.Button(root, text="Blue", width=8, command=lambda: change_colour("blue"))
    blue_button.pack(pady=5)

    root.mainloop()

Quit button example
~~~~~~~~~~~~~~~~~~~~~~~~

| ``root.destroy`` closes the window, so it can be used as the command of a Quit button.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Quit button")

    quit_button = tk.Button(root, text="Quit", font=("Arial", 14), bg="salmon",
                            command=root.destroy)
    quit_button.pack(pady=40)

    root.mainloop()

invoke example
~~~~~~~~~~~~~~~~~~

| ``invoke()`` runs the button's command from code, just as if it had been clicked.
| Here the Enter key "presses" the button.

.. code-block:: python

    import tkinter as tk


    def greet():
        result_label.config(text="Hello!")


    root = tk.Tk()
    root.geometry("300x200")
    root.title("Button invoke")

    greet_button = tk.Button(root, text="Greet", font=("Arial", 14), command=greet)
    greet_button.pack(pady=20)

    result_label = tk.Label(root, text="Press Enter or click", font=("Arial", 16))
    result_label.pack()

    # Pressing Enter anywhere in the window invokes the button
    root.bind("<Return>", lambda event: greet_button.invoke())

    root.mainloop()

----

Parameter syntax
----------------------

.. py:function:: button_widget = tk.Button(parent, option=value)

    | parent is the window or frame object.
    | Options can be passed as parameters separated by commas.

    **Parameters:**

    .. py:attribute:: activebackground

        | Syntax: ``button_widget = tk.Button(parent, activebackground="color")``
        | Description: Sets the background color of the button when it is active or pressed.
        | Default: SystemButtonFace RGB: (240, 240, 240)
        | Example: ``button_widget = tk.Button(root, activebackground="lightblue")``

    .. py:attribute:: activeforeground

        | Syntax: ``button_widget = tk.Button(parent, activeforeground="color")``
        | Description: Sets the foreground (text) color of the button when it is active or pressed.
        | Default: SystemButtonText RGB: (0, 0, 0)
        | Example: ``button_widget = tk.Button(root, activeforeground="white")``

    .. py:attribute:: anchor

        | Syntax: ``button_widget = tk.Button(parent, anchor="position")``
        | Description: Determines where the text is positioned within the button. Position values are "center", "n", "s", "e", "w", "ne", "nw", "se", "sw".
        | Default: ``"center"``
        | Example: ``button_widget = tk.Button(root, anchor="center")``

    .. py:attribute:: background
    .. py:attribute:: bg

        | Syntax: ``button_widget = tk.Button(parent, bg="color")``
        | Description: Sets the background color of the button.
        | Default: SystemButtonFace RGB: (240, 240, 240)
        | Example: ``button_widget = tk.Button(root, bg="blue")``

    .. py:attribute:: bitmap

        | Syntax: ``button_widget = tk.Button(parent, bitmap="bitmap_name")``
        | Description: Sets a bitmap to be displayed on the button.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(root, bitmap="error")``

    .. py:attribute:: borderwidth
    .. py:attribute:: bd

        | Syntax: ``button_widget = tk.Button(parent, bd=width)``
        | Description: Sets the width of the button's border.
        | Default: ``2``
        | Example: ``button_widget = tk.Button(root, bd=2)``

    .. py:attribute:: command

        | Syntax: ``button_widget = tk.Button(parent, command=callback_function)``
        | Description: Specifies the function to call when the button is clicked. Do not include parentheses after the function name.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(root, command=on_click)``

    .. py:attribute:: compound

        | Syntax: ``button_widget = tk.Button(parent, compound="position")``
        | Description: Specifies the relative position of the image and text on the button. Common values are "top", "bottom", "left", "right", "center".
        | Default: ``None``
        | Example: ``button_widget = tk.Button(root, compound="left")``

    .. py:attribute:: cursor

        | Syntax: ``button_widget = tk.Button(parent, cursor="cursor_type")``
        | Description: Changes the mouse cursor when it hovers over the button.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(root, cursor="hand2")``

        | Possible values include:
            - **"arrow"**: Standard arrow cursor.
            - **"circle"**: Small circle cursor.
            - **"clock"**: Clock or watch cursor.
            - **"cross"**: Crosshair cursor.
            - **"dotbox"**: Dotted box cursor.
            - **"exchange"**: Arrows pointing in opposite directions.
            - **"fleur"**: Four-way arrow for moving.
            - **"hand2"**: Hand cursor, commonly used to indicate a clickable item.
            - **"heart"**: Heart-shaped cursor.
            - **"man"**: Icon of a person.
            - **"mouse"**: Cursor shaped like a mouse.
            - **"pirate"**: Skull-and-crossbones cursor.
            - **"plus"**: Plus sign cursor.
            - **"shuttle"**: Shuttle or spaceship.
            - **"sizing"**: Cursor for resizing.
            - **"spider"**: Spider cursor.
            - **"spraycan"**: Spray can cursor.
            - **"star"**: Star-shaped cursor.
            - **"target"**: Target or bullseye cursor.
            - **"tcross"**: T-shaped crosshair cursor.
            - **"umbrella"**: Umbrella cursor.
            - **"wait"**: Hourglass or watch cursor.
            - **"xterm"**: I-beam cursor, commonly used for text selection.

    .. py:attribute:: default

        | Syntax: ``button_widget = tk.Button(parent, default="state")``
        | Description: Sets the default button state. State values are "normal", "active", "disabled".
        | Default: ``"disabled"``
        | Example: ``button_widget = tk.Button(root, default="active")``

    .. py:attribute:: disabledforeground

        | Syntax: ``button_widget = tk.Button(parent, disabledforeground="color")``
        | Description: Sets the foreground (text) color of the button when it is disabled.
        | Default: SystemDisabledText RGB: (109, 109, 109)
        | Example: ``button_widget = tk.Button(root, disabledforeground="grey")``

    .. py:attribute:: fg
    .. py:attribute:: foreground

        | Syntax: ``button_widget = tk.Button(parent, fg="color")``
        | Description: Sets the foreground (text) color of the button.
        | Default: SystemButtonText RGB: (0, 0, 0)
        | Example: ``button_widget = tk.Button(root, fg="white")``

    .. py:attribute:: font

        | Syntax: ``button_widget = tk.Button(parent, font=("font_name", size))``
        | Description: Sets the font type and size of the button text.
        | Default: ``None``; Default Font Family: Segoe UI; Default Font Size: 9
        | Example: ``button_widget = tk.Button(root, font=("Arial", 12))``

    .. py:attribute:: height

        | Syntax: ``button_widget = tk.Button(parent, height=height_in_lines)``
        | Description: Sets the height of the button in lines of text.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(root, height=2)``

    .. py:attribute:: highlightbackground

        | Syntax: ``button_widget = tk.Button(parent, highlightbackground="color")``
        | Description: Sets the color of the focus highlight when the button does not have focus.
        | Default: SystemButtonFace RGB: (240, 240, 240)
        | Example: ``button_widget = tk.Button(root, highlightbackground="black")``

    .. py:attribute:: highlightcolor

        | Syntax: ``button_widget = tk.Button(parent, highlightcolor="color")``
        | Description: Sets the color of the focus highlight when the button has focus.
        | Default: SystemWindowFrame RGB: (100, 100, 100)
        | Example: ``button_widget = tk.Button(root, highlightcolor="red")``

    .. py:attribute:: highlightthickness

        | Syntax: ``button_widget = tk.Button(parent, highlightthickness=thickness)``
        | Description: Sets the thickness of the focus highlight.
        | Default: ``1``
        | Example: ``button_widget = tk.Button(root, highlightthickness=1)``

    .. py:attribute:: image

        | Syntax: ``button_widget = tk.Button(parent, image=image_object)``
        | Description: Sets an image to be displayed on the button.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(root, image=my_image)``

    .. py:attribute:: justify

        | Syntax: ``button_widget = tk.Button(parent, justify="alignment")``
        | Description: Specifies how multiple lines of text are aligned. Alignment values are "left", "center", "right".
        | Default: ``"center"``
        | Example: ``button_widget = tk.Button(root, justify="center")``

    .. py:attribute:: overrelief

        | Syntax: ``button_widget = tk.Button(parent, overrelief="relief_type")``
        | Description: Sets the border style while the mouse pointer is over the button. Common values are "raised", "sunken", "flat", "ridge", "solid", "groove".
        | Default: ``None``
        | Example: ``button_widget = tk.Button(root, overrelief="raised")``

    .. py:attribute:: padx

        | Syntax: ``button_widget = tk.Button(parent, padx=padding)``
        | Description: Sets the horizontal padding inside the button.
        | Default: ``1``
        | Example: ``button_widget = tk.Button(root, padx=10)``

    .. py:attribute:: pady

        | Syntax: ``button_widget = tk.Button(parent, pady=padding)``
        | Description: Sets the vertical padding inside the button.
        | Default: ``1``
        | Example: ``button_widget = tk.Button(root, pady=5)``

    .. py:attribute:: relief

        | Syntax: ``button_widget = tk.Button(parent, relief="relief_type")``
        | Description: Sets the border style of the button. Common values are "flat", "raised", "sunken", "ridge", "solid", "groove".
        | Default: ``"raised"``
        | Example: ``button_widget = tk.Button(root, relief="solid")``

    .. py:attribute:: repeatdelay

        | Syntax: ``button_widget = tk.Button(parent, repeatdelay=delay_ms)``
        | Description: Sets the delay in milliseconds before the button action repeats when held down.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(root, repeatdelay=500)``

    .. py:attribute:: repeatinterval

        | Syntax: ``button_widget = tk.Button(parent, repeatinterval=interval_ms)``
        | Description: Sets the interval in milliseconds between repeats when the button is held down.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(root, repeatinterval=100)``

    .. py:attribute:: state

        | Syntax: ``button_widget = tk.Button(parent, state="state")``
        | Description: Sets the state of the button. State values are "normal", "active", "disabled".
        | Default: ``"normal"``
        | Example: ``button_widget = tk.Button(root, state="disabled")``

    .. py:attribute:: takefocus

        | Syntax: ``button_widget = tk.Button(parent, takefocus=boolean)``
        | Description: Determines whether the button can receive focus via the Tab key.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(root, takefocus=True)``

    .. py:attribute:: text

        | Syntax: ``button_widget = tk.Button(parent, text="text")``
        | Description: Sets the text displayed on the button.
        | Default: ``""``
        | Example: ``button_widget = tk.Button(root, text="Click Me")``

    .. py:attribute:: textvariable

        | Syntax: ``button_widget = tk.Button(parent, textvariable=stringvar)``
        | Description: Binds a StringVar variable to the button's text, allowing dynamic updates.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(root, textvariable=my_var)``

    .. py:attribute:: underline

        | Syntax: ``button_widget = tk.Button(parent, underline=index)``
        | Description: Specifies the index of the character in the text to underline.
        | Default: ``-1`` (No underline)
        | Example: ``button_widget = tk.Button(root, text="Save", underline=1)``

    .. py:attribute:: width

        | Syntax: ``button_widget = tk.Button(parent, width=width_in_chars)``
        | Description: Sets the width of the button in characters.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(root, width=10)``

    .. py:attribute:: wraplength

        | Syntax: ``button_widget = tk.Button(parent, wraplength=width_in_pixels)``
        | Description: Specifies the width (in pixels) at which the text should wrap to the next line.
        | Default: ``0`` (No wrapping)
        | Example: ``button_widget = tk.Button(root, wraplength=100)``



----

Default options
-----------------------

| Code to get the defaults for each button option is below.

.. code-block:: python

    import tkinter as tk

    root = tk.Tk()

    widget = tk.Button(root)
    widget_options = widget.keys()

    for option in widget_options:
        print(f"{option}: {widget.cget(option)}")  # cget retrieves the current value of the option




