# tk Frame - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Frames")

box = tk.Frame(root, bg="lightblue", padx=20, pady=20)
box.pack(pady=20)

hello_label = tk.Label(box, text="Hello")
hello_label.pack()

root.mainloop()
