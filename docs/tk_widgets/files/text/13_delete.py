# tk Text - delete

import tkinter as tk


def clear():
    text_box.delete("1.0", tk.END)


root = tk.Tk()
root.geometry("300x250")
root.title("delete")

text_box = tk.Text(root, width=30, height=6)
text_box.insert("1.0", "Line 1\nLine 2\nLine 3")
text_box.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

root.mainloop()
