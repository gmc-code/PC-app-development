# ttk Radiobutton - command

import tkinter as tk
from tkinter import ttk


def change_colour():
    root.config(bg=colour.get())


root = tk.Tk()
root.geometry("300x200")
root.title("command")

colour = tk.StringVar(value="white")

for name in ["white", "pink", "lightblue", "lightgreen"]:
    ttk.Radiobutton(root, text=name, variable=colour, value=name,
                    command=change_colour).pack(pady=2)

root.mainloop()
