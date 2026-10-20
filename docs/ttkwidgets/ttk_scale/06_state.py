# ttk Scale - state

import tkinter as tk
from tkinter import ttk


def lock():
    speed_scale.state(["disabled"])


root = tk.Tk()
root.geometry("300x200")
root.title("state")

speed_scale = ttk.Scale(root, from_=0, to=100, length=250)
speed_scale.pack(pady=20)

ttk.Button(root, text="Lock", command=lock).pack()

root.mainloop()
