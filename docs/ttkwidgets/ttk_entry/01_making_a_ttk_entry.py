# ttk Entry - Making a ttk Entry

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first ttk Entry")

ttk.Label(root, text="Type your name:").pack(pady=5)

name_entry = ttk.Entry(root)    # 1. Create the entry
name_entry.pack()               # 2. Place it

root.mainloop()                 # Keep the window open
