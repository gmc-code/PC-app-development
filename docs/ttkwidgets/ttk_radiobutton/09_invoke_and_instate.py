# ttk Radiobutton - invoke and instate

import tkinter as tk
from tkinter import ttk


def show():
    if large_radio.instate(["selected"]):
        result_label.config(text="Large chosen: $5")
    else:
        result_label.config(text="Small chosen: $3")


root = tk.Tk()
root.geometry("300x200")
root.title("invoke and instate")

size = tk.StringVar(value="none")

small_radio = ttk.Radiobutton(root, text="Small", variable=size, value="Small", command=show)
small_radio.pack()
large_radio = ttk.Radiobutton(root, text="Large", variable=size, value="Large", command=show)
large_radio.pack()

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

small_radio.invoke()            # Choose Small and run show() at the start

root.mainloop()
