# tk Frame - config

import tkinter as tk


def light_on():
    room.config(bg="yellow")


def light_off():
    room.config(bg="black")


root = tk.Tk()
root.geometry("300x200")
root.title("config")

room = tk.Frame(root, width=200, height=100, bg="black")
room.pack(pady=10)

tk.Button(root, text="Light on", command=light_on).pack()
tk.Button(root, text="Light off", command=light_off).pack()

root.mainloop()
