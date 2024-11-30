====================================================
tk Entry
====================================================

| See: https://www.geeksforgeeks.org/python-tkinter-entry-widget/

----

Usage
---------------

| The `tkinter.Entry` widget provides an input field.
| To create an entry widget the general syntax is (assuming import via "import tkinter as tk")

.. py:function:: entry_widget  = tk.Entry(parent, option=value)

    | `parent` is the window or frame object.
    | Options can be passed as parameters separated by commas.

----

Using a variable for the text of an entry widget
----------------------------------------------------

.. image:: images/entry_get.png
    :scale: 100%

This code creates a simple Tkinter GUI application that allows a user to enter their name into an entry field and display the entered name in a label when a button is clicked. Here's a breakdown of its functionality:

1. **Main Window Setup**: Initializes the main window with a specified size and title.
2. **Entry Widget**: Provides a text entry field where the user can input their name.
3. **StringVar**: Associates the entry field with a `StringVar`, `name_var`,  to manage the input text.
4. **Button**: When clicked, triggers a function to retrieve the text from `name_var` and sets the ``text`` value of the label widget.
5. **Label**: Displays the retrieved text in a label, formatted to show on two lines.

| Using tk.StringVar():

- **name_var = tk.StringVar()** creates a Tkinter variable of type StringVar. This variable is used to dynamically update and retrieve the value of a string associated with the Entry widget.
- **get_name()** is a function that retrieves the current value of name_var using **name_var.get()**
- tk.Entry(window, **textvariable=name_var**, font=('calibre', 24, 'normal'), width=20) creates an entry widget for text input.
- **textvariable=name_var** links the entry widget to the name_var StringVar, so any text entered in the widget updates name_var and vice versa.
- tk.Button(window, text="Submit", **command=get_name**) creates a button that, when clicked, calls the get_name function.

.. code-block:: python

    import tkinter as tk

    # Create the main window
    window = tk.Tk()
    window.geometry("500x300")  # Set window size
    window.title("Entry Example")  # Set window title

    # Create a StringVar to associate with the entry
    name_var = tk.StringVar()

    # Function to get the value from the entry field and display it in the label
    def get_name():
        name = name_var.get()
        output_label.config(text=f"Name entered:\n{name}")

    # Create the entry widget for input
    name_entry = tk.Entry(window, textvariable=name_var, font=('calibre', 24, 'normal'), width=20)
    name_entry.pack(pady=20)  # Add some padding to the top

    # Create a button to trigger the get_name function
    submit_button = tk.Button(window, text="Submit", command=get_name)
    submit_button.pack(pady=10)

    # Create a label to display the output
    output_label = tk.Label(window, text="", font=('calibre', 24, 'normal'), width=30, height=2)
    output_label.pack(pady=20)

    # Run the main event loop
    window.mainloop()

----

Validation via the validate option
--------------------------------------

The `validate` option in Tkinter is used to control when validation should occur for an entry widget. It works in conjunction with the `validatecommand` option, which specifies the function to call for validation.

The `validate` option determines the conditions under which the validation function is called. It can take the following values:

- **'focus'**: Validation occurs when the entry widget gains or loses focus.
- **'focusin'**: Validation occurs when the entry widget gains focus.
- **'focusout'**: Validation occurs when the entry widget loses focus.
- **'key'**: Validation occurs whenever the user types something in the entry widget.
- **'all'**: Validation occurs under all the above conditions.
- **'none'**: No validation occurs (default).

The `validatecommand` option specifies the function to call for validation. This function should return `True` if the input is valid and `False` otherwise. The function can take various substitution codes as arguments, such as:

- **%d** : Action code. It indicates the type of action that triggered the validation. Possible values are: 1 for an insertion; 0 for a deletion; -1 for any other action.
- **%i** : Index of the character string to be inserted/deleted, or -1 if not applicable.
- **%P** : The value of the entry if the edit is allowed. This is the new value of the widget's text.
- **%s** : The current value of the entry before the edit.
- **%S** : The text string being inserted or deleted, if any.
- **%v** : The type of validation currently set; the current value of the **validate** option. This can be: none, focus, focusin, focusout, key
- **%V** : The type of event that triggered the validation; the current value of the **validatecommand** option. This can be: key, focusin, focusout, forced
- **%W** : The name of the widget triggering the callback.

.. image:: images/validation_substitutions.png
    :scale: 100%

| Run the code below and type in "abcD". THis shows what each validation substitution code does.

.. code-block:: python

    import tkinter as tk


    def on_validate(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        output_text.set(
            f"Action: {action}\n"
            f"Index: {index}\n"
            f"Value if allowed: {value_if_allowed}\n"
            f"Prior value: {prior_value}\n"
            f"Text: {text}\n"
            f"Validation type: {validation_type}\n"
            f"Trigger type: {trigger_type}\n"
            f"Widget name: {widget_name}"
        )
        return True


    window = tk.Tk()
    window.title("Validation Example")
    window.geometry("500x350")

    output_text = tk.StringVar()
    output_label = tk.Label(window, font=("Arial",16), textvariable=output_text, justify="left")
    output_label.pack(pady=10)

    entry_var = tk.StringVar()
    entry_field = tk.Entry(window, font=("Arial",24), textvariable=entry_var, validate="key", validatecommand=(window.register(on_validate), "%d", "%i", "%P", "%s", "%S", "%v", "%V", "%W"))
    entry_field.pack(pady=10)


    window.mainloop()

----

Numeric validation
~~~~~~~~~~~~~~~~~~~~~

| In the code below, the validate_input function checks if the new value (new_value) is a digit or an empty string.
| The window.register(validate_input) registers the validation function with Tkinter.
| %P is used to pass the new value of the entry to the validate_age function, allowing it to check if the entire new value is a valid age
| The validate='key' option specifies that validation should occur whenever the user types something.
| The validatecommand=vcmd option sets the validation command to the registered function.


.. code-block:: python

    import tkinter as tk

    def validate_input(new_value):
        # Check if the new value is numeric
        return new_value.isdigit() or new_value == ""

    window = tk.Tk()
    window.title("Validate Entry Example")
    window.geometry("500x300")  # Set window size

    # Register the validation function
    vcmd = (window.register(validate_input), '%P')

    entry = tk.Entry(window, font=("Arial", 24), validate='key', validatecommand=vcmd)
    entry.pack(pady=10)

    window.mainloop()

----

.. admonition:: Tasks

    #. Modify the code above to validate for an age from 0 to 120.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code above to validate for an age from 0 to 120.

                .. code-block:: python

                    import tkinter as tk


                    def validate_age(new_value):
                        if new_value.isdigit():
                            age = int(new_value)
                            return 0 <= age <= 120  # Returns True if within range, otherwise False
                        else:
                            return new_value == ""  # Returns True if empty, otherwise False


                    window = tk.Tk()
                    window.title("Age Validation Example")
                    window.geometry("500x300")  # Set window size

                    # Register the validation function
                    vcmd = (window.register(validate_age), "%P")

                    entry = tk.Entry(window, font=("Arial", 24), validate="key", validatecommand=vcmd)
                    entry.pack(pady=10)

                    window.mainloop()


Phone number validation
~~~~~~~~~~~~~~~~~~~~~~~~~~

| The code below will ensure that the entry field only accepts numeric input up to 10 digits.
| **validate_phone** checks for a numeric input and that the length is no more than 10 digits.

.. code-block:: python

    import tkinter as tk

    def validate_phone(new_value):
        # Check if the new value is numeric and has at most 10 digits
        return new_value.isdigit() and len(new_value) <= 10

    window = tk.Tk()
    window.title("Phone Number Validation Example")
    window.geometry("500x300")  # Set window size

    # Register the validation function
    vcmd = (window.register(validate_phone), '%P')

    entry = tk.Entry(window, font=("Arial", 24), validate='key', validatecommand=vcmd)
    entry.pack(pady=10)

    window.mainloop()



.. admonition:: Tasks

    #. Modify the code above to validate for a mobile phone number that requires a space after 4 digits and again after another 3 digits.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code above to validate for a mobile phone number that requires a space after 4 digits and again after another 3 digits.

                .. code-block:: python

                    import tkinter as tk


                    def validate_phone(new_value):
                        # Check if the new value follows the pattern: 4 digits, a space, 3 digits, a space, 3 digits
                        if len(new_value) == 0:
                            return True
                        if len(new_value) in [5, 9]:
                            return new_value[-1] == ' '  # Ensure the 5th and 9th characters are spaces
                        if len(new_value) in [1, 2, 3, 4, 6, 7, 8, 10, 11, 12]:
                            return new_value[-1].isdigit()  # Ensure other positions are digits
                        return False

                    window = tk.Tk()
                    window.title("Phone Number Validation Example")
                    window.geometry("500x300")  # Set window size

                    # Register the validation function
                    vcmd = (window.register(validate_phone), '%P')

                    entry = tk.Entry(window, validate='key', validatecommand=vcmd, font=("Arial",20))
                    entry.pack(pady=10)

                    window.mainloop()

----

EMail validation

.. code-block:: python

    import tkinter as tk
    import re

    def validate_email(new_value):
        # Define the regex pattern for a valid email address
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, new_value) is not None or new_value == ""

    window = tk.Tk()
    window.title("Email Validation Example")

    # Register the validation function
    vcmd = (window.register(validate_email), '%P')

    entry = tk.Entry(window, validate='key', validatecommand=vcmd)
    entry.pack(pady=10)

    window.mainloop()




----

Option details
--------------------

.. py:function:: entry_widget = tk.Entry(parent, option=value)

    | parent is the window or frame object.
    | Options can be passed as parameters separated by commas.

    **Parameters:**

    .. py:attribute:: background
    .. py:attribute:: bg

        | Syntax: ``entry_widget = tk.Entry(parent, bg="color")``
        | Description: Sets the background color of the entry field.
        | Default: SystemWindow RGB: (255, 255, 255)
        | Example: ``entry_widget = tk.Entry(window, bg="lightgrey")``

    .. py:attribute:: bd
    .. py:attribute:: borderwidth

        | Syntax: ``entry_widget = tk.Entry(parent, bd=width)``
        | Description: Sets the width of the border around the entry field.
        | Default: ``2``
        | Example: ``entry_widget = tk.Entry(window, bd=5)``

    .. py:attribute:: cursor

        | Syntax: ``entry_widget = tk.Entry(parent, cursor="cursor_type")``
        | Description: Changes the cursor when hovering over the entry field.
        | Default: ``None``
        | Example: ``entry_widget = tk.Entry(window, cursor="xterm")``
        | Possible values include:

            - **"arrow"**: Standard arrow cursor.
            - **"xterm"**: I-beam cursor for text selection.
            - **"hand2"**: Hand cursor.
            - **"cross"**: Crosshair cursor.
            - **"plus"**: Plus sign cursor.
            - **"wait"**: Hourglass cursor.

    .. py:attribute:: disabledbackground

        | Syntax: ``entry_widget = tk.Entry(parent, disabledbackground="color")``
        | Description: Sets the background color when the entry is disabled.
        | Default: SystemDisabled RGB: (240, 240, 240)
        | Example: ``entry_widget = tk.Entry(window, disabledbackground="lightgrey")``

    .. py:attribute:: disabledforeground

        | Syntax: ``entry_widget = tk.Entry(parent, disabledforeground="color")``
        | Description: Sets the text color when the entry is disabled.
        | Default: SystemDisabledText RGB: (109, 109, 109)
        | Example: ``entry_widget = tk.Entry(window, disabledforeground="darkgrey")``

    .. py:attribute:: exportselection

        | Syntax: ``entry_widget = tk.Entry(parent, exportselection=boolean)``
        | Description: Determines if the text selection is exported to the clipboard.
        | Default: ``1``
        | Example: ``entry_widget = tk.Entry(window, exportselection=False)``

    .. py:attribute:: font

        | Syntax: ``entry_widget = tk.Entry(parent, font=("font_name", size))``
        | Description: Sets the font type and size of the entry text.
        | Default: System font and size
        | Example: ``entry_widget = tk.Entry(window, font=("Arial", 12))``

    .. py:attribute:: foreground
    .. py:attribute:: fg

        | Syntax: ``entry_widget = tk.Entry(parent, fg="color")``
        | Description: Sets the text color of the entry field.
        | Default: SystemWindowText RGB: (0, 0, 0)
        | Example: ``entry_widget = tk.Entry(window, fg="blue")``

    .. py:attribute:: highlightbackground

        | Syntax: ``entry_widget = tk.Entry(parent, highlightbackground="color")``
        | Description: Sets the color of the highlight when the entry does not have focus.
        | Default: SystemButtonFace RGB: (240, 240, 240)
        | Example: ``entry_widget = tk.Entry(window, highlightbackground="grey")``

    .. py:attribute:: highlightcolor

        | Syntax: ``entry_widget = tk.Entry(parent, highlightcolor="color")``
        | Description: Sets the color of the highlight when the entry has focus.
        | Default: SystemHighlight RGB: (100, 100, 100)
        | Example: ``entry_widget = tk.Entry(window, highlightcolor="blue")``

    .. py:attribute:: highlightthickness

        | Syntax: ``entry_widget = tk.Entry(parent, highlightthickness=thickness)``
        | Description: Sets the thickness of the focus highlight border.
        | Default: ``1``
        | Example: ``entry_widget = tk.Entry(window, highlightthickness=2)``

    .. py:attribute:: insertbackground

        | Syntax: ``entry_widget = tk.Entry(parent, insertbackground="color")``
        | Description: Sets the color of the insertion cursor (caret).
        | Default: SystemWindowText RGB: (0, 0, 0)
        | Example: ``entry_widget = tk.Entry(window, insertbackground="red")``

    .. py:attribute:: insertborderwidth

        | Syntax: ``entry_widget = tk.Entry(parent, insertborderwidth=width)``
        | Description: Sets the width of the insertion cursor's border.
        | Default: ``0``
        | Example: ``entry_widget = tk.Entry(window, insertborderwidth=1)``

    .. py:attribute:: insertofftime

        | Syntax: ``entry_widget = tk.Entry(parent, insertofftime=milliseconds)``
        | Description: Sets the time the insertion cursor is off per blink in milliseconds.
        | Default: ``300``
        | Example: ``entry_widget = tk.Entry(window, insertofftime=500)``

    .. py:attribute:: insertontime

        | Syntax: ``entry_widget = tk.Entry(parent, insertontime=milliseconds)``
        | Description: Sets the time the insertion cursor is on per blink in milliseconds.
        | Default: ``600``
        | Example: ``entry_widget = tk.Entry(window, insertontime=500)``

    .. py:attribute:: insertwidth

        | Syntax: ``entry_widget = tk.Entry(parent, insertwidth=width)``
        | Description: Sets the width of the insertion cursor.
        | Default: ``2``
        | Example: ``entry_widget = tk.Entry(window, insertwidth=3)``

    .. py:attribute:: justify

        | Syntax: ``entry_widget = tk.Entry(parent, justify="alignment")``
        | Description: Specifies how the text is aligned within the entry field.
        | Default: ``left``
        | Example: ``entry_widget = tk.Entry(window, justify="center")``
        | Possible values include:

            - **"left"**: Aligns text to the left.
            - **"center"**: Centers text within the field.
            - **"right"**: Aligns text to the right.

    .. py:attribute:: relief

        | Syntax: ``entry_widget = tk.Entry(parent, relief="relief_type")``
        | Description: Sets the border style of the entry field.
        | Default: ``flat``
        | Example: ``entry_widget = tk.Entry(window, relief="sunken")``
        | Possible values include:

            - **"flat"**
            - **"raised"**
            - **"sunken"**
            - **"groove"**
            - **"ridge"**

    .. py:attribute:: show

        | Syntax: ``entry_widget = tk.Entry(parent, show="character")``
        | Description: Masks characters, often used for passwords.
        | Default: ``None``
        | Example: ``entry_widget = tk.Entry(window, show="*")``

    .. py:attribute:: state

        | Syntax: ``entry_widget = tk.Entry(parent, state="state")``
        | Description: Sets the state of the entry field.
        | Default: ``normal``
        | Example: ``entry_widget = tk.Entry(window, state="disabled")``
        | Possible values include:

            - **"normal"**
            - **"disabled"**
            - **"readonly"**

    .. py:attribute:: takefocus

        | Syntax: ``entry_widget = tk.Entry(parent, takefocus=boolean)``
        | Description: Determines if the entry field can receive focus via keyboard navigation.
        | Default: ``1``
        | Example: ``entry_widget = tk.Entry(window, takefocus=False)``

    .. py:attribute:: textvariable

        | Syntax: ``entry_widget = tk.Entry(parent, textvariable=variable)``
        | Description: Associates a Tkinter variable (usually a StringVar) with the entry text.
        | Default: ``None``
        | Example: ``entry_widget = tk.Entry(window, textvariable=my_var)``

    .. py:attribute:: validate

        | Syntax: ``entry_widget = tk.Entry(parent, validate="validation_type")``
        | Description: Sets the type of validation to apply to the entry field.
        | Default: ``none``
        | Example: ``entry_widget = tk.Entry(window, validate="focusout")``
        | Possible values include:

            - **"none"**: No validation.
            - **"focus"**: Validation occurs when the entry loses focus.
            - **"focusin"**: Validation occurs when the entry gains focus.
            - **"focusout"**: Validation occurs when the entry loses focus.
            - **"key"**: Validation occurs on every keystroke.

    .. py:attribute:: width

        | Syntax: ``entry_widget = tk.Entry(parent, width=characters)``
        | Description: Sets the width of the entry field in characters.
        | Default: ``20``
        | Example: ``entry_widget = tk.Entry(window, width=30)``

    .. py:attribute:: xscrollcommand

        | Syntax: ``entry_widget = tk.Entry(parent, xscrollcommand=scroll_function)``
        | Description: Specifies a function for horizontal scrolling.
        | Default: ``None``
        | Example: ``entry_widget = tk.Entry(window, xscrollcommand=my_scroll_function)``
