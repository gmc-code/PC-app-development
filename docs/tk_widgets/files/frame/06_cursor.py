# tk Frame - cursor

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("cursor")

target_frame = tk.Frame(root, width=150, height=100, bg="yellow", cursor="cross")
target_frame.pack(pady=40)

root.mainloop()
