# tk Label - fg (text colour)

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("fg")

label = tk.Label(root, text="Blue words", font=("Arial", 24), fg="blue")
label.pack()

root.mainloop()
