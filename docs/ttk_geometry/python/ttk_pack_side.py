import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("pack side")
root.geometry("250x150")

style = ttk.Style()
style.configure("Side.TLabel", background="#dddddd")

label1 = ttk.Label(text="Left", style="Side.TLabel")
label1.pack(side="left")

label2 = ttk.Label(text="Top", style="Side.TLabel")
label2.pack(side="top")

label3 = ttk.Label(text="Right", style="Side.TLabel")
label3.pack(side="right")

label4 = ttk.Label(text="Bottom", style="Side.TLabel")
label4.pack(side="bottom")

root.mainloop()