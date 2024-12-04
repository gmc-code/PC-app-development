import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Checkbutton Example")

# Create a frame with a background color
frame1 = tk.Frame(root, bg="light blue")
frame1.pack(anchor="nw", padx=10, pady=10)

# Define a font style
fontStyle = font.Font(family="Lucida Grande", size=18)

# Define the options for group 1
options_grp1 = ["Option 1", "Option 2", "Option 3"]

# Create a list to hold the IntVar for each checkbutton
option_vars1 = []
for option in options_grp1:
    var = tk.IntVar()
    option_vars1.append(var)
    # Preselect "Option 1"
    if option == "Option 1":
        var.set(1)

# Create and pack the checkbuttons for group 1
for option, var in zip(options_grp1, option_vars1):
    button = tk.Checkbutton(frame1, text=option, variable=var, indicatoron=0,
                            bg="white", fg="black", font=fontStyle, padx=10, pady=5)
    button.pack(anchor="nw", side="left", padx=5, pady=5)


# Define the options for group 2
options_grp2 = ["Option 4", "Option 5", "Option 6"]

# Create a list to hold the IntVar for each checkbutton
option_vars2 = []
for option in options_grp2:
    var = tk.IntVar()
    option_vars2.append(var)
    # Preselect "Option 4"
    if option == "Option 4":
        var.set(1)

# Create and pack the checkbuttons for group 2
for option, var in zip(options_grp2, option_vars2):
    button = tk.Checkbutton(root, text=option, variable=var, indicatoron=1,
                            bg="white", fg="black", font=fontStyle, padx=10, pady=5)
    button.pack(anchor="nw", side="left", padx=5, pady=5)

# Run the main event loop
root.mainloop()
