# ttk Frame - Tasks Q2

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Frames")

row = ttk.Frame(root)
row.pack(pady=20)
for colour in ["Red", "Green", "Blue"]:
    ttk.Button(row, text=colour).pack(side="left", padx=5)

root.mainloop()
