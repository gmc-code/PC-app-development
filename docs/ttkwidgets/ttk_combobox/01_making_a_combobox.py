# ttk Combobox - Making a Combobox

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first Combobox")

fruit_box = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"])   # 1. Create it
fruit_box.set("Apple")                                                 # 2. Starting item
fruit_box.pack(pady=30)                                                # 3. Place it

root.mainloop()                 # Keep the window open
