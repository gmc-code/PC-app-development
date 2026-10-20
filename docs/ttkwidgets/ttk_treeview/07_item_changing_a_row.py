# ttk Treeview - item (changing a row)

import tkinter as tk
from tkinter import ttk


def add_point():
    for row_id in table.selection():
        name, points = table.item(row_id, "values")
        table.item(row_id, values=(name, int(points) + 1))


root = tk.Tk()
root.geometry("320x230")
root.title("Changing a row")

table = ttk.Treeview(root, columns=("team", "points"), show="headings", height=3)
table.heading("team", text="Team")
table.heading("points", text="Points")
for row in [("Red", 0), ("Blue", 0), ("Gold", 0)]:
    table.insert("", tk.END, values=row)
table.pack(pady=10)

ttk.Button(root, text="Add a point to the selected team", command=add_point).pack()

root.mainloop()
