# tk Entry - get

import tkinter as tk


def say_hello():
    name = name_entry.get()                     # Read the typed name
    answer_label.config(text="Hello " + name)   # Show it on the label


root = tk.Tk()
root.geometry("300x200")
root.title("get")

name_entry = tk.Entry(root, font=("Arial", 16))
name_entry.pack(pady=10)

hello_button = tk.Button(root, text="Say hello", command=say_hello)
hello_button.pack()

answer_label = tk.Label(root, text="", font=("Arial", 16))
answer_label.pack(pady=10)

root.mainloop()
