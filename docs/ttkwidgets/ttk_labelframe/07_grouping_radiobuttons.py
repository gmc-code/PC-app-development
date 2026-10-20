# ttk LabelFrame - Grouping radiobuttons

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x250")
root.title("Order")

size_box = ttk.LabelFrame(root, text="Size", padding=10)
size_box.pack(fill="x", padx=10, pady=5)

size = tk.StringVar(value="Small")
for choice in ["Small", "Medium", "Large"]:
    ttk.Radiobutton(size_box, text=choice, variable=size, value=choice).pack(anchor="w")

drink_box = ttk.LabelFrame(root, text="Drink", padding=10)
drink_box.pack(fill="x", padx=10, pady=5)

drink = tk.StringVar(value="Water")
for choice in ["Water", "Juice"]:
    ttk.Radiobutton(drink_box, text=choice, variable=drink, value=choice).pack(anchor="w")

root.mainloop()
