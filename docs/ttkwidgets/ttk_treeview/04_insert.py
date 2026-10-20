# ttk Treeview - insert

import tkinter as tk
from tkinter import ttk


def add_row():
    table.insert("", tk.END, values=(name_entry.get(), score_entry.get()))
    name_entry.delete(0, tk.END)
    score_entry.delete(0, tk.END)


root = tk.Tk()
root.geometry("320x300")
root.title("insert")

form = ttk.Frame(root, padding=5)
form.pack()
ttk.Label(form, text="Name:").grid(row=0, column=0)
name_entry = ttk.Entry(form, width=12)
name_entry.grid(row=0, column=1)
ttk.Label(form, text="Score:").grid(row=1, column=0)
score_entry = ttk.Entry(form, width=12)
score_entry.grid(row=1, column=1)
ttk.Button(form, text="Add", command=add_row).grid(row=2, column=0, columnspan=2, pady=5)

table = ttk.Treeview(root, columns=("name", "score"), show="headings", height=6)
table.heading("name", text="Name")
table.heading("score", text="Score")
table.pack()

root.mainloop()
