# tk Message - font

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("font")

quote = tk.Message(root, text="Science is a way of thinking.", width=250,
                   font=("Georgia", 16, "italic"))
quote.pack(pady=20)

root.mainloop()
