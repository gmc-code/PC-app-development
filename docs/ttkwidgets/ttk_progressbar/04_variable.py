# ttk Progressbar - variable

import tkinter as tk
from tkinter import ttk


def take_damage():
    health.set(max(health.get() - 10, 0))       # Go down 10, but not below 0


def heal():
    health.set(100)


root = tk.Tk()
root.geometry("300x200")
root.title("variable")

health = tk.IntVar(value=100)

ttk.Label(root, text="Health").pack(pady=5)
ttk.Progressbar(root, length=250, variable=health).pack()
ttk.Label(root, textvariable=health, font=("Arial", 16)).pack()

ttk.Button(root, text="Take damage", command=take_damage).pack(pady=2)
ttk.Button(root, text="Heal", command=heal).pack()

root.mainloop()
