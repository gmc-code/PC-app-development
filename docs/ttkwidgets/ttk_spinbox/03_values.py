# ttk Spinbox - values

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("values")

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

day_spinbox = ttk.Spinbox(root, values=days)
day_spinbox.set(days[0])
day_spinbox.pack(pady=30)

root.mainloop()
