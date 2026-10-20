# ttk Entry - Getting a number

import tkinter as tk
from tkinter import ttk


def convert():
    try:
        cm = float(cm_entry.get())
        answer_label.config(text=f"{cm} cm = {cm / 100} m")
    except ValueError:
        answer_label.config(text="Please type a number")


root = tk.Tk()
root.geometry("300x200")
root.title("cm to m")

cm_entry = ttk.Entry(root, width=10, font=("Arial", 14))
cm_entry.pack(pady=10)

ttk.Button(root, text="Convert", command=convert).pack()

answer_label = ttk.Label(root, text="", font=("Arial", 14))
answer_label.pack(pady=10)

root.mainloop()
