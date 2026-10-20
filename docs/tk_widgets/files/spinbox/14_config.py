# tk Spinbox - config

import tkinter as tk


def adults_only():
    age_spinbox.config(from_=18, to=100, bg="lightyellow")


root = tk.Tk()
root.geometry("300x200")
root.title("config")

age_spinbox = tk.Spinbox(root, from_=0, to=100, width=5)
age_spinbox.pack(pady=10)

adults_button = tk.Button(root, text="Adults only", command=adults_only)
adults_button.pack()

root.mainloop()
