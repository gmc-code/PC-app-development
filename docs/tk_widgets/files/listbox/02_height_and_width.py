# tk Listbox - height and width

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("height and width")

number_list = tk.Listbox(root, height=4, width=15)
for number in range(1, 11):
    number_list.insert(tk.END, f"Number {number}")
number_list.pack(pady=10)

root.mainloop()
