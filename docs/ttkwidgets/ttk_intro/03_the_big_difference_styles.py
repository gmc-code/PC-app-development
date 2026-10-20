# ttk widgets and styling - The big difference: styles

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("ttk style")

style = ttk.Style()                                     # 1. Make a Style object
style.theme_use("clam")                                 # 2. Choose a theme (see below)
style.configure("TButton", foreground="white", background="purple",
                font=("Arial", 14))                     # 3. Style every ttk Button

ttk.Button(root, text="One").pack(pady=5)               # No colour options needed
ttk.Button(root, text="Two").pack(pady=5)

root.mainloop()
