# ttk Button - invoke

import tkinter as tk
from tkinter import ttk


def greet():
    result_label.config(text="Hello!")


root = tk.Tk()
root.geometry("300x200")
root.title("invoke")

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(pady=20)

result_label = ttk.Label(root, text="Press Enter or click")
result_label.pack()

root.bind("<Return>", lambda event: greet_button.invoke())

root.mainloop()
