# tk Label - text

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("text")

label = tk.Label(root, text="Line one\nLine two")
label.pack()

root.mainloop()
