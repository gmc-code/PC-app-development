# ttk Spinbox - textvariable

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("textvariable")

players = tk.IntVar(value=4)

ttk.Spinbox(root, from_=1, to=8, textvariable=players).pack(pady=20)
ttk.Label(root, textvariable=players, font=("Arial", 20)).pack()

root.mainloop()
