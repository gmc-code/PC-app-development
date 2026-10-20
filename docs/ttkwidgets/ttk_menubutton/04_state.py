# ttk Menubutton - state

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

locked_button = ttk.Menubutton(root, text="Locked", state="disabled")
locked_menu = tk.Menu(locked_button, tearoff=0)
locked_menu.add_command(label="Secret")
locked_button.config(menu=locked_menu)
locked_button.pack(pady=40)

root.mainloop()
