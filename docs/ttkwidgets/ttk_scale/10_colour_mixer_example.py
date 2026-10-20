# ttk Scale - Colour mixer example

import tkinter as tk
from tkinter import ttk


def mix(value):
    red = int(red_scale.get())
    green = int(green_scale.get())
    blue = int(blue_scale.get())
    colour = f"#{red:02x}{green:02x}{blue:02x}"
    colour_label.config(background=colour, text=colour)


root = tk.Tk()
root.geometry("300x260")
root.title("Colour mixer")

ttk.Label(root, text="Red").pack()
red_scale = ttk.Scale(root, from_=0, to=255, length=250, command=mix)
red_scale.pack()

ttk.Label(root, text="Green").pack()
green_scale = ttk.Scale(root, from_=0, to=255, length=250, command=mix)
green_scale.pack()

ttk.Label(root, text="Blue").pack()
blue_scale = ttk.Scale(root, from_=0, to=255, length=250, command=mix)
blue_scale.pack()

colour_label = ttk.Label(root, text="#000000", background="#000000", foreground="white",
                         width=20, anchor="center", padding=10)
colour_label.pack(pady=10)

root.mainloop()
