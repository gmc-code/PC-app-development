# ttk Scale - config

import tkinter as tk
from tkinter import ttk


def hard_mode():
    level_scale.config(to=20)
    info_label.config(text="Levels 1 to 20")


root = tk.Tk()
root.geometry("300x200")
root.title("config")

level_scale = ttk.Scale(root, from_=1, to=10, length=250)
level_scale.pack(pady=20)

info_label = ttk.Label(root, text="Levels 1 to 10")
info_label.pack()

ttk.Button(root, text="Hard mode", command=hard_mode).pack(pady=10)

root.mainloop()
