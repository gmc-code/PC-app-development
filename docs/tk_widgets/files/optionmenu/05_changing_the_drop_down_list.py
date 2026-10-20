# tk OptionMenu - Changing the drop-down list

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("drop-down list")

animal = tk.StringVar(value="Koala")

animal_menu = tk.OptionMenu(root, animal, "Koala", "Kangaroo", "Wombat", "Emu")
animal_menu.config(font=("Arial", 16))
animal_menu["menu"].config(font=("Arial", 16), bg="lightgreen")     # The list that drops down
animal_menu.pack(pady=20)

root.mainloop()
