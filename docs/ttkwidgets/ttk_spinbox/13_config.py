# ttk Spinbox - config

import tkinter as tk
from tkinter import ttk


def adults_only():
    age_spinbox.config(from_=18, to=100)
    age_spinbox.set(18)


root = tk.Tk()
root.geometry("300x200")
root.title("config")

age_spinbox = ttk.Spinbox(root, from_=0, to=100, width=5)
age_spinbox.set(0)
age_spinbox.pack(pady=20)

ttk.Button(root, text="Adults only", command=adults_only).pack()

root.mainloop()
