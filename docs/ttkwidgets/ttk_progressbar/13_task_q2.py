# ttk Progressbar - Tasks Q2

import tkinter as tk
from tkinter import ttk


def next_step():
    if bar["value"] < 5:
        bar["value"] = bar["value"] + 1
        value_label.config(text=f"{int(bar['value'])} of 5")


root = tk.Tk()
root.geometry("300x200")
root.title("Progress")

bar = ttk.Progressbar(root, length=250, maximum=5, value=3)
bar.pack(pady=20)

value_label = ttk.Label(root, text="3 of 5")
value_label.pack()

ttk.Button(root, text="Next", command=next_step).pack(pady=10)

root.mainloop()
