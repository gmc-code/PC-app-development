import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("create_image")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

picture = tk.PhotoImage(file="logo.png")
canvas.create_image(150, 100, image=picture)

root.mainloop()
