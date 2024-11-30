====================================================
tk Widget Interactions
====================================================

| See: https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/

----

Variable Binding
-------------------------

| Widgets can share and update common variables.
| For example, StringVar, IntVar, DoubleVar, and BooleanVar are special Tkinter variables that can be linked to multiple widgets.
| When the variable's value changes, all linked widgets update automatically.

.. code-block:: python

    import tkinter as tk

    # Create the main window
    root = tk.Tk()
    window.geometry("300x200")
    window.title("Tkinter Widget Interaction Examples")

    # Example 1: Variable Binding
    shared_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=shared_var)
    entry.pack()
    label = tk.Label(root, textvariable=shared_var)
    label.pack()

----

Event Binding
--------------------

Widgets can respond to events such as mouse clicks, key presses, or other actions. You can bind events to functions using the bind method.

def on_button_click(event):
    print("Button clicked!")

button_event = tk.Button(root, text="Click Me")
button_event.bind("<Button-1>", on_button_click)
button_event.pack()

# Example 3: Command Callbacks
def on_button_click_command():
    print("Button clicked!")

button_command = tk.Button(root, text="Click Me", command=on_button_click_command)
button_command.pack()

# Example 4: Grid Geometry Manager
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)

# Example 5: Widget Communication
def update_label():
    label_communication.config(text="Updated Text")

button_communication = tk.Button(root, text="Update", command=update_label)
button_communication.pack()
label_communication = tk.Label(root, text="Original Text")
label_communication.pack()

# Example 6: Using Frames for Grouping
frame = tk.Frame(root)
frame.pack()
button1 = tk.Button(frame, text="Button 1")
button2 = tk.Button(frame, text="Button 2")
button1.pack(side="left")
button2.pack(side="right")

# Example 7: Advanced Interactions
def scheduled_task():
    print("Task executed")
    window.after(1000, scheduled_task)  # Repeat every 1000ms

window.after(1000, scheduled_task)

# Run the application
window.mainloop()
