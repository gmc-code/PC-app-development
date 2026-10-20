# ttk Entry - bind (pressing Enter)

import tkinter as tk
from tkinter import ttk


def add_item(event=None):
    items_label.config(text=items_label.cget("text") + "\n" + item_entry.get())
    item_entry.delete(0, tk.END)


root = tk.Tk()
root.geometry("300x250")
root.title("bind")

item_entry = ttk.Entry(root, font=("Arial", 14))
item_entry.pack(pady=5)
item_entry.bind("<Return>", add_item)

ttk.Button(root, text="Add", command=add_item).pack()

items_label = ttk.Label(root, text="Shopping list:")
items_label.pack(pady=5)

root.mainloop()
