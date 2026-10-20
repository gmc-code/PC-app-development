# tk Spinbox - textvariable

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("textvariable")

players = tk.IntVar(value=4)        # Start on 4

players_spinbox = tk.Spinbox(root, from_=1, to=8, textvariable=players)
players_spinbox.pack(pady=20)

root.mainloop()
