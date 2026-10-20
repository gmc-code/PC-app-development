# tk LabelFrame - padx and pady

import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("padx and pady")

no_pad = tk.LabelFrame(root, text="No padding")
no_pad.pack(pady=10)
tk.Button(no_pad, text="Squashed").pack()

padded = tk.LabelFrame(root, text="Padding", padx=30, pady=15)
padded.pack(pady=10)
tk.Button(padded, text="Roomy").pack()

root.mainloop()
