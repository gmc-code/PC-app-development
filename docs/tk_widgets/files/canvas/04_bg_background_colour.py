# tk Canvas - bg (background colour)

import tkinter as tk

root = tk.Tk()
root.geometry("320x240")
root.title("bg")

night_sky = tk.Canvas(root, width=300, height=200, bg="midnightblue")
night_sky.pack(pady=10)

root.mainloop()
