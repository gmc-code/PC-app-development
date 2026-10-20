# ttk Label - font

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("font")

ttk.Label(root, text="Arial 24", font=("Arial", 24)).pack(pady=5)
ttk.Label(root, text="Bold and italic", font=("Arial", 18, "bold italic")).pack(pady=5)

root.mainloop()
