# ttk Radiobutton - Tasks Q4

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Sizes")

style = ttk.Style()
style.theme_use("clam")
style.map("Size.Toolbutton", background=[("selected", "lightgreen")])

size = tk.StringVar(value="Medium")

row = ttk.Frame(root)
row.pack(pady=40)
for choice in ["Small", "Medium", "Large"]:
    ttk.Radiobutton(row, text=choice, variable=size, value=choice,
                    style="Size.Toolbutton").pack(side="left", padx=2)

root.mainloop()
