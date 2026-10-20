# ttk Sizegrip - With a status bar

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("350x220")
root.title("Status bar")

status_bar = ttk.Frame(root, relief="sunken", borderwidth=1)
status_bar.pack(side="bottom", fill="x")

ttk.Sizegrip(status_bar).pack(side="right")
ttk.Label(status_bar, text="Ready").pack(side="left", padx=5)

notes_box = tk.Text(root, wrap="word")
notes_box.insert("1.0", "Drag the corner to make this window bigger.")
notes_box.pack(fill="both", expand=True)

root.mainloop()
