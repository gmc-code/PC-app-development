# tk Label - cget

import tkinter as tk


def add_one():
    number = int(label.cget("text"))    # Read the label and turn it into a number
    label.config(text=number + 1)       # Show the new number


root = tk.Tk()
root.geometry("300x200")
root.title("cget")

label = tk.Label(root, text="0", font=("Arial", 40))
label.pack(pady=20)

button = tk.Button(root, text="Add 1", command=add_one)
button.pack()

root.mainloop()
