====================================================
tk button
====================================================

| See: https://www.geeksforgeeks.org/python-creating-a-button-in-tkinter/?ref=lbp
| See: https://www.youtube.com/watch?v=8VoTtF-CxrM
| See: https://www.youtube.com/watch?v=mPQdJDVtev0

----

Usage
---------------

| The `tkinter.Button` widget provides a button.
| To create a button widget the general syntax is:

.. py:function:: button_widget = tk.Button(parent, option=value)

    | parent is the window or frame object.
    | Options can be passed as parameters separated by commas.


STANDARD OPTIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

    activebackground, activeforeground, anchor,
    background, bitmap, borderwidth, cursor,
    disabledforeground, font, foreground
    highlightbackground, highlightcolor,
    highlightthickness, image, justify,
    padx, pady, relief, repeatdelay,
    repeatinterval, takefocus, text,
    textvariable, underline, wraplength

WIDGET-SPECIFIC OPTIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

    command, compound, default, height,
    overrelief, state, width


----

Code example
---------------

.. code-block:: python

    import tkinter as tk

    def button_clicked():
        print("Button clicked!")

    window = tk.Tk()

    # Creating a button with specified options
    button = tk.Button(window,
                    text="Click Me",
                    command=button_clicked,
                    activebackground="blue",
                    activeforeground="white",
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",
                    padx=10,
                    pady=5,
                    width=15,
                    wraplength=100)

    button.pack(padx=20, pady=20)

    window.mainloop()

----

Parameter syntax
----------------------

.. py:function:: button_widget = tk.Button(parent, option=value)

    | parent is the window or frame object.
    | Options can be passed as parameters separated by commas.

    **Parameters:**

    .. py:attribute:: text

        | Syntax: ``button_widget = tk.Button(parent, text="Click Me")``
        | Description: Sets the text displayed on the button.
        | Default: ``""``
        | Example: ``button_widget = tk.Button(window, text="Click Me")``

    .. py:attribute:: command

        | Syntax: ``button_widget = tk.Button(parent, command=callback_function)``
        | Description: Specifies the function to be called when the button is clicked.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, command=on_click)``

    .. py:attribute:: activebackground

        | Syntax: ``button_widget = tk.Button(parent, activebackground="color")``
        | Description: Sets the background color of the button when it is active or pressed.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, activebackground="lightblue")``

    .. py:attribute:: activeforeground

        | Syntax: ``button_widget = tk.Button(parent, activeforeground="color")``
        | Description: Sets the foreground (text) color of the button when it is active or pressed.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, activeforeground="white")``

    .. py:attribute:: anchor

        | Syntax: ``button_widget = tk.Button(parent, anchor="position")``
        | Description: Determines where the text is positioned within the button. Common values are "center", "n", "s", "e", "w", etc.
        | Default: ``"center"``
        | Example: ``button_widget = tk.Button(window, anchor="center")``

    .. py:attribute:: bd
    .. py:attribute:: borderwidth

        | Syntax: ``button_widget = tk.Button(parent, bd=width)``
        | Description: Sets the width of the button's border.
        | Default: ``2``
        | Example: ``button_widget = tk.Button(window, bd=2)``

    .. py:attribute:: bg
    .. py:attribute:: background

        | Syntax: ``button_widget = tk.Button(parent, bg="color")``
        | Description: Sets the background color of the button.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, bg="blue")``

    .. py:attribute:: cursor

        | Syntax: ``button_widget = tk.Button(parent, cursor="cursor_type")``
        | Description: Changes the mouse cursor when it hovers over the button.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, cursor="hand2")``

    .. py:attribute:: disabledforeground

        | Syntax: ``button_widget = tk.Button(parent, disabledforeground="color")``
        | Description: Sets the foreground (text) color of the button when it is disabled.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, disabledforeground="grey")``

    .. py:attribute:: fg

        | Syntax: ``button_widget = tk.Button(parent, fg="color")``
        | Description: Sets the foreground (text) color of the button.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, fg="white")``

    .. py:attribute:: font

        | Syntax: ``button_widget = tk.Button(parent, font=("font_name", size))``
        | Description: Sets the font type and size of the button text.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, font=("Arial", 12))``

    .. py:attribute:: height

        | Syntax: ``button_widget = tk.Button(parent, height=height_in_lines)``
        | Description: Sets the height of the button in lines of text.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, height=2)``

    .. py:attribute:: highlightbackground

        | Syntax: ``button_widget = tk.Button(parent, highlightbackground="color")``
        | Description: Sets the color of the focus highlight when the button does not have focus.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, highlightbackground="black")``

    .. py:attribute:: highlightcolor

        | Syntax: ``button_widget = tk.Button(parent, highlightcolor="color")``
        | Description: Sets the color of the focus highlight when the button has focus.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, highlightcolor="red")``

    .. py:attribute:: highlightthickness

        | Syntax: ``button_widget = tk.Button(parent, highlightthickness=thickness)``
        | Description: Sets the thickness of the focus highlight.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, highlightthickness=1)``

    .. py:attribute:: justify

        | Syntax: ``button_widget = tk.Button(parent, justify="alignment")``
        | Description: Specifies how multiple lines of text are aligned. Common values are "left", "center", "right".
        | Default: ``"center"``
        | Example: ``button_widget = tk.Button(window, justify="center")``

    .. py:attribute:: overrelief

        | Syntax: ``button_widget = tk.Button(parent, overrelief="relief_type")``
        | Description: Sets the relief style of the button when the mouse is over it. Common values are "raised", "sunken", "flat", "ridge", "solid", "groove".
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, overrelief="raised")``

    .. py:attribute:: padx

        | Syntax: ``button_widget = tk.Button(parent, padx=padding)``
        | Description: Sets the horizontal padding inside the button.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, padx=10)``

    .. py:attribute:: pady

        | Syntax: ``button_widget = tk.Button(parent, pady=padding)``
        | Description: Sets the vertical padding inside the button.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, pady=5)``

    .. py:attribute:: width

        | Syntax: ``button_widget = tk.Button(parent, width=width_in_characters)``
        | Description: Sets the width of the button in characters.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, width=20)``

    .. py:attribute:: wraplength

        | Syntax: ``button_widget = tk.Button(parent, wraplength=length_in_pixels)``
        | Description: Sets the wrap length for the button text in pixels.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, wraplength=100)``


Additional parameters
--------------------------

.. py:function:: button_widget = tk.Button(parent, option=value)

    | parent is the window or frame object.
    | Options can be passed as parameters separated by commas.

    .. py:attribute:: bitmap

        | Syntax: ``button_widget = tk.Button(parent, bitmap="bitmap_name")``
        | Description: Sets a bitmap to be displayed on the button.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, bitmap="error")```

    .. py:attribute:: image

        | Syntax: ``button_widget = tk.Button(parent, image=image_object)``
        | Description: Sets an image to be displayed on the button.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, image=my_image)``

    .. py:attribute:: relief

        | Syntax: ``button_widget = tk.Button(parent, relief="relief_type")``
        | Description: Sets the type of border relief. Common values are "flat", "raised", "sunken", "groove", "ridge".
        | Default: ``"flat"``
        | Example: ``button_widget = tk.Button(window, relief="raised")``

    .. py:attribute:: repeatdelay

        | Syntax: ``button_widget = tk.Button(parent, repeatdelay=milliseconds)``
        | Description: Sets the delay in milliseconds before the button starts repeating the command when held down.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, repeatdelay=500)``

    .. py:attribute:: repeatinterval

        | Syntax: ``button_widget = tk.Button(parent, repeatinterval=milliseconds)``
        | Description: Sets the interval in milliseconds between repeats of the command when the button is held down.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, repeatinterval=100)``

    .. py:attribute:: takefocus

        | Syntax: ``button_widget = tk.Button(parent, takefocus=boolean)``
        | Description: Determines whether the button can receive focus via keyboard navigation.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, takefocus=True)``

    .. py:attribute:: textvariable

        | Syntax: ``button_widget = tk.Button(parent, textvariable=variable)``
        | Description: Associates a Tkinter variable (usually a StringVar) with the button text.
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, textvariable=my_var)``

    .. py:attribute:: underline

        | Syntax: ``button_widget = tk.Button(parent, underline=index)``
        | Description: Underlines the character at the specified index in the button text.
        | Default: ``-1``
        | Example: ``button_widget = tk.Button(window, underline=0)``

    .. py:attribute:: compound

        | Syntax: ``button_widget = tk.Button(parent, compound="position")``
        | Description: Specifies the relative position of the image and text on the button. Common values are "top", "bottom", "left", "right", "center".
        | Default: ``None``
        | Example: ``button_widget = tk.Button(window, compound="left")``

    .. py:attribute:: default

        | Syntax: ``button_widget = tk.Button(parent, default="state")``
        | Description: Sets the default button state. Common values are "normal", "active", "disabled".
        | Example: ``button_widget = tk.Button(window, default="active")``

    .. py:attribute:: state

        | Syntax: ``button_widget = tk.Button(parent, state="state")``
        | Description: Sets the state of the button. Common values are "normal", "active", "disabled".
        | Example: ``button_widget = tk.Button(window, state="disabled")``
