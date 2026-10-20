# tk Entry - width

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("width")

short_entry = tk.Entry(root, width=5)
short_entry.pack(pady=10)

long_entry = tk.Entry(root, width=40)
long_entry.pack(pady=10)

root.mainloop()
