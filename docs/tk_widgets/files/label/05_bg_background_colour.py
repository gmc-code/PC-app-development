# tk Label - bg (background colour)

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("bg")

label = tk.Label(root, text="Yellow background", font=("Arial", 18), bg="yellow")
label.pack()

root.mainloop()
