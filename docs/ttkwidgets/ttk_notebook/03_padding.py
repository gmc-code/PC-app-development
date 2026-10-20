# ttk Notebook - padding

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("padding")

notebook = ttk.Notebook(root, padding=10)
notebook.pack(fill="both", expand=True)

page = ttk.Frame(notebook)
notebook.add(page, text="Padded")
ttk.Label(page, text="There is space around this page").pack(pady=20)

root.mainloop()
