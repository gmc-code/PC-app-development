# ttk Treeview - Tasks Q3

import tkinter as tk
from tkinter import ttk


def add():
    table.insert("", tk.END, values=(name_entry.get(), year_entry.get()))


root = tk.Tk()
root.geometry("350x330")
root.title("Class list")

table = ttk.Treeview(root, columns=("name", "year"), show="headings", height=6)
table.heading("name", text="Name")
table.heading("year", text="Year")
table.column("year", width=60, anchor="center")

for row in [("Ava", 7), ("Ben", 8), ("Chloe", 7), ("Dev", 8)]:
    table.insert("", tk.END, values=row)

table.pack(pady=10)

name_entry = ttk.Entry(root)
name_entry.pack()
year_entry = ttk.Entry(root, width=5)
year_entry.pack(pady=2)
ttk.Button(root, text="Add", command=add).pack()

root.mainloop()
