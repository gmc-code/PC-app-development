# tk Radiobutton - selectcolor

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("selectcolor")

pet = tk.StringVar(value="Dog")

tk.Radiobutton(root, text="Dog", variable=pet, value="Dog", selectcolor="yellow").pack()
tk.Radiobutton(root, text="Cat", variable=pet, value="Cat", selectcolor="yellow").pack()

root.mainloop()
