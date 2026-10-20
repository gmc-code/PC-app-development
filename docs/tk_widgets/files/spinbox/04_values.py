# tk Spinbox - values

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("values")

day_spinbox = tk.Spinbox(root, values=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))
day_spinbox.pack(pady=20)

root.mainloop()
