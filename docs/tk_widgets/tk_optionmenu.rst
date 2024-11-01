====================================================
tk Optionmenu
====================================================

| See: https://www.geeksforgeeks.org/tkinter-optionmenu-widget/

----

Usage
---------------

| The `tkinter.OptionMenu` widget provides a dropdown menu.
| To create an OptionMenu widget, the general syntax is:

.. py:function:: option_menu_widget = tk.OptionMenu(parent, variable, *values)

    | parent is the window or frame object.
    | variable is a `tk.StringVar` that holds the selected value.
    | *values are the options to be displayed in the dropdown menu, passed as separate arguments.

----

Sample OptionMenu
--------------------

.. code-block:: python

    import tkinter as tk

    def show_selection(*args):
        selected_fruit = fruit_var.get()
        text_widget.delete(1.0, 'end')
        text_widget.insert(tk.END, f"You selected: \n{selected_fruit}")

    # Create the main window
    window = tk.Tk()
    window.title("Fruit Selector")

    # Define a variable to hold the selected option
    fruit_var = tk.StringVar(window)
    fruit_var.trace("w", show_selection)  # Trace the variable to call show_selection on change

    # Define the options for the OptionMenu
    fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

    # Set the default value for the OptionMenu
    fruit_var.set(fruits[0])

    # Create the OptionMenu widget
    option_menu = tk.OptionMenu(window, fruit_var, *fruits)
       # Define the options for the OptionMenu
    fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

    # Set the default value for the OptionMenu
    fruit_var.set(fruits[0])

    # Create the OptionMenu widget
    option_menu = tk.OptionMenu(window, fruit_var, *fruits) option_menu.pack(pady=10)

    # Create a text widget to display the selected option with increased space
    text_widget = tk.Text(window, height=2, width=20, bg="white", fg="black", font=("Helvetica", 12), bd=2, relief="solid")
    text_widget.pack(pady=10, padx=20)

    # Run the main event loop
    window.mainloop()


| ``*fruits``: The asterisk (`*`) is used to unpack the list `fruits` into individual arguments.
| This means that each item in the `fruits` list is passed as a separate argument to the `OptionMenu`.
| For example, if `fruits = ["Apple", "Banana", "Cherry"]`, the `*fruits` will be equivalent to passing `"Apple", "Banana", "Cherry"` as separate arguments.

----

Parameter syntax
----------------------

.. py:function:: option_menu_widget = tk.OptionMenu(parent, variable, *values)

    | parent is the window or frame object where the OptionMenu will be placed.
    | variable is a Tkinter variable (like `tk.StringVar`) that stores the current selection.
    | values are the list of options that will appear in the menu.

    **Parameters:**

    .. py:attribute:: activebackground

        | Syntax: ``option_menu_widget.config(activebackground="color")``
        | Description: Background color of the selected item when active or hovered.
        | Default: SystemButtonFace
        | Example: ``option_menu_widget.config(activebackground="lightblue")``

    .. py:attribute:: activeforeground

        | Syntax: ``option_menu_widget.config(activeforeground="color")``
        | Description: Text color of the selected item when active or hovered.
        | Default: SystemButtonText
        | Example: ``option_menu_widget.config(activeforeground="white")``

    .. py:attribute:: anchor

        | Syntax: ``option_menu_widget.config(anchor="position")``
        | Description: Controls position of the text in the widget (e.g., "center", "w").
        | Default: center
        | Example: ``option_menu_widget.config(anchor="w")``

    .. py:attribute:: background or bg

        | Syntax: ``option_menu_widget.config(bg="color")``
        | Description: Background color of the menu.
        | Default: SystemButtonFace
        | Example: ``option_menu_widget.config(bg="white")``

    .. py:attribute:: bd or borderwidth

        | Syntax: ``option_menu_widget.config(bd=value)``
        | Description: Border width of the widget in pixels.
        | Default: 2
        | Example: ``option_menu_widget.config(bd=4)``

    .. py:attribute:: bitmap

        | Syntax: ``option_menu_widget.config(bitmap="bitmap")``
        | Description: Specifies a bitmap to display in place of text.
        | Default: None
        | Example: ``option_menu_widget.config(bitmap="warning")``

    .. py:attribute:: cursor

        | Syntax: ``option_menu_widget.config(cursor="cursor_type")``
        | Description: Changes the cursor when hovering over the menu.
        | Default: None
        | Example: ``option_menu_widget.config(cursor="hand2")``

    .. py:attribute:: direction

        | Syntax: ``option_menu_widget.config(direction="direction")``
        | Description: Specifies where the menu opens relative to the widget.
        | Default: below
        | Example: ``option_menu_widget.config(direction="above")``

    .. py:attribute:: disabledforeground

        | Syntax: ``option_menu_widget.config(disabledforeground="color")``
        | Description: Text color when the widget is disabled.
        | Default: SystemDisabledText
        | Example: ``option_menu_widget.config(disabledforeground="gray")``

    .. py:attribute:: fg or foreground

        | Syntax: ``option_menu_widget.config(fg="color")``
        | Description: Text color in the menu.
        | Default: SystemButtonText
        | Example: ``option_menu_widget.config(fg="blue")``

    .. py:attribute:: font

        | Syntax: ``option_menu_widget.config(font=("FontName", size, style))``
        | Description: Font of the text in the menu.
        | Default: TkDefaultFont
        | Example: ``option_menu_widget.config(font=("Arial", 12, "italic"))``

    .. py:attribute:: height

        | Syntax: ``option_menu_widget.config(height=value)``
        | Description: Height of the menu in number of lines.
        | Default: 0 (auto)
        | Example: ``option_menu_widget.config(height=2)``

    .. py:attribute:: highlightbackground

        | Syntax: ``option_menu_widget.config(highlightbackground="color")``
        | Description: Highlight color around the menu when it has focus.
        | Default: SystemButtonFace
        | Example: ``option_menu_widget.config(highlightbackground="orange")``

    .. py:attribute:: highlightcolor

        | Syntax: ``option_menu_widget.config(highlightcolor="color")``
        | Description: Color of the highlight border when focused.
        | Default: SystemWindowFrame
        | Example: ``option_menu_widget.config(highlightcolor="red")``

    .. py:attribute:: highlightthickness

        | Syntax: ``option_menu_widget.config(highlightthickness=value)``
        | Description: Thickness of the focus highlight border.
        | Default: 2
        | Example: ``option_menu_widget.config(highlightthickness=3)``

    .. py:attribute:: image

        | Syntax: ``option_menu_widget.config(image=image_object)``
        | Description: Specifies an image to display in place of text.
        | Default: None
        | Example: ``option_menu_widget.config(image=my_image)``

    .. py:attribute:: indicatoron

        | Syntax: ``option_menu_widget.config(indicatoron=boolean)``
        | Description: Displays or hides the indicator triangle.
        | Default: 1 (on)
        | Example: ``option_menu_widget.config(indicatoron=False)``

    .. py:attribute:: justify

        | Syntax: ``option_menu_widget.config(justify="alignment")``
        | Description: Specifies text alignment (left, center, or right).
        | Default: center
        | Example: ``option_menu_widget.config(justify="left")``

    .. py:attribute:: menu

        | Syntax: ``option_menu_widget["menu"]``
        | Description: Accesses the menu widget for customization.
        | Default: .!optionmenu.menu
        | Example: ``option_menu_widget["menu"].config(bg="lightgray")``

    .. py:attribute:: padx

        | Syntax: ``option_menu_widget.config(padx=value)``
        | Description: Horizontal padding around the text.
        | Default: 5
        | Example: ``option_menu_widget.config(padx=10)``

    .. py:attribute:: pady

        | Syntax: ``option_menu_widget.config(pady=value)``
        | Description: Vertical padding around the text.
        | Default: 4
        | Example: ``option_menu_widget.config(pady=8)``

    .. py:attribute:: relief

        | Syntax: ``option_menu_widget.config(relief="style")``
        | Description: Specifies the border style (e.g., "raised", "sunken").
        | Default: raised
        | Example: ``option_menu_widget.config(relief="flat")``

    .. py:attribute:: compound

        | Syntax: ``option_menu_widget.config(compound="position")``
        | Description: Specifies the position of text relative to an image.
        | Default: none
        | Example: ``option_menu_widget.config(compound="left")``

    .. py:attribute:: state

        | Syntax: ``option_menu_widget.config(state="state")``
        | Description: Controls the widget’s state (e.g., "normal", "disabled").
        | Default: normal
        | Example: ``option_menu_widget.config(state="disabled")``

    .. py:attribute:: takefocus

        | Syntax: ``option_menu_widget.config(takefocus=boolean)``
        | Description: Specifies whether the widget can take focus.
        | Default: 0
        | Example: ``option_menu_widget.config(takefocus=1)``

    .. py:attribute:: text

        | Syntax: ``option_menu_widget.config(text="text")``
        | Description: Sets the default text for the menu.
        | Default: Option 1
        | Example: ``option_menu_widget.config(text="Select an option")``

    .. py:attribute:: textvariable

        | Syntax: ``option_menu_widget.config(textvariable=tk.StringVar)``
        | Description: Variable linked to the displayed text.
        | Default: PY_VAR0
        | Example: ``option_menu_widget.config(textvariable=my_var)``

    .. py:attribute:: underline

        | Syntax: ``option_menu_widget.config(underline=index)``
        | Description: Underlines the character at the specified index.
        | Default: -1 (no underline)
        | Example: ``option_menu_widget.config(underline=0)``

    .. py:attribute:: width

        | Syntax: ``option_menu_widget.config(width=value)``
        | Description: Width of the menu in number of characters.
        | Default: 0 (auto)
        | Example: ``option_menu_widget.config(width=10)``

    .. py:attribute:: wraplength

        | Syntax: ``option_menu_widget.config(wraplength=value)``
        | Description: Specifies the wrap width of the text in pixels.
        | Default: 0 (no wrap)
        | Example: ``option_menu_widget.config(wraplength=100)``



----

Default options
-----------------------

| Code to get the defaults for each button option is below.

.. code-block:: python

    import tkinter as tk

    window = tk.Tk()

    button = tk.Button(window)
    button_options = button.keys()

    for option in button_options:
        print(f"{option}: {button.cget(option)}")  # cget retrieves the current value of the option

