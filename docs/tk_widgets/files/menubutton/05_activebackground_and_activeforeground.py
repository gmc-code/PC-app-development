# tk Menubutton - activebackground and activeforeground

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("active colours")

pick_button = tk.Menubutton(root, text="Hover over me", relief="raised", bg="lightgray",
                            activebackground="gold", activeforeground="black")
pick_menu = tk.Menu(pick_button, tearoff=0)
pick_menu.add_command(label="One")
pick_menu.add_command(label="Two")
pick_button.config(menu=pick_menu)
pick_button.pack(pady=20)

root.mainloop()
