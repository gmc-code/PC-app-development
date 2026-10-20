# ttk Spinbox - Making a ttk Spinbox

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first ttk Spinbox")

tickets_spinbox = ttk.Spinbox(root, from_=1, to=10)    # 1. Create it
tickets_spinbox.set(1)                                 #    and choose the starting value
tickets_spinbox.pack(pady=30)                          # 2. Place it

root.mainloop()                 # Keep the window open
