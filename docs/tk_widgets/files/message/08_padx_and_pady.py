# tk Message - padx and pady

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("padx and pady")

tip = tk.Message(root, text="Tip: save your work often!", width=250,
                 bg="lightyellow", padx=20, pady=20)
tip.pack(pady=20)

root.mainloop()
