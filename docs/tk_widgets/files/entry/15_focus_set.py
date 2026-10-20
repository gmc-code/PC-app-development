# tk Entry - focus_set

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("focus_set")

first_entry = tk.Entry(root, font=("Arial", 16))
first_entry.pack(pady=10)

second_entry = tk.Entry(root, font=("Arial", 16))
second_entry.pack(pady=10)

second_entry.focus_set()        # The cursor starts in the second box

root.mainloop()
