# tk Label - font

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("font")

label_1 = tk.Label(root, text="Arial size 24", font=("Arial", 24))
label_1.pack()

label_2 = tk.Label(root, text="Bold and italic", font=("Arial", 18, "bold italic"))
label_2.pack()

root.mainloop()
