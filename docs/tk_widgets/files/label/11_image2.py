from pathlib import Path
import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("image")

# Get the directory where this script is currently located
script_dir = Path(__file__).parent
image_path = script_dir / "logo.png"

# Load the picture using the full path
picture = tk.PhotoImage(file=image_path)

label = tk.Label(root, image=picture, text="Our logo", compound="top")
label.pack(pady=20)

root.mainloop()