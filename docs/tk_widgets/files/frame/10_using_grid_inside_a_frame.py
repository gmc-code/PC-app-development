# tk Frame - Using grid inside a frame

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("grid in a frame")

tk.Label(root, text="Sign up", font=("Arial", 16)).pack(pady=5)    # pack in root

form = tk.Frame(root)
form.pack()

tk.Label(form, text="Name:").grid(row=0, column=0)      # grid in form
tk.Entry(form).grid(row=0, column=1)
tk.Label(form, text="Email:").grid(row=1, column=0)
tk.Entry(form).grid(row=1, column=1)

root.mainloop()
