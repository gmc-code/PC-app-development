# tk Toplevel - withdraw and deiconify

import tkinter as tk


def hide():
    notes_window.withdraw()


def show():
    notes_window.deiconify()


root = tk.Tk()
root.geometry("300x200")
root.title("withdraw")

notes_window = tk.Toplevel(root)
notes_window.title("Notes")
notes_window.geometry("200x150")
tk.Text(notes_window).pack()

tk.Button(root, text="Hide notes", command=hide).pack(pady=20)
tk.Button(root, text="Show notes", command=show).pack()

root.mainloop()
