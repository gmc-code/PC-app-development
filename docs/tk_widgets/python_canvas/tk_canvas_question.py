import tkinter as tk

root = tk.Tk()
root.title("Canvas Question")

canvas = tk.Canvas(root, width=400, height=250, bg="white")
canvas.pack()

canvas.create_rectangle(20, 20, 140, 100, fill="yellow")
canvas.create_oval(200, 20, 300, 120, fill="green")
canvas.create_line(20, 150, 300, 200, fill="red",width=5)

root.mainloop()