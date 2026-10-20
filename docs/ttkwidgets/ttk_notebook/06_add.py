# ttk Notebook - add

import tkinter as tk
from tkinter import ttk


def new_tab():
    number = len(notebook.tabs()) + 1
    page = ttk.Frame(notebook, padding=10)
    notebook.add(page, text=f"Note {number}")
    tk.Text(page, height=4, width=25).pack()
    notebook.select(page)                       # Show the new tab


root = tk.Tk()
root.geometry("320x220")
root.title("add")

ttk.Button(root, text="New tab", command=new_tab).pack(pady=5)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

new_tab()                                       # Start with one tab

root.mainloop()
