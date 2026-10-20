# tk Entry - show

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("show")

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, font=("Arial", 16), show="*")
password_entry.pack()

root.mainloop()
