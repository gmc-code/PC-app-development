# tk Menu - activebackground and activeforeground

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("active colours")

menubar = tk.Menu(root)
root.config(menu=menubar)

game_menu = tk.Menu(menubar, tearoff=0, activebackground="gold", activeforeground="black")
game_menu.add_command(label="New game")
game_menu.add_command(label="High scores")
menubar.add_cascade(label="Game", menu=game_menu)

root.mainloop()
