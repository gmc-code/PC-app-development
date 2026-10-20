# ttk PanedWindow - Tasks Q2

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Panes")

panes = ttk.PanedWindow(root, orient="vertical")
panes.pack(fill="both", expand=True)

panes.add(tk.Label(panes, text="Top", bg="yellow"), weight=1)
panes.add(tk.Label(panes, text="Bottom", bg="orange"), weight=1)

root.mainloop()
