# ttk Menubutton - add_radiobutton

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("add_radiobutton")

size = tk.StringVar(value="Medium")

size_button = ttk.Menubutton(root, textvariable=size, width=12)   # Shows the choice
size_menu = tk.Menu(size_button, tearoff=0)
for choice in ["Small", "Medium", "Large"]:
    size_menu.add_radiobutton(label=choice, variable=size, value=choice)
size_button.config(menu=size_menu)
size_button.pack(pady=40)

root.mainloop()
