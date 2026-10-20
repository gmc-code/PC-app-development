# tk OptionMenu - state

import tkinter as tk


def lock():
    year_menu.config(state="disabled")


root = tk.Tk()
root.geometry("300x200")
root.title("state")

year = tk.StringVar(value="Year 7")

year_menu = tk.OptionMenu(root, year, "Year 7", "Year 8", "Year 9")
year_menu.pack(pady=10)

lock_button = tk.Button(root, text="Lock my choice", command=lock)
lock_button.pack()

root.mainloop()
