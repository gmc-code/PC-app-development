# ttk Scale - get

import tkinter as tk
from tkinter import ttk


def convert():
    celsius = round(temp_scale.get())
    fahrenheit = celsius * 9 / 5 + 32
    result_label.config(text=f"{celsius} °C = {fahrenheit} °F")


root = tk.Tk()
root.geometry("300x200")
root.title("get")

temp_scale = ttk.Scale(root, from_=0, to=100, length=250)
temp_scale.pack(pady=20)

ttk.Button(root, text="Convert", command=convert).pack()

result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
