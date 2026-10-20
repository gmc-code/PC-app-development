# Tkinter widgets - grid

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("grid")

tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)
tk.Label(root, text="Age:").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)

root.mainloop()
