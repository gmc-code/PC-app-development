# ttk LabelFrame - padding

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x250")
root.title("padding")

squashed = ttk.LabelFrame(root, text="No padding")
squashed.pack(pady=10)
ttk.Button(squashed, text="Squashed").pack()

roomy = ttk.LabelFrame(root, text="Padding", padding=(30, 15))
roomy.pack(pady=10)
ttk.Button(roomy, text="Roomy").pack()

root.mainloop()
