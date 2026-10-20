# ttk Label - padding

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("padding")

ttk.Label(root, text="Padded", font=("Arial", 18), background="lightgreen",
          padding=(40, 20)).pack(pady=40)

root.mainloop()
