# tk Entry - config

import tkinter as tk


def show_answer():
    answer_entry.config(state="normal")         # Unlock the box
    answer_entry.delete(0, tk.END)
    answer_entry.insert(0, "Canberra")
    answer_entry.config(state="readonly")       # Lock it again


root = tk.Tk()
root.geometry("300x200")
root.title("config")

question_label = tk.Label(root, text="Capital of Australia?", font=("Arial", 14))
question_label.pack(pady=5)

answer_entry = tk.Entry(root, font=("Arial", 16), state="readonly")
answer_entry.pack()

show_button = tk.Button(root, text="Show answer", command=show_answer)
show_button.pack(pady=10)

root.mainloop()
