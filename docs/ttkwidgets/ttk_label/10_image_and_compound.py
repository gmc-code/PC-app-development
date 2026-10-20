# ttk Label - image and compound

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("image")

picture = tk.PhotoImage(file="logo.png")

ttk.Label(root, image=picture, text="Our logo", compound="top").pack(pady=20)

root.mainloop()
