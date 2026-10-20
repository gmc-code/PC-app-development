# ttk Frame - config

import tkinter as tk
from tkinter import ttk


def light_on():
    room.config(style="On.TFrame")


def light_off():
    room.config(style="Off.TFrame")


root = tk.Tk()
root.geometry("300x220")
root.title("config")

style = ttk.Style()
style.configure("On.TFrame", background="yellow")
style.configure("Off.TFrame", background="black")

room = ttk.Frame(root, width=200, height=100, style="Off.TFrame")
room.pack(pady=10)

ttk.Button(root, text="Light on", command=light_on).pack()
ttk.Button(root, text="Light off", command=light_off).pack()

root.mainloop()
