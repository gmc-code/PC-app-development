# ttk Radiobutton - Tasks Q2

import tkinter as tk
from tkinter import ttk


def show():
    result_label.config(text="You travel by " + transport.get())


root = tk.Tk()
root.geometry("300x200")
root.title("Transport")

transport = tk.StringVar(value="Walk")

for choice in ["Bus", "Car", "Walk"]:
    ttk.Radiobutton(root, text=choice, variable=transport, value=choice).pack()

ttk.Button(root, text="Show", command=show).pack(pady=5)
result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
