# tk Scrollbar - Colours

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("colours")

scrollbar = tk.Scrollbar(root, bg="orange", troughcolor="lightyellow",
                         activebackground="red")
scrollbar.pack(side="right", fill="y")

item_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
item_list.pack(side="left", fill="both", expand=True)
scrollbar.config(command=item_list.yview)

for number in range(1, 51):
    item_list.insert(tk.END, f"Item {number}")

root.mainloop()
