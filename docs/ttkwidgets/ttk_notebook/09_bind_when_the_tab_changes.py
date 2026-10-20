# ttk Notebook - bind (when the tab changes)

import tkinter as tk
from tkinter import ttk


def tab_changed(event):
    number = notebook.index("current")
    name = notebook.tab(number, "text")
    status_label.config(text=f"You are on the {name} tab (tab number {number})")


root = tk.Tk()
root.geometry("320x200")
root.title("NotebookTabChanged")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

for name in ["Red", "Green", "Blue"]:
    page = ttk.Frame(notebook, padding=10)
    notebook.add(page, text=name)
    ttk.Label(page, text=f"The {name} page").pack()

notebook.bind("<<NotebookTabChanged>>", tab_changed)

status_label = ttk.Label(root, text="")
status_label.pack(pady=5)

root.mainloop()
