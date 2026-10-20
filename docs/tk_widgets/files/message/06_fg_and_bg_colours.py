# tk Message - fg and bg (colours)

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("fg and bg")

warning = tk.Message(root, text="Warning: the oven is hot. Use oven mitts.", width=250,
                     fg="white", bg="red", font=("Arial", 14))
warning.pack(pady=20)

root.mainloop()
