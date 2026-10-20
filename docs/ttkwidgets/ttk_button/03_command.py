# ttk Button - command

import tkinter as tk
from tkinter import ttk


def add_one():
    number = int(count_label.cget("text"))
    count_label.config(text=number + 1)


root = tk.Tk()
root.geometry("300x200")
root.title("command")

count_label = ttk.Label(root, text="0", font=("Arial", 36))
count_label.pack(pady=10)

add_button = ttk.Button(root, text="Add 1", command=add_one)
add_button.pack()

root.mainloop()
