# tk Entry - relief and borderwidth

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("relief")

entry = tk.Entry(root, font=("Arial", 16), relief="solid", borderwidth=2)
entry.pack(pady=20)

root.mainloop()
