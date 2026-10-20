# tk Checkbutton - variable

import tkinter as tk


def check():
    if homework.get() == 1:
        result_label.config(text="Well done!")
    else:
        result_label.config(text="Better get started...")


root = tk.Tk()
root.geometry("300x200")
root.title("variable")

homework = tk.IntVar()

homework_check = tk.Checkbutton(root, text="Homework done", variable=homework)
homework_check.pack(pady=10)

check_button = tk.Button(root, text="Check", command=check)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
