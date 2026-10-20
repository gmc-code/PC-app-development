# tk LabelFrame - config

import tkinter as tk

round_number = 1


def next_round():
    global round_number             # Allow the function to change round_number
    round_number = round_number + 1
    game_box.config(text=f"Round {round_number}")


root = tk.Tk()
root.geometry("300x200")
root.title("config")

game_box = tk.LabelFrame(root, text="Round 1", font=("Arial", 14), padx=20, pady=10)
game_box.pack(pady=20)

tk.Button(game_box, text="Next round", command=next_round).pack()

root.mainloop()
