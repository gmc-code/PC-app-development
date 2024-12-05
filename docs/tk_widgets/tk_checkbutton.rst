====================================================
tk Checkbutton
====================================================

| See: https://www.geeksforgeeks.org/python-tkinter-checkbutton-widget/

----

Usage
---------------

| The `tkinter.Checkbutton` widget provides a checkbutton (checkbox).
| To create a checkbutton widget, the general syntax is (assuming import via "import tkinter as tk"):

.. py:function:: checkbutton_widget = tk.Checkbutton(parent, option=value)

    | parent is the window or frame object.
    | Options can be passed as parameters separated by commas.

----

Using check buttons
---------------------------

.. image:: images/check_buttons.png
    :scale: 100%

| This code demonstrates the creation of check boxes (check buttons).
| The zip function is used to efficiently loop through 2 lists together.

.. py:function:: for item1, item2 in zip(list1, list2)

    - The `zip` function pairs each element from `list1` with the corresponding element from `list2`.
    - In each iteration of the loop, item1 is an element from `list1` and `item2` is the corresponding element from `list2`.


 | State Management: option_vars1 is a list that holds IntVar objects. Each IntVar is associated with a checkbutton and is used to track whether the checkbutton is selected (1) or not selected (0). While those values are not used to do anything in the code below, they should be set up in preparation for doing so.

.. code-block:: python

    import tkinter as tk
    from tkinter import font

    # Create the main window
    root = tk.Tk()
    root.title("Checkbutton Example")

    # Create a frame with a background color
    frame1 = tk.Frame(root, bg="light blue")
    frame1.pack(anchor="nw", padx=10, pady=10)

    # Define a font style
    fontStyle = font.Font(family="Lucida Grande", size=18)

    # Define the options for group 1
    options_grp1 = ["Option 1", "Option 2", "Option 3"]

    # Create a list to hold the IntVar for each checkbutton
    option_vars1 = []
    for option in options_grp1:
        var = tk.IntVar()
        option_vars1.append(var)
        # Preselect "Option 1"
        if option == "Option 1":
            var.set(1)

    # Create and pack the checkbuttons for group 1
    for option, var in zip(options_grp1, option_vars1):
        button = tk.Checkbutton(frame1, text=option, variable=var, indicatoron=0,
                                bg="white", fg="black", font=fontStyle, padx=10, pady=5)
        button.pack(anchor="nw", side="left", padx=5, pady=5)


    # Define the options for group 2
    options_grp2 = ["Option 4", "Option 5", "Option 6"]

    # Create a list to hold the IntVar for each checkbutton
    option_vars2 = []
    for option in options_grp2:
        var = tk.IntVar()
        option_vars2.append(var)
        # Preselect "Option 4"
        if option == "Option 4":
            var.set(1)

    # Create and pack the checkbuttons for group 2
    for option, var in zip(options_grp2, option_vars2):
        button = tk.Checkbutton(root, text=option, variable=var, indicatoron=1,
                                bg="white", fg="black", font=fontStyle, padx=10, pady=5)
        button.pack(anchor="nw", side="left", padx=5, pady=5)

    # Run the main event loop
    root.mainloop()

----

Parameter syntax
----------------------

.. py:function:: checkbutton_widget = tk.Checkbutton(parent, option=value)

    | parent is the window or frame object.
    | Options can be passed as parameters separated by commas.

    **Parameters:**

    .. py:attribute:: activebackground

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, activebackground="color")``
        | Description: Sets the background color of the checkbutton when it is active.
        | Default: SystemButtonFace
        | Example: ``checkbutton_widget = tk.Checkbutton(root, activebackground="lightblue")``

    .. py:attribute:: activeforeground

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, activeforeground="color")``
        | Description: Sets the foreground color of the checkbutton when it is active.
        | Default: SystemWindowText
        | Example: ``checkbutton_widget = tk.Checkbutton(root, activeforeground="blue")``

    .. py:attribute:: anchor

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, anchor="position")``
        | Description: Sets the anchor position for the text and indicator.
        | Default: center
        | Example: ``checkbutton_widget = tk.Checkbutton(root, anchor="w")``

    .. py:attribute:: background

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, background="color")``
        | Description: Sets the background color of the checkbutton.
        | Default: SystemButtonFace
        | Example: ``checkbutton_widget = tk.Checkbutton(root, background="lightyellow")``

    .. py:attribute:: bd

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, bd=border_width)``
        | Description: Sets the border width of the checkbutton.
        | Default: 2
        | Example: ``checkbutton_widget = tk.Checkbutton(root, bd=5)``

    .. py:attribute:: bg

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, bg="color")``
        | Description: Sets the background color of the checkbutton.
        | Default: SystemButtonFace
        | Example: ``checkbutton_widget = tk.Checkbutton(root, bg="lightyellow")``

    .. py:attribute:: bitmap

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, bitmap="bitmap_name")``
        | Description: Sets a bitmap image to be displayed on the checkbutton.
        | Default: None
        | Example: ``checkbutton_widget = tk.Checkbutton(root, bitmap="error")``

    .. py:attribute:: borderwidth

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, borderwidth=width)``
        | Description: Sets the width of the border around the checkbutton.
        | Default: 2
        | Example: ``checkbutton_widget = tk.Checkbutton(root, borderwidth=3)``

    .. py:attribute:: command

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, command=function)``
        | Description: Specifies a function to be called when the checkbutton is toggled.
        | Default: None
        | Example: ``checkbutton_widget = tk.Checkbutton(root, command=my_function)``

    .. py:attribute:: compound

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, compound="position")``
        | Description: Specifies how to display the image and text (if both are set).
        | Default: none
        | Example: ``checkbutton_widget = tk.Checkbutton(root, compound="left")``

    .. py:attribute:: cursor

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, cursor="cursor_type")``
        | Description: Sets the mouse cursor when hovering over the checkbutton.
        | Default: arrow
        | Example: ``checkbutton_widget = tk.Checkbutton(root, cursor="hand2")``

    .. py:attribute:: disabledforeground

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, disabledforeground="color")``
        | Description: Sets the foreground color when the checkbutton is disabled.
        | Default: SystemDisabledText
        | Example: ``checkbutton_widget = tk.Checkbutton(root, disabledforeground="gray")``

    .. py:attribute:: fg

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, fg="color")``
        | Description: Sets the foreground color of the checkbutton (text color).
        | Default: SystemWindowText
        | Example: ``checkbutton_widget = tk.Checkbutton(root, fg="black")``

    .. py:attribute:: font

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, font=("font_name", size, "style"))``
        | Description: Specifies the font type, size, and style for the text of the checkbutton.
        | Default: TkDefaultFont
        | Example: ``checkbutton_widget = tk.Checkbutton(root, font=("Arial", 12, "bold"))``

    .. py:attribute:: height

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, height=value)``
        | Description: Sets the height of the checkbutton.
        | Default: 0 (automatically determined)
        | Example: ``checkbutton_widget = tk.Checkbutton(root, height=2)``

    .. py:attribute:: highlightbackground

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, highlightbackground="color")``
        | Description: Sets the background color of the checkbutton when it does not have focus.
        | Default: SystemButtonFace
        | Example: ``checkbutton_widget = tk.Checkbutton(root, highlightbackground="gray")``

    .. py:attribute:: highlightcolor

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, highlightcolor="color")``
        | Description: Sets the color of the highlight when the checkbutton has focus.
        | Default: SystemWindowFrame
        | Example: ``checkbutton_widget = tk.Checkbutton(root, highlightcolor="blue")``

    .. py:attribute:: highlightthickness

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, highlightthickness=thickness)``
        | Description: Sets the thickness of the highlight border.
        | Default: 1
        | Example: ``checkbutton_widget = tk.Checkbutton(root, highlightthickness=2)``

    .. py:attribute:: image

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, image="image_name")``
        | Description: Sets an image to be displayed on the checkbutton.
        | Default: None
        | Example: ``checkbutton_widget = tk.Checkbutton(root, image=my_image)``

    .. py:attribute:: indicatoron

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, indicatoron=1)``
        | Description: Specifies whether to show the indicator (true or false).
        | Default: 1
        | Example: ``checkbutton_widget = tk.Checkbutton(root, indicatoron=0)``

    .. py:attribute:: justify

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, justify="position")``
        | Description: Sets the justification of the text (left, center, right).
        | Default: center
        | Example: ``checkbutton_widget = tk.Checkbutton(root, justify="right")``

    .. py:attribute:: offrelief

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, offrelief="style")``
        | Description: Sets the relief style for the indicator when off.
        | Default: raised
        | Example: ``checkbutton_widget = tk.Checkbutton(root, offrelief="flat")``

    .. py:attribute:: offvalue

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, offvalue=value)``
        | Description: Sets the value associated with the checkbutton when it is not checked.
        | Default: 0
        | Example: ``checkbutton_widget = tk.Checkbutton(root, offvalue=0)``

    .. py:attribute:: onvalue

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, onvalue=value)``
        | Description: Sets the value associated with the checkbutton when it is checked.
        | Default: 1
        | Example: ``checkbutton_widget = tk.Checkbutton(root, onvalue=1)``

    .. py:attribute:: overrelief

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, overrelief="style")``
        | Description: Sets the relief style for the indicator when hovered over.
        | Default: None
        | Example: ``checkbutton_widget = tk.Checkbutton(root, overrelief="sunken")``

    .. py:attribute:: padx

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, padx=padding_value)``
        | Description: Sets the horizontal padding within the checkbutton.
        | Default: 1
        | Example: ``checkbutton_widget = tk.Checkbutton(root, padx=10)``

    .. py:attribute:: pady

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, pady=padding_value)``
        | Description: Sets the vertical padding within the checkbutton.
        | Default: 1
        | Example: ``checkbutton_widget = tk.Checkbutton(root, pady=10)``

    .. py:attribute:: relief

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, relief="style")``
        | Description: Sets the border style of the checkbutton. Options include `flat`, `raised`, `sunken`, `groove`, `ridge`.
        | Default: flat
        | Example: ``checkbutton_widget = tk.Checkbutton(root, relief="raised")``

    .. py:attribute:: selectcolor

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, selectcolor="color")``
        | Description: Sets the color of the indicator when the checkbutton is selected.
        | Default: SystemWindow
        | Example: ``checkbutton_widget = tk.Checkbutton(root, selectcolor="lightgreen")``

    .. py:attribute:: selectimage

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, selectimage="image_name")``
        | Description: Sets an image to be displayed when the checkbutton is selected.
        | Default: None
        | Example: ``checkbutton_widget = tk.Checkbutton(root, selectimage=my_selected_image)``

    .. py:attribute:: state

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, state="state_type")``
        | Description: Sets the state of the checkbutton. Options include `normal`, `disabled`, or `active`.
        | Default: normal
        | Example: ``checkbutton_widget = tk.Checkbutton(root, state="disabled")``

    .. py:attribute:: takefocus

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, takefocus=1)``
        | Description: Allows the checkbutton to take focus on click.
        | Default: None
        | Example: ``checkbutton_widget = tk.Checkbutton(root, takefocus=1)``

    .. py:attribute:: text

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, text="label")``
        | Description: Sets the text label for the checkbutton.
        | Default: None
        | Example: ``checkbutton_widget = tk.Checkbutton(root, text="Option 1")``

    .. py:attribute:: textvariable

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, textvariable=variable)``
        | Description: Associates a variable with the text of the checkbutton.
        | Default: None
        | Example: ``checkbutton_widget = tk.Checkbutton(root, textvariable=my_text_var)``

    .. py:attribute:: tristateimage

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, tristateimage="image_name")``
        | Description: Sets an image to be displayed when the checkbutton is in a tri-state mode.
        | Default: None
        | Example: ``checkbutton_widget = tk.Checkbutton(root, tristateimage=my_tristate_image)``

    .. py:attribute:: tristatevalue

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, tristatevalue=value)``
        | Description: Sets the value associated with the checkbutton in a tri-state mode.
        | Default: None
        | Example: ``checkbutton_widget = tk.Checkbutton(root, tristatevalue=2)``

    .. py:attribute:: underline

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, underline=index)``
        | Description: Specifies the index of the character to underline in the text.
        | Default: -1 (no underline)
        | Example: ``checkbutton_widget = tk.Checkbutton(root, underline=0)``

    .. py:attribute:: variable

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, variable=control_variable)``
        | Description: Associates the checkbutton with a control variable (e.g., `IntVar`, `StringVar`).
        | Default: !checkbutton-1
        | Example: ``checkbutton_widget = tk.Checkbutton(root, variable=my_var)``

    .. py:attribute:: width

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, width=width_value)``
        | Description: Sets the width of the checkbutton.
        | Default: 0 (automatically determined)
        | Example: ``checkbutton_widget = tk.Checkbutton(root, width=30)``

    .. py:attribute:: wraplength

        | Syntax: ``checkbutton_widget = tk.Checkbutton(parent, wraplength=length)``
        | Description: Sets the line length for text wrapping in the checkbutton.
        | Default: 0 (no wrapping)
        | Example: ``checkbutton_widget = tk.Checkbutton(root, wraplength=100)``
