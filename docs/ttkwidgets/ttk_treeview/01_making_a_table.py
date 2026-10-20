# ttk Treeview - Making a table

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("320x220")
root.title("My first Treeview")

table = ttk.Treeview(root, columns=("name", "score"), show="headings")   # 1. Create it

table.heading("name", text="Name")              # 2. Headings
table.heading("score", text="Score")

table.insert("", tk.END, values=("Ava", 95))    # 3. Rows
table.insert("", tk.END, values=("Ben", 88))
table.insert("", tk.END, values=("Chloe", 91))

table.pack(pady=10)

root.mainloop()                 # Keep the window open
