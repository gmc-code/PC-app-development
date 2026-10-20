# ttk Spinbox - get and set

import tkinter as tk
from tkinter import ttk


def calculate():
    pizzas = int(pizza_spinbox.get())
    result_label.config(text=f"{pizzas * 8} slices")


def reset():
    pizza_spinbox.set(1)
    result_label.config(text="")


root = tk.Tk()
root.geometry("300x220")
root.title("get and set")

ttk.Label(root, text="How many pizzas?").pack(pady=5)

pizza_spinbox = ttk.Spinbox(root, from_=1, to=20, width=5)
pizza_spinbox.set(1)
pizza_spinbox.pack()

ttk.Button(root, text="How many slices?", command=calculate).pack(pady=5)
ttk.Button(root, text="Reset", command=reset).pack()

result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=5)

root.mainloop()
