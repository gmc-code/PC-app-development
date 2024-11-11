import tkinter as tk


# Function to set the label color
def set_label_color():
    label.config(fg=color_var.get())


# Create the main window
root = tk.Tk()
root.geometry("400x150")
root.title("Modify via Radiobutton Example")

# Create a StringVar to hold the color value
color_var = tk.StringVar()
color_var.set("black")  # Initial value

# Create Radiobuttons to toggle the label color using the color as value
blue_radiobutton = tk.Radiobutton(root, text="Blue Label", variable=color_var, value="blue", command=set_label_color)
blue_radiobutton.grid(row=0, column=0, padx=10, pady=5, sticky="w")

green_radiobutton = tk.Radiobutton(root, text="Green Label", variable=color_var, value="green", command=set_label_color)
green_radiobutton.grid(row=1, column=0, padx=10, pady=5, sticky="w")

red_radiobutton = tk.Radiobutton(root, text="Red Label", variable=color_var, value="red", command=set_label_color)
red_radiobutton.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Create a Label widget
label = tk.Label(root, text="Sample Text", font=("Helvetica", 16), fg="black")
label.grid(row=0, column=1, rowspan=3, padx=10, pady=20)

# Run the application
root.mainloop()
