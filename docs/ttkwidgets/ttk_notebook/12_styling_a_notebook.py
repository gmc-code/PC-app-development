# ttk Notebook - Styling a Notebook

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("320x200")
root.title("Notebook style")

style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook", background="lightgray")
style.configure("TNotebook.Tab", font=("Arial", 12), padding=(15, 5), background="silver")
style.map("TNotebook.Tab", background=[("selected", "gold")],
          foreground=[("selected", "black")])

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

for name in ["Maths", "Science", "English"]:
    page = ttk.Frame(notebook, padding=10)
    notebook.add(page, text=name)
    ttk.Label(page, text=f"{name} homework").pack()

root.mainloop()
