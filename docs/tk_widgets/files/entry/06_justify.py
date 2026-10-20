# tk Entry - justify

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("justify")

left_entry = tk.Entry(root, font=("Arial", 16), justify="left")
left_entry.pack(pady=5)

centre_entry = tk.Entry(root, font=("Arial", 16), justify="center")
centre_entry.pack(pady=5)

right_entry = tk.Entry(root, font=("Arial", 16), justify="right")
right_entry.pack(pady=5)

root.mainloop()
