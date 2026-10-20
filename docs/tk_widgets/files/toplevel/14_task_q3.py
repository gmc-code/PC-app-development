# tk Toplevel - Tasks Q3

import tkinter as tk


def open_about():
    about = tk.Toplevel(root, bg="lightblue")
    about.title("About")
    about.geometry("250x100")
    about.resizable(False, False)
    tk.Label(about, text="Made by Sam", bg="lightblue").pack(pady=10)
    tk.Button(about, text="Close", command=about.destroy).pack()


root = tk.Tk()
root.geometry("300x200")
root.title("Main")

tk.Button(root, text="About", command=open_about).pack(pady=60)

root.mainloop()
