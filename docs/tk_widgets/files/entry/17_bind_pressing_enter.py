# tk Entry - bind (pressing Enter)

import tkinter as tk


def say_hello(event=None):
    answer_label.config(text="Hello " + name_entry.get())


root = tk.Tk()
root.geometry("300x200")
root.title("bind")

name_entry = tk.Entry(root, font=("Arial", 16))
name_entry.pack(pady=10)
name_entry.bind("<Return>", say_hello)      # Press Enter to run say_hello

hello_button = tk.Button(root, text="Say hello", command=say_hello)
hello_button.pack()

answer_label = tk.Label(root, text="", font=("Arial", 16))
answer_label.pack(pady=10)

root.mainloop()
