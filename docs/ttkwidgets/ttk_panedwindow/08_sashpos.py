# ttk PanedWindow - sashpos

import tkinter as tk
from tkinter import ttk


def half():
    width = panes.winfo_width()
    panes.sashpos(0, width // 2)        # Move the sash to the middle


root = tk.Tk()
root.geometry("400x220")
root.title("sashpos")

panes = ttk.PanedWindow(root, orient="horizontal")
panes.pack(fill="both", expand=True)

panes.add(tk.Label(panes, text="Left", bg="lightblue", width=8))
panes.add(tk.Label(panes, text="Right", bg="lightgreen"), weight=1)

ttk.Button(root, text="Split in half", command=half).pack(pady=5)

root.mainloop()
