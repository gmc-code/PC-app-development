import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("300x200")
root.title("Toggle via checkbox Example")

# Create a BooleanVar to hold the boolean value
bool_var = tk.BooleanVar()
bool_var.set(False)  # Initial value

# Function to toggle the label color
def toggle_label_color():
    if bool_var.get():
        label.config(fg="blue")  # Set label color to blue
    else:
        label.config(fg="black")  # Set label color to black

# Create a Checkbutton to toggle the label color
toggle_checkbutton = tk.Checkbutton(root, text="Blue Label",  variable=bool_var, command=toggle_label_color)
toggle_checkbutton.grid(row=0, column=0, padx=10, pady=20)

# Create a Label widget
label = tk.Label(root, text="Text to colour", font=("Helvetica", 16), fg="black")
label.grid(row=0, column=1, pady=20)

# Run the application
root.mainloop()
