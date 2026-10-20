# tk Radiobutton - Checking a quiz answer

import tkinter as tk


def check():
    if answer.get() == "Mars":
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Try again", fg="red")


root = tk.Tk()
root.geometry("300x250")
root.title("Quiz")

question_label = tk.Label(root, text="Which planet is red?", font=("Arial", 14))
question_label.pack(pady=5)

answer = tk.StringVar(value="none")

for planet in ["Venus", "Mars", "Jupiter"]:
    tk.Radiobutton(root, text=planet, variable=answer, value=planet).pack()

check_button = tk.Button(root, text="Check", command=check)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
