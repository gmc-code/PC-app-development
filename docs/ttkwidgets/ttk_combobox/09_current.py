# ttk Combobox - current

import tkinter as tk
from tkinter import ttk


def show_position():
    number = month_box.current()
    result_label.config(text=f"{month_box.get()} is month number {number + 1}")


root = tk.Tk()
root.geometry("300x200")
root.title("current")

months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

month_box = ttk.Combobox(root, values=months, state="readonly")
month_box.current(0)                    # Choose the first month
month_box.pack(pady=10)

ttk.Button(root, text="Which number?", command=show_position).pack()

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
