# ttk Entry - Changing colour for a wrong answer

import tkinter as tk
from tkinter import ttk


def check():
    if answer_entry.get().lower() == "canberra":
        answer_entry.config(style="Right.TEntry")
    else:
        answer_entry.config(style="Wrong.TEntry")


root = tk.Tk()
root.geometry("300x200")
root.title("Right or wrong")

style = ttk.Style()
style.theme_use("clam")
style.configure("Right.TEntry", fieldbackground="lightgreen")
style.configure("Wrong.TEntry", fieldbackground="pink")

ttk.Label(root, text="Capital of Australia?").pack(pady=5)

answer_entry = ttk.Entry(root, font=("Arial", 14))
answer_entry.pack()

ttk.Button(root, text="Check", command=check).pack(pady=10)

root.mainloop()
