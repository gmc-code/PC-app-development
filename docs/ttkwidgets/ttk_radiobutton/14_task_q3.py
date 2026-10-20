# ttk Radiobutton - Tasks Q3

import tkinter as tk
from tkinter import ttk


def check():
    if answer.get() == 20:
        result_label.config(text="Correct!", foreground="green")
    else:
        result_label.config(text="Try again", foreground="red")


root = tk.Tk()
root.geometry("300x200")
root.title("Quiz")

ttk.Label(root, text="What is 4 x 5?", font=("Arial", 14)).pack()

answer = tk.IntVar(value=0)
for number in [15, 20, 25]:
    ttk.Radiobutton(root, text=number, variable=answer, value=number,
                    command=check).pack()

result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
