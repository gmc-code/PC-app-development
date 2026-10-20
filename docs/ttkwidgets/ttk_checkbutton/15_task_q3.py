# ttk Checkbutton - Tasks Q3

import tkinter as tk
from tkinter import ttk


def how_many():
    total = maths.get() + science.get() + art.get()
    count_label.config(text=f"Subjects ticked: {total}")


root = tk.Tk()
root.geometry("300x200")
root.title("Subjects")

maths = tk.IntVar()
science = tk.IntVar(value=1)
art = tk.IntVar()

ttk.Checkbutton(root, text="Maths", variable=maths).pack()
ttk.Checkbutton(root, text="Science", variable=science).pack()
ttk.Checkbutton(root, text="Art", variable=art).pack()

ttk.Button(root, text="How many?", command=how_many).pack(pady=5)
count_label = ttk.Label(root, text="")
count_label.pack()

root.mainloop()
