# tk Entry - font

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("font")

entry = tk.Entry(root, font=("Arial", 24))
entry.pack(pady=20)

root.mainloop()
