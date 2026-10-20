# ttk Separator - Side-by-side sections

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("320x200")
root.title("Two sections")

left = ttk.Frame(root, padding=10)
left.pack(side="left", fill="both", expand=True)
ttk.Label(left, text="Player 1", font=("Arial", 14)).pack()
ttk.Label(left, text="Score: 0").pack()

ttk.Separator(root, orient="vertical").pack(side="left", fill="y", pady=10)

right = ttk.Frame(root, padding=10)
right.pack(side="left", fill="both", expand=True)
ttk.Label(right, text="Player 2", font=("Arial", 14)).pack()
ttk.Label(right, text="Score: 0").pack()

root.mainloop()
