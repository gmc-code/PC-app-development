# tk Label - textvariable

import tkinter as tk


def win():
    message.set("You win!")     # The label updates by itself


root = tk.Tk()
root.geometry("300x200")
root.title("textvariable")

message = tk.StringVar(value="Click the button")

label = tk.Label(root, textvariable=message, font=("Arial", 18))
label.pack(pady=20)

button = tk.Button(root, text="Play", command=win)
button.pack()

root.mainloop()
