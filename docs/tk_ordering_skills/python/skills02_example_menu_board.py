import tkinter as tk

root = tk.Tk()
root.title("Juice Bar")
root.geometry("400x300")
root.config(bg="lightyellow")

# Title
title_label = tk.Label(root)  # 1. create
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")  # 2. position
title_label.config(text="Juice Bar Menu", font=("Arial", 20, "bold"), bg="lightyellow", fg="darkorange")  # 3. configure

# Orange
orange_label = tk.Label(root)  # 1. create
orange_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")  # 2. position
orange_label.config(text="Orange", font=("Arial", 14), bg="lightyellow")  # 3. configure

orange_price = tk.Label(root)  # 1. create
orange_price.grid(row=1, column=1, padx=10, pady=5, sticky="e")  # 2. position
orange_price.config(text="$5.00", font=("Arial", 14), bg="lightyellow")  # 3. configure

# Apple
apple_label = tk.Label(root)  # 1. create
apple_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")  # 2. position
apple_label.config(text="Apple", font=("Arial", 14), bg="lightyellow")  # 3. configure

apple_price = tk.Label(root)  # 1. create
apple_price.grid(row=2, column=1, padx=10, pady=5, sticky="e")  # 2. position
apple_price.config(text="$4.50", font=("Arial", 14), bg="lightyellow")  # 3. configure

root.mainloop()
