# tk OptionMenu - set (the variable)

import tkinter as tk


def reset():
    team.set("Red")


root = tk.Tk()
root.geometry("300x200")
root.title("set")

team = tk.StringVar(value="Red")

team_menu = tk.OptionMenu(root, team, "Red", "Blue", "Green", "Yellow")
team_menu.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack()

root.mainloop()
