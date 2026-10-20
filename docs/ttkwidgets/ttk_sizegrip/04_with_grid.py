# ttk Sizegrip - With grid

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("grid")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

big_box = tk.Text(root)
big_box.grid(row=0, column=0, sticky="nsew")      # Fills its cell

ttk.Sizegrip(root).grid(row=1, column=0, sticky="se")

root.mainloop()
