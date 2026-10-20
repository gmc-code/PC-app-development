# tk Menubutton - Tasks Q2

import tkinter as tk


def choose(pet):
    result_label.config(text="You chose " + pet)


root = tk.Tk()
root.geometry("300x200")
root.title("Pets")

pet_button = tk.Menubutton(root, text="Pets ▼", relief="raised")
pet_menu = tk.Menu(pet_button, tearoff=0)
pet_menu.add_command(label="Dog", command=lambda: choose("Dog"))
pet_menu.add_command(label="Cat", command=lambda: choose("Cat"))
pet_menu.add_command(label="Fish", command=lambda: choose("Fish"))
pet_button.config(menu=pet_menu)
pet_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
