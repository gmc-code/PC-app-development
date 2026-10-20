# tk Toplevel - padx and pady

import tkinter as tk


def open_window():
    padded_window = tk.Toplevel(root, padx=30, pady=30, bg="white")
    padded_window.title("Padded")
    tk.Label(padded_window, text="There is space all around me", bg="lightblue").pack()


root = tk.Tk()
root.geometry("300x200")
root.title("padx and pady")

tk.Button(root, text="Open", command=open_window).pack(pady=60)

root.mainloop()
