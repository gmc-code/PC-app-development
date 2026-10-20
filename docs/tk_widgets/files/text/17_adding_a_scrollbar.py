# tk Text - Adding a scrollbar

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("scrollbar")

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")      # Scrollbar down the right side

text_box = tk.Text(root, width=30, height=8, yscrollcommand=scrollbar.set)
text_box.pack(side="left", padx=10, pady=10)

scrollbar.config(command=text_box.yview)

for number in range(1, 51):
    text_box.insert(tk.END, f"Line {number}\n")

root.mainloop()
