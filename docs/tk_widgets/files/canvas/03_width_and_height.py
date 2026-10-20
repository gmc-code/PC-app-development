# tk Canvas - width and height

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("width and height")

small_canvas = tk.Canvas(root, width=150, height=100, bg="lightblue")
small_canvas.pack(pady=20)

root.mainloop()
