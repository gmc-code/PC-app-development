# ttk Checkbutton - command

import tkinter as tk
from tkinter import ttk


def update():
    if big.get() == 1:
        word_label.config(font=("Arial", 30))
    else:
        word_label.config(font=("Arial", 12))


root = tk.Tk()
root.geometry("300x200")
root.title("command")

big = tk.IntVar()

ttk.Checkbutton(root, text="Big text", variable=big, command=update).pack(pady=10)

word_label = ttk.Label(root, text="Hello", font=("Arial", 12))
word_label.pack()

root.mainloop()
