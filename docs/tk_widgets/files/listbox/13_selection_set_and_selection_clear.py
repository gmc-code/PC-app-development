# tk Listbox - selection_set and selection_clear

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("selection_set")

size_list = tk.Listbox(root, height=3)
for size in ["Small", "Medium", "Large"]:
    size_list.insert(tk.END, size)
size_list.selection_set(1)          # "Medium" is chosen at the start
size_list.pack(pady=10)

root.mainloop()
