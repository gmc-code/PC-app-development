# ttk PanedWindow - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Panes")

panes = ttk.PanedWindow(root, orient="horizontal")
panes.pack(fill="both", expand=True)

panes.add(tk.Label(panes, text="Left", bg="yellow"), weight=1)
panes.add(tk.Label(panes, text="Right", bg="orange"), weight=1)

root.mainloop()
