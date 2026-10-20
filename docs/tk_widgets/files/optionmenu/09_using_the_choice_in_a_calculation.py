# tk OptionMenu - Using the choice in a calculation

import tkinter as tk

prices = {"Small": 3, "Medium": 4, "Large": 5}


def show_price(choice):
    price_label.config(text=f"Price: ${prices[choice]}")


root = tk.Tk()
root.geometry("300x200")
root.title("Drink sizes")

size = tk.StringVar(value="Small")

size_menu = tk.OptionMenu(root, size, *prices, command=show_price)
size_menu.pack(pady=10)

price_label = tk.Label(root, text="Price: $3", font=("Arial", 16))
price_label.pack()

root.mainloop()
