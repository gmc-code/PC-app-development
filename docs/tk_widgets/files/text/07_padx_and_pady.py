# tk Text - padx and pady

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("padx and pady")

text_box = tk.Text(root, width=25, height=4, padx=15, pady=15)
text_box.insert("1.0", "There is space\naround this text.")
text_box.pack(pady=10)

root.mainloop()
