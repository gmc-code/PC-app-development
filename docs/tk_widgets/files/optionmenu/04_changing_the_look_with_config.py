# tk OptionMenu - Changing the look with config

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("config")

size = tk.StringVar(value="Medium")

size_menu = tk.OptionMenu(root, size, "Small", "Medium", "Large")
size_menu.config(font=("Arial", 16), width=10, bg="lightyellow", activebackground="gold")
size_menu.pack(pady=20)

root.mainloop()
