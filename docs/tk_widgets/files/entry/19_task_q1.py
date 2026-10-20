# tk Entry - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Sign in")

user_label = tk.Label(root, text="Username:")
user_label.pack()

user_entry = tk.Entry(root, font=("Arial", 16), bg="lightblue")
user_entry.pack()

root.mainloop()
