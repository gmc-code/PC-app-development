# tk Entry - select_range

import tkinter as tk


def check():
    if answer_entry.get() == "12":
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Try again", fg="red")
        answer_entry.focus_set()                    # Cursor back in the box
        answer_entry.select_range(0, tk.END)        # Highlight the wrong answer


root = tk.Tk()
root.geometry("300x200")
root.title("select_range")

question_label = tk.Label(root, text="What is 3 x 4?", font=("Arial", 16))
question_label.pack(pady=5)

answer_entry = tk.Entry(root, font=("Arial", 16), width=5)
answer_entry.pack()

check_button = tk.Button(root, text="Check", command=check)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack()

root.mainloop()
