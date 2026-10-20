# ttk Scrollbar - Styling a ttk Scrollbar

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Scrollbar style")

style = ttk.Style()
style.theme_use("clam")
style.configure("Vertical.TScrollbar", background="orange", troughcolor="lightyellow",
                arrowcolor="white", arrowsize=20)
style.map("Vertical.TScrollbar", background=[("active", "darkorange")])

scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

item_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
item_list.pack(side="left", fill="both", expand=True)
scrollbar.config(command=item_list.yview)

for number in range(1, 51):
    item_list.insert(tk.END, f"Item {number}")

root.mainloop()
