# tk Frame - padx and pady

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("padx and pady")

padded_frame = tk.Frame(root, bg="lightgreen", padx=30, pady=20)
padded_frame.pack(pady=20)

name_label = tk.Label(padded_frame, text="Lots of space around me")
name_label.pack()

root.mainloop()
