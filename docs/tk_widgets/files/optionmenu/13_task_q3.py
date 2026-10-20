# tk OptionMenu - Tasks Q3

import tkinter as tk


def change_colour(choice):
    root.config(bg=choice)


root = tk.Tk()
root.geometry("300x200")
root.title("Colours")

colours = ["white", "pink", "orange", "lightgreen", "skyblue"]

colour = tk.StringVar(value=colours[0])

colour_menu = tk.OptionMenu(root, colour, *colours, command=change_colour)
colour_menu.pack(pady=20)

root.mainloop()
