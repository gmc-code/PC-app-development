# tk Radiobutton - config

import tkinter as tk


def lock_answer():
    for radio in all_radios:
        radio.config(state="disabled")      # No more changing the answer


root = tk.Tk()
root.geometry("300x200")
root.title("config")

answer = tk.StringVar(value="none")

a_radio = tk.Radiobutton(root, text="A", variable=answer, value="A", command=lock_answer)
a_radio.pack()
b_radio = tk.Radiobutton(root, text="B", variable=answer, value="B", command=lock_answer)
b_radio.pack()

all_radios = [a_radio, b_radio]

root.mainloop()
