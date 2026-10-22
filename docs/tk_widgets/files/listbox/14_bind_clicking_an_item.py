# tk Listbox - bind (clicking an item)

import tkinter as tk


def show_colour(event):
    chosen = colour_list.curselection()
    if chosen:
        colour = colour_list.get(chosen[0])
        colour_label.config(bg=colour, text=colour)


root = tk.Tk()
root.geometry("300x250")
root.title("bind")

colour_list = tk.Listbox(root, height=7)
for colour in ["red", "orange", "yellow", "green", "blue"]:
    colour_list.insert(tk.END, colour)
colour_list.pack(pady=5)
colour_list.bind("<<ListboxSelect>>", show_colour)

colour_label = tk.Label(root, text="Click a colour", width=20, height=2)
colour_label.pack(pady=5)

root.mainloop()
