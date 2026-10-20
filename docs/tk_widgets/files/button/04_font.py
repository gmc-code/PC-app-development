# tk Button - font

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("font")

button = tk.Button(root, text="Big button", font=("Arial", 20, "bold"))
button.pack(pady=20)

root.mainloop()
