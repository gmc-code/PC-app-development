# tk LabelFrame - cget

import tkinter as tk


def show_title():
    result_label.config(text="This box is called: " + box.cget("text"))


root = tk.Tk()
root.geometry("300x200")
root.title("cget")

box = tk.LabelFrame(root, text="Mystery box", padx=20, pady=10)
box.pack(pady=10)
tk.Button(box, text="What is my title?", command=show_title).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
