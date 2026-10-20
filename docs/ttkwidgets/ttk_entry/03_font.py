# ttk Entry - font

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("font")

ttk.Entry(root, font=("Arial", 18)).pack(pady=40)

root.mainloop()
