# tk Menu - add_checkbutton

import tkinter as tk


def change_theme():
    if dark.get() == 1:
        root.config(bg="black")
    else:
        root.config(bg="white")


root = tk.Tk()
root.geometry("300x200")
root.title("add_checkbutton")
root.config(bg="white")

dark = tk.IntVar()

menubar = tk.Menu(root)
root.config(menu=menubar)

view_menu = tk.Menu(menubar, tearoff=0)
view_menu.add_checkbutton(label="Dark mode", variable=dark, command=change_theme)
menubar.add_cascade(label="View", menu=view_menu)

root.mainloop()
