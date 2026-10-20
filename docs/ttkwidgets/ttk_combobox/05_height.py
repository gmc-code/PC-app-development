# ttk Combobox - height

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("height")

numbers = list(range(1, 51))

number_box = ttk.Combobox(root, values=numbers, height=5)
number_box.set(1)
number_box.pack(pady=30)

root.mainloop()
