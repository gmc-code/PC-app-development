import tkinter as tk

root = tk.Tk()
root.title("Taco Truck")
root.geometry("400x250")

title_label = tk.Label(root)  # 1. create
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")  # 2. position
title_label.config(text="Taco Truck", font=("Arial", 20, "bold"))  # 3. configure

beef_label = tk.Label(root)  # 1. create
beef_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")  # 2. position
beef_label.config(text="Beef taco", font=("Arial", 14))  # 3. configure

beef_price = tk.Label(root)  # 1. create
beef_price.grid(row=1, column=1, padx=10, pady=5, sticky="e")  # 2. position
beef_price.config(text="$4.00", font=("Arial", 14))  # 3. configure

fish_label = tk.Label(root)  # 1. create
fish_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")  # 2. position
fish_label.config(text="Fish taco", font=("Arial", 14))  # 3. configure

fish_price = tk.Label(root)  # 1. create
fish_price.grid(row=2, column=1, padx=10, pady=5, sticky="e")  # 2. position
fish_price.config(text="$5.50", font=("Arial", 14))  # 3. configure

root.mainloop()
