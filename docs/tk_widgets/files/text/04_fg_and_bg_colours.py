# tk Text - fg and bg (colours)

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("fg and bg")

text_box = tk.Text(root, width=30, height=6, fg="white", bg="black")
text_box.pack(pady=10)

root.mainloop()
