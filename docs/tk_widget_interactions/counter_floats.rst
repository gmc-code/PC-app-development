====================================================
Counter: floats
====================================================

| See: https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/
| See: https://dafarry.github.io/tkinterbook/tkinter-events-and-bindings.htm

----

Required Syntax
-----------------------------------

.. py:class:: DoubleVar

    | Syntax: ``float_var = tk.DoubleVar()``
    | Description: Creates a Tkinter variable for holding an integer.
    | Default: None
    | Example: ``float_var = tk.DoubleVar()``

.. py:method:: get

    | Syntax: ``current_value = float_var.get()``
    | Description: Retrieves the current value of the `DoubleVar`.
    | Default: None
    | Example: ``current_value = float_var.get()``

.. py:method:: set

    | Syntax: ``float_var.set(new_value)``
    | Description: Sets the value of the `DoubleVar` to the specified integer.
    | Default: None
    | Example: ``float_var.set(42)``

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

.. py:attribute:: bind

    | Syntax: ``widget.bind("<Event>", handler_function)``
    | Description: Binds an event, such as a mouse click or key press, to a specific function. Using `lambda` allows passing event data or wrapping the callback with additional parameters.
    | Default: ``None``
    | Example: ``button_increment.bind("<ButtonPress-1>", start_increment)``

.. py:method:: after

    | Syntax: ``job_id = root.after(delay_ms, callback_function)``
    | Description: Schedules `callback_function` to be called after a delay specified in milliseconds. Returns a job ID, which can be used to cancel the scheduled function with `after_cancel()`.
    | Default: ``None``
    | Example: ``job_id = root.after(1000, update_label)``

.. py:method:: after_cancel

    | Syntax: ``root.after_cancel(job_id)``
    | Description: Cancels a scheduled callback function that was set up using `after()`. The `job_id` should be the identifier returned by `after()`.
    | Default: ``None``
    | Example: ``root.after_cancel(job_id)``


----

Code example
~~~~~~~~~~~~~~~~~~


.. image:: images/increment_integer.png
    :scale: 100%


| Here's a breakdown of the code:

1. **Event Binding**:

   - **Purpose**: Tkinter's `.bind()` method allows widgets to respond to specific events, such as mouse clicks or key presses, by attaching them to a handler function.
   - In this code: ``button_increment.bind("<ButtonPress-1>", start_increment)``, `<ButtonPress-1>` refers to pressing the left mouse button.
   - In this code: ``button_increment.bind("<ButtonRelease-1>", stop_action)``, `<ButtonRelease-1>` refers to releasing the left mouse button.
   - `start_increment` is triggered when the button is pressed, while `stop_action` is called when the button is released, stopping the continuous action.

2. **Using `after()` to Schedule Repeated Calls**:

   - **Purpose**: The ``after()`` method in Tkinter is used to schedule the repeated execution of the increment or decrement function every 100 milliseconds, allowing for continuous adjustment while the button is held down.
   - **Syntax**: `widget.after(milliseconds, function_name)`
   - `root.after(100, start_increment)` schedules the ``start_increment`` function to run again after a delay of 100 milliseconds, creating a loop that continues to increment the value while the button is pressed.
   - The ``after()`` method calls ``start_increment`` after each delay, creating a cycle that continues until stopped (e.g., by releasing the button).

3. **Stopping the Repeating Action**:

   - **Purpose**: `stop_action` is called when the mouse button is released, canceling any repeating actions with `root.after_cancel()`.
   - **Syntax**: `root.after_cancel(job_id)`
   - This code, ``if "increment_job" in globals()``, checks if `increment_job` is defined (using `globals()`), then cancels the ongoing `after` job, stopping the repeat.

4. **Increment Button `+`**

   - When you click the `+` button, the `increment_value` function is called.
   - Inside `increment_value`:
     - It retrieves the current value from `float_var`.
     - It increments this value by `0.1`.
     - The result is rounded to one decimal place to avoid floating-point precision issues.
     - The `float_var` is updated with the new value, which immediately updates the displayed label text.

5. **Hold-to-Increment**

     - When the `+` button is pressed and held, the `start_increment` function triggers.
     - `start_increment` starts a delayed loop using `root.after(500, repeat_increment)` to call `repeat_increment` after 500 milliseconds.
     - `repeat_increment` repeatedly calls `increment_value` every 100 milliseconds until the button is released.
     - Releasing the button triggers `stop_action`, which cancels the ongoing repeat loop.


.. code-block:: python

    import tkinter as tk


    # Function to increment the float value by 0.1
    def increment_value():
        current_value = float_var.get()
        float_var.set(round(current_value + 0.1, 1))  # Increment the value by 0.1


    # Function to decrement the float value by 0.1
    def decrement_value():
        current_value = float_var.get()
        float_var.set(round(current_value - 0.1, 1))  # Decrement the value by 0.1


    # Function to reset the float value to zero
    def reset_value():
        float_var.set(0.0)  # Reset the value to 0.0


    # Function to start repeating increment after a delay
    def start_increment(event):
        global increment_job
        # Start the repeating increment after 500 ms
        increment_job = root.after(500, repeat_increment)


    def repeat_increment():
        increment_value()
        global increment_job
        # Continue repeating every 100 ms
        increment_job = root.after(100, repeat_increment)


    # Function to start repeating decrement after a delay
    def start_decrement(event):
        global decrement_job
        # Start the repeating decrement after 500 ms
        decrement_job = root.after(500, repeat_decrement)


    def repeat_decrement():
        decrement_value()
        global decrement_job
        # Continue repeating every 100 ms
        decrement_job = root.after(100, repeat_decrement)


    # Function to stop repeating action
    def stop_action(event):
        global increment_job, decrement_job
        if "increment_job" in globals():
            root.after_cancel(increment_job)
            del increment_job
        if "decrement_job" in globals():
            root.after_cancel(decrement_job)
            del decrement_job

    # Create the main window
    root = tk.Tk()
    root.geometry("300x200")
    root.title("DoubleVar Example")

    # Create a DoubleVar to hold the float value
    float_var = tk.DoubleVar()
    float_var.set(0.0)  # Initial value

    # Create a Label widget with textvariable, formatted to show one decimal place
    label = tk.Label(root, textvariable=float_var, font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=3, pady=5)

    # Create Buttons to trigger the value update
    button_decrement = tk.Button(root, text="-", width=4, command=decrement_value, font=("Helvetica", 24), bg="#FF6666")  # Light red
    button_reset = tk.Button(root, text="Reset", command=reset_value, font=("Helvetica", 16), bg="#FFFF99")  # Light yellow
    button_increment = tk.Button(root, text="+", width=4, command=increment_value, font=("Helvetica", 24), bg="#99FF99")  # Light green

    # Bind mouse events to buttons for repeating action
    button_increment.bind("<ButtonPress-1>", start_increment)
    button_increment.bind("<ButtonRelease-1>", stop_action)
    button_decrement.bind("<ButtonPress-1>", start_decrement)
    button_decrement.bind("<ButtonRelease-1>", stop_action)

    # Position the buttons below the label
    button_decrement.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    button_reset.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    button_increment.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

    # Run the application
    root.mainloop()
