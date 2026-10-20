# tk Frame - destroy

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("destroy")

welcome_frame = tk.Frame(root, bg="lightyellow", padx=20, pady=20)
welcome_frame.pack(pady=20)
tk.Label(welcome_frame, text="Welcome!", bg="lightyellow", font=("Arial", 18)).pack()
tk.Button(welcome_frame, text="Close this message", command=welcome_frame.destroy).pack()

root.mainloop()
