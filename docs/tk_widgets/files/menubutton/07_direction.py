# tk Menubutton - direction

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("direction")

up_button = tk.Menubutton(root, text="Opens upwards ▲", relief="raised", direction="above")
up_menu = tk.Menu(up_button, tearoff=0)
up_menu.add_command(label="First")
up_menu.add_command(label="Second")
up_button.config(menu=up_menu)
up_button.pack(side="bottom", pady=10)

root.mainloop()
