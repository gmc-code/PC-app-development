# tk OptionMenu - get (the variable)

import tkinter as tk


def show():
    result_label.config(text="You picked " + pet.get())


root = tk.Tk()
root.geometry("300x200")
root.title("get")

pet = tk.StringVar(value="Dog")

pet_menu = tk.OptionMenu(root, pet, "Dog", "Cat", "Rabbit")
pet_menu.pack(pady=10)

show_button = tk.Button(root, text="Show", command=show)
show_button.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
