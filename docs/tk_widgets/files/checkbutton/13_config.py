# tk Checkbutton - config

import tkinter as tk


def lock():
    rules_check.config(state="disabled", text="Rules accepted")


root = tk.Tk()
root.geometry("300x200")
root.title("config")

rules = tk.IntVar()

rules_check = tk.Checkbutton(root, text="Accept the rules", variable=rules, command=lock)
rules_check.pack(pady=20)

root.mainloop()
