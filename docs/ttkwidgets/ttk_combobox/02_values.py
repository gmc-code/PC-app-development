# ttk Combobox - values

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("values")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

planet_box = ttk.Combobox(root, values=planets)
planet_box.set("Earth")
planet_box.pack(pady=30)

root.mainloop()
