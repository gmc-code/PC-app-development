# ttk PanedWindow - width and height

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("width and height")

panes = ttk.PanedWindow(root, orient="horizontal", width=250, height=120)
panes.pack(pady=30)

panes.add(tk.Label(panes, text="Left", bg="lightblue"))
panes.add(tk.Label(panes, text="Right", bg="lightgreen"))

root.mainloop()
