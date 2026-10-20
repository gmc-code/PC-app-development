# ttk Entry - foreground

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("foreground")

ttk.Entry(root, font=("Arial", 16), foreground="blue").pack(pady=40)

root.mainloop()
