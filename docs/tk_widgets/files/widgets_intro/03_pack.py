# Tkinter widgets - pack

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("pack")

tk.Label(root, text="First").pack(pady=5)
tk.Label(root, text="Second").pack(pady=5)
tk.Label(root, text="Third").pack(pady=5)

root.mainloop()
