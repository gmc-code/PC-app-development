# tk Frame - width and height

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("width and height")

empty_frame = tk.Frame(root, width=200, height=100, bg="orange")
empty_frame.pack(pady=20)

root.mainloop()
