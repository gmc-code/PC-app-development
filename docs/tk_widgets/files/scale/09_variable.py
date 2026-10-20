# tk Scale - variable

import tkinter as tk


def show():
    result_label.config(text=f"You chose {score.get()}")


root = tk.Tk()
root.geometry("300x200")
root.title("variable")

score = tk.IntVar(value=5)

score_scale = tk.Scale(root, from_=1, to=10, orient="horizontal", variable=score)
score_scale.pack()

show_button = tk.Button(root, text="Show", command=show)
show_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
