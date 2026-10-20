# ttk Entry - focus_set and select_range

import tkinter as tk
from tkinter import ttk


def check():
    if answer_entry.get() == "9":
        result_label.config(text="Correct!", foreground="green")
    else:
        result_label.config(text="Try again", foreground="red")
        answer_entry.focus_set()
        answer_entry.select_range(0, tk.END)


root = tk.Tk()
root.geometry("300x200")
root.title("focus_set")

ttk.Label(root, text="What is 3 x 3?", font=("Arial", 14)).pack(pady=5)

answer_entry = ttk.Entry(root, width=5, font=("Arial", 14))
answer_entry.pack()
answer_entry.focus_set()

ttk.Button(root, text="Check", command=check).pack(pady=5)

result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
