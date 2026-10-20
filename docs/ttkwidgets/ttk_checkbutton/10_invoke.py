# ttk Checkbutton - invoke

import tkinter as tk
from tkinter import ttk


def show():
    result_label.config(text=f"Dark mode: {dark.get()}")


root = tk.Tk()
root.geometry("300x200")
root.title("invoke")

dark = tk.IntVar()

dark_check = ttk.Checkbutton(root, text="Dark mode", variable=dark, command=show)
dark_check.pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack()

dark_check.invoke()             # Tick it and run show() at the start

root.mainloop()
