# tk Spinbox - state

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

size_spinbox = tk.Spinbox(root, values=("Small", "Medium", "Large"), state="readonly")
size_spinbox.pack(pady=20)

root.mainloop()
