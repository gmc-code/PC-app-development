# ttk Radiobutton - width and padding

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("width and padding")

sport = tk.StringVar(value="Soccer")

for choice in ["Soccer", "Netball", "Basketball"]:
    ttk.Radiobutton(root, text=choice, variable=sport, value=choice,
                    width=15, padding=5).pack(anchor="w", padx=80)

root.mainloop()
