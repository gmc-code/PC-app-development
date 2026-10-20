# tk Scale - from\_ and to

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("from_ and to")

rating_scale = tk.Scale(root, from_=10, to=1)    # 10 at the top, 1 at the bottom
rating_scale.pack()

root.mainloop()
