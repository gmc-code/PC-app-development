# tk LabelFrame - Grouping radiobuttons

import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("Order")

size_box = tk.LabelFrame(root, text="Size", padx=10, pady=5)
size_box.pack(fill="x", padx=10, pady=5)

size = tk.StringVar(value="Small")
for choice in ["Small", "Medium", "Large"]:
    tk.Radiobutton(size_box, text=choice, variable=size, value=choice).pack(anchor="w")

drink_box = tk.LabelFrame(root, text="Drink", padx=10, pady=5)
drink_box.pack(fill="x", padx=10, pady=5)

drink = tk.StringVar(value="Water")
for choice in ["Water", "Juice"]:
    tk.Radiobutton(drink_box, text=choice, variable=drink, value=choice).pack(anchor="w")

root.mainloop()
