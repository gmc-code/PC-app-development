# ttk Checkbutton - Making a ttk Checkbutton

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first ttk Checkbutton")

cheese = tk.IntVar()            # 1. Variable: 1 = ticked, 0 = not ticked

cheese_check = ttk.Checkbutton(root, text="Cheese", variable=cheese)   # 2. Create it
cheese_check.pack(pady=20)      # 3. Place it

root.mainloop()                 # Keep the window open
