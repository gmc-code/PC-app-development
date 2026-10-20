# tk Menu - Tasks Q2

import tkinter as tk


def change_colour(colour):
    root.config(bg=colour)


root = tk.Tk()
root.geometry("300x200")
root.title("Menus")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

colour_menu = tk.Menu(menubar, tearoff=0)
colour_menu.add_command(label="Red", command=lambda: change_colour("red"))
colour_menu.add_command(label="Green", command=lambda: change_colour("green"))
colour_menu.add_command(label="Blue", command=lambda: change_colour("blue"))
menubar.add_cascade(label="Colour", menu=colour_menu)

root.mainloop()
