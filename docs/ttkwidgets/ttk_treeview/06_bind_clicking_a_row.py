# ttk Treeview - bind (clicking a row)

import tkinter as tk
from tkinter import ttk


def row_clicked(event):
    for row_id in table.selection():
        planet, moons = table.item(row_id, "values")
        result_label.config(text=f"{planet} has {moons} moons")


root = tk.Tk()
root.geometry("320x250")
root.title("TreeviewSelect")

table = ttk.Treeview(root, columns=("planet", "moons"), show="headings", height=5,
                     selectmode="browse")
table.heading("planet", text="Planet")
table.heading("moons", text="Moons")
for row in [("Mercury", 0), ("Venus", 0), ("Earth", 1), ("Mars", 2), ("Jupiter", 95)]:
    table.insert("", tk.END, values=row)
table.pack(pady=10)
table.bind("<<TreeviewSelect>>", row_clicked)

result_label = ttk.Label(root, text="Click a planet", font=("Arial", 14))
result_label.pack()

root.mainloop()
