# not as reliable as binding on different keyboards so not used here
import tkinter as tk

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


# Function to increment the integer value
def increment_value(event):
    # print(event.state)
    if event.state == 9:  # Shift key
        increment = 100
    elif event.state == 131080:  # Alt key
        increment = 10
    else:
        increment = 1
    current_value = int_var.get()
    int_var.set(current_value + increment)  # Increment the value


# Function to decrement the integer value
def decrement_value(event):
    if event.state == 9:  # Shift key
        decrement = 100
    elif event.state == 131080:  # Alt key
        decrement = 10
    else:
        decrement = 1
    current_value = int_var.get()
    int_var.set(current_value - decrement)  # Decrement the value


# Function to reset the integer value to zero
def reset_value():
    int_var.set(0)  # Reset the value to 0


# Create Buttons to trigger the value update
button_decrement = tk.Button(window, text="-", width=4, font=("Helvetica", 24), bg="#FF6666")  # Light red
button_reset = tk.Button(window, text="Reset", command=reset_value, font=("Helvetica", 16), bg="#FFFF99")  # Light yellow
button_increment = tk.Button(window, text="+", width=4, font=("Helvetica", 24), bg="#99FF99")  # Light green

# Bind mouse click events to the increment and decrement functions
button_decrement.bind("<Button-1>", decrement_value)
button_increment.bind("<Button-1>", increment_value)

# Position the buttons below the label
button_decrement.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
button_reset.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
button_increment.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

# Run the application
window.mainloop()
