# ttk Entry - width

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("width")

ttk.Entry(root, width=5).pack(pady=10)
ttk.Entry(root, width=40).pack(pady=10)

root.mainloop()
