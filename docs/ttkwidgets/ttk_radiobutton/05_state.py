# ttk Radiobutton - state

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

seat = tk.StringVar(value="Window")

ttk.Radiobutton(root, text="Window seat", variable=seat, value="Window").pack()
ttk.Radiobutton(root, text="Aisle seat (full)", variable=seat, value="Aisle",
                state="disabled").pack()

root.mainloop()
