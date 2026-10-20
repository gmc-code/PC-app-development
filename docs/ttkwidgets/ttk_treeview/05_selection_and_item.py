# ttk Treeview - selection and item

import tkinter as tk
from tkinter import ttk


def show_selected():
    selected = table.selection()
    if selected:
        name, score = table.item(selected[0], "values")
        result_label.config(text=f"{name} scored {score}")
    else:
        result_label.config(text="Click a row first")


root = tk.Tk()
root.geometry("320x260")
root.title("selection and item")

table = ttk.Treeview(root, columns=("name", "score"), show="headings", height=4,
                     selectmode="browse")
table.heading("name", text="Name")
table.heading("score", text="Score")
for row in [("Ava", 95), ("Ben", 88), ("Chloe", 91)]:
    table.insert("", tk.END, values=row)
table.pack(pady=10)

ttk.Button(root, text="Show selected", command=show_selected).pack()

result_label = ttk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
