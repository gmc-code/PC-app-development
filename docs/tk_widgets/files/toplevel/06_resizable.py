# tk Toplevel - resizable

import tkinter as tk


def open_window():
    fixed = tk.Toplevel(root)
    fixed.title("Fixed size")
    fixed.geometry("250x120")
    fixed.resizable(False, False)       # Cannot be resized
    tk.Label(fixed, text="Try to resize me!").pack(pady=40)


root = tk.Tk()
root.geometry("300x200")
root.title("resizable")

tk.Button(root, text="Open", command=open_window).pack(pady=60)

root.mainloop()
