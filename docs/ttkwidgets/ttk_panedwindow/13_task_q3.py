# ttk PanedWindow - Tasks Q3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x200")
root.title("Animals")

panes = ttk.PanedWindow(root, orient="horizontal")
panes.pack(fill="both", expand=True)

animal_list = tk.Listbox(panes, width=15)
for animal in ["Koala", "Wombat", "Platypus"]:
    animal_list.insert(tk.END, animal)
panes.add(animal_list, weight=0)

notes_box = tk.Text(panes)
panes.add(notes_box, weight=1)

root.mainloop()
