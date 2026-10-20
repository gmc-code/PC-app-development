# tk Canvas - Making a Canvas

import tkinter as tk            # Load the tkinter library

root = tk.Tk()                  # Make the window
root.geometry("320x240")        # Window size: 320 wide, 240 high
root.title("My first canvas")   # Words in the title bar

canvas = tk.Canvas(root, width=300, height=200, bg="white")    # 1. Create the canvas
canvas.pack(pady=10)                                            # 2. Place it

canvas.create_line(20, 20, 280, 180)                            # 3. Draw a line

root.mainloop()                 # Keep the window open
