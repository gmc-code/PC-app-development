# tk Spinbox - font and width

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("font and width")

score_spinbox = tk.Spinbox(root, from_=0, to=99, font=("Arial", 24), width=4)
score_spinbox.pack(pady=20)

root.mainloop()
