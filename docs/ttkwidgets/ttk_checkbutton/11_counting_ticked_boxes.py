# ttk Checkbutton - Counting ticked boxes

import tkinter as tk
from tkinter import ttk


def count():
    total = cheese.get() + ham.get() + olives.get()
    result_label.config(text=f"Price: ${10 + total * 2}")


root = tk.Tk()
root.geometry("300x200")
root.title("Pizza")

cheese = tk.IntVar()
ham = tk.IntVar()
olives = tk.IntVar()

ttk.Checkbutton(root, text="Cheese", variable=cheese, command=count).pack()
ttk.Checkbutton(root, text="Ham", variable=ham, command=count).pack()
ttk.Checkbutton(root, text="Olives", variable=olives, command=count).pack()

result_label = ttk.Label(root, text="Price: $10", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
