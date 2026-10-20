# ttk Spinbox - wrap

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("wrap")

hour_spinbox = ttk.Spinbox(root, from_=1, to=12, wrap=True)
hour_spinbox.set(12)
hour_spinbox.pack(pady=30)

root.mainloop()
