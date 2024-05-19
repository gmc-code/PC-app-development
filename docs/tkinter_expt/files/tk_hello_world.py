from tkinter import *
from tkinter import ttk

root2 = Tk()
frm = ttk.Frame(root2, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root2.destroy).grid(column=1, row=0)
root2.mainloop()
