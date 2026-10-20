# ttk Sizegrip - Making a Sizegrip

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first Sizegrip")

grip = ttk.Sizegrip(root)                       # 1. Create it
grip.pack(side="bottom", anchor="se")           # 2. Bottom-right corner

ttk.Label(root, text="Drag the bottom-right corner", font=("Arial", 12)).pack(pady=60)

root.mainloop()                 # Keep the window open
