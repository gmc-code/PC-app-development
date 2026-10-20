# ttk Spinbox - Tasks Q3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Colours")

colour_spinbox = ttk.Spinbox(root, values=("Red", "Orange", "Yellow", "Green"),
                             wrap=True)
colour_spinbox.set("Red")
colour_spinbox.pack(pady=30)

root.mainloop()
