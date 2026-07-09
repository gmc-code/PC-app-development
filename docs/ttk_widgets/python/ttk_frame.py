
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ttk.Frame Widget Example")
root.geometry("400x200")

# 1. Create a Style object
style = ttk.Style()
# Force a theme that uses manual engine shading instead of OS native graphics
style.theme_use('clam')


frame = ttk.Frame(
    root,
    borderwidth=5,
    relief="groove",
    width=150,
    height=150
)

# Prevent the frame from shrinking to fit nothing; force its explicit size
frame.pack_propagate(False)
frame.pack(padx=20, pady=20)

root.mainloop()
