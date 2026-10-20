# tk LabelFrame - width and height

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("width and height")

empty_box = tk.LabelFrame(root, text="Coming soon", width=200, height=100)
empty_box.pack(pady=20)

root.mainloop()
