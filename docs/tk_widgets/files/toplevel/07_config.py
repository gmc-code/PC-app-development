# tk Toplevel - config

import tkinter as tk


def open_window():
    party = tk.Toplevel(root)
    party.title("Party")
    party.geometry("250x150")
    tk.Button(party, text="Pink", command=lambda: party.config(bg="pink")).pack(pady=10)
    tk.Button(party, text="Gold", command=lambda: party.config(bg="gold")).pack()


root = tk.Tk()
root.geometry("300x200")
root.title("config")

tk.Button(root, text="Open", command=open_window).pack(pady=60)

root.mainloop()
