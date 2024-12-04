import tkinter as tk
from tkinter import font


# Create the main window
root = tk.Tk()
root.title("Option Buttons")

# Create a frame with a background color
frame = tk.Frame(root, bg="light blue")
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Define a font style
fontStyle = font.Font(family="Lucida Grande", size=18)

# Create a StringVar to hold the selected option
option_grp1_var = tk.StringVar(value=None)  # No default value

# Define the options
options = ["Option 1", "Option 2", "Option 3"]

# Create and pack the radio buttons
for option in options:
    button = tk.Radiobutton(frame, text=option, value=option, variable=option_grp1_var,
                            bg="white", fg="black", font=fontStyle, indicatoron=0, padx=10, pady=5)
    button.pack(side="left", padx=5, pady=5)
option_grp1_var.set("Option 1")


# Create a StringVar to hold the selected option
option_grp2_var = tk.StringVar(value=None)  # No default value

# Define the options
options = ["Option 4", "Option 5", "Option 6"]

# Create and pack the radio buttons
for option in options:
    button = tk.Radiobutton(root, text=option, value=option, variable=option_grp2_var,
                            bg="white", fg="black", font=fontStyle, indicatoron=1, padx=10, pady=5)
    button.pack(side="left", padx=5, pady=5)
option_grp2_var.set("Option 4")

# Run the main event loop
root.mainloop()
