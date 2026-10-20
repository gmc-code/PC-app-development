# ttk Entry - justify

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("justify")

for side in ["left", "center", "right"]:
    entry = ttk.Entry(root, justify=side, font=("Arial", 14))
    entry.insert(0, side)
    entry.pack(pady=5)

root.mainloop()
