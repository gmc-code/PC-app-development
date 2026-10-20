# ttk PanedWindow - add

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x200")
root.title("add")

panes = ttk.PanedWindow(root, orient="horizontal")
panes.pack(fill="both", expand=True)

menu_frame = ttk.Frame(panes, padding=10)
ttk.Button(menu_frame, text="Planets").pack(pady=3)
ttk.Button(menu_frame, text="Stars").pack(pady=3)
panes.add(menu_frame)

notes_box = tk.Text(panes, wrap="word")
notes_box.insert("1.0", "Type your notes here")
panes.add(notes_box)

root.mainloop()
