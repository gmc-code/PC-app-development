# ttk LabelFrame - Making a ttk LabelFrame

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first ttk LabelFrame")

details = ttk.LabelFrame(root, text="Your details", padding=10)   # 1. Create it
details.pack(pady=20)                                             # 2. Place it

ttk.Label(details, text="Name:").pack()          # 3. Widgets go in "details"
ttk.Entry(details).pack()

root.mainloop()                 # Keep the window open
