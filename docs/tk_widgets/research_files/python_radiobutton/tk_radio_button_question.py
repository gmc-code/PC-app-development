import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Radio Buttons Question")
root.geometry("300x300")

# Create a frame with a background color
frame = tk.Frame(root, bg="light blue")
frame.pack(anchor="nw", padx=10, pady=10)

# Define a font style
font_style = ("Lucida Grande", 18)

# Create a StringVar to hold the selected option
option_var = tk.StringVar(value="Option 1")   # default value

# Define the options
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Create and pack the radio buttons
for option in options:
    button = tk.Radiobutton(frame, text=option, value=option, variable=option_var,
                            bg="white", fg="black", font=font_style, indicatoron=1, padx=10, pady=5)
    button.pack(anchor="nw", side="top", padx=5, pady=5)
# option_var.set("Option 1")

# Run the main event loop
root.mainloop()

