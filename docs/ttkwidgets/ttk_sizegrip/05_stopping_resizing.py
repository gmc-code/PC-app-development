# ttk Sizegrip - Stopping resizing

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("minsize")
root.minsize(250, 150)                          # Cannot be made smaller than this

ttk.Sizegrip(root).pack(side="bottom", anchor="se")
ttk.Label(root, text="Try to make me tiny!").pack(pady=60)

root.mainloop()
