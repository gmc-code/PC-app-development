# ttk widgets and styling - instate

import tkinter as tk
from tkinter import ttk


def lock_or_unlock():
    if submit_button.instate(["disabled"]):
        submit_button.state(["!disabled"])      # Turn on
        lock_button.config(text="Lock")
    else:
        submit_button.state(["disabled"])       # Turn off
        lock_button.config(text="Unlock")


root = tk.Tk()
root.geometry("300x200")
root.title("state and instate")

submit_button = ttk.Button(root, text="Submit")
submit_button.pack(pady=20)

lock_button = ttk.Button(root, text="Lock", command=lock_or_unlock)
lock_button.pack()

root.mainloop()
