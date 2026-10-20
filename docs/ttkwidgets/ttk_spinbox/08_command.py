# ttk Spinbox - command

import tkinter as tk
from tkinter import ttk


def update_price():
    tickets = int(tickets_spinbox.get())
    price_label.config(text=f"Total: ${tickets * 15}")


root = tk.Tk()
root.geometry("300x200")
root.title("command")

tickets_spinbox = ttk.Spinbox(root, from_=1, to=10, width=5, state="readonly",
                              command=update_price)
tickets_spinbox.set(1)
tickets_spinbox.pack(pady=20)

price_label = ttk.Label(root, text="Total: $15", font=("Arial", 16))
price_label.pack()

root.mainloop()
