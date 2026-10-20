# tk Label - padx and pady

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("padx and pady")

label = tk.Label(root, text="Padded", font=("Arial", 18), bg="lightgreen", padx=40, pady=20)
label.pack()

root.mainloop()
