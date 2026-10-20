# tk Label - anchor

import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("anchor")

label_1 = tk.Label(root, text="top left", bg="lightyellow", width=25, height=3, anchor="nw")
label_1.pack(pady=5)

label_2 = tk.Label(root, text="middle", bg="lightyellow", width=25, height=3, anchor="center")
label_2.pack(pady=5)

label_3 = tk.Label(root, text="bottom right", bg="lightyellow", width=25, height=3, anchor="se")
label_3.pack(pady=5)

root.mainloop()
