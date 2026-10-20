# ttk Entry - Tasks Q3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Login")

style = ttk.Style()
style.theme_use("clam")
style.configure("TEntry", fieldbackground="lightblue")

ttk.Label(root, text="Username:").pack()
user_entry = ttk.Entry(root, font=("Arial", 14))
user_entry.pack()

ttk.Label(root, text="Password:").pack()
password_entry = ttk.Entry(root, font=("Arial", 14), show="*")
password_entry.pack()

root.mainloop()
