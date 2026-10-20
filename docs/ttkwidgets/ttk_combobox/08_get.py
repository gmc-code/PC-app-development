# ttk Combobox - get

import tkinter as tk
from tkinter import ttk


def show():
    result_label.config(text="You chose " + year_box.get())


root = tk.Tk()
root.geometry("300x200")
root.title("get")

year_box = ttk.Combobox(root, values=["Year 7", "Year 8", "Year 9"], state="readonly")
year_box.set("Year 7")
year_box.pack(pady=10)

ttk.Button(root, text="Show", command=show).pack()

result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
