# tk Text - font

import tkinter as tk

root = tk.Tk()
root.geometry("350x200")
root.title("font")

text_box = tk.Text(root, width=25, height=4, font=("Comic Sans MS", 14))
text_box.pack(pady=10)

root.mainloop()
