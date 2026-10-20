# tk LabelFrame - labelanchor

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("labelanchor")

centred = tk.LabelFrame(root, text="Centred title", labelanchor="n", padx=20, pady=10)
centred.pack(pady=20)

tk.Label(centred, text="The title is in the middle").pack()

root.mainloop()
