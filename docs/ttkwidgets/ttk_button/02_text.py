# ttk Button - text

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("text")

start_button = ttk.Button(root, text="Start the game")
start_button.pack(pady=20)

root.mainloop()
