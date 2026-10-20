# tk Canvas - create_rectangle

import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("create_rectangle")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

canvas.create_rectangle(20, 20, 120, 80)                                    # Outline only
canvas.create_rectangle(150, 20, 280, 80, fill="yellow")                    # Filled
canvas.create_rectangle(20, 110, 120, 180, fill="orange", outline="red", width=4)
canvas.create_rectangle(150, 110, 220, 180, fill="skyblue", outline="")    # No edge

root.mainloop()
