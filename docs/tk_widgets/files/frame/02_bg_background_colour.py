# tk Frame - bg (background colour)

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("bg")

top_frame = tk.Frame(root, bg="pink")
top_frame.pack(fill="x")

title_label = tk.Label(top_frame, text="My App", bg="pink", font=("Arial", 18))
title_label.pack()

root.mainloop()
