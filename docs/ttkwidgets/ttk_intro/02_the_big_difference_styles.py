# ttk widgets and styling - The big difference: styles

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("tk colours")

tk.Button(root, text="One", fg="white", bg="purple", font=("Arial", 14)).pack(pady=5)
tk.Button(root, text="Two", fg="white", bg="purple", font=("Arial", 14)).pack(pady=5)

root.mainloop()
