# ttk Button - state and instate

import tkinter as tk
from tkinter import ttk


def vote():
    vote_button.state(["disabled"])         # Can only vote once
    result_label.config(text="Thanks for voting!")


def reset():
    vote_button.state(["!disabled"])        # Turn back on
    result_label.config(text="")


root = tk.Tk()
root.geometry("300x200")
root.title("state")

vote_button = ttk.Button(root, text="Vote", command=vote)
vote_button.pack(pady=10)

ttk.Button(root, text="Reset", command=reset).pack()

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
