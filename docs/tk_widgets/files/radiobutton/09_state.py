# tk Radiobutton - state

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

seat = tk.StringVar(value="Window")

tk.Radiobutton(root, text="Window seat", variable=seat, value="Window").pack()
tk.Radiobutton(root, text="Aisle seat (full)", variable=seat, value="Aisle",
               state="disabled").pack()

root.mainloop()
