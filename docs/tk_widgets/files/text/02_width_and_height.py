# tk Text - width and height

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("width and height")

small_box = tk.Text(root, width=20, height=3)
small_box.pack(pady=10)

root.mainloop()
