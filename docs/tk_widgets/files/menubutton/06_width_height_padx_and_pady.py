# tk Menubutton - width, height, padx and pady

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("size")

big_button = tk.Menubutton(root, text="Big menu", relief="raised",
                           width=15, height=2, padx=10, pady=5)
big_menu = tk.Menu(big_button, tearoff=0)
big_menu.add_command(label="Item")
big_button.config(menu=big_menu)
big_button.pack(pady=20)

root.mainloop()
