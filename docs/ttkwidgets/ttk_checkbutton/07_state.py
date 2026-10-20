# ttk Checkbutton - state

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

chips = tk.IntVar()
ice_cream = tk.IntVar()

ttk.Checkbutton(root, text="Chips", variable=chips).pack(pady=5)
ttk.Checkbutton(root, text="Ice cream (sold out)", variable=ice_cream,
                state="disabled").pack(pady=5)

root.mainloop()
