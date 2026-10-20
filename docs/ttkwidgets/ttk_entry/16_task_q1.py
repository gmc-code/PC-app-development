# ttk Entry - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Login")

ttk.Label(root, text="Username:").pack()
user_entry = ttk.Entry(root, font=("Arial", 14))
user_entry.pack()

root.mainloop()
