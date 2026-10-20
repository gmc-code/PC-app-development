# tk Entry - textvariable

import tkinter as tk


def make_capitals():
    word.set(word.get().upper())    # Read the word, make it CAPITALS, put it back


root = tk.Tk()
root.geometry("300x200")
root.title("textvariable")

word = tk.StringVar(value="hello")

entry = tk.Entry(root, textvariable=word, font=("Arial", 16))
entry.pack(pady=20)

button = tk.Button(root, text="CAPITALS", command=make_capitals)
button.pack()

root.mainloop()
