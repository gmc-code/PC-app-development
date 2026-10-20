# tk LabelFrame - A form with grid

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Form")

form = tk.LabelFrame(root, text="Sign up", padx=10, pady=10)
form.pack(pady=20)

tk.Label(form, text="Name:").grid(row=0, column=0, sticky="e")
tk.Entry(form).grid(row=0, column=1, pady=2)
tk.Label(form, text="Email:").grid(row=1, column=0, sticky="e")
tk.Entry(form).grid(row=1, column=1, pady=2)

root.mainloop()
