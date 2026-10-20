# ttk Label - anchor

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("anchor")

for position in ["w", "center", "e"]:
    ttk.Label(root, text=position, width=30, anchor=position,
              background="lightyellow").pack(pady=5)

root.mainloop()
