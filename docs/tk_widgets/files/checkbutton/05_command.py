# tk Checkbutton - command

import tkinter as tk


def change_colour():
    if dark.get() == 1:
        root.config(bg="black")
    else:
        root.config(bg="white")


root = tk.Tk()
root.geometry("300x200")
root.title("command")
root.config(bg="white")

dark = tk.IntVar()

dark_check = tk.Checkbutton(root, text="Dark mode", variable=dark, command=change_colour)
dark_check.pack(pady=20)

root.mainloop()
