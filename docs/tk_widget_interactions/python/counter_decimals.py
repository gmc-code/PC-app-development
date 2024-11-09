import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("300x200")
root.title("DoubleVar Example")

# Create a DoubleVar to hold the float value
double_var = tk.DoubleVar()
double_var.set(0.0)  # Initial value

# Initialize global variables
increment_job = None
decrement_job = None
speed_up_job = None

# Create a Label widget with textvariable
label = tk.Label(root, textvariable=double_var, font=("Helvetica", 16))
label.grid(row=0, column=0, columnspan=3, pady=5)

# Function to increment the float value
def increment_value():
    current_value = double_var.get()
    double_var.set(round(current_value + 0.1, 1))  # Increment the value by 0.1

# Function to decrement the float value
def decrement_value():
    current_value = double_var.get()
    double_var.set(round(current_value - 0.1, 1))  # Decrement the value by 0.1

# Function to reset the float value to zero
def reset_value():
    double_var.set(0.0)  # Reset the value to 0.0

# Function to start repeating increment
def start_increment(event):
    global increment_job, speed_up_job  # Declare globals
    increment_value()
    increment_job = root.after(600, repeat_increment)  # Initial slower speed
    speed_up_job = root.after(1000, speed_up_increment)  # Speed up after 1 second

# Function to start repeating decrement
def start_decrement(event):
    global decrement_job, speed_up_job  # Declare globals
    decrement_value()
    decrement_job = root.after(600, repeat_decrement)  # Initial slower speed
    speed_up_job = root.after(1000, speed_up_decrement)  # Speed up after 1 second

# Function to repeat increment
def repeat_increment():
    global increment_job  # Declare global
    increment_value()
    increment_job = root.after(300, repeat_increment)  # Continue at slower speed

# Function to repeat decrement
def repeat_decrement():
    global decrement_job  # Declare global
    decrement_value()
    decrement_job = root.after(300, repeat_decrement)  # Continue at slower speed

# Function to speed up increment
def speed_up_increment():
    global increment_job  # Declare global
    root.after_cancel(increment_job)
    increment_value()
    increment_job = root.after(150, repeat_increment)  # Faster speed

# Function to speed up decrement
def speed_up_decrement():
    global decrement_job  # Declare global
    root.after_cancel(decrement_job)
    decrement_value()
    decrement_job = root.after(150, repeat_decrement)  # Faster speed

# Function to stop repeating action
def stop_action(event):
    global increment_job, decrement_job, speed_up_job  # Declare globals
    if increment_job is not None:
        root.after_cancel(increment_job)
        increment_job = None
    if decrement_job is not None:
        root.after_cancel(decrement_job)
        decrement_job = None
    if speed_up_job is not None:
        root.after_cancel(speed_up_job)
        speed_up_job = None

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
