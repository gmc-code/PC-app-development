# ttk Combobox - Tasks Q2

import tkinter as tk
from tkinter import ttk


def show():
    result_label.config(text="You picked " + holiday_box.get())


root = tk.Tk()
root.geometry("300x200")
root.title("Holidays")

holiday_box = ttk.Combobox(root, values=["Beach", "Snow", "City", "Camping"],
                           state="readonly")
holiday_box.set("Beach")
holiday_box.pack(pady=10)

ttk.Button(root, text="Show", command=show).pack()
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
