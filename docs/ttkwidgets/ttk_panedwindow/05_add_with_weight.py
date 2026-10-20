# ttk PanedWindow - add with weight

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x200")
root.title("weight")

panes = ttk.PanedWindow(root, orient="horizontal")
panes.pack(fill="both", expand=True)

panes.add(tk.Label(panes, text="Menu\n(weight 0)", bg="lightblue", width=12), weight=0)
panes.add(tk.Label(panes, text="Main area\n(weight 1)", bg="white"), weight=1)

root.mainloop()
