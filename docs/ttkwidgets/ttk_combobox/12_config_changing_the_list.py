# ttk Combobox - config (changing the list)

import tkinter as tk
from tkinter import ttk

foods = {
    "Fruit": ["Apple", "Banana", "Mango"],
    "Vegetables": ["Carrot", "Pea", "Potato"],
}


def change_list(event):
    group = group_box.get()
    food_box.config(values=foods[group])
    food_box.current(0)


root = tk.Tk()
root.geometry("300x200")
root.title("Changing the list")

group_box = ttk.Combobox(root, values=list(foods), state="readonly")
group_box.set("Fruit")
group_box.pack(pady=10)
group_box.bind("<<ComboboxSelected>>", change_list)

food_box = ttk.Combobox(root, values=foods["Fruit"], state="readonly")
food_box.current(0)
food_box.pack(pady=10)

root.mainloop()
