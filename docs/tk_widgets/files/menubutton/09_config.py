# tk Menubutton - config

import tkinter as tk


def choose(sport):
    sport_button.config(text=sport + " ▼")


root = tk.Tk()
root.geometry("300x200")
root.title("config")

sport_button = tk.Menubutton(root, text="Choose a sport ▼", relief="raised", width=18)
sport_menu = tk.Menu(sport_button, tearoff=0)
for sport in ["Cricket", "Netball", "Soccer", "Tennis"]:
    sport_menu.add_command(label=sport, command=lambda sport=sport: choose(sport))
sport_button.config(menu=sport_menu)
sport_button.pack(pady=20)

root.mainloop()
