# ttk LabelFrame - A form with grid

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Form")

form = ttk.LabelFrame(root, text="Sign up", padding=10)
form.pack(pady=20)

ttk.Label(form, text="Name:").grid(row=0, column=0, sticky="e", pady=2)
ttk.Entry(form).grid(row=0, column=1, pady=2)
ttk.Label(form, text="Email:").grid(row=1, column=0, sticky="e", pady=2)
ttk.Entry(form).grid(row=1, column=1, pady=2)

root.mainloop()
