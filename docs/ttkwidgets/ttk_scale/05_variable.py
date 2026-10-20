# ttk Scale - variable

import tkinter as tk
from tkinter import ttk


def show(value):
    number_label.config(text=round(rating.get()))


root = tk.Tk()
root.geometry("300x200")
root.title("variable")

rating = tk.DoubleVar(value=5)

ttk.Scale(root, from_=1, to=10, length=250, variable=rating, command=show).pack(pady=20)

number_label = ttk.Label(root, text="5", font=("Arial", 30))
number_label.pack()

root.mainloop()
