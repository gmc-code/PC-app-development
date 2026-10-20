# ttk PanedWindow - Panes inside panes

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x250")
root.title("Panes inside panes")

outer = ttk.PanedWindow(root, orient="horizontal")
outer.pack(fill="both", expand=True)

outer.add(tk.Label(outer, text="Files", bg="lightblue", width=12))

inner = ttk.PanedWindow(outer, orient="vertical")      # Inside "outer"
outer.add(inner, weight=1)

inner.add(tk.Label(inner, text="Code", bg="white"), weight=3)
inner.add(tk.Label(inner, text="Output", bg="black", fg="white"), weight=1)

root.mainloop()
