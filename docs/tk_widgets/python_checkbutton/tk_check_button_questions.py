import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Checkbutton Question")
# Set the size of the window
root.geometry("350x300")

# Create a frame with a background color
frame1 = tk.Frame(root, bg="light blue")
frame1.pack(anchor="nw", padx=10, pady=10)

# Define a font style
fontStyle = font.Font(family="Lucida Grande", size=18)

# Define the options for group 1
options_grp1 = ["Checkbox 1", "Checkbox 2", "Checkbox 3", "Checkbox 4"]

for option in options_grp1:
    var = tk.IntVar()

    if option == "Checkbox 1":
        var.set(1)

    button = tk.Checkbutton(
        frame1, text=option, variable=var, indicatoron=1,
        bg="white", fg="black", font=fontStyle, padx=10, pady=5
    )
    button.pack(anchor="nw", side="top", padx=5, pady=5)


# Run the main event loop
root.mainloop()
