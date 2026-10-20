# ttk Scrollbar - Tasks Q3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Fruit")

fruit_list = tk.Listbox(root, height=5)
fruit_list.grid(row=0, column=0)

scrollbar = ttk.Scrollbar(root, command=fruit_list.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
fruit_list.config(yscrollcommand=scrollbar.set)

for fruit in ["Apple", "Banana", "Cherry", "Grape", "Kiwi",
              "Lemon", "Mango", "Orange", "Peach", "Pear"]:
    fruit_list.insert(tk.END, fruit)

root.mainloop()
