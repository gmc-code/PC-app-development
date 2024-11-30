# not as reliable as binding on different keyboards so not used here
import tkinter as tk


# Function to determine increment/decrement amount based on modifier keys
def get_increment(event):
    if event.state == 131081:  # AltShift key
        increment = 1000
    elif event.state == 9:  # Shift key
        increment = 100
    elif event.state == 131080:  # Alt key
        increment = 10
    else:
        increment = 1
    return increment


# Function to increment the integer value
def increment_value(event):
    increment = get_increment(event)
    current_value = int_var.get()
    int_var.set(current_value + increment)


# Function to decrement the integer value
def decrement_value(event):
    decrement = get_increment(event)
    current_value = int_var.get()
    int_var.set(current_value - decrement)


# Function to reset the integer value to zero
def reset_value():
    int_var.set(0)  # Reset the value to 0


# Function to start repeating increment after a delay
def start_increment(event):
    global increment_job
    increment_value(event)  # Initial increment
    increment_job = window.after(500, lambda: repeat_increment(event))


def repeat_increment(event):
    increment_value(event)
    global increment_job
    increment_job = window.after(100, lambda: repeat_increment(event))


# Function to start repeating decrement after a delay
def start_decrement(event):
    global decrement_job
    decrement_value(event)  # Initial decrement
    decrement_job = window.after(500, lambda: repeat_decrement(event))


def repeat_decrement(event):
    decrement_value(event)
    global decrement_job
    decrement_job = window.after(100, lambda: repeat_decrement(event))


# Function to stop repeating action
def stop_action(event):
    global increment_job, decrement_job
    if "increment_job" in globals():
        window.after_cancel(increment_job)
        del increment_job
    if "decrement_job" in globals():
        window.after_cancel(decrement_job)
        del decrement_job


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
button_decrement = tk.Button(root, text="-", width=4, font=("Helvetica", 24), bg="#FF6666")  # Light red
button_reset = tk.Button(root, text="Reset", command=reset_value, font=("Helvetica", 16), bg="#FFFF99")  # Light yellow
button_increment = tk.Button(root, text="+", width=4, font=("Helvetica", 24), bg="#99FF99")  # Light green

# Bind mouse events to buttons for single and repeating action
button_increment.bind("<ButtonPress-1>", start_increment)
button_increment.bind("<ButtonRelease-1>", stop_action)
button_decrement.bind("<ButtonPress-1>", start_decrement)
button_decrement.bind("<ButtonRelease-1>", stop_action)

# Position the buttons below the label
button_decrement.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
button_reset.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
button_increment.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

# Run the application
window.mainloop()
