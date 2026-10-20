# tk Scrollbar - Tasks Q2

import tkinter as tk


def bottom():
    number_list.yview_moveto(1)


root = tk.Tk()
root.geometry("300x200")
root.title("Numbers")

tk.Button(root, text="Bottom", command=bottom).pack(side="bottom")

scrollbar = tk.Scrollbar(root, width=25)
scrollbar.pack(side="right", fill="y")

number_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
number_list.pack(side="left", fill="both", expand=True)
scrollbar.config(command=number_list.yview)

for number in range(1, 201):
    number_list.insert(tk.END, number)

root.mainloop()
