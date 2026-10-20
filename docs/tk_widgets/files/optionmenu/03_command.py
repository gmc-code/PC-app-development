# tk OptionMenu - command

import tkinter as tk


def change_colour(choice):
    root.config(bg=choice)


root = tk.Tk()
root.geometry("300x200")
root.title("command")

colour = tk.StringVar(value="white")

colour_menu = tk.OptionMenu(root, colour, "white", "pink", "lightblue", "lightgreen",
                            command=change_colour)
colour_menu.pack(pady=20)

root.mainloop()
