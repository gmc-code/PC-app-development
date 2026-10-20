# ttk Menubutton - Tasks Q3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Colours")

colour = tk.StringVar(value="Red")

colour_button = ttk.Menubutton(root, textvariable=colour, width=10)
colour_menu = tk.Menu(colour_button, tearoff=0)
for choice in ["Red", "Green", "Blue"]:
    colour_menu.add_radiobutton(label=choice, variable=colour, value=choice)
colour_button.config(menu=colour_menu)
colour_button.pack(pady=40)

root.mainloop()
