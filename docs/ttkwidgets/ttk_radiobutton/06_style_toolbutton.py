# ttk Radiobutton - style="Toolbutton"

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Toolbutton")

level = tk.StringVar(value="Easy")

row = ttk.Frame(root)
row.pack(pady=40)
for choice in ["Easy", "Medium", "Hard"]:
    ttk.Radiobutton(row, text=choice, variable=level, value=choice,
                    style="Toolbutton", width=8).pack(side="left", padx=2)

root.mainloop()
