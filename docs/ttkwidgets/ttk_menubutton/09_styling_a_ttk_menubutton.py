# ttk Menubutton - Styling a ttk Menubutton

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Menubutton style")

style = ttk.Style()
style.theme_use("clam")
style.configure("TMenubutton", font=("Arial", 14), foreground="white",
                background="seagreen", padding=8)
style.map("TMenubutton", background=[("active", "mediumseagreen")])

food_button = ttk.Menubutton(root, text="Food")
food_menu = tk.Menu(food_button, tearoff=0, font=("Arial", 14), bg="honeydew")
food_menu.add_command(label="Pizza")
food_menu.add_command(label="Pasta")
food_button.config(menu=food_menu)
food_button.pack(pady=40)

root.mainloop()
