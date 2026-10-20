# tk LabelFrame - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Profile")

about = tk.LabelFrame(root, text="About you", padx=10, pady=10)
about.pack(pady=20)

name_label = tk.Label(about, text="Name:")
name_label.pack()
name_entry = tk.Entry(about)
name_entry.pack()

root.mainloop()
