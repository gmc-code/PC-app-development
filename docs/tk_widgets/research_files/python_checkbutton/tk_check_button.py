import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Checkbutton Example")

# Create a frame with a background color
frame1 = tk.Frame(root, bg="light blue")
frame1.pack(anchor="nw", padx=10, pady=10)

# Define a font style
font_style = ("Lucida Grande", 18)

# Define the options for group 1
options_grp1 = ["Checkbox 1", "Checkbox 2", "Checkbox 3"]
# Store each checkbox's IntVar using its label as the key.
variables = {}

for option in options_grp1:
    # Each checkbutton has its own IntVar.
    # IntVar() defaults to 0 (unchecked).
    variables[option] = tk.IntVar()

    # Make the first checkbutton checked initially.
    if option == "Checkbox 1":
        variables[option].set(1)

    button = tk.Checkbutton(
        frame1, text=option, variable=variables[option], indicatoron=1,
        bg="white", fg="black", font=font_style, padx=10, pady=5
    )
    button.pack(anchor="nw", padx=5, pady=5)

# Run the main event loop
root.mainloop()
