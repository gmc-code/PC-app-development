# tk Menubutton - add_radiobutton

import tkinter as tk


def show():
    size_button.config(text="Size: " + size.get())


root = tk.Tk()
root.geometry("300x200")
root.title("add_radiobutton")

size = tk.StringVar(value="Medium")

size_button = tk.Menubutton(root, text="Size: Medium", relief="raised", width=15)
size_menu = tk.Menu(size_button, tearoff=0)
for choice in ["Small", "Medium", "Large"]:
    size_menu.add_radiobutton(label=choice, variable=size, value=choice, command=show)
size_button.config(menu=size_menu)
size_button.pack(pady=20)

root.mainloop()
