# tk Button - cursor

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("cursor")

button = tk.Button(root, text="Point at me", font=("Arial", 14), cursor="hand2")
button.pack(pady=20)

root.mainloop()
