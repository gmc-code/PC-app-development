# tk Radiobutton - Tasks Q4

import tkinter as tk


def check():
    if answer.get() == 30:
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Try again", fg="red")


root = tk.Tk()
root.geometry("300x200")
root.title("Quiz")

question_label = tk.Label(root, text="What is 5 x 6?", font=("Arial", 14))
question_label.pack()

answer = tk.IntVar(value=0)

for number in [25, 30, 35]:
    tk.Radiobutton(root, text=number, variable=answer, value=number,
                   command=check).pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
