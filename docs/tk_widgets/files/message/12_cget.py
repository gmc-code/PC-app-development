# tk Message - cget

import tkinter as tk


def count_words():
    words = info.cget("text").split()
    count_label.config(text=f"That message has {len(words)} words")


root = tk.Tk()
root.geometry("300x200")
root.title("cget")

info = tk.Message(root, text="Plants make their own food using sunlight, water and air.",
                  width=250)
info.pack(pady=10)

tk.Button(root, text="Count words", command=count_words).pack()

count_label = tk.Label(root, text="")
count_label.pack(pady=5)

root.mainloop()
