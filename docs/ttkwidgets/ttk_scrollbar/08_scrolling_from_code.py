# ttk Scrollbar - Scrolling from code

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x250")
root.title("yview_moveto")

box = ttk.Frame(root)
box.pack(pady=5)

scrollbar = ttk.Scrollbar(box)
scrollbar.pack(side="right", fill="y")

name_list = tk.Listbox(box, height=8, yscrollcommand=scrollbar.set)
name_list.pack(side="left")
scrollbar.config(command=name_list.yview)

for number in range(1, 101):
    name_list.insert(tk.END, f"Student {number}")

ttk.Button(root, text="Top", command=lambda: name_list.yview_moveto(0)).pack(side="left", padx=50)
ttk.Button(root, text="Bottom", command=lambda: name_list.yview_moveto(1)).pack(side="left")

root.mainloop()
