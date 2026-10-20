# tk Text - insert

import tkinter as tk


def add_line():
    text_box.insert(tk.END, "Another line\n")


root = tk.Tk()
root.geometry("300x250")
root.title("insert")

text_box = tk.Text(root, width=30, height=6)
text_box.insert("1.0", "First line\n")       # Starting text
text_box.pack(pady=10)

add_button = tk.Button(root, text="Add a line", command=add_line)
add_button.pack()

root.mainloop()
