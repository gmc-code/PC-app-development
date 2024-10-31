import tkinter as tk
from tkinter import font

def display_option():
    selected_option = option_var.get()
    text_widget.delete(1.0, 'end')
    text_widget.insert(tk.END, f"You selected: {selected_option}")

# Create the main window
root = tk.Tk()
root.title("Option Buttons")

# Create a frame with a background color
frame = tk.Frame(root, bg="light blue")
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Define a font style
fontStyle = font.Font(family="Lucida Grande", size=18)

# Create a StringVar to hold the selected option
option_var = tk.StringVar(value=None)  # No default value

# Define the options
options = ["Option 1", "Option 2", "Option 3"]

# Create and pack the radio buttons
for option in options:
    button = tk.Radiobutton(frame, text=option, variable=option_var, value=option,
                            command=display_option, bg="white", fg="black",
                            font=fontStyle, indicatoron=0, padx=10, pady=5)
    button.pack(side="left", padx=5, pady=5)

# Create a text widget to display the selected option
text_widget = tk.Text(root, height=2, width=30, bg="white", fg="black",
                        font=fontStyle, bd=2, relief="solid")
text_widget.pack(padx=10, pady=10)

# Run the main event loop
root.mainloop()
