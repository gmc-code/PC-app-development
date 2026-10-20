# tk Entry - fg and bg (colours)

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("fg and bg")

entry = tk.Entry(root, font=("Arial", 18), fg="navy", bg="lightyellow")
entry.pack(pady=20)

root.mainloop()
