# tk Spinbox - wrap

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("wrap")

hour_spinbox = tk.Spinbox(root, from_=1, to=12, wrap=True)
hour_spinbox.pack(pady=20)

root.mainloop()
