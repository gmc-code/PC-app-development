# tk Radiobutton - command

import tkinter as tk


def change_colour():
    root.config(bg=colour.get())     # Use the chosen value as the colour


root = tk.Tk()
root.geometry("300x200")
root.title("command")

colour = tk.StringVar(value="white")

tk.Radiobutton(root, text="Red", variable=colour, value="red", command=change_colour).pack()
tk.Radiobutton(root, text="Green", variable=colour, value="green", command=change_colour).pack()
tk.Radiobutton(root, text="Blue", variable=colour, value="blue", command=change_colour).pack()

root.mainloop()
