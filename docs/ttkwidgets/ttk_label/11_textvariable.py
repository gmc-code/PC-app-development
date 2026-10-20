# ttk Label - textvariable

import tkinter as tk
from tkinter import ttk


def win():
    message.set("You win!")


root = tk.Tk()
root.geometry("300x200")
root.title("textvariable")

message = tk.StringVar(value="Click Play")

ttk.Label(root, textvariable=message, font=("Arial", 18)).pack(pady=20)
ttk.Button(root, text="Play", command=win).pack()

root.mainloop()
