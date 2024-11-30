import tkinter as tk


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


# Create the main window
window = tk.Tk()
window.geometry("300x200")
window.title("DoubleVar Example")

# Create a DoubleVar to hold the float value
double_var = tk.DoubleVar()
double_var.set(0.0)  # Initial value

# Create a Label widget with textvariable
label = tk.Label(window, textvariable=double_var, font=("Helvetica", 16))
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
