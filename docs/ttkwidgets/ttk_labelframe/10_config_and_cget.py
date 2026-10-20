# ttk LabelFrame - config and cget

import tkinter as tk
from tkinter import ttk


def next_round():
    number = int(game_box.cget("text").replace("Round ", ""))
    game_box.config(text=f"Round {number + 1}")


root = tk.Tk()
root.geometry("300x200")
root.title("config and cget")

game_box = ttk.LabelFrame(root, text="Round 1", padding=20)
game_box.pack(pady=30)
ttk.Button(game_box, text="Next round", command=next_round).pack()

root.mainloop()
