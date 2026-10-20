# ttk LabelFrame - width and height

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("width and height")

ttk.LabelFrame(root, text="Coming soon", width=200, height=100).pack(pady=30)

root.mainloop()
