# tk Canvas - create_text

import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("create_text")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

canvas.create_text(150, 60, text="Hello!", font=("Arial", 32, "bold"), fill="blue")
canvas.create_text(150, 140, text="Words on a canvas", font=("Arial", 14))

root.mainloop()
