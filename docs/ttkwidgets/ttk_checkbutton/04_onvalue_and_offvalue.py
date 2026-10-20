# ttk Checkbutton - onvalue and offvalue

import tkinter as tk
from tkinter import ttk


def show():
    result_label.config(text="Extra cheese: " + extra.get())


root = tk.Tk()
root.geometry("300x200")
root.title("onvalue and offvalue")

extra = tk.StringVar(value="No")

ttk.Checkbutton(root, text="Extra cheese", variable=extra, onvalue="Yes",
                offvalue="No", command=show).pack(pady=20)

result_label = ttk.Label(root, text="Extra cheese: No")
result_label.pack()

root.mainloop()
