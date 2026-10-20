# tk Button - Tasks Q4

import tkinter as tk
import random


def roll():
    dice_label.config(text=random.randint(1, 6))


root = tk.Tk()
root.geometry("300x200")
root.title("Dice")

roll_button = tk.Button(root, text="Roll", font=("Arial", 16), command=roll)
roll_button.pack(pady=10)

dice_label = tk.Label(root, text="?", font=("Arial", 40))
dice_label.pack()

root.mainloop()
