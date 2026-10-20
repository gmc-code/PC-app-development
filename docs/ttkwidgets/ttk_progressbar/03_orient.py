# ttk Progressbar - orient

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("orient")

for level in [20, 50, 80]:
    ttk.Progressbar(root, orient="vertical", length=150, value=level).pack(side="left", padx=30)

root.mainloop()
