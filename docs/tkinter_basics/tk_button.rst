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

    .. py:attribute:: command

        | Syntax: ``button_widget = tk.Button(parent, command=callback_function)``
        | Description: Specifies the function to be called when the button is clicked.

    .. py:attribute:: activebackground

        | Syntax: ``button_widget = tk.Button(parent, activebackground="color")``
        | Description: Sets the background color of the button when it is active or pressed.

    .. py:attribute:: activeforeground

        | Syntax: ``button_widget = tk.Button(parent, activeforeground="color")``
        | Description: Sets the foreground (text) color of the button when it is active or pressed.

    .. py:attribute:: anchor

        | Syntax: ``button_widget = tk.Button(parent, anchor="position")``
        | Description: Determines where the text is positioned within the button. Common values are "center", "n", "s", "e", "w", etc.

    .. py:attribute:: bd

        | Syntax: ``button_widget = tk.Button(parent, bd=width)``
        | Description: Sets the width of the button's border.

    .. py:attribute:: bg

        | Syntax: ``button_widget = tk.Button(parent, bg="color")``
        | Description: Sets the background color of the button.

    .. py:attribute:: cursor

        | Syntax: ``button_widget = tk.Button(parent, cursor="cursor_type")``
        | Description: Changes the mouse cursor when it hovers over the button.

    .. py:attribute:: disabledforeground

        | Syntax: ``button_widget = tk.Button(parent, disabledforeground="color")``
        | Description: Sets the foreground (text) color of the button when it is disabled.

    .. py:attribute:: fg

        | Syntax: ``button_widget = tk.Button(parent, fg="color")``
        | Description: Sets the foreground (text) color of the button.

    .. py:attribute:: font

        | Syntax: ``button_widget = tk.Button(parent, font=("font_name", size))``
        | Description: Sets the font type and size of the button text.

    .. py:attribute:: height

        | Syntax: ``button_widget = tk.Button(parent, height=height_in_lines)``
        | Description: Sets the height of the button in lines of text.

    .. py:attribute:: highlightbackground

        | Syntax: ``button_widget = tk.Button(parent, highlightbackground="color")``
        | Description: Sets the color of the focus highlight when the button does not have focus.

    .. py:attribute:: highlightcolor

        | Syntax: ``button_widget = tk.Button(parent, highlightcolor="color")``
        | Description: Sets the color of the focus highlight when the button has focus.

    .. py:attribute:: highlightthickness

        | Syntax: ``button_widget = tk.Button(parent, highlightthickness=thickness)``
        | Description: Sets the thickness of the focus highlight.

    .. py:attribute:: justify

        | Syntax: ``button_widget = tk.Button(parent, justify="alignment")``
        | Description: Specifies how multiple lines of text are aligned. Common values are "left", "center", "right".

    .. py:attribute:: overrelief

        | Syntax: ``button_widget = tk.Button(parent, overrelief="relief_type")``
        | Description: Sets the relief style of the button when the mouse is over it. Common values are "raised", "sunken", "flat", "ridge", "solid", "groove".

    .. py:attribute:: padx

        | Syntax: ``button_widget = tk.Button(parent, padx=padding)``
        | Description: Sets the horizontal padding inside the button.

    .. py:attribute:: pady

        | Syntax: ``button_widget = tk.Button(parent, pady=padding)``
        | Description: Sets the vertical padding inside the button.

    .. py:attribute:: width

        | Syntax: ``button_widget = tk.Button(parent, width=width_in_characters)``
        | Description: Sets the width of the button in characters.

    .. py:attribute:: wraplength

        | Syntax: ``button_widget = tk.Button(parent, wraplength=length_in_pixels)``
        | Description: Sets the wrap length for the button text in pixels.
