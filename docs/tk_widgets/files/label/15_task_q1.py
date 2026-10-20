# tk Label - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("About me")

name_label = tk.Label(root, text="Sam", font=("Arial", 24), fg="white", bg="blue")
name_label.pack()

root.mainloop()
