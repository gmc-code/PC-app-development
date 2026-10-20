# ttk Radiobutton - Making a group of ttk Radiobuttons

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first ttk Radiobuttons")

drink = tk.StringVar(value="Water")     # 1. One shared variable; "Water" is chosen at the start

ttk.Radiobutton(root, text="Water", variable=drink, value="Water").pack()   # 2. Create
ttk.Radiobutton(root, text="Juice", variable=drink, value="Juice").pack()   #    and place
ttk.Radiobutton(root, text="Milk", variable=drink, value="Milk").pack()

root.mainloop()                 # Keep the window open
