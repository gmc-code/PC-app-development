# tk Text - insertbackground and selectbackground

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("cursor colours")

text_box = tk.Text(root, width=30, height=6, fg="white", bg="black",
                   insertbackground="white", selectbackground="purple")
text_box.pack(pady=10)

root.mainloop()
