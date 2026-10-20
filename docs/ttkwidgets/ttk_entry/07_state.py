# ttk Entry - state

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

for setting in ["normal", "readonly", "disabled"]:
    entry = ttk.Entry(root)
    entry.insert(0, setting)            # Insert before locking the box
    entry.config(state=setting)
    entry.pack(pady=5)

root.mainloop()
