from pathlib import Path
import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("create_image")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

# Get the directory where this script is located and point to the image
script_dir = Path(__file__).parent
image_path = script_dir / "logo.png"

picture = tk.PhotoImage(file=image_path)
canvas.create_image(150, 100, image=picture)

root.mainloop()