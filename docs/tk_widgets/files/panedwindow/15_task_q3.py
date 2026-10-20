# tk PanedWindow - Tasks Q3

import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("Animals")

panes = tk.PanedWindow(root, sashwidth=5)
panes.pack(fill="both", expand=True)

animal_list = tk.Listbox(panes)
for animal in ["Koala", "Wombat", "Platypus"]:
    animal_list.insert(tk.END, animal)
panes.add(animal_list, width=120)

notes_box = tk.Text(panes)
panes.add(notes_box)

root.mainloop()
