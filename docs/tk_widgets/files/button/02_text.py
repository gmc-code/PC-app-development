# tk Button - text

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("text")

button = tk.Button(root, text="Start the game")
button.pack(pady=20)

root.mainloop()
