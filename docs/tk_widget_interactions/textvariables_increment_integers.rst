====================================================
Label textvariable: Increment integers
====================================================

| See: https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/

----

Increment label integer via buttons
---------------------------------------

.. image:: images/increment_integer.png
    :scale: 100%


Required Syntax
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: IntVar

    | Syntax: ``int_var = tk.IntVar()``
    | Description: Creates a Tkinter variable for holding an integer.
    | Default: None
    | Example: ``int_var = tk.IntVar()``

.. py:method:: get

    | Syntax: ``current_value = int_var.get()``
    | Description: Retrieves the current value of the ``IntVar``.
    | Default: None
    | Example: ``current_value = int_var.get()``

.. py:method:: set

    | Syntax: ``int_var.set(new_value)``
    | Description: Sets the value of the ``IntVar`` to the specified integer.
    | Default: None
    | Example: ``int_var.set(42)``

.. py:attribute:: textvariable

    | Syntax: ``label_widget = tk.Label(parent, textvariable=variable)``
    | Description: Associates a Tkinter variable with the label text.
    | Default: None
    | Example: ``label_widget = tk.Label(window, textvariable=my_var)``

.. py:attribute:: command

    | Syntax: ``button_widget = tk.Button(parent, command=callback_function)``
    | Description: Specifies the function to be called when the button is clicked.
    | Default: ``None``
    | Example: ``button_widget = tk.Button(window, command=on_click)``


Code features
~~~~~~~~~~~~~~~~~~

| Here's a breakdown of the main parts of the code:

1. **Create a variable: IntVar**:

   - ``int_var = tk.IntVar()``: Creates an ``IntVar`` instance, ``int_var``, which is a special Tkinter variable for holding integer data.
   - ``int_var.set(0)``: Sets the initial value of ``int_var`` to 0.

2. **Link variable to Label with textvariable**:

   - ``label = tk.Label(root, textvariable=int_var, font=("Helvetica", 16))``: Creates a label in the ``root`` window.
   - The ``textvariable`` parameter is linked to ``int_var``, so the label text displays ``int_var``'s value.

3. **Define the Functions**:

   - These functions use ``.get()`` and ``.set()`` methods on the variable  ``int_var``.
   - ``def increment_value()``: Defines a function to increment ``int_var``'s value by 1.
   - ``def decrement_value()``: Defines a function to decrement ``int_var``'s value by 1.
   - ``def reset_value()``: Defines a function to reset ``int_var``'s value to 0.

4. **Set Button commands**:

   - ``button_decrement = tk.Button(root, text="-", width=4, command=decrement_value, font=("Helvetica", 24), bg="#FF6666")``: Creates a button that calls ``decrement_value`` when clicked.
   - ``button_reset = tk.Button(root, text="Reset", command=reset_value, font=("Helvetica", 16), bg="#FFFF99")``: Creates a button that calls ``reset_value`` when clicked.
   - ``button_increment = tk.Button(root, text="+", width=4, command=increment_value, font=("Helvetica", 24), bg="#99FF99")``: Creates a button that calls ``increment_value`` when clicked.

Code
~~~~~~~~~~~

| This code creates a basic GUI with buttons to increment, decrement, and reset an integer value displayed in a label.

.. code-block:: python

    import tkinter as tk


    # Function to increment the integer value
    def increment_value():
        current_value = int_var.get()
        int_var.set(current_value + 1)  # Increment the value by 1


    # Function to decrement the integer value
    def decrement_value():
        current_value = int_var.get()
        int_var.set(current_value - 1)  # Decrement the value by 1


    # Function to reset the integer value to zero
    def reset_value():
        int_var.set(0)  # Reset the value to 0


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

    # Create Buttons to trigger the value update
    button_decrement = tk.Button(root, text="-", width=4, command=decrement_value, font=("Helvetica", 24), bg="#FF6666")  # Light red
    button_reset = tk.Button(root, text="Reset", command=reset_value, font=("Helvetica", 16), bg="#FFFF99")  # Light yellow
    button_increment = tk.Button(root, text="+", width=4, command=increment_value, font=("Helvetica", 24), bg="#99FF99")  # Light green

    # Position the buttons below the label
    button_decrement.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    button_reset.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    button_increment.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

    # Run the application
    window.mainloop()



