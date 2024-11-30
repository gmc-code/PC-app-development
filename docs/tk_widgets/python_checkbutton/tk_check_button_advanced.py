import tkinter as tk
from tkinter import font

def display_options():
    selected_options = [option for option, var in zip(options, option_vars) if var.get()]
    text_widget.delete(1.0, 'end')
    text_widget.insert(tk.END, f"You selected: {', '.join(selected_options)}")

# Create the main window
root = tk.Tk()
window.title("Checkbutton Example")

# Create a frame with a background color
frame = tk.Frame(root, bg="light blue")
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Define a font style
fontStyle = font.Font(family="Lucida Grande", size=18)

# Define the options
options = ["Option 1", "Option 2", "Option 3"]

# Create a list to hold the IntVar for each checkbutton
option_vars = [tk.IntVar() for _ in options]

# Create and pack the checkbuttons
for option, var in zip(options, option_vars):
    button = tk.Checkbutton(frame, text=option, variable=var, command=display_options,
                            bg="white", fg="black", font=fontStyle, padx=10, pady=5)
    button.pack(side="left", padx=5, pady=5)

# Create a text widget to display the selected options
text_widget = tk.Text(root, height=2, width=40, bg="white", fg="black", font=fontStyle, bd=2, relief="solid")
text_widget.pack(padx=10, pady=10)

# Run the main event loop
window.mainloop()
