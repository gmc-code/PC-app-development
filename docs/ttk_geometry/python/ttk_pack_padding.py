import tkinter as tk
from tkinter import ttk

root = tk.Tk()

style = ttk.Style()
style.configure("Red.TLabel", background="red", foreground="white")
style.configure("Purple.TLabel", background="purple", foreground="white")

label1 = ttk.Label(root, text="Red", style="Red.TLabel", anchor="center")
label1.pack(ipadx=30, ipady=6)

label2 = ttk.Label(root, text="Purple", style="Purple.TLabel", anchor="center")
label2.pack(pady=20, ipadx=8, ipady=20)

root.mainloop()
