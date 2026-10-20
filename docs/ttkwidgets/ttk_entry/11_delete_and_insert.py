# ttk Entry - delete and insert

import tkinter as tk
from tkinter import ttk


def clear():
    word_entry.delete(0, tk.END)


def reset():
    word_entry.delete(0, tk.END)
    word_entry.insert(0, "Type here")


root = tk.Tk()
root.geometry("300x200")
root.title("delete and insert")

word_entry = ttk.Entry(root, font=("Arial", 14))
word_entry.insert(0, "Type here")
word_entry.pack(pady=10)

ttk.Button(root, text="Clear", command=clear).pack(pady=2)
ttk.Button(root, text="Reset", command=reset).pack(pady=2)

root.mainloop()
