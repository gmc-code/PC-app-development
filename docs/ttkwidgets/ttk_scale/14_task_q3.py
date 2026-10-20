# ttk Scale - Tasks Q3

import tkinter as tk
from tkinter import ttk


def show_battery(value):
    battery_label.config(text=f"Battery: {int(float(value))}%")


root = tk.Tk()
root.geometry("300x200")
root.title("Battery")

ttk.Scale(root, from_=0, to=100, length=250, command=show_battery).pack(pady=20)

battery_label = ttk.Label(root, text="Battery: 0%", font=("Arial", 16))
battery_label.pack()

root.mainloop()
