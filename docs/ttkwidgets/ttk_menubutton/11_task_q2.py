# ttk Menubutton - Tasks Q2

import tkinter as tk
from tkinter import ttk


def choose(pet):
    result_label.config(text="You chose " + pet)


root = tk.Tk()
root.geometry("300x200")
root.title("Pets")

pet_button = ttk.Menubutton(root, text="Pets")
pet_menu = tk.Menu(pet_button, tearoff=0)
for pet in ["Dog", "Cat", "Fish"]:
    pet_menu.add_command(label=pet, command=lambda pet=pet: choose(pet))
pet_button.config(menu=pet_menu)
pet_button.pack(pady=30)

result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
