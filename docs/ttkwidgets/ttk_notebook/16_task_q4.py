# ttk Notebook - Tasks Q4

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("My app")

style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook.Tab", font=("Arial", 12))
style.map("TNotebook.Tab", background=[("selected", "lightgreen")])

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

for name in ["Home", "Games", "Help"]:
    page = ttk.Frame(notebook, padding=10)
    notebook.add(page, text=name)
    ttk.Label(page, text=f"The {name} page").pack()

root.mainloop()
