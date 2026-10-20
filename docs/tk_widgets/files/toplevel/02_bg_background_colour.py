# tk Toplevel - bg (background colour)

import tkinter as tk


def open_window():
    yellow_window = tk.Toplevel(root, bg="lightyellow")
    yellow_window.title("Yellow window")
    yellow_window.geometry("250x150")
    tk.Label(yellow_window, text="I am yellow", bg="lightyellow").pack(pady=40)


root = tk.Tk()
root.geometry("300x200")
root.title("bg")

tk.Button(root, text="Open", command=open_window).pack(pady=60)

root.mainloop()
