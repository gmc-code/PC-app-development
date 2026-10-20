# tk Entry - Getting a number

import tkinter as tk


def double_it():
    try:
        number = float(number_entry.get())          # Text -> number
        answer_label.config(text=number * 2)
    except ValueError:
        answer_label.config(text="Please type a number")


root = tk.Tk()
root.geometry("300x200")
root.title("Getting a number")

number_entry = tk.Entry(root, font=("Arial", 16), width=10)
number_entry.pack(pady=10)

double_button = tk.Button(root, text="Double it", command=double_it)
double_button.pack()

answer_label = tk.Label(root, text="", font=("Arial", 16))
answer_label.pack(pady=10)

root.mainloop()
