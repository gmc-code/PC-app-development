# tk Menu - add_radiobutton

import tkinter as tk


def change_level():
    level_label.config(text="Level: " + level.get())


root = tk.Tk()
root.geometry("300x200")
root.title("add_radiobutton")

level = tk.StringVar(value="Easy")

menubar = tk.Menu(root)
root.config(menu=menubar)

level_menu = tk.Menu(menubar, tearoff=0)
for choice in ["Easy", "Medium", "Hard"]:
    level_menu.add_radiobutton(label=choice, variable=level, value=choice,
                               command=change_level)
menubar.add_cascade(label="Level", menu=level_menu)

level_label = tk.Label(root, text="Level: Easy", font=("Arial", 16))
level_label.pack(pady=40)

root.mainloop()
