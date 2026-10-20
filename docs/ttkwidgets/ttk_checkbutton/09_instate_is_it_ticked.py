# ttk Checkbutton - instate (is it ticked?)

import tkinter as tk
from tkinter import ttk


def check():
    if sound_check.instate(["selected"]):
        result_label.config(text="Sound is on")
    else:
        result_label.config(text="Sound is off")


root = tk.Tk()
root.geometry("300x200")
root.title("instate")

sound = tk.IntVar()

sound_check = ttk.Checkbutton(root, text="Sound", variable=sound)
sound_check.pack(pady=10)

ttk.Button(root, text="Check", command=check).pack()

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
