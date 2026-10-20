# ttk Progressbar - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Progress")

bar = ttk.Progressbar(root, length=250, maximum=5, value=3)
bar.pack(pady=40)

root.mainloop()
