# tk Button - Tasks Q5

import tkinter as tk


def set_size(size):
    word_label.config(font=("Arial", size))


root = tk.Tk()
root.geometry("300x250")
root.title("Sizes")

small_button = tk.Button(root, text="Small", width=10, command=lambda: set_size(10))
small_button.pack(pady=2)

medium_button = tk.Button(root, text="Medium", width=10, command=lambda: set_size(20))
medium_button.pack(pady=2)

large_button = tk.Button(root, text="Large", width=10, command=lambda: set_size(30))
large_button.pack(pady=2)

word_label = tk.Label(root, text="Hello", font=("Arial", 20))
word_label.pack(pady=10)

root.mainloop()
