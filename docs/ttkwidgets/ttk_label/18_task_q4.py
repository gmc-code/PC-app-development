# ttk Label - Tasks Q4

import tkinter as tk
from tkinter import ttk


def double():
    number = int(number_label.cget("text"))
    number_label.config(text=number * 2)


root = tk.Tk()
root.geometry("300x200")
root.title("Double")

number_label = ttk.Label(root, text="1", font=("Arial", 36))
number_label.pack(pady=10)

ttk.Button(root, text="Double", command=double).pack()

root.mainloop()
