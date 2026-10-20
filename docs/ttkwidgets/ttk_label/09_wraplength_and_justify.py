# ttk Label - wraplength and justify

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("wraplength")

ttk.Label(root, text="This sentence is too long for one line, so it wraps onto the next.",
          font=("Arial", 13), wraplength=200, justify="center").pack(pady=30)

root.mainloop()
