# ttk Scrollbar - Tasks Q4

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Numbers")

style = ttk.Style()
style.theme_use("clam")
style.configure("Vertical.TScrollbar", background="green", troughcolor="lightgreen")

scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

number_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
number_list.pack(side="left", fill="both", expand=True)
scrollbar.config(command=number_list.yview)

for number in range(1, 201):
    number_list.insert(tk.END, number)

root.mainloop()
