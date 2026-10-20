# ttk Separator - Making a Separator

import tkinter as tk            # Load tkinter
from tkinter import ttk         # Load the themed widgets

root = tk.Tk()                  # Make the window
root.geometry("300x200")
root.title("My first Separator")

ttk.Label(root, text="Part 1: Questions", font=("Arial", 14)).pack(pady=10)

line = ttk.Separator(root, orient="horizontal")    # 1. Create it
line.pack(fill="x", padx=20, pady=10)              # 2. Stretch it across the window

ttk.Label(root, text="Part 2: Answers", font=("Arial", 14)).pack(pady=10)

root.mainloop()                 # Keep the window open
