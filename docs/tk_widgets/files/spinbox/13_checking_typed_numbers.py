# tk Spinbox - Checking typed numbers

import tkinter as tk


def double():
    try:
        number = int(number_spinbox.get())
        result_label.config(text=f"Double: {number * 2}")
    except ValueError:
        result_label.config(text="That is not a number!")


root = tk.Tk()
root.geometry("300x200")
root.title("Checking")

number_spinbox = tk.Spinbox(root, from_=1, to=100, width=6, font=("Arial", 16))
number_spinbox.pack(pady=10)

double_button = tk.Button(root, text="Double it", command=double)
double_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=5)

root.mainloop()
