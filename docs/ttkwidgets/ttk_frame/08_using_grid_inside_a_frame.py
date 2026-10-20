# ttk Frame - Using grid inside a frame

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("grid in a frame")

ttk.Label(root, text="Sign up", font=("Arial", 16)).pack(pady=10)

form = ttk.Frame(root, padding=10)
form.pack()

ttk.Label(form, text="Name:").grid(row=0, column=0, sticky="e", pady=2)
ttk.Entry(form).grid(row=0, column=1, pady=2)
ttk.Label(form, text="Email:").grid(row=1, column=0, sticky="e", pady=2)
ttk.Entry(form).grid(row=1, column=1, pady=2)

root.mainloop()
