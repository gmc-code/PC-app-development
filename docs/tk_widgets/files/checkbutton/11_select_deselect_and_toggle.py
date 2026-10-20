# tk Checkbutton - select, deselect and toggle

import tkinter as tk


def tick_all():
    for box in all_boxes:
        box.select()


def clear_all():
    for box in all_boxes:
        box.deselect()


root = tk.Tk()
root.geometry("300x220")
root.title("select and deselect")

red = tk.IntVar()
green = tk.IntVar()
blue = tk.IntVar()

red_check = tk.Checkbutton(root, text="Red", variable=red)
red_check.pack()
green_check = tk.Checkbutton(root, text="Green", variable=green)
green_check.pack()
blue_check = tk.Checkbutton(root, text="Blue", variable=blue)
blue_check.pack()

all_boxes = [red_check, green_check, blue_check]

tick_button = tk.Button(root, text="Tick all", command=tick_all)
tick_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear all", command=clear_all)
clear_button.pack()

root.mainloop()
