# tk Listbox - size

import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("size")

name_list = tk.Listbox(root, height=5)
for name in ["Ava", "Ben", "Chloe", "Dev"]:
    name_list.insert(tk.END, name)
name_list.pack(pady=5)

count_label = tk.Label(root, text=f"There are {name_list.size()} names")
count_label.pack()

root.mainloop()
