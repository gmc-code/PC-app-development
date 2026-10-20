# ttk Notebook - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("My app")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

home_page = ttk.Frame(notebook, padding=10)
games_page = ttk.Frame(notebook, padding=10)
help_page = ttk.Frame(notebook, padding=10)
notebook.add(home_page, text="Home")
notebook.add(games_page, text="Games")
notebook.add(help_page, text="Help")

ttk.Label(home_page, text="Welcome!").pack()
ttk.Label(games_page, text="Pick a game").pack()
ttk.Label(help_page, text="Ask your teacher").pack()

root.mainloop()
