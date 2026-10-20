# ttk Scrollbar - Making a ttk Scrollbar

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first ttk Scrollbar")

scrollbar = ttk.Scrollbar(root, orient="vertical")              # 1. Create it
scrollbar.pack(side="right", fill="y")

item_list = tk.Listbox(root, yscrollcommand=scrollbar.set)      # 2. Widget -> scrollbar
item_list.pack(side="left", fill="both", expand=True)

scrollbar.config(command=item_list.yview)                       # 3. Scrollbar -> widget

for number in range(1, 101):
    item_list.insert(tk.END, f"Item {number}")

root.mainloop()                 # Keep the window open
