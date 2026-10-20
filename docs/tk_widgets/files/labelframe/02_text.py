# tk LabelFrame - text

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("text")

settings = tk.LabelFrame(root, text="Settings", padx=10, pady=10)
settings.pack(pady=20)

tk.Checkbutton(settings, text="Sound on").pack()

root.mainloop()
