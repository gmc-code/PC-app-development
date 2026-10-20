# ttk Spinbox - bind (Increment and Decrement)

import tkinter as tk
from tkinter import ttk


def going_up(event):
    result_label.config(text="Up!", foreground="green")


def going_down(event):
    result_label.config(text="Down!", foreground="red")


root = tk.Tk()
root.geometry("300x200")
root.title("bind")

level_spinbox = ttk.Spinbox(root, from_=1, to=10, width=5)
level_spinbox.set(5)
level_spinbox.pack(pady=20)
level_spinbox.bind("<<Increment>>", going_up)
level_spinbox.bind("<<Decrement>>", going_down)

result_label = ttk.Label(root, text="", font=("Arial", 16))
result_label.pack()

root.mainloop()
