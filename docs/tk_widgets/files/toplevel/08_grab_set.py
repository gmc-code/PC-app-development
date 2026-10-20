# tk Toplevel - grab_set

import tkinter as tk


def ask():
    question = tk.Toplevel(root)
    question.title("Are you sure?")
    question.geometry("250x120")
    question.grab_set()                 # The main window cannot be clicked
    tk.Label(question, text="Delete everything?").pack(pady=10)
    tk.Button(question, text="Yes", width=8, command=lambda: yes(question)).pack(side="left", padx=25)
    tk.Button(question, text="No", width=8, command=question.destroy).pack(side="left")


def yes(window):
    status_label.config(text="Everything deleted!")
    window.destroy()


root = tk.Tk()
root.geometry("300x200")
root.title("grab_set")

tk.Button(root, text="Delete", command=ask).pack(pady=30)
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
