import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("pack fill y")
root.geometry("250x150")

style = ttk.Style()
style.configure("Expand.TLabel", background="lightblue")

label = ttk.Label(root, text="Expanding Label", style="Expand.TLabel")
label.pack(expand=True, fill='y')

root.mainloop()