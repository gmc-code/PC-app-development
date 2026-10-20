# ttk Checkbutton - width and padding

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("width and padding")

toppings = []                       # Keep every variable in a list
for topping in ["Ham", "Pineapple", "Mushrooms"]:
    choice = tk.IntVar()
    toppings.append(choice)
    ttk.Checkbutton(root, text=topping, variable=choice, width=15,
                    padding=5).pack(anchor="w", padx=80)

root.mainloop()
