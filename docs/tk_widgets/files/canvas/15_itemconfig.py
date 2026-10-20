# tk Canvas - itemconfig

import tkinter as tk


def go():
    canvas.itemconfig(light, fill="green")
    canvas.itemconfig(sign, text="GO")


def stop():
    canvas.itemconfig(light, fill="red")
    canvas.itemconfig(sign, text="STOP")


root = tk.Tk()
root.geometry("320x280")
root.title("itemconfig")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=5)

light = canvas.create_oval(100, 20, 200, 120, fill="red")
sign = canvas.create_text(150, 160, text="STOP", font=("Arial", 24, "bold"))

tk.Button(root, text="Go", command=go).pack(side="left", padx=60)
tk.Button(root, text="Stop", command=stop).pack(side="left")

root.mainloop()
