# ttk widgets and styling - Theme picker example

import tkinter as tk
from tkinter import ttk


def change_theme(theme_name):
    style.theme_use(theme_name)
    current_label.config(text="Theme: " + theme_name)


root = tk.Tk()
root.geometry("350x300")
root.title("Theme picker")

style = ttk.Style()

current_label = ttk.Label(root, text="Theme: " + style.theme_use(), font=("Arial", 14))
current_label.pack(pady=5)

for theme_name in style.theme_names():
    ttk.Button(root, text=theme_name,
               command=lambda name=theme_name: change_theme(name)).pack(pady=2)

ttk.Checkbutton(root, text="A checkbutton").pack(pady=5)
ttk.Entry(root).pack()

root.mainloop()
