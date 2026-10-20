# tk Menu - tk_popup (right-click menu)

import tkinter as tk


def show_popup(event):
    popup_menu.tk_popup(event.x_root, event.y_root)


def change_colour(colour):
    root.config(bg=colour)


root = tk.Tk()
root.geometry("300x200")
root.title("Right-click menu")

popup_menu = tk.Menu(root, tearoff=0)
popup_menu.add_command(label="Pink", command=lambda: change_colour("pink"))
popup_menu.add_command(label="Light blue", command=lambda: change_colour("lightblue"))
popup_menu.add_command(label="White", command=lambda: change_colour("white"))

root.bind("<Button-3>", show_popup)     # Right-click anywhere in the window

tk.Label(root, text="Right-click me!", font=("Arial", 16)).pack(pady=60)

root.mainloop()
