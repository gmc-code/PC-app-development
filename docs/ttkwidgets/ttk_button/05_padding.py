# ttk Button - padding

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("padding")

big_button = ttk.Button(root, text="Big button", padding=(30, 15))
big_button.pack(pady=40)

root.mainloop()
