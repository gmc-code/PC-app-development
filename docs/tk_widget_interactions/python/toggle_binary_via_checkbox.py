import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x100")
root.title("Toggle Binary via Checkbox Example")

# Create a BooleanVar to hold the boolean value
bool_var = tk.BooleanVar()
bool_var.set(False)  # Initial value

# Function to toggle the label between decimal and binary
def toggle_label():
    if bool_var.get():
        label.config(fg="blue", text=bin(9)[2:])  # omit leading "0b"
    else:
        label.config(fg="black", text="9")  # Set label color to black and text to decimal

# Create a Checkbutton to toggle the label between decimal and binary
toggle_checkbutton = tk.Checkbutton(root, text="Toggle Binary", variable=bool_var, command=toggle_label)
toggle_checkbutton.grid(row=0, column=0, padx=10, pady=20)

# Create a Label widget
label = tk.Label(root, text="9", font=("Helvetica", 16), fg="black")
label.grid(row=0, column=1, pady=20)

# Run the application
root.mainloop()
