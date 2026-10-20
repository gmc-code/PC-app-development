# tk Button - width and height

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("width and height")

yes_button = tk.Button(root, text="Yes", width=15)
yes_button.pack(pady=5)

no_button = tk.Button(root, text="No", width=15)
no_button.pack(pady=5)

tall_button = tk.Button(root, text="Tall", width=15, height=3)
tall_button.pack(pady=5)

root.mainloop()
