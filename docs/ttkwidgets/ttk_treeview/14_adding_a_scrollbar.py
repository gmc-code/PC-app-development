# ttk Treeview - Adding a scrollbar

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("320x230")
root.title("Scrollbar")

box = ttk.Frame(root, padding=10)
box.pack(fill="both", expand=True)

scrollbar = ttk.Scrollbar(box)
scrollbar.pack(side="right", fill="y")

table = ttk.Treeview(box, columns=("number", "times7"), show="headings",
                     yscrollcommand=scrollbar.set)
table.heading("number", text="Number")
table.heading("times7", text="x 7")
table.pack(side="left", fill="both", expand=True)

scrollbar.config(command=table.yview)

for number in range(1, 101):
    table.insert("", tk.END, values=(number, number * 7))

root.mainloop()
