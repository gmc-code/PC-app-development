import tkinter as tk
import random


def inc_rand_int():
    return random.randint(1,10)


# Function to increment the integer value
def increment_value():
    current_value = int_var.get()
    inc = inc_rand_int()
    int_var.set(current_value + inc)  # Increment the value by INC


# Function to decrement the integer value
def decrement_value():
    current_value = int_var.get()
    inc = inc_rand_int()
    int_var.set(current_value - inc)  # Decrement the value by INC


# Function to reset the integer value to zero
def reset_value():
    int_var.set(0)  # Reset the value to 0


# Create the main window
window = tk.Tk()
window.geometry("300x200")
window.title("IntVar Example")

# Create an IntVar to hold the integer value
int_var = tk.IntVar()
int_var.set(0)  # Initial value

# Create a Label widget with textvariable
label = tk.Label(window, textvariable=int_var, font=("Helvetica", 16))
label.grid(row=0, column=0, columnspan=3, pady=5)

# Create Buttons to trigger the value update
button_decrement = tk.Button(window, text="-", width=4, command=decrement_value, font=("Helvetica", 24), bg="#FF6666")  # Light red
button_reset = tk.Button(window, text="Reset", command=reset_value, font=("Helvetica", 16), bg="#FFFF99")  # Light yellow
button_increment = tk.Button(window, text="+", width=4, command=increment_value, font=("Helvetica", 24), bg="#99FF99")  # Light green

# Position the buttons below the label
button_decrement.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
button_reset.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
button_increment.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

# Run the application
window.mainloop()
