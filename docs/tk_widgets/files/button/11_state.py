# tk Button - state

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

on_button = tk.Button(root, text="I work", state="normal")
on_button.pack(pady=10)

off_button = tk.Button(root, text="I am turned off", state="disabled")
off_button.pack(pady=10)

root.mainloop()
