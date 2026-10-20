# tk OptionMenu - Using a Python list of choices

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("List of choices")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

day = tk.StringVar(value=days[0])           # Start on the first item in the list

day_menu = tk.OptionMenu(root, day, *days)
day_menu.pack(pady=20)

root.mainloop()
