# tk PanedWindow - forget

import tkinter as tk


def hide_help():
    panes.forget(help_label)


def show_help():
    panes.add(help_label)


root = tk.Tk()
root.geometry("400x250")
root.title("forget")

panes = tk.PanedWindow(root, sashwidth=5)
panes.pack(fill="both", expand=True)

game_label = tk.Label(panes, text="Game area", bg="white")
help_label = tk.Label(panes, text="Help:\nUse the arrow keys", bg="lightyellow")
panes.add(game_label)
panes.add(help_label)

tk.Button(root, text="Hide help", command=hide_help).pack(side="left", padx=10, pady=5)
tk.Button(root, text="Show help", command=show_help).pack(side="left", padx=10, pady=5)

root.mainloop()
