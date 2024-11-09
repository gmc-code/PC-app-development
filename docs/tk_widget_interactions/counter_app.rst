====================================================
Counter app
====================================================

| See: https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/

----

Required Syntax
-----------------------------------

.. py:class:: IntVar

    | Syntax: ``int_var = tk.IntVar()``
    | Description: Creates a Tkinter variable for holding an integer.
    | Default: None
    | Example: ``int_var = tk.IntVar()``

.. py:method:: get

    | Syntax: ``current_value = int_var.get()``
    | Description: Retrieves the current value of the `IntVar`.
    | Default: None
    | Example: ``current_value = int_var.get()``

.. py:method:: set

    | Syntax: ``int_var.set(new_value)``
    | Description: Sets the value of the `IntVar` to the specified integer.
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

.. py:attribute:: bind

    | Syntax: ``widget.bind("<Event>", handler_function)``
    | Lambda Syntax: ``widget.bind("<Event>", lambda event: callback_function())``
    | Description: Binds an event, such as a mouse click or key press, to a specific function. Using `lambda` allows passing event data or wrapping the callback with additional parameters.
    | Default: ``None``
    | Example: ``button_widget.bind("<ButtonPress-1>", lambda event: on_press(event))``

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


.. image:: images/increment_number.png
    :scale: 100%

| This code demonstrates how to use event binding and `lambda` functions in Tkinter to handle repeating actions for button presses.
| This setup enables the button to continuously increment or decrement the value while the button is held down, and stop when released.
| Here's a breakdown of the code for binding and using `lambda` in this context:

1. **Event Binding**:

   - **Purpose**: Tkinter's `.bind()` method allows widgets to respond to specific events, such as mouse clicks or key presses, by attaching them to a handler function.
   - In this code: ``button_increment.bind("<ButtonPress-1>", start_increment)``, `<ButtonPress-1>` refers to pressing the left mouse button.
   - In this code: ``button_increment.bind("<ButtonRelease-1>", stop_action)``, `<ButtonRelease-1>` refers to releasing the left mouse button.
   - `start_increment` is triggered when the button is pressed, while `stop_action` is called when the button is released, stopping the continuous action.

2. **Using Lambda with `after()`**:

   - **Purpose**: `lambda` functions are used here to delay and repeatedly execute functions, allowing the increment or decrement function to repeat every 100 milliseconds as long as the button is held down.
   - **Syntax**: `widget.after(milliseconds, lambda: function(event))`
   - `root.after(100, lambda: start_increment(event))` calls `start_increment` after 100 milliseconds. The `lambda` function allows passing `event` to `start_increment` and ensures the function is wrapped for delayed, repeated calls.

3. **Stopping the Repeating Action**:

   - **Purpose**: `stop_action` is called when the mouse button is released, canceling any repeating actions with `root.after_cancel()`.
   - **Syntax**: `root.after_cancel(job_id)`
   - This code, ``if "increment_job" in globals()``, checks if `increment_job` is defined (using `globals()`), then cancels the ongoing `after` job, stopping the repeat.



.. code-block:: python

    import tkinter as tk

    # Create the main window
    root = tk.Tk()
    root.geometry("300x200")
    root.title("IntVar Example")

    # Create an IntVar to hold the integer value
    int_var = tk.IntVar()
    int_var.set(0)  # Initial value

    # Create a Label widget with textvariable
    label = tk.Label(root, textvariable=int_var, font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=3, pady=5)


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


    # Function to start repeating increment
    def start_increment(event):
        increment_value()
        global increment_job
        increment_job = root.after(100, lambda: start_increment(event))


    # Function to start repeating decrement
    def start_decrement(event):
        decrement_value()
        global decrement_job
        decrement_job = root.after(100, lambda: start_decrement(event))


    # Function to stop repeating action
    def stop_action(event):
        if "increment_job" in globals():
            root.after_cancel(increment_job)
        if "decrement_job" in globals():
            root.after_cancel(decrement_job)


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

----


Mouse events
~~~~~~~~~~~~~~~~~~~~

| Here is a list of common mouse events in Tkinter.
| These events can be used with `.bind()` to trigger functions in response to mouse actions on widgets.

1. **Button Press Events**:

   - `<ButtonPress>` or `<Button>`: Any mouse button is pressed.
   - `<ButtonPress-1>` or `<Button-1>`: Left mouse button is pressed.
   - `<ButtonPress-2>` or `<Button-2>`: Middle mouse button is pressed (usually the scroll wheel).
   - `<ButtonPress-3>` or `<Button-3>`: Right mouse button is pressed.

2. **Button Release Events**:

   - `<ButtonRelease>`: Any mouse button is released.
   - `<ButtonRelease-1>`: Left mouse button is released.
   - `<ButtonRelease-2>`: Middle mouse button is released.
   - `<ButtonRelease-3>`: Right mouse button is released.

3. **Double-Click Events**:

   - `<Double-Button-1>`: Double-click of the left mouse button.
   - `<Double-Button-2>`: Double-click of the middle mouse button.
   - `<Double-Button-3>`: Double-click of the right mouse button.

4. **Mouse Motion Events**:

   - `<Motion>`: Mouse is moved while inside a widget.

5. **Mouse Enter/Leave Events**:

   - `<Enter>`: Mouse pointer enters the widget area.
   - `<Leave>`: Mouse pointer leaves the widget area.

6. **Mouse Wheel Event**:

   - `<MouseWheel>`: Mouse wheel is scrolled (Windows and macOS).
   - `<Button-4>`: Mouse wheel scroll up (Linux).
   - `<Button-5>`: Mouse wheel scroll down (Linux).

