# tk Button - config

import tkinter as tk


def vote():
    vote_button.config(text="Thanks for voting!", state="disabled")


root = tk.Tk()
root.geometry("300x200")
root.title("config")

vote_button = tk.Button(root, text="Vote", font=("Arial", 16), command=vote)
vote_button.pack(pady=20)

root.mainloop()
