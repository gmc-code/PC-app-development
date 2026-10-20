# ttk Checkbutton - Tasks Q4

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Subjects")

style = ttk.Style()
style.theme_use("clam")
style.configure("TCheckbutton", font=("Arial", 14))
style.map("TCheckbutton", foreground=[("selected", "purple")])

maths = tk.IntVar()
science = tk.IntVar(value=1)
art = tk.IntVar()

ttk.Checkbutton(root, text="Maths", variable=maths).pack()
ttk.Checkbutton(root, text="Science", variable=science).pack()
ttk.Checkbutton(root, text="Art", variable=art).pack()

root.mainloop()
