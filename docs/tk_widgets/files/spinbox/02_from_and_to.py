# tk Spinbox - from\_ and to

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("from_ and to")

age_spinbox = tk.Spinbox(root, from_=5, to=18)
age_spinbox.pack(pady=20)

root.mainloop()
