# ttk Combobox - Tasks Q4

import tkinter as tk
from tkinter import ttk


def times_seven(event):
    number = int(number_box.get())
    answer_label.config(text=f"{number} x 7 = {number * 7}")


root = tk.Tk()
root.geometry("300x200")
root.title("Times 7")

number_box = ttk.Combobox(root, values=list(range(1, 13)), state="readonly",
                          width=5)
number_box.pack(pady=20)
number_box.bind("<<ComboboxSelected>>", times_seven)

answer_label = ttk.Label(root, text="Pick a number", font=("Arial", 16))
answer_label.pack()

root.mainloop()
