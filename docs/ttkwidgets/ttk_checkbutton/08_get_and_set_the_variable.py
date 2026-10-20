# ttk Checkbutton - get and set (the variable)

import tkinter as tk
from tkinter import ttk


def tick_all():
    for option in [red, green, blue]:
        option.set(1)


def clear_all():
    for option in [red, green, blue]:
        option.set(0)


root = tk.Tk()
root.geometry("300x220")
root.title("get and set")

red = tk.IntVar()
green = tk.IntVar(value=1)          # Starts ticked
blue = tk.IntVar()

ttk.Checkbutton(root, text="Red", variable=red).pack()
ttk.Checkbutton(root, text="Green", variable=green).pack()
ttk.Checkbutton(root, text="Blue", variable=blue).pack()

ttk.Button(root, text="Tick all", command=tick_all).pack(pady=5)
ttk.Button(root, text="Clear all", command=clear_all).pack()

root.mainloop()
