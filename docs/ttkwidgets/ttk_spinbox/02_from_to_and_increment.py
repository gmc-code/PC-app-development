# ttk Spinbox - from\_, to and increment

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("from_, to and increment")

minutes = ttk.Spinbox(root, from_=0, to=60, increment=5)
minutes.set(0)
minutes.pack(pady=30)

root.mainloop()
