# tk Scale - orient

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("orient")

speed_scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
speed_scale.pack(pady=20)

root.mainloop()
