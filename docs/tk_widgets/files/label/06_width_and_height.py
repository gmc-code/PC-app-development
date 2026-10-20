# tk Label - width and height

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("width and height")

label = tk.Label(root, text="Big label", bg="lightblue", width=20, height=3)
label.pack()

root.mainloop()
