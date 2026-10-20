# ttk Menubutton - padding

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("padding")

big_button = ttk.Menubutton(root, text="Big menu", padding=(20, 8))
big_menu = tk.Menu(big_button, tearoff=0)
big_menu.add_command(label="Item")
big_button.config(menu=big_menu)
big_button.pack(pady=40)

root.mainloop()
