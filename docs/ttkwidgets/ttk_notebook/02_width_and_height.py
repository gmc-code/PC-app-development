# ttk Notebook - width and height

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x220")
root.title("width and height")

notebook = ttk.Notebook(root, width=250, height=120)
notebook.pack(pady=20)

for name in ["One", "Two", "Three"]:
    page = ttk.Frame(notebook)
    notebook.add(page, text=name)
    ttk.Label(page, text=f"This is page {name}").pack(pady=20)

root.mainloop()
