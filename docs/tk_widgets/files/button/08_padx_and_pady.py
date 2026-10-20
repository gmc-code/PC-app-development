# tk Button - padx and pady

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("padx and pady")

button = tk.Button(root, text="Padded", padx=40, pady=15)
button.pack(pady=20)

root.mainloop()
