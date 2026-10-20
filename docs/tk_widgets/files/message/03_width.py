# tk Message - width

import tkinter as tk

root = tk.Tk()
root.geometry("350x250")
root.title("width")

text = "Koalas sleep for up to 20 hours a day and eat only gum leaves."

narrow = tk.Message(root, text=text, width=100, bg="lightblue")
narrow.pack(pady=5)

wide = tk.Message(root, text=text, width=300, bg="lightgreen")
wide.pack(pady=5)

root.mainloop()
