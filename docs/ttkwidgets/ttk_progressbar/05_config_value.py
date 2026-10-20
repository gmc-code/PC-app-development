# ttk Progressbar - config(value=...)

import tkinter as tk
from tkinter import ttk


def answer_question():
    if bar["value"] < bar["maximum"]:
        bar["value"] = bar["value"] + 1
        count_label.config(text=f"Questions done: {int(bar['value'])} of 5")


root = tk.Tk()
root.geometry("300x200")
root.title("value")

bar = ttk.Progressbar(root, length=250, maximum=5, value=0)
bar.pack(pady=20)

count_label = ttk.Label(root, text="Questions done: 0 of 5")
count_label.pack()

ttk.Button(root, text="Answer a question", command=answer_question).pack(pady=10)

root.mainloop()
