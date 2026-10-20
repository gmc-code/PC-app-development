# ttk Spinbox - Tasks Q4

import tkinter as tk
from tkinter import ttk


def times_three():
    number = int(number_spinbox.get())
    answer_label.config(text=f"{number} x 3 = {number * 3}")


root = tk.Tk()
root.geometry("300x200")
root.title("Times 3")

number_spinbox = ttk.Spinbox(root, from_=1, to=10, width=5, command=times_three)
number_spinbox.set(1)
number_spinbox.pack(pady=20)

answer_label = ttk.Label(root, text="1 x 3 = 3", font=("Arial", 16))
answer_label.pack()

root.mainloop()
