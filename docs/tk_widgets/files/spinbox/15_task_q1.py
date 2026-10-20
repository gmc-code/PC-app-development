# tk Spinbox - Tasks Q1

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Tickets")

tickets_spinbox = tk.Spinbox(root, from_=1, to=6, font=("Arial", 20), width=4)
tickets_spinbox.pack(pady=20)

root.mainloop()
