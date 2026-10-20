# ttk Scale - command

import tkinter as tk
from tkinter import ttk


def show_value(value):
    number = int(float(value))          # "42.7" -> 42.7 -> 42
    value_label.config(text=f"Volume: {number}")


root = tk.Tk()
root.geometry("300x200")
root.title("command")

ttk.Scale(root, from_=0, to=100, length=250, command=show_value).pack(pady=20)

value_label = ttk.Label(root, text="Volume: 0", font=("Arial", 16))
value_label.pack()

root.mainloop()
