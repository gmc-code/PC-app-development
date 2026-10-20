# tk Spinbox - Tasks Q4

import tkinter as tk


def times_three():
    number = int(number_spinbox.get())
    answer_label.config(text=f"{number} x 3 = {number * 3}")


root = tk.Tk()
root.geometry("300x200")
root.title("Times 3")

number_spinbox = tk.Spinbox(root, from_=1, to=10, width=5, command=times_three)
number_spinbox.pack(pady=10)

answer_label = tk.Label(root, text="1 x 3 = 3", font=("Arial", 16))
answer_label.pack()

root.mainloop()
