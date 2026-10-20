# ttk Entry - textvariable

import tkinter as tk
from tkinter import ttk


def shout():
    word.set(word.get().upper())


root = tk.Tk()
root.geometry("300x200")
root.title("textvariable")

word = tk.StringVar(value="hello")

ttk.Entry(root, textvariable=word, font=("Arial", 16)).pack(pady=20)
ttk.Button(root, text="SHOUT", command=shout).pack()

root.mainloop()
