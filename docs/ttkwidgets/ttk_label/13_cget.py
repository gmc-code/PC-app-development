# ttk Label - cget

import tkinter as tk
from tkinter import ttk


def add_five():
    number = int(score_label.cget("text"))
    score_label.config(text=number + 5)


root = tk.Tk()
root.geometry("300x200")
root.title("cget")

score_label = ttk.Label(root, text="0", font=("Arial", 40))
score_label.pack(pady=10)

ttk.Button(root, text="Add 5", command=add_five).pack()

root.mainloop()
