# ttk Notebook - select

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("select")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

start_page = ttk.Frame(notebook, padding=10)
game_page = ttk.Frame(notebook, padding=10)
notebook.add(start_page, text="Start")
notebook.add(game_page, text="Game")

ttk.Label(start_page, text="Ready to play?").pack()
ttk.Button(start_page, text="Play", command=lambda: notebook.select(game_page)).pack(pady=10)

ttk.Label(game_page, text="Game started!", font=("Arial", 18)).pack()
ttk.Button(game_page, text="Back", command=lambda: notebook.select(0)).pack(pady=10)

root.mainloop()
