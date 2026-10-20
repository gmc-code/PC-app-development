# tk Menubutton - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Pets")

pet_button = tk.Menubutton(root, text="Pets ▼", relief="raised")
pet_menu = tk.Menu(pet_button, tearoff=0)
pet_menu.add_command(label="Dog")
pet_menu.add_command(label="Cat")
pet_menu.add_command(label="Fish")
pet_button.config(menu=pet_menu)
pet_button.pack(pady=20)

root.mainloop()
