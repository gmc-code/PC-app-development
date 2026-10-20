# ttk Frame - A row of buttons

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Button row")

button_row = ttk.Frame(root)
button_row.pack(pady=30)

for word in ["Back", "Home", "Next"]:
    ttk.Button(button_row, text=word, width=8).pack(side="left", padx=5)

root.mainloop()
