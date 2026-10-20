# tk Canvas - delete

import tkinter as tk
import random


def add_star():
    x = random.randint(10, 290)
    y = random.randint(10, 190)
    canvas.create_oval(x, y, x + 6, y + 6, fill="white", outline="")


def clear():
    canvas.delete("all")


root = tk.Tk()
root.geometry("320x280")
root.title("delete")

canvas = tk.Canvas(root, width=300, height=200, bg="black")
canvas.pack(pady=5)

tk.Button(root, text="Add a star", command=add_star).pack(side="left", padx=50)
tk.Button(root, text="Clear", command=clear).pack(side="left")

root.mainloop()
