# ttk Scale - orient and length

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("orient and length")

ttk.Scale(root, from_=0, to=100, orient="horizontal", length=200).pack(pady=10)
ttk.Scale(root, from_=100, to=0, orient="vertical", length=120).pack()

root.mainloop()
