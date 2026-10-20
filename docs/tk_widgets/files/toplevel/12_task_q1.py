# tk Toplevel - Tasks Q1

import tkinter as tk


def open_about():
    about = tk.Toplevel(root)
    about.title("About")
    about.geometry("250x100")
    tk.Label(about, text="Made by Sam").pack(pady=20)


root = tk.Tk()
root.geometry("300x200")
root.title("Main")

tk.Button(root, text="About", command=open_about).pack(pady=60)

root.mainloop()
