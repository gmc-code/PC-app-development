import tkinter as tk


# Function to toggle the label color and case
def toggle_label():
    if bool_var.get():
        label.config(fg="blue", text=label.cget("text").upper())  # Set label color to blue and text to uppercase
    else:
        label.config(fg="black", text=label.cget("text").lower())  # Set label color to black and text to lowercase


# Create the main window
window = tk.Tk()
window.geometry("400x100")
window.title("Toggle via Checkbox Example")

# Create a BooleanVar to hold the boolean value
bool_var = tk.BooleanVar()
bool_var.set(False)  # Initial value

# Create a Checkbutton to toggle the label color and case
toggle_checkbutton = tk.Checkbutton(window, text="Toggle Case and Color", variable=bool_var, command=toggle_label)
toggle_checkbutton.grid(row=0, column=0, padx=10, pady=20)

# Create a Label widget
label = tk.Label(window, text="Case and Colour", font=("Helvetica", 16), fg="black")
label.grid(row=0, column=1, pady=20)

# Run the application
window.mainloop()
