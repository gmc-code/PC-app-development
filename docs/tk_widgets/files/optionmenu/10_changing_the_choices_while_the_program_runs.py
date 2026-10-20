# tk OptionMenu - Changing the choices while the program runs

import tkinter as tk


def show_fruit():
    change_choices(["Apple", "Banana", "Mango"])


def show_vegetables():
    change_choices(["Carrot", "Pea", "Potato"])


def change_choices(new_choices):
    menu = food_menu["menu"]
    menu.delete(0, "end")                   # 1. Remove the old choices
    for item in new_choices:                # 2. Add the new ones
        menu.add_command(label=item, command=lambda item=item: food.set(item))
    food.set(new_choices[0])                # Show the first new choice


root = tk.Tk()
root.geometry("300x200")
root.title("Changing choices")

food = tk.StringVar(value="Apple")

food_menu = tk.OptionMenu(root, food, "Apple", "Banana", "Mango")
food_menu.pack(pady=10)

fruit_button = tk.Button(root, text="Fruit", command=show_fruit)
fruit_button.pack(pady=2)

veg_button = tk.Button(root, text="Vegetables", command=show_vegetables)
veg_button.pack(pady=2)

root.mainloop()
