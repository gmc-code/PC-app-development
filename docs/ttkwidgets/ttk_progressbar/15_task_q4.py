# ttk Progressbar - Tasks Q4

import tkinter as tk
from tkinter import ttk


def fill():
    if bar["value"] < 100:
        bar["value"] = bar["value"] + 5
        root.after(100, fill)
    else:
        status_label.config(text="Ready!")


root = tk.Tk()
root.geometry("300x200")
root.title("Loading")

bar = ttk.Progressbar(root, length=250)
bar.pack(pady=30)

status_label = ttk.Label(root, text="Loading...", font=("Arial", 16))
status_label.pack()

fill()

root.mainloop()
