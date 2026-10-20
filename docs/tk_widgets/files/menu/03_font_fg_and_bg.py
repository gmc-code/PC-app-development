# tk Menu - font, fg and bg

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("font, fg and bg")

menubar = tk.Menu(root)
root.config(menu=menubar)

colour_menu = tk.Menu(menubar, tearoff=0, font=("Arial", 14), fg="white", bg="navy")
colour_menu.add_command(label="Red")
colour_menu.add_command(label="Green")
menubar.add_cascade(label="Colours", menu=colour_menu)

root.mainloop()
