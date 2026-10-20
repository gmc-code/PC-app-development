# ttk Scale - value

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("value")

ttk.Scale(root, from_=0, to=100, length=250, value=50).pack(pady=40)

root.mainloop()
