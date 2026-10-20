# tk Spinbox - increment

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("increment")

minutes_spinbox = tk.Spinbox(root, from_=0, to=60, increment=5)
minutes_spinbox.pack(pady=20)

root.mainloop()
