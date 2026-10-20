# tk Scrollbar - Scrolling from code

import tkinter as tk


def go_top():
    name_list.yview_moveto(0)


def go_bottom():
    name_list.yview_moveto(1)


root = tk.Tk()
root.geometry("300x250")
root.title("yview_moveto")

list_frame = tk.Frame(root)
list_frame.pack(pady=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

name_list = tk.Listbox(list_frame, height=8, yscrollcommand=scrollbar.set)
name_list.pack(side="left")
scrollbar.config(command=name_list.yview)

for number in range(1, 101):
    name_list.insert(tk.END, f"Student {number}")

tk.Button(root, text="Top", command=go_top).pack(side="left", padx=60)
tk.Button(root, text="Bottom", command=go_bottom).pack(side="left")

root.mainloop()
