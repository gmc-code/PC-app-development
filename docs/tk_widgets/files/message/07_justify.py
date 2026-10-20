# tk Message - justify

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("justify")

poem = tk.Message(root, text="Roses are red,\nviolets are blue,\nPython is fun\nand Tkinter is too!",
                  width=250, justify="center", font=("Arial", 14))
poem.pack(pady=10)

root.mainloop()
