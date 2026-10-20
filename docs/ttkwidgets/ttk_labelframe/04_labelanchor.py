# ttk LabelFrame - labelanchor

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("labelanchor")

centred = ttk.LabelFrame(root, text="Centred title", labelanchor="n", padding=15)
centred.pack(pady=30)
ttk.Label(centred, text="The title is in the middle").pack()

root.mainloop()
