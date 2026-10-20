# tk Checkbutton - Tasks Q4

import tkinter as tk


def change_size():
    if big.get() == 1:
        word_label.config(font=("Arial", 30))
    else:
        word_label.config(font=("Arial", 12))


root = tk.Tk()
root.geometry("300x200")
root.title("Big text")

big = tk.IntVar()

big_check = tk.Checkbutton(root, text="Big text", variable=big, command=change_size)
big_check.pack(pady=10)

word_label = tk.Label(root, text="Hello", font=("Arial", 12))
word_label.pack()

root.mainloop()
