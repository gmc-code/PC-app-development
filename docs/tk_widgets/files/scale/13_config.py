# tk Scale - config

import tkinter as tk


def hard_mode():
    level_scale.config(to=20, troughcolor="red")


root = tk.Tk()
root.geometry("300x200")
root.title("config")

level_scale = tk.Scale(root, from_=1, to=10, orient="horizontal", length=200, label="Level")
level_scale.pack()

hard_button = tk.Button(root, text="Hard mode", command=hard_mode)
hard_button.pack(pady=10)

root.mainloop()
