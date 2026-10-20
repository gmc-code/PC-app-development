# Tkinter widgets - place

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("place")

tk.Label(root, text="Top left").place(x=10, y=10)
tk.Label(root, text="Over here").place(x=180, y=140)

root.mainloop()
