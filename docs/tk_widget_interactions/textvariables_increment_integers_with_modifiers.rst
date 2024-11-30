===============================================================
Label textvariable: Increment integers with  binding modifiers
===============================================================

| See: https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/

----

Increment label integer via buttons with modifiers
-------------------------------------------------------

.. image:: images/increment_integer.png
    :scale: 100%

| The code creates a Tkinter GUI application to manage an integer value with customizable increment, decrement, and reset functionality:

1. An `IntVar` is created to hold the integer value: ``int_var = tk.IntVar()``.
2. The `set` method initializes the value: ``int_var.set(0)``.
3. The `get` method retrieves the current value: ``current_value = int_var.get()``.
4. A label is associated with the `IntVar`: ``label = tk.Label(window, textvariable=int_var)``.
5. Buttons are created for increment, decrement, and reset operations.
6. `bind` is used to associate mouse clicks with functions for different increments and decrements:

   - `<Button-1>` triggers single-step changes. ``button_increment.bind("<Button-1>", increment_by_1)``
   - `<Alt-Button-1>` triggers 10-step changes. ``button_increment.bind("<Alt-Button-1>", increment_by_10)``
7. The `increment_value` and `decrement_value` functions adjust the value by specified amounts.
8. The `reset_value` function sets the value to 0.


Required Syntax
~~~~~~~~~~~~~~~~~~~~~

.. py:class:: IntVar

    | Syntax: ``int_var = tk.IntVar()``
    | Description: Creates a Tkinter variable for holding an integer.
    | Default: None
    | Example: ``int_var = tk.IntVar()``

.. py:method:: set

    | Syntax: ``int_var.set(new_value)``
    | Description: Sets the value of the ``IntVar`` to the specified integer.
    | Default: None
    | Example: ``int_var.set(42)``

.. py:method:: get

    | Syntax: ``current_value = int_var.get()``
    | Description: Retrieves the current value of the ``IntVar``.
    | Default: None
    | Example: ``current_value = int_var.get()``

.. py:attribute:: textvariable

    | Syntax: ``label_widget = tk.Label(parent, textvariable=variable)``
    | Description: Associates a Tkinter variable with the label text. If the variable is changed, the label text is updated.
    | Default: None
    | Example: ``label_widget = tk.Label(window, textvariable=my_var)``

.. py:attribute:: command

    | Syntax: ``button_widget = tk.Button(parent, command=callback_function)``
    | Description: Specifies the function to be called when the button is clicked.
    | Default: ``None``
    | Example: ``button_widget = tk.Button(window, command=on_click)``

.. py:attribute:: bind

    | Syntax: ``widget.bind("<Event>", handler_function)``
    | Description: Binds an event, such as a mouse click or key press, to a specific function.
    | Default: ``None``
    | Example: ``button_increment.bind("<Button-1>", increment_by_1)``  # No modifier
    | Example: ``button_increment.bind("<Alt-Button-1>", increment_by_10)``  # Alt + Click
    | Example: ``button_increment.bind("<Shift-Button-1>", increment_by_100)``  # Shift + Click
    | Example: ``button_increment.bind("<Alt-Shift-Button-1>", increment_by_1000)``  # Alt + Shift + Click


Code features
~~~~~~~~~~~~~~~~~~

| This Tkinter program demonstrates the use of ``IntVar`` to manage and display an integer value, with buttons for incrementing, decrementing, and resetting the value.
| The variable ``int_var`` is bound to the label using ``textvariable``, dynamically updating the label's display as the value changes.
| Buttons use ``command`` functions for standard operations like resetting.
| The ``bind`` method assigns specific key-modified mouse events (e.g., ``<Shift-Button-1>``) to functions that increment or decrement by different amounts.
| Modifier keys allow more flexible interactions with shared buttons for multiple actions.

Code
~~~~~~~~~~~~~~~~~~

| This code creates a basic GUI with buttons to increment, decrement, and reset an integer value displayed in a label.
| It allows the use of Alt-clicking increment in steps of 10.

.. code-block:: python

    import tkinter as tk


    # Function to increment the integer value by a specified amount
    def increment_value(increment):
        current_value = int_var.get()
        int_var.set(current_value + increment)


    # Function to decrement the integer value by a specified amount
    def decrement_value(decrement):
        current_value = int_var.get()
        int_var.set(current_value - decrement)


    # Function to reset the integer value to zero
    def reset_value():
        int_var.set(0)  # Reset the value to 0


    # Increment functions for different amounts
    def increment_by_1(event):
        increment_value(1)


    def increment_by_10(event):
        increment_value(10)


    # Decrement functions for different amounts
    def decrement_by_1(event):
        decrement_value(1)


    def decrement_by_10(event):
        decrement_value(10)


    # Create the main window
    root = tk.Tk()
    window.geometry("300x200")
    window.title("IntVar Example")

    # Create an IntVar to hold the integer value
    int_var = tk.IntVar()
    int_var.set(0)  # Initial value

    # Create a Label widget with textvariable
    label = tk.Label(root, textvariable=int_var, font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=3, pady=5)

    # Create Buttons
    button_decrement = tk.Button(root, text="-", width=4, font=("Helvetica", 24), bg="#FF6666")  # Light red
    button_reset = tk.Button(root, text="Reset", command=reset_value, font=("Helvetica", 16), bg="#FFFF99")  # Light yellow
    button_increment = tk.Button(root, text="+", width=4, font=("Helvetica", 24), bg="#99FF99")  # Light green

    # Bind different increments based on modifier keys
    button_increment.bind("<Button-1>", increment_by_1)  # No modifier
    button_increment.bind("<Alt-Button-1>", increment_by_10)  # Alt + Click

    # Bind different decrements based on modifier keys
    button_decrement.bind("<Button-1>", decrement_by_1)  # No modifier
    button_decrement.bind("<Alt-Button-1>", decrement_by_10)  # Alt + Click

    # Position the buttons below the label
    button_decrement.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    button_reset.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    button_increment.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

    # Run the application
    window.mainloop()


----

.. admonition:: Tasks

    #. Modify the previous code to allow the use of Alt-clicking and Shift-clicking to increment in steps of 10, 100 respectively.
    #. Modify the previous code to allow the use of Alt-clicking and Shift-clicking and Alt-Shift-clicking to increment in steps of 10, 100 and 1000 respectively.


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the previous code to allow the use of Alt-clicking and Shift-clicking to increment in steps of 10, 100 respectively.

                .. code-block:: python

                    import tkinter as tk


                    # Function to increment the integer value by a specified amount
                    def increment_value(increment):
                        current_value = int_var.get()
                        int_var.set(current_value + increment)


                    # Function to decrement the integer value by a specified amount
                    def decrement_value(decrement):
                        current_value = int_var.get()
                        int_var.set(current_value - decrement)


                    # Function to reset the integer value to zero
                    def reset_value():
                        int_var.set(0)  # Reset the value to 0


                    # Increment functions for different amounts
                    def increment_by_1(event):
                        increment_value(1)


                    def increment_by_10(event):
                        increment_value(10)


                    def increment_by_100(event):
                        increment_value(100)


                    def increment_by_1000(event):
                        increment_value(1000)


                    # Decrement functions for different amounts
                    def decrement_by_1(event):
                        decrement_value(1)


                    def decrement_by_10(event):
                        decrement_value(10)


                    def decrement_by_100(event):
                        decrement_value(100)


                    def decrement_by_1000(event):
                        decrement_value(1000)


                    # Create the main window
                    root = tk.Tk()
                    window.geometry("300x200")
                    window.title("IntVar Example")

                    # Create an IntVar to hold the integer value
                    int_var = tk.IntVar()
                    int_var.set(0)  # Initial value

                    # Create a Label widget with textvariable
                    label = tk.Label(root, textvariable=int_var, font=("Helvetica", 16))
                    label.grid(row=0, column=0, columnspan=3, pady=5)

                    # Create Buttons
                    button_decrement = tk.Button(root, text="-", width=4, font=("Helvetica", 24), bg="#FF6666")  # Light red
                    button_reset = tk.Button(root, text="Reset", command=reset_value, font=("Helvetica", 16), bg="#FFFF99")  # Light yellow
                    button_increment = tk.Button(root, text="+", width=4, font=("Helvetica", 24), bg="#99FF99")  # Light green

                    # Bind different increments based on modifier keys
                    button_increment.bind("<Button-1>", increment_by_1)  # No modifier
                    button_increment.bind("<Alt-Button-1>", increment_by_10)  # Alt + Click
                    button_increment.bind("<Shift-Button-1>", increment_by_100)  # Shift + Click
                    button_increment.bind("<Alt-Shift-Button-1>", increment_by_1000)  # Alt + Shift + Click

                    # Bind different decrements based on modifier keys
                    button_decrement.bind("<Button-1>", decrement_by_1)  # No modifier
                    button_decrement.bind("<Alt-Button-1>", decrement_by_10)  # Alt + Click
                    button_decrement.bind("<Shift-Button-1>", decrement_by_100)  # Shift + Click
                    button_decrement.bind("<Alt-Shift-Button-1>", decrement_by_1000)  # Alt + Shift + Click

                    # Position the buttons below the label
                    button_decrement.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
                    button_reset.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
                    button_increment.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

                    # Run the application
                    window.mainloop()


            .. tab-item:: Q2

                Modify the previous code to allow the use of Alt-clicking and Shift-clicking and Alt-Shift-clicking to increment in steps of 10, 100 and 1000 respectively.

                .. code-block:: python

                    import tkinter as tk


                    # Function to increment the integer value by a specified amount
                    def increment_value(increment):
                        current_value = int_var.get()
                        int_var.set(current_value + increment)


                    # Function to decrement the integer value by a specified amount
                    def decrement_value(decrement):
                        current_value = int_var.get()
                        int_var.set(current_value - decrement)


                    # Function to reset the integer value to zero
                    def reset_value():
                        int_var.set(0)  # Reset the value to 0


                    # Increment functions for different amounts
                    def increment_by_1(event):
                        increment_value(1)


                    def increment_by_10(event):
                        increment_value(10)


                    def increment_by_100(event):
                        increment_value(100)


                    def increment_by_1000(event):
                        increment_value(1000)


                    # Decrement functions for different amounts
                    def decrement_by_1(event):
                        decrement_value(1)


                    def decrement_by_10(event):
                        decrement_value(10)


                    def decrement_by_100(event):
                        decrement_value(100)


                    def decrement_by_1000(event):
                        decrement_value(1000)


                    # Create the main window
                    root = tk.Tk()
                    window.geometry("300x200")
                    window.title("IntVar Example")

                    # Create an IntVar to hold the integer value
                    int_var = tk.IntVar()
                    int_var.set(0)  # Initial value

                    # Create a Label widget with textvariable
                    label = tk.Label(root, textvariable=int_var, font=("Helvetica", 16))
                    label.grid(row=0, column=0, columnspan=3, pady=5)

                    # Create Buttons
                    button_decrement = tk.Button(root, text="-", width=4, font=("Helvetica", 24), bg="#FF6666")  # Light red
                    button_reset = tk.Button(root, text="Reset", command=reset_value, font=("Helvetica", 16), bg="#FFFF99")  # Light yellow
                    button_increment = tk.Button(root, text="+", width=4, font=("Helvetica", 24), bg="#99FF99")  # Light green

                    # Bind different increments based on modifier keys
                    button_increment.bind("<Button-1>", increment_by_1)  # No modifier
                    button_increment.bind("<Alt-Button-1>", increment_by_10)  # Alt + Click
                    button_increment.bind("<Shift-Button-1>", increment_by_100)  # Shift + Click
                    button_increment.bind("<Alt-Shift-Button-1>", increment_by_1000)  # Alt + Shift + Click

                    # Bind different decrements based on modifier keys
                    button_decrement.bind("<Button-1>", decrement_by_1)  # No modifier
                    button_decrement.bind("<Alt-Button-1>", decrement_by_10)  # Alt + Click
                    button_decrement.bind("<Shift-Button-1>", decrement_by_100)  # Shift + Click
                    button_decrement.bind("<Alt-Shift-Button-1>", decrement_by_1000)  # Alt + Shift + Click

                    # Position the buttons below the label
                    button_decrement.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
                    button_reset.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
                    button_increment.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

                    # Run the application
                    window.mainloop()