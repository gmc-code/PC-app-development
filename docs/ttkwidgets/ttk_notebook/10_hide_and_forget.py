# ttk Notebook - hide and forget

import tkinter as tk
from tkinter import ttk


def hide_help():
    notebook.hide(help_page)


def show_help():
    notebook.add(help_page)


root = tk.Tk()
root.geometry("300x220")
root.title("hide")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

home_page = ttk.Frame(notebook, padding=10)
help_page = ttk.Frame(notebook, padding=10)
notebook.add(home_page, text="Home")
notebook.add(help_page, text="Help")

ttk.Button(home_page, text="Hide Help tab", command=hide_help).pack(pady=5)
ttk.Button(home_page, text="Show Help tab", command=show_help).pack(pady=5)
ttk.Label(help_page, text="Here is some help.").pack()

root.mainloop()
