import tkinter as tk

# Function to change the integer value by a specified amount
def change_value(amount):
    current_value = int_var.get()
    int_var.set(current_value + amount)

# Function to reset the integer value to zero
def reset_value():
    int_var.set(0)  # Reset the value to 0

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

# Create Buttons
button_decrement = tk.Button(root, text="-", width=4, font=("Helvetica", 24), bg="#FF6666")  # Light red
button_reset = tk.Button(root, text="Reset", command=reset_value, font=("Helvetica", 16), bg="#FFFF99")  # Light yellow
button_increment = tk.Button(root, text="+", width=4, font=("Helvetica", 24), bg="#99FF99")  # Light green

# Bind increment and decrement buttons using lambdas
button_increment.bind("<Button-1>", lambda event: change_value(1))       # No modifier
button_increment.bind("<Alt-Button-1>", lambda event: change_value(10))  # Alt + Click
button_increment.bind("<Shift-Button-1>", lambda event: change_value(100)) # Shift + Click
button_increment.bind("<Alt-Shift-Button-1>", lambda event: change_value(1000)) # Alt-Shift + Click

button_decrement.bind("<Button-1>", lambda event: change_value(-1))      # No modifier
button_decrement.bind("<Alt-Button-1>", lambda event: change_value(-10)) # Alt + Click
button_decrement.bind("<Shift-Button-1>", lambda event: change_value(-100)) # Shift + Click
button_decrement.bind("<Alt-Shift-Button-1>", lambda event: change_value(-1000)) # Alt-Shift + Click

# Position the buttons below the label
button_decrement.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
button_reset.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
button_increment.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

# Run the application
root.mainloop()
