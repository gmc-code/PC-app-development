# ttk PanedWindow - panes

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("panes")

panes = ttk.PanedWindow(root, orient="horizontal")
panes.pack(fill="both", expand=True)

for colour in ["pink", "lightblue", "lightgreen"]:
    panes.add(tk.Label(panes, text=colour, bg=colour), weight=1)

ttk.Label(root, text=f"Number of panes: {len(panes.panes())}").pack()

root.mainloop()
