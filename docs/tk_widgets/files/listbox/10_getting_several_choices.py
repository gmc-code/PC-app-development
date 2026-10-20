# tk Listbox - Getting several choices

import tkinter as tk


def order():
    toppings = []
    for index in topping_list.curselection():
        toppings.append(topping_list.get(index))
    result_label.config(text="Your toppings: " + ", ".join(toppings))


root = tk.Tk()
root.geometry("300x250")
root.title("Several choices")

topping_list = tk.Listbox(root, selectmode="multiple", height=5)
for topping in ["Cheese", "Ham", "Pineapple", "Olives", "Mushrooms"]:
    topping_list.insert(tk.END, topping)
topping_list.pack(pady=5)

order_button = tk.Button(root, text="Order", command=order)
order_button.pack()

result_label = tk.Label(root, text="", wraplength=250)
result_label.pack(pady=5)

root.mainloop()
