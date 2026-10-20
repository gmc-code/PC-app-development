# tk Menu - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Menus")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

root.mainloop()
