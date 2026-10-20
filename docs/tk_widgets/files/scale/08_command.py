# tk Scale - command

import tkinter as tk


def show_size(value):
    size = int(value)                           # Text -> number
    word_label.config(font=("Arial", size))


root = tk.Tk()
root.geometry("300x250")
root.title("command")

size_scale = tk.Scale(root, from_=8, to=40, orient="horizontal", length=200,
                      label="Text size", command=show_size)
size_scale.pack()

word_label = tk.Label(root, text="Hello", font=("Arial", 8))
word_label.pack(pady=10)

root.mainloop()
