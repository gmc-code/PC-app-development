# ttk Treeview - Tasks Q4

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("350x250")
root.title("Class list")

table = ttk.Treeview(root, columns=("name", "year"), show="headings")
table.heading("name", text="Name")
table.heading("year", text="Year")
table.column("year", width=60, anchor="center")
table.tag_configure("year7", foreground="blue")
table.tag_configure("year8", foreground="green")

for name, year in [("Ava", 7), ("Ben", 8), ("Chloe", 7), ("Dev", 8)]:
    table.insert("", tk.END, values=(name, year), tags=(f"year{year}",))

table.pack(pady=10)

root.mainloop()
