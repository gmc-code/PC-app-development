# ttk Entry - get

import tkinter as tk
from tkinter import ttk


def say_hello():
    answer_label.config(text="Hello " + name_entry.get())


root = tk.Tk()
root.geometry("300x200")
root.title("get")

name_entry = ttk.Entry(root, font=("Arial", 14))
name_entry.pack(pady=10)

ttk.Button(root, text="Say hello", command=say_hello).pack()

answer_label = ttk.Label(root, text="", font=("Arial", 14))
answer_label.pack(pady=10)

root.mainloop()
