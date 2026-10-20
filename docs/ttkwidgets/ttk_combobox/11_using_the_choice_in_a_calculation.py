# ttk Combobox - Using the choice in a calculation

import tkinter as tk
from tkinter import ttk

prices = {"Small": 3, "Medium": 4, "Large": 5}


def show_price(event):
    price_label.config(text=f"Price: ${prices[size_box.get()]}")


root = tk.Tk()
root.geometry("300x200")
root.title("Drink sizes")

size_box = ttk.Combobox(root, values=list(prices), state="readonly")
size_box.set("Small")
size_box.pack(pady=20)
size_box.bind("<<ComboboxSelected>>", show_price)

price_label = ttk.Label(root, text="Price: $3", font=("Arial", 16))
price_label.pack()

root.mainloop()
