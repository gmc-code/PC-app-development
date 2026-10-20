# ttk Notebook - Making a Notebook

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first Notebook")

notebook = ttk.Notebook(root)                   # 1. Create the Notebook
notebook.pack(fill="both", expand=True)

home_page = ttk.Frame(notebook, padding=10)     # 2. A Frame for each page
help_page = ttk.Frame(notebook, padding=10)

notebook.add(home_page, text="Home")            # 3. Add them as tabs
notebook.add(help_page, text="Help")

ttk.Label(home_page, text="Welcome to the app!").pack()             # 4. Widgets on each page
ttk.Label(help_page, text="Click the tabs to change page.").pack()

root.mainloop()                 # Keep the window open
