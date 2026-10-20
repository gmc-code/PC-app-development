# tk Entry - Tasks Q4

import tkinter as tk


def next_year():
    try:
        age = int(age_entry.get())
        answer_label.config(text=f"Next year you will be {age + 1}")
    except ValueError:
        answer_label.config(text="Please type a whole number")


root = tk.Tk()
root.geometry("300x200")
root.title("Age")

age_label = tk.Label(root, text="How old are you?")
age_label.pack(pady=5)

age_entry = tk.Entry(root, font=("Arial", 16), width=5)
age_entry.pack()

next_button = tk.Button(root, text="Next year", command=next_year)
next_button.pack(pady=5)

answer_label = tk.Label(root, text="", font=("Arial", 14))
answer_label.pack()

root.mainloop()
