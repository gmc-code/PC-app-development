# tk Radiobutton - font, fg and bg

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("font, fg and bg")

size = tk.StringVar(value="Small")

tk.Radiobutton(root, text="Small", variable=size, value="Small",
               font=("Arial", 16), fg="purple", bg="lavender").pack(pady=2)
tk.Radiobutton(root, text="Large", variable=size, value="Large",
               font=("Arial", 16), fg="purple", bg="lavender").pack(pady=2)

root.mainloop()
