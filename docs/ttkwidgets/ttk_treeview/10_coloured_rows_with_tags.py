# ttk Treeview - Coloured rows with tags

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("320x220")
root.title("tags")

table = ttk.Treeview(root, columns=("name", "score"), show="headings", height=6)
table.heading("name", text="Name")
table.heading("score", text="Score")

table.tag_configure("pass", foreground="green")
table.tag_configure("fail", foreground="red", background="mistyrose")

for name, score in [("Ava", 95), ("Ben", 42), ("Chloe", 71), ("Dev", 38)]:
    if score >= 50:
        table.insert("", tk.END, values=(name, score), tags=("pass",))
    else:
        table.insert("", tk.END, values=(name, score), tags=("fail",))

table.pack(pady=10)

root.mainloop()
