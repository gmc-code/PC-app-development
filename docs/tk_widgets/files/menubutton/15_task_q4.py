# tk Menubutton - Tasks Q4

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Extras")

sound = tk.IntVar()
music = tk.IntVar()

extras_button = tk.Menubutton(root, text="Extras ▼", relief="raised")
extras_menu = tk.Menu(extras_button, tearoff=0)
extras_menu.add_checkbutton(label="Sound", variable=sound)
extras_menu.add_checkbutton(label="Music", variable=music)
extras_button.config(menu=extras_menu)
extras_button.pack(pady=20)

root.mainloop()
