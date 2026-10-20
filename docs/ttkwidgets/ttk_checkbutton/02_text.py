# ttk Checkbutton - text

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("text")

agree = tk.IntVar()
ttk.Checkbutton(root, text="I agree to the rules", variable=agree).pack(pady=20)

root.mainloop()
