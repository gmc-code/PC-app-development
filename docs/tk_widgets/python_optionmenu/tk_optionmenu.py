import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Fruit Selector")
root.geometry("300x200")

# Define a variable to hold the selected option
fruit_var = tk.StringVar(root)

# Define the options for the OptionMenu
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Set the default value for the OptionMenu
fruit_var.set(fruits[0])

# Define the font style
fontStyle1 = font.Font(family="Arial", size=16, weight="bold")
# Define the font style
fontStyle2 = font.Font(family="Arial", size=14, weight="normal")

# Create the OptionMenu widget
option_menu = tk.OptionMenu(root, fruit_var, *fruits)
option_menu.config(font=fontStyle1, bg="light green", fg="black", activebackground="dark green", activeforeground="white")
option_menu["menu"].config(font=fontStyle2, bg="light blue", fg="black", activebackground="dark blue", activeforeground="white")
option_menu.pack(pady=10, padx=10)

# Run the main event loop
root.mainloop()
