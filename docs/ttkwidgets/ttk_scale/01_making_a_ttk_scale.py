# ttk Scale - Making a ttk Scale

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first ttk Scale")

volume_scale = ttk.Scale(root, from_=0, to=100, length=250)    # 1. Create it
volume_scale.pack(pady=40)                                     # 2. Place it

root.mainloop()                 # Keep the window open
