# ttk Button - Sending a value with lambda

import tkinter as tk
from tkinter import ttk


def change_colour(colour):
    root.config(bg=colour)


root = tk.Tk()
root.geometry("300x200")
root.title("lambda")

ttk.Button(root, text="Red", command=lambda: change_colour("red")).pack(pady=5)
ttk.Button(root, text="Green", command=lambda: change_colour("green")).pack(pady=5)
ttk.Button(root, text="Blue", command=lambda: change_colour("blue")).pack(pady=5)

root.mainloop()
