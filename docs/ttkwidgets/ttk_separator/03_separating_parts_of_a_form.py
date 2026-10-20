# ttk Separator - Separating parts of a form

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x280")
root.title("Order form")

ttk.Label(root, text="Pizza order", font=("Arial", 16, "bold")).pack(pady=5)
ttk.Separator(root).pack(fill="x", padx=10, pady=5)

ttk.Label(root, text="Name:").pack()
ttk.Entry(root).pack()
ttk.Separator(root).pack(fill="x", padx=10, pady=10)

size = tk.StringVar(value="Medium")
for choice in ["Small", "Medium", "Large"]:
    ttk.Radiobutton(root, text=choice, variable=size, value=choice).pack()
ttk.Separator(root).pack(fill="x", padx=10, pady=10)

ttk.Button(root, text="Order").pack()

root.mainloop()
