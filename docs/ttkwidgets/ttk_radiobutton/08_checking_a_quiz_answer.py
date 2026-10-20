# ttk Radiobutton - Checking a quiz answer

import tkinter as tk
from tkinter import ttk


def check():
    if answer.get() == "Mars":
        result_label.config(text="Correct!", foreground="green")
    else:
        result_label.config(text="Try again", foreground="red")


root = tk.Tk()
root.geometry("300x220")
root.title("Quiz")

ttk.Label(root, text="Which planet is red?", font=("Arial", 14)).pack(pady=5)

answer = tk.StringVar(value="none")

for planet in ["Venus", "Mars", "Jupiter"]:
    ttk.Radiobutton(root, text=planet, variable=answer, value=planet).pack()

ttk.Button(root, text="Check", command=check).pack(pady=5)

result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
