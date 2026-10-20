# tk Label - Tasks Q4

import tkinter as tk


def add_five():
    number = int(number_label.cget("text"))
    number_label.config(text=number + 5)


root = tk.Tk()
root.geometry("300x200")
root.title("Add 5")

number_label = tk.Label(root, text="0", font=("Arial", 40))
number_label.pack(pady=20)

add_button = tk.Button(root, text="Add 5", command=add_five)
add_button.pack()

root.mainloop()
