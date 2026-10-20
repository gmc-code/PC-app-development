# tk Menubutton - text

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("text")

options_button = tk.Menubutton(root, text="Options ▼", relief="raised")
options_menu = tk.Menu(options_button, tearoff=0)
options_menu.add_command(label="Settings")
options_menu.add_command(label="Help")
options_button.config(menu=options_menu)
options_button.pack(pady=20)

root.mainloop()
