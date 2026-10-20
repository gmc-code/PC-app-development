# tk Text - undo

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("undo")

text_box = tk.Text(root, width=30, height=6, undo=True)
text_box.pack(pady=10)

root.mainloop()
