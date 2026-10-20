# ttk Combobox - Adding typed items to the list

import tkinter as tk
from tkinter import ttk


def add_name(event=None):
    new_name = name_box.get()
    names = list(name_box.cget("values"))
    if new_name and new_name not in names:
        names.append(new_name)
        name_box.config(values=names)
        result_label.config(text=f"{new_name} added")


root = tk.Tk()
root.geometry("300x200")
root.title("Adding items")

name_box = ttk.Combobox(root, values=["Ava", "Ben"])
name_box.pack(pady=10)
name_box.bind("<Return>", add_name)

ttk.Button(root, text="Add name", command=add_name).pack()

result_label = ttk.Label(root, text="Type a name and press Enter")
result_label.pack(pady=10)

root.mainloop()
