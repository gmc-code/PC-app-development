# tk Checkbutton - Counting ticked boxes

import tkinter as tk


def count():
    total = cheese.get() + ham.get() + olives.get()
    result_label.config(text=f"Toppings: {total}   Price: ${10 + total * 2}")


root = tk.Tk()
root.geometry("300x220")
root.title("Pizza")

cheese = tk.IntVar()
ham = tk.IntVar()
olives = tk.IntVar()

tk.Checkbutton(root, text="Cheese", variable=cheese, command=count).pack()
tk.Checkbutton(root, text="Ham", variable=ham, command=count).pack()
tk.Checkbutton(root, text="Olives", variable=olives, command=count).pack()

result_label = tk.Label(root, text="Toppings: 0   Price: $10", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
