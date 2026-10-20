# tk Spinbox - Tasks Q3

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Colours")

colour_spinbox = tk.Spinbox(root, values=("Red", "Orange", "Yellow", "Green"),
                            wrap=True)
colour_spinbox.pack(pady=20)

root.mainloop()
