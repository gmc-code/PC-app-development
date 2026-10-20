# tk Menu - add_separator

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("add_separator")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()                       # A line between the groups
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

root.mainloop()
