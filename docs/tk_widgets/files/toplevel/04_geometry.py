# tk Toplevel - geometry

import tkinter as tk


def open_window():
    help_window = tk.Toplevel(root)
    help_window.title("Help")                       # title
    help_window.geometry("250x120+100+100")         # size and position
    tk.Label(help_window, text="Click Start to play.").pack(pady=40)


root = tk.Tk()
root.geometry("300x200")
root.title("title and geometry")

tk.Button(root, text="Help", command=open_window).pack(pady=60)

root.mainloop()
