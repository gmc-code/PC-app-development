# ttk Notebook - state

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("tab state")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

level_1 = ttk.Frame(notebook)
level_2 = ttk.Frame(notebook)
notebook.add(level_1, text="Level 1")
notebook.add(level_2, text="Level 2 (locked)", state="disabled")

ttk.Label(level_1, text="Finish level 1 to unlock level 2").pack(pady=20)

root.mainloop()
