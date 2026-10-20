# ttk Scrollbar - With grid

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("grid")

ttk.Label(root, text="Countries").grid(row=0, column=0)

country_list = tk.Listbox(root, height=6)
country_list.grid(row=1, column=0)

scrollbar = ttk.Scrollbar(root, command=country_list.yview)
scrollbar.grid(row=1, column=1, sticky="ns")
country_list.config(yscrollcommand=scrollbar.set)

for country in ["Australia", "Brazil", "Canada", "Denmark", "Egypt", "France",
                "Germany", "India", "Japan", "Kenya"]:
    country_list.insert(tk.END, country)

root.mainloop()
