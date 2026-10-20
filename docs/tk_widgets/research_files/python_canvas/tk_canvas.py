import tkinter as tk

root = tk.Tk()
root.title("Canvas Example")

canvas = tk.Canvas(root, width=400, height=250, bg="white")
canvas.pack(padx=10, pady=10)

canvas.create_rectangle(20, 20, 140, 100, fill="lightblue")
canvas.create_oval(180, 20, 300, 100, fill="pink")
canvas.create_line(20, 150, 300, 200, width=3)
canvas.create_text(200, 225, text="Canvas Example")

root.mainloop()

