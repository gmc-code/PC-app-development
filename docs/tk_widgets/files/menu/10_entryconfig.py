# tk Menu - entryconfig

import tkinter as tk


def start():
    game_menu.entryconfig("Start", state="disabled")
    game_menu.entryconfig("Stop", state="normal")
    status_label.config(text="Playing...")


def stop():
    game_menu.entryconfig("Start", state="normal")
    game_menu.entryconfig("Stop", state="disabled")
    status_label.config(text="Stopped")


root = tk.Tk()
root.geometry("300x200")
root.title("entryconfig")

menubar = tk.Menu(root)
root.config(menu=menubar)

game_menu = tk.Menu(menubar, tearoff=0)
game_menu.add_command(label="Start", command=start)
game_menu.add_command(label="Stop", command=stop, state="disabled")
menubar.add_cascade(label="Game", menu=game_menu)

status_label = tk.Label(root, text="Stopped", font=("Arial", 16))
status_label.pack(pady=40)

root.mainloop()
