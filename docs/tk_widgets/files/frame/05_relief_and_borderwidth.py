# tk Frame - relief and borderwidth

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("relief")

border_frame = tk.Frame(root, relief="groove", borderwidth=3, padx=10, pady=10)
border_frame.pack(pady=20)

tk.Label(border_frame, text="Username").pack()
tk.Entry(border_frame).pack()

root.mainloop()
