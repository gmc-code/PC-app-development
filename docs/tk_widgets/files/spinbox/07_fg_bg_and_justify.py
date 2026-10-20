# tk Spinbox - fg, bg and justify

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("fg, bg and justify")

level_spinbox = tk.Spinbox(root, from_=1, to=10, font=("Arial", 18), width=5,
                           fg="white", bg="navy", justify="center")
level_spinbox.pack(pady=20)

root.mainloop()
