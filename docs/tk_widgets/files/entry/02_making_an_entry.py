# tk Entry - Making an Entry

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Entry with a label")

name_label = tk.Label(root, text="Type your name:")
name_label.pack(pady=5)

name_entry = tk.Entry(root)
name_entry.pack()

root.mainloop()
