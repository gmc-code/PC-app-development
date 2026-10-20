# ttk Separator - Tasks Q2

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Sections")

ttk.Label(root, text="My Notes", font=("Arial", 16)).pack(pady=10)
ttk.Separator(root).pack(fill="x", padx=20, pady=10)
ttk.Label(root, text="Bring a hat").pack(pady=10)

root.mainloop()
