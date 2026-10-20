# ttk PanedWindow - Tasks Q4

import tkinter as tk
from tkinter import ttk


def remove_list():
    try:
        panes.forget(animal_list)
    except tk.TclError:
        pass            # Already removed


root = tk.Tk()
root.geometry("400x230")
root.title("Animals")

panes = ttk.PanedWindow(root, orient="horizontal")
panes.pack(fill="both", expand=True)

animal_list = tk.Listbox(panes, width=15)
for animal in ["Koala", "Wombat", "Platypus"]:
    animal_list.insert(tk.END, animal)
panes.add(animal_list, weight=0)

notes_box = tk.Text(panes)
panes.add(notes_box, weight=1)

ttk.Button(root, text="Remove list", command=remove_list).pack(pady=5)

root.mainloop()
