# ttk Radiobutton - get and set (the variable)

import tkinter as tk
from tkinter import ttk


def reset():
    drink.set("none")           # Matches no button, so nothing is chosen


root = tk.Tk()
root.geometry("300x200")
root.title("get and set")

drink = tk.StringVar(value="Juice")

for choice in ["Water", "Juice", "Milk"]:
    ttk.Radiobutton(root, text=choice, variable=drink, value=choice).pack()

ttk.Button(root, text="Reset", command=reset).pack(pady=10)

root.mainloop()
