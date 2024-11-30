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
root.title("Integer Counter Example")

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
