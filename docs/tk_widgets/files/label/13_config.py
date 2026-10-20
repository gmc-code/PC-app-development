# tk Label - config

import tkinter as tk


def change():
    label.config(text="Changed!", fg="white", bg="green")


root = tk.Tk()
root.geometry("300x200")
root.title("config")

label = tk.Label(root, text="Not changed yet", font=("Arial", 18), bg="lightgray")
label.pack(pady=20)

button = tk.Button(root, text="Change the label", command=change)
button.pack()

root.mainloop()
