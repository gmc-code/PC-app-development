# ttk Treeview - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("350x250")
root.title("Class list")

table = ttk.Treeview(root, columns=("name", "year"), show="headings")
table.heading("name", text="Name")
table.heading("year", text="Year")

for row in [("Ava", 7), ("Ben", 8), ("Chloe", 7), ("Dev", 8)]:
    table.insert("", tk.END, values=row)

table.pack(pady=10)

root.mainloop()
