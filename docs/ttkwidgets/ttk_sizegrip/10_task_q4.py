# ttk Sizegrip - Tasks Q4

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Resize me")

status_bar = ttk.Frame(root)
status_bar.pack(side="bottom", fill="x")
ttk.Sizegrip(status_bar).pack(side="right")
ttk.Label(status_bar, text="Words: 0").pack(side="left", padx=5)

text_box = tk.Text(root)
text_box.pack(fill="both", expand=True)

root.mainloop()
