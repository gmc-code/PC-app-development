# tk Scale - length

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("length")

long_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=250)
long_scale.pack(pady=20)

root.mainloop()
