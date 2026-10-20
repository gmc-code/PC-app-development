# tk Canvas - relief, borderwidth and highlightthickness

import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("border")

canvas = tk.Canvas(root, width=280, height=180, bg="white",
                   relief="solid", borderwidth=3, highlightthickness=0)
canvas.pack(pady=10)

root.mainloop()
