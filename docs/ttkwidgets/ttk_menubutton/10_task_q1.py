# ttk Menubutton - Tasks Q1

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Pets")

pet_button = ttk.Menubutton(root, text="Pets")
pet_menu = tk.Menu(pet_button, tearoff=0)
for pet in ["Dog", "Cat", "Fish"]:
    pet_menu.add_command(label=pet)
pet_button.config(menu=pet_menu)
pet_button.pack(pady=30)

root.mainloop()
