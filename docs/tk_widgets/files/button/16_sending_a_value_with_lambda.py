# tk Button - Sending a value with lambda

import tkinter as tk


def change_colour(colour):
    root.config(bg=colour)      # Change the window's background colour


root = tk.Tk()
root.geometry("300x200")
root.title("lambda")

red_button = tk.Button(root, text="Red", width=10, command=lambda: change_colour("red"))
red_button.pack(pady=5)

green_button = tk.Button(root, text="Green", width=10, command=lambda: change_colour("green"))
green_button.pack(pady=5)

blue_button = tk.Button(root, text="Blue", width=10, command=lambda: change_colour("blue"))
blue_button.pack(pady=5)

root.mainloop()
