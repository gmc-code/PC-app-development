# ttk Button - config and cget

import tkinter as tk
from tkinter import ttk


def switch():
    if light_button.cget("text") == "Turn ON":
        light_button.config(text="Turn OFF")
        light_label.config(text="Light is ON")
    else:
        light_button.config(text="Turn ON")
        light_label.config(text="Light is OFF")


root = tk.Tk()
root.geometry("300x200")
root.title("config and cget")

light_button = ttk.Button(root, text="Turn ON", width=12, command=switch)
light_button.pack(pady=20)

light_label = ttk.Label(root, text="Light is OFF", font=("Arial", 16))
light_label.pack()

root.mainloop()
