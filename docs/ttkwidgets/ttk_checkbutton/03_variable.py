# ttk Checkbutton - variable

import tkinter as tk
from tkinter import ttk


def check():
    if homework.get() == 1:
        result_label.config(text="Well done!")
    else:
        result_label.config(text="Better get started...")


root = tk.Tk()
root.geometry("300x200")
root.title("variable")

homework = tk.IntVar()

ttk.Checkbutton(root, text="Homework done", variable=homework).pack(pady=10)
ttk.Button(root, text="Check", command=check).pack()

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
