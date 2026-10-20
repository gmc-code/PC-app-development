# ttk Progressbar - Making a Progressbar

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first Progressbar")

bar = ttk.Progressbar(root, length=250, maximum=100, value=40)   # 1. Create it: 40 out of 100
bar.pack(pady=40)                                                # 2. Place it

root.mainloop()                 # Keep the window open
