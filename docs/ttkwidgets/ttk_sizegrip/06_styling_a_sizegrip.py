# ttk Sizegrip - Styling a Sizegrip

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Sizegrip style")

style = ttk.Style()
style.configure("Status.TFrame", background="lightsteelblue")
style.configure("Status.TLabel", background="lightsteelblue")
style.configure("Status.TSizegrip", background="lightsteelblue")

status_bar = ttk.Frame(root, style="Status.TFrame")
status_bar.pack(side="bottom", fill="x")
ttk.Sizegrip(status_bar, style="Status.TSizegrip").pack(side="right")
ttk.Label(status_bar, text="Saved", style="Status.TLabel").pack(side="left", padx=5)

root.mainloop()
