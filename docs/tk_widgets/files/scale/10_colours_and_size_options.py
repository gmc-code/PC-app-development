# tk Scale - Colours and size options

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("colours")

fancy_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=250,
                       bg="orange", fg="navy", troughcolor="lightyellow",
                       width=25, sliderlength=40)
fancy_scale.pack(pady=10)

hidden_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=250,
                        showvalue=0)
hidden_scale.pack(pady=10)

root.mainloop()
