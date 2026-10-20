# ttk Menubutton - add_checkbutton

import tkinter as tk
from tkinter import ttk


def show():
    result_label.config(text=f"Sound: {sound.get()}   Music: {music.get()}")


root = tk.Tk()
root.geometry("300x200")
root.title("add_checkbutton")

sound = tk.IntVar(value=1)
music = tk.IntVar()

extras_button = ttk.Menubutton(root, text="Extras")
extras_menu = tk.Menu(extras_button, tearoff=0)
extras_menu.add_checkbutton(label="Sound", variable=sound, command=show)
extras_menu.add_checkbutton(label="Music", variable=music, command=show)
extras_button.config(menu=extras_menu)
extras_button.pack(pady=30)

result_label = ttk.Label(root, text="Sound: 1   Music: 0")
result_label.pack()

root.mainloop()
