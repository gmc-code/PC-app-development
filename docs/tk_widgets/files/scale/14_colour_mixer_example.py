# tk Scale - Colour mixer example

import tkinter as tk


def mix(value):
    red = red_scale.get()
    green = green_scale.get()
    blue = blue_scale.get()
    colour = f"#{red:02x}{green:02x}{blue:02x}"
    colour_label.config(bg=colour, text=colour)


root = tk.Tk()
root.geometry("300x300")
root.title("Colour mixer")

red_scale = tk.Scale(root, from_=0, to=255, orient="horizontal", length=250,
                     label="Red", troughcolor="red", command=mix)
red_scale.pack()
green_scale = tk.Scale(root, from_=0, to=255, orient="horizontal", length=250,
                       label="Green", troughcolor="green", command=mix)
green_scale.pack()
blue_scale = tk.Scale(root, from_=0, to=255, orient="horizontal", length=250,
                      label="Blue", troughcolor="blue", command=mix)
blue_scale.pack()

colour_label = tk.Label(root, text="#000000", bg="#000000", fg="white", width=20, height=2)
colour_label.pack(pady=10)

root.mainloop()
