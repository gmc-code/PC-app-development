# ttk Separator - Tasks Q4

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Blue line")

style = ttk.Style()
style.configure("Blue.TSeparator", background="blue")

ttk.Label(root, text="My Notes", font=("Arial", 16)).pack(pady=10)
ttk.Separator(root, style="Blue.TSeparator").pack(fill="x", padx=20, pady=10)
ttk.Label(root, text="Bring a hat").pack(pady=10)

root.mainloop()
