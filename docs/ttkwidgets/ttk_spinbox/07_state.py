# ttk Spinbox - state

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

size_spinbox = ttk.Spinbox(root, values=("Small", "Medium", "Large"), state="readonly")
size_spinbox.set("Small")
size_spinbox.pack(pady=30)

root.mainloop()
