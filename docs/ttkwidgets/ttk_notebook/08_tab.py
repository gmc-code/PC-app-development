# ttk Notebook - tab

import tkinter as tk
from tkinter import ttk


def unlock():
    notebook.tab(1, state="normal", text="Level 2")
    notebook.select(1)


root = tk.Tk()
root.geometry("300x200")
root.title("tab")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

level_1 = ttk.Frame(notebook, padding=10)
level_2 = ttk.Frame(notebook, padding=10)
notebook.add(level_1, text="Level 1")
notebook.add(level_2, text="Level 2 (locked)", state="disabled")

ttk.Button(level_1, text="Finish level 1", command=unlock).pack(pady=20)
ttk.Label(level_2, text="Welcome to level 2!", font=("Arial", 16)).pack(pady=20)

root.mainloop()
