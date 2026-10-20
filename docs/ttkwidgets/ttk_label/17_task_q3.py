# ttk Label - Tasks Q3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Heading")

style = ttk.Style()
style.configure("Heading.TLabel", font=("Arial", 20, "bold"), foreground="darkgreen")

ttk.Label(root, text="Science", style="Heading.TLabel").pack(pady=10)
ttk.Label(root, text="Chapter 1: Cells").pack()

root.mainloop()
