# tk Toplevel - Tasks Q4

import tkinter as tk


def add_ten():
    score = int(score_label.cget("text").replace("Score: ", ""))
    score_label.config(text=f"Score: {score + 10}")


def open_bonus():
    bonus = tk.Toplevel(root)
    bonus.title("Bonus")
    bonus.geometry("200x100")
    tk.Button(bonus, text="Add 10 points", command=add_ten).pack(pady=30)


root = tk.Tk()
root.geometry("300x200")
root.title("Game")

score_label = tk.Label(root, text="Score: 0", font=("Arial", 18))
score_label.pack(pady=30)

tk.Button(root, text="Bonus", command=open_bonus).pack()

root.mainloop()
