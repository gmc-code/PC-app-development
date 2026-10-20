# tk Listbox - font

import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("font")

pet_list = tk.Listbox(root, font=("Arial", 16), height=4)
for pet in ["Dog", "Cat", "Fish", "Bird"]:
    pet_list.insert(tk.END, pet)
pet_list.pack(pady=10)

root.mainloop()
