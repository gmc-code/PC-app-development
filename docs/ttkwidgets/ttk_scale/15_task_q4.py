# ttk Scale - Tasks Q4

import tkinter as tk
from tkinter import ttk


def times_table():
    number = round(number_scale.get())
    answer_label.config(text=f"{number} x 9 = {number * 9}")


root = tk.Tk()
root.geometry("300x200")
root.title("Times table")

number_scale = ttk.Scale(root, from_=1, to=12, length=250)
number_scale.pack(pady=20)

ttk.Button(root, text="Times table", command=times_table).pack()

answer_label = ttk.Label(root, text="", font=("Arial", 16))
answer_label.pack(pady=10)

root.mainloop()
