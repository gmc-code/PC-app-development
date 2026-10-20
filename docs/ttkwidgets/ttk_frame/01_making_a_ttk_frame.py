# ttk Frame - Making a ttk Frame

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first ttk Frame")

box = ttk.Frame(root, padding=20, relief="solid", borderwidth=1)   # 1. Create the frame
box.pack(pady=20)                                                  #    and place it

ttk.Label(box, text="I am inside the frame").pack()     # 2. "box", not "root"
ttk.Button(box, text="OK").pack(pady=5)

root.mainloop()                 # Keep the window open
