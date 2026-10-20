# tk Menubutton - state

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("state")

locked_button = tk.Menubutton(root, text="Locked ▼", relief="raised", state="disabled")
locked_menu = tk.Menu(locked_button, tearoff=0)
locked_menu.add_command(label="Secret")
locked_button.config(menu=locked_menu)
locked_button.pack(pady=20)

root.mainloop()
