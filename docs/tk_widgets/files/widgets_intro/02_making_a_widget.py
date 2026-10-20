# Tkinter widgets - Making a widget

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("My app")

greeting = tk.Label(root, text="Hello!", font=("Arial", 24), fg="blue")   # 1. Create
greeting.pack()                                                            # 2. Place

root.mainloop()
