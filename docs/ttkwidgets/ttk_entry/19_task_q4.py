# ttk Entry - Tasks Q4

import tkinter as tk
from tkinter import ttk


def log_in():
    welcome_label.config(text="Welcome " + user_entry.get())


root = tk.Tk()
root.geometry("300x250")
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

ttk.Button(root, text="Log in", command=log_in).pack(pady=10)

welcome_label = ttk.Label(root, text="")
welcome_label.pack()

root.mainloop()
