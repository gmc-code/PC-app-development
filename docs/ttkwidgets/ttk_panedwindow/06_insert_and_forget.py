# ttk PanedWindow - insert and forget

import tkinter as tk
from tkinter import ttk


def hide_help():
    try:
        panes.forget(help_label)
    except tk.TclError:
        pass                            # Already hidden, so do nothing


def show_help():
    panes.insert(0, help_label)       # Put it back as the first pane


root = tk.Tk()
root.geometry("400x250")
root.title("insert and forget")

panes = ttk.PanedWindow(root, orient="horizontal")
panes.pack(fill="both", expand=True)

help_label = tk.Label(panes, text="Help:\nUse the arrows", bg="lightyellow", width=15)
game_label = tk.Label(panes, text="Game area", bg="white")
panes.add(help_label)
panes.add(game_label, weight=1)

ttk.Button(root, text="Hide help", command=hide_help).pack(side="left", padx=40, pady=5)
ttk.Button(root, text="Show help", command=show_help).pack(side="left")

root.mainloop()
