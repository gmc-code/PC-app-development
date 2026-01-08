import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("pack anchor")
root.geometry('250x150')

style = ttk.Style()
style.configure("Blue.TLabel", background="lightblue")
style.configure("Green.TLabel", background="lightgreen")
style.configure("Pink.TLabel", background="lightpink")

label1 = ttk.Label(root, text="Top-Left", style="Blue.TLabel")
label1.pack(anchor='nw')

label2 = ttk.Label(root, text="Center", style="Green.TLabel")
label2.pack(anchor='center')

label3 = ttk.Label(root, text="Bottom-Right", style="Pink.TLabel")
label3.pack(anchor='se')

root.mainloop()