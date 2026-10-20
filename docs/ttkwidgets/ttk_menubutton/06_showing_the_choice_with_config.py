# ttk Menubutton - Showing the choice with config

import tkinter as tk
from tkinter import ttk


def choose(sport):
    sport_button.config(text=sport)


root = tk.Tk()
root.geometry("300x200")
root.title("config")

sport_button = ttk.Menubutton(root, text="Choose a sport", width=18)
sport_menu = tk.Menu(sport_button, tearoff=0)
for sport in ["Cricket", "Netball", "Soccer", "Tennis"]:
    sport_menu.add_command(label=sport, command=lambda sport=sport: choose(sport))
sport_button.config(menu=sport_menu)
sport_button.pack(pady=40)

root.mainloop()
