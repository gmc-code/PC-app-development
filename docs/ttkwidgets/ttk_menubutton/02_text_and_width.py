# ttk Menubutton - text and width

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("text and width")

options_button = ttk.Menubutton(root, text="Options", width=15)
options_menu = tk.Menu(options_button, tearoff=0)
options_menu.add_command(label="Settings")
options_menu.add_command(label="Help")
options_button.config(menu=options_menu)
options_button.pack(pady=40)

root.mainloop()
