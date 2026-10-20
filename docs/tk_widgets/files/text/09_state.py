# tk Text - state

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

text_box = tk.Text(root, width=30, height=6)
text_box.insert("1.0", "You can read this,\nbut you cannot change it.")
text_box.config(state="disabled")       # Lock the box after putting text in
text_box.pack(pady=10)

root.mainloop()
