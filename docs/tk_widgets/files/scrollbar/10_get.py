# tk Scrollbar - get

import tkinter as tk


def where():
    top, bottom = scrollbar.get()
    result_label.config(text=f"You have scrolled {round(bottom * 100)}% of the way")


root = tk.Tk()
root.geometry("300x250")
root.title("get")

list_frame = tk.Frame(root)
list_frame.pack(pady=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

item_list = tk.Listbox(list_frame, height=8, yscrollcommand=scrollbar.set)
item_list.pack(side="left")
scrollbar.config(command=item_list.yview)

for number in range(1, 51):
    item_list.insert(tk.END, f"Item {number}")

tk.Button(root, text="How far?", command=where).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
