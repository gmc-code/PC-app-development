# ttk Scrollbar - Tasks Q2

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Long line")

scrollbar = ttk.Scrollbar(root, orient="horizontal")
scrollbar.pack(side="bottom", fill="x")

long_text = tk.Text(root, wrap="none", xscrollcommand=scrollbar.set)
long_text.pack(fill="both", expand=True)
scrollbar.config(command=long_text.xview)

long_text.insert("1.0", "This is a very very long line of text " * 6)

root.mainloop()
