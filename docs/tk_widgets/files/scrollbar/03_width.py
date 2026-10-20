# tk Scrollbar - width

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("width")

scrollbar = tk.Scrollbar(root, width=30)
scrollbar.pack(side="right", fill="y")

word_list = tk.Listbox(root, yscrollcommand=scrollbar.set)
word_list.pack(side="left", fill="both", expand=True)
scrollbar.config(command=word_list.yview)

for number in range(1, 51):
    word_list.insert(tk.END, f"Word {number}")

root.mainloop()
