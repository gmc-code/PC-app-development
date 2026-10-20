# tk Menubutton - add_checkbutton

import tkinter as tk


def show():
    chosen = []
    if cheese.get() == 1:
        chosen.append("cheese")
    if ham.get() == 1:
        chosen.append("ham")
    if olives.get() == 1:
        chosen.append("olives")
    result_label.config(text="Toppings: " + ", ".join(chosen))


root = tk.Tk()
root.geometry("300x200")
root.title("add_checkbutton")

cheese = tk.IntVar()
ham = tk.IntVar()
olives = tk.IntVar()

topping_button = tk.Menubutton(root, text="Toppings ▼", relief="raised")
topping_menu = tk.Menu(topping_button, tearoff=0)
topping_menu.add_checkbutton(label="Cheese", variable=cheese, command=show)
topping_menu.add_checkbutton(label="Ham", variable=ham, command=show)
topping_menu.add_checkbutton(label="Olives", variable=olives, command=show)
topping_button.config(menu=topping_menu)
topping_button.pack(pady=20)

result_label = tk.Label(root, text="Toppings: ")
result_label.pack()

root.mainloop()
