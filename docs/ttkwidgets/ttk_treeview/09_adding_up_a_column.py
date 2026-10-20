# ttk Treeview - Adding up a column

import tkinter as tk
from tkinter import ttk


def average():
    total = 0
    rows = table.get_children()
    for row_id in rows:
        name, score = table.item(row_id, "values")
        total = total + int(score)
    result_label.config(text=f"Class average: {total / len(rows):.1f}")


root = tk.Tk()
root.geometry("320x260")
root.title("Average")

table = ttk.Treeview(root, columns=("name", "score"), show="headings", height=5)
table.heading("name", text="Name")
table.heading("score", text="Score")
for row in [("Ava", 95), ("Ben", 88), ("Chloe", 91), ("Dev", 76), ("Eli", 84)]:
    table.insert("", tk.END, values=row)
table.pack(pady=10)

ttk.Button(root, text="Average", command=average).pack()
result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=5)

root.mainloop()
