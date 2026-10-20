# ttk Scale - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Rating")

ttk.Scale(root, from_=1, to=10, length=250, value=5).pack(pady=30)

root.mainloop()
