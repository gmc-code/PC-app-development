import tkinter as tk


# Function to set the label color
def set_label_color(color):
    label.config(fg=color)


# Create the main window
root = tk.Tk()
root.geometry("400x150")
root.title("Toggle via Radiobutton Example")

# Create an IntVar to hold the integer value
color_var = tk.IntVar()
color_var.set(0)  # Initial value

# Create Radiobuttons to toggle the label color using lambda
blue_radiobutton = tk.Radiobutton(root, text="Blue Label", variable=color_var, value=1, command=lambda: set_label_color("blue"))
blue_radiobutton.grid(row=0, column=0, padx=10, pady=5, sticky="w")

green_radiobutton = tk.Radiobutton(root, text="Green Label", variable=color_var, value=2, command=lambda: set_label_color("green"))
green_radiobutton.grid(row=1, column=0, padx=10, pady=5, sticky="w")

red_radiobutton = tk.Radiobutton(root, text="Red Label", variable=color_var, value=3, command=lambda: set_label_color("red"))
red_radiobutton.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Create a Label widget
label = tk.Label(root, text="Sample Text", font=("Helvetica", 16), fg="black")
label.grid(row=0, column=1, rowspan=3, padx=10, pady=20)

# Run the application
root.mainloop()
