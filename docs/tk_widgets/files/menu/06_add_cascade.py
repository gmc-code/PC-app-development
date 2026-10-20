# tk Menu - add_cascade

import tkinter as tk


def set_size(size):
    word_label.config(font=("Arial", size))


root = tk.Tk()
root.geometry("300x200")
root.title("add_cascade")

menubar = tk.Menu(root)
root.config(menu=menubar)

view_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=view_menu)       # View on the menu bar

size_menu = tk.Menu(view_menu, tearoff=0)
size_menu.add_command(label="Small", command=lambda: set_size(10))
size_menu.add_command(label="Large", command=lambda: set_size(30))
view_menu.add_cascade(label="Text size", menu=size_menu)    # Sub-menu inside View

word_label = tk.Label(root, text="Hello", font=("Arial", 10))
word_label.pack(pady=40)

root.mainloop()
