# tk Scale - Tasks Q4

import tkinter as tk


def times_table():
    number = number_scale.get()
    answer_label.config(text=f"{number} x 7 = {number * 7}")


root = tk.Tk()
root.geometry("300x200")
root.title("Times table")

number_scale = tk.Scale(root, from_=1, to=12, orient="horizontal", length=250)
number_scale.pack()

table_button = tk.Button(root, text="Times table", command=times_table)
table_button.pack(pady=5)

answer_label = tk.Label(root, text="", font=("Arial", 14))
answer_label.pack()

root.mainloop()
