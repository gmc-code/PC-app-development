# ttk Label - Making a ttk Label

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first ttk Label")

hello_label = ttk.Label(root, text="Hello, world!")    # 1. Create the label
hello_label.pack(pady=20)                             # 2. Place it

root.mainloop()                 # Keep the window open
