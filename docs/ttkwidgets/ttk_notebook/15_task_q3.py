# ttk Notebook - Tasks Q3

import tkinter as tk
from tkinter import ttk


def unlock():
    notebook.tab(bonus_page, state="normal")
    notebook.select(bonus_page)


root = tk.Tk()
root.geometry("320x200")
root.title("My app")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

home_page = ttk.Frame(notebook, padding=10)
games_page = ttk.Frame(notebook, padding=10)
help_page = ttk.Frame(notebook, padding=10)
bonus_page = ttk.Frame(notebook, padding=10)
notebook.add(home_page, text="Home")
notebook.add(games_page, text="Games")
notebook.add(help_page, text="Help")
notebook.add(bonus_page, text="Bonus", state="disabled")

ttk.Label(home_page, text="Welcome!").pack()
ttk.Label(games_page, text="Pick a game").pack()
ttk.Button(games_page, text="Unlock bonus", command=unlock).pack(pady=10)
ttk.Label(help_page, text="Ask your teacher").pack()
ttk.Label(bonus_page, text="You found the bonus!").pack()

root.mainloop()
