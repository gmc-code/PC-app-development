# ttk Button - image and compound

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("image")

picture = tk.PhotoImage(file="logo.png")

logo_button = ttk.Button(root, text="Home", image=picture, compound="left")
logo_button.pack(pady=40)

root.mainloop()
