# ttk Scrollbar - get

import tkinter as tk
from tkinter import ttk


def how_far():
    top, bottom = scrollbar.get()
    result_label.config(text=f"You have scrolled {round(bottom * 100)}% of the way")


root = tk.Tk()
root.geometry("300x250")
root.title("get")

box = ttk.Frame(root)
box.pack(pady=5)

scrollbar = ttk.Scrollbar(box)
scrollbar.pack(side="right", fill="y")

item_list = tk.Listbox(box, height=8, yscrollcommand=scrollbar.set)
item_list.pack(side="left")
scrollbar.config(command=item_list.yview)

for number in range(1, 51):
    item_list.insert(tk.END, f"Item {number}")

ttk.Button(root, text="How far?", command=how_far).pack()
result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
