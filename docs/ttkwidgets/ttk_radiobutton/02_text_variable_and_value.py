# ttk Radiobutton - text, variable and value

import tkinter as tk
from tkinter import ttk


def show():
    result_label.config(text="You chose " + year.get())


root = tk.Tk()
root.geometry("300x200")
root.title("text, variable and value")

year = tk.StringVar(value="Year 7")

for choice in ["Year 7", "Year 8", "Year 9"]:
    ttk.Radiobutton(root, text=choice, variable=year, value=choice).pack()

ttk.Button(root, text="Show", command=show).pack(pady=5)

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
