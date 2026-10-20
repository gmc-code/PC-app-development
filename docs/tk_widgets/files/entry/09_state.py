# tk Entry - state

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

normal_entry = tk.Entry(root, state="normal")
normal_entry.pack(pady=5)

readonly_entry = tk.Entry(root, state="readonly")
readonly_entry.pack(pady=5)

disabled_entry = tk.Entry(root, state="disabled")
disabled_entry.pack(pady=5)

root.mainloop()
