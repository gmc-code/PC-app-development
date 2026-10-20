# Tkinter widgets - Tasks Q3

import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Test")

tk.Label(root, text="Username:").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)

root.mainloop()
