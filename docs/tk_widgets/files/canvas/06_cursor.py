# tk Canvas - cursor

import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("cursor")

canvas = tk.Canvas(root, width=300, height=200, bg="white", cursor="pencil")
canvas.pack(pady=10)

root.mainloop()
