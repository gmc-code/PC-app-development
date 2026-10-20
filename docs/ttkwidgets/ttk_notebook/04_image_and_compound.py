# ttk Notebook - image and compound

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("image")

picture = tk.PhotoImage(file="logo.png")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

home_page = ttk.Frame(notebook)
notebook.add(home_page, text="Home", image=picture, compound="left")
ttk.Label(home_page, text="A tab with a picture").pack(pady=20)

root.mainloop()
