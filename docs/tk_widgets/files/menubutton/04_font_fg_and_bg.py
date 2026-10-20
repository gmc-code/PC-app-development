# tk Menubutton - font, fg and bg

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("font, fg and bg")

food_button = tk.Menubutton(root, text="Food ▼", relief="raised",
                            font=("Arial", 14), fg="white", bg="green")
food_menu = tk.Menu(food_button, tearoff=0, font=("Arial", 14), bg="lightgreen")
food_menu.add_command(label="Pizza")
food_menu.add_command(label="Pasta")
food_button.config(menu=food_menu)
food_button.pack(pady=20)

root.mainloop()
